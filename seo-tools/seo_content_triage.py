#!/usr/bin/env python3
"""Monthly, read-only triage of English main-content depth and case-page overlap.

The thresholds are editorial review signals only. They are not search-engine
word-count requirements and never trigger page removal or deindexing.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from html.parser import HTMLParser
import os
import re
import sys
import urllib.parse

import seo_full_site_audit as audit

WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*")
MIN_WORD_TOKENS = 300
SIMILARITY_THRESHOLD = 0.38
SIMILARITY_STOPWORDS = {
    "about", "after", "before", "buyer", "case", "cases", "china", "client",
    "company", "from", "have", "into", "more", "most", "need", "only", "order",
    "our", "project", "sourcing", "supplier", "that", "their", "there", "these",
    "they", "this", "through", "with", "work", "your",
}
CASE_TEMPLATE_PATTERNS = (
    re.compile(
        r"This page is an illustrative .*? Product photography shows a category, not a customer shipment\.",
        re.IGNORECASE,
    ),
    re.compile(
        r"Transparency note: the client name and selected commercial details are pseudonymized or illustrative\. "
        r"The sourcing risks and control methods are representative examples, not third-party endorsements\.",
        re.IGNORECASE,
    ),
    re.compile(
        r"This expanded control plan is a representative procurement method for this product category\. "
        r"It does not claim that every listed step was performed for a named client or shipment\.",
        re.IGNORECASE,
    ),
)
CASE_TEMPLATE_LABELS = re.compile(
    r"\b(?:illustrative buyer profile|illustrative scenario|illustrative market|illustrative buyer type|"
    r"example buyer requirement|possible sourcing workstream|buyer control points|possible process objective|"
    r"detailed sourcing control plan|from requirement freeze to shipment handover|requirement snapshot|"
    r"supplier screening|validation gates|buyer handover pack|scenario\s+\d+)\b",
    re.IGNORECASE,
)
NON_CONTENT_PATHS = ("/contact", "/terms", "/privacy")
LOCALIZED_PREFIXES = {"zh", "es", "pt", "ru", "ja"}
MAX_WORKERS = 12


class MainTextParser(HTMLParser):
    """Collect visible text under main/article while dropping site chrome."""

    SKIP_TAGS = {"script", "style", "nav", "footer", "header", "aside", "noscript", "svg", "form", "button"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.main_depth = 0
        self.skip_depth = 0
        self.parts: list[str] = []
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.casefold()
        values = {key.casefold(): (value or "") for key, value in attrs}
        if tag == "a" and values.get("href") and "nofollow" not in values.get("rel", "").casefold().split():
            self.links.append(values["href"])
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
        if tag in {"main", "article"}:
            self.main_depth += 1

    def handle_endtag(self, tag: str) -> None:
        tag = tag.casefold()
        if tag in self.SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1
        if tag in {"main", "article"}:
            self.main_depth = max(0, self.main_depth - 1)

    def handle_data(self, data: str) -> None:
        if self.main_depth and not self.skip_depth and data.strip():
            self.parts.append(data.strip())


def is_english_content(site: audit.Site, url: str) -> bool:
    path = urllib.parse.urlsplit(url).path.rstrip("/") or "/"
    if any(path == suffix or path.endswith(suffix) for suffix in NON_CONTENT_PATHS):
        return False
    first = path.lstrip("/").split("/", 1)[0].casefold()
    if site.name == "Xiaodu":
        return path == "/" or path == "/en" or path.startswith("/en/")
    if site.name == "StayChina":
        return path == "/en" or path.startswith("/en/")
    if site.name == "Pomerol":
        return first == "en" or first not in LOCALIZED_PREFIXES
    return False


def inspect(url: str) -> tuple[str, str, int, list[str], str]:
    try:
        status, final_url, body = audit.fetch(url)
        if status != 200:
            return url, "", 0, [], f"HTTP {status} -> {final_url}"
        if urllib.parse.urlsplit(final_url).hostname != urllib.parse.urlsplit(url).hostname:
            return url, "", 0, [], f"unexpected final host -> {final_url}"
        parser = MainTextParser()
        parser.feed(body.decode("utf-8", "replace"))
        text = " ".join(" ".join(parser.parts).split())
        if not text:
            return url, "", 0, parser.links, "no visible text in <main>/<article>"
        return url, text, len(WORD_RE.findall(text)), parser.links, ""
    except Exception as error:  # noqa: BLE001
        return url, "", 0, [], f"{type(error).__name__}: {error}"


def normalize_internal_url(site: audit.Site, source_url: str, href: str) -> str | None:
    target = urllib.parse.urljoin(source_url, href)
    parts = urllib.parse.urlsplit(target)
    host = (parts.hostname or "").casefold()
    canonical = site.canonical_host.casefold()
    root = canonical.removeprefix("www.")
    if host not in {canonical, root, f"www.{root}"}:
        return None
    path = parts.path or "/"
    if path != "/":
        path = path.rstrip("/") or "/"
    return urllib.parse.urlunsplit(("https", canonical, path, "", ""))


def similarity_pairs(pages: list[tuple[str, str]]) -> list[tuple[float, str, str, int]]:
    docs: list[tuple[str, set[str]]] = []
    for url, text in pages:
        for pattern in CASE_TEMPLATE_PATTERNS:
            text = pattern.sub(" ", text)
        text = CASE_TEMPLATE_LABELS.sub(" ", text)
        tokens = {
            token for token in WORD_RE.findall(text.casefold())
            if len(token) > 2 and token not in SIMILARITY_STOPWORDS
        }
        docs.append((url, tokens))

    pairs: list[tuple[float, str, str, int]] = []
    for index, (left_url, left) in enumerate(docs):
        for right_url, right in docs[index + 1:]:
            union = left | right
            if not union:
                continue
            shared = len(left & right)
            score = shared / len(union)
            if score >= SIMILARITY_THRESHOLD:
                pairs.append((score, left_url, right_url, shared))
    return sorted(pairs, reverse=True)


def audit_site(site: audit.Site) -> tuple[str, list[str]]:
    urls = audit.load_sitemap(site)
    selected = sorted({url for url in urls if is_english_content(site, url)})
    sitemap_keys = {normalize_internal_url(site, url, url): url for url in urls}
    pages: list[tuple[str, str, int, list[str], str]] = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(inspect, url) for url in sorted(set(urls))]
        for future in as_completed(futures):
            pages.append(future.result())

    errors = [(url, error) for url, _, _, _, error in pages if error]
    page_map = {url: (text, word_count, links, error) for url, text, word_count, links, error in pages}
    flagged = sorted(
        (count, url) for url, _, count, _, error in pages
        if url in selected and not error and count < MIN_WORD_TOKENS
    )
    inbound_sources: dict[str, set[str]] = defaultdict(set)
    for source_url, (_, _, links, error) in page_map.items():
        if error:
            continue
        source_key = normalize_internal_url(site, source_url, source_url)
        for href in links:
            target_key = normalize_internal_url(site, source_url, href)
            if target_key in sitemap_keys and target_key != source_key:
                inbound_sources[target_key].add(source_url)
    orphan_keys = sorted(key for key in sitemap_keys if not inbound_sources[key])
    weakly_linked_keys = sorted(key for key in sitemap_keys if len(inbound_sources[key]) == 1)
    report = [
        f"### {site.name}",
        "",
        f"Sitemap pages fetched for link graph: **{len(urls)}**",
        f"English/default-language non-contact pages checked: **{len(selected)}**",
        f"Fetch or empty-main issues: **{len(errors)}**",
        f"Editorial review candidates below {MIN_WORD_TOKENS} English word tokens: **{len(flagged)}**",
        f"Sitemap URLs with no same-site HTML inlinks: **{len(orphan_keys)}**",
        f"Sitemap URLs with only one same-site HTML inlink: **{len(weakly_linked_keys)}**",
        "",
        "Low word count is a review cue, not a quality verdict or indexation recommendation.",
        "",
    ]
    if flagged:
        report.extend(f"- `{count}` — {url}" for count, url in flagged)
        report.append("")
    if errors:
        report.extend(["Fetch/content extraction issues:", ""])
        report.extend(f"- {url}: {error}" for url, error in errors)
        report.append("")
    if orphan_keys:
        report.extend(["No-inlink sitemap URLs (manual review):", ""])
        report.extend(f"- {sitemap_keys[key]}" for key in orphan_keys[:50])
        if len(orphan_keys) > 50:
            report.append(f"- … {len(orphan_keys) - 50} additional URL(s) omitted")
        report.append("")
    if weakly_linked_keys:
        report.extend(["URLs linked by one source page (source is shown for review):", ""])
        for key in weakly_linked_keys[:50]:
            source = next(iter(inbound_sources[key]))
            report.append(f"- {sitemap_keys[key]} ← {source}")
        if len(weakly_linked_keys) > 50:
            report.append(f"- … {len(weakly_linked_keys) - 50} additional URL(s) omitted")
        report.append("")

    if site.name == "Pomerol":
        cases = [(url, text) for url, text, _, _, error in pages if "/case-studies/" in url and not error]
        pairs = similarity_pairs(cases)
        report.extend([
            "Case-page similarity screen:",
            "",
            f"- Case-study pages checked: **{len(cases)}**",
            f"- Page pairs above template-normalized Jaccard {SIMILARITY_THRESHOLD:.2f}: **{len(pairs)}**",
            "- Shared scenario disclosures and fixed control-plan labels are excluded before comparison; this lexical screen flags candidates for editorial review and does not prove duplication or predict a search penalty.",
            "",
        ])
        report.extend(f"- `{score:.2f}` ({shared} shared tokens) — {left} ↔ {right}" for score, left, right, shared in pairs[:20])
        if pairs:
            report.append("")

    return "\n".join(report), [f"{url}: {error}" for url, error in errors]


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    report = [
        "# Monthly English main-content editorial triage",
        "",
        f"Threshold: fewer than {MIN_WORD_TOKENS} English word tokens is a manual review cue only. This is not a Google word-count rule, and the script never removes or deindexes pages.",
        "Case similarity is a lexical Jaccard screen, not a duplicate-content verdict.",
        "Internal inlinks are collected from same-site HTML anchors in all sitemap pages; no-inlink URLs are review candidates, not automatic errors.",
        "",
    ]
    failures: list[str] = []
    for site in audit.SITES:
        try:
            section, errors = audit_site(site)
            report.append(section)
            failures.extend(f"{site.name}: {error}" for error in errors)
        except Exception as error:  # noqa: BLE001
            failures.append(f"{site.name}: {type(error).__name__}: {error}")
            report.extend([f"### {site.name}", "", f"Audit could not complete: {type(error).__name__}: {error}", ""])
    if failures:
        report.extend(["## Audit errors", ""])
        report.extend(f"- {error}" for error in failures)
        report.append("")
    output = "\n".join(report)
    print(output)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write(output)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
