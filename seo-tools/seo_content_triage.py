#!/usr/bin/env python3
"""Monthly, read-only triage of English main-content depth and case-page overlap.

The thresholds are editorial review signals only. They are not search-engine
word-count requirements and never trigger page removal or deindexing.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
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

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.casefold()
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


def inspect(url: str) -> tuple[str, str, int, str]:
    try:
        status, final_url, body = audit.fetch(url)
        if status != 200:
            return url, "", 0, f"HTTP {status} -> {final_url}"
        if urllib.parse.urlsplit(final_url).hostname != urllib.parse.urlsplit(url).hostname:
            return url, "", 0, f"unexpected final host -> {final_url}"
        parser = MainTextParser()
        parser.feed(body.decode("utf-8", "replace"))
        text = " ".join(" ".join(parser.parts).split())
        if not text:
            return url, "", 0, "no visible text in <main>/<article>"
        return url, text, len(WORD_RE.findall(text)), ""
    except Exception as error:  # noqa: BLE001
        return url, "", 0, f"{type(error).__name__}: {error}"


def similarity_pairs(pages: list[tuple[str, str]]) -> list[tuple[float, str, str, int]]:
    docs: list[tuple[str, set[str]]] = []
    for url, text in pages:
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
    pages: list[tuple[str, str, int, str]] = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(inspect, url) for url in selected]
        for future in as_completed(futures):
            pages.append(future.result())

    errors = [(url, error) for url, _, _, error in pages if error]
    flagged = sorted((count, url) for url, _, count, error in pages if not error and count < MIN_WORD_TOKENS)
    report = [
        f"### {site.name}",
        "",
        f"English/default-language non-contact pages checked: **{len(selected)}**",
        f"Fetch or empty-main issues: **{len(errors)}**",
        f"Editorial review candidates below {MIN_WORD_TOKENS} English word tokens: **{len(flagged)}**",
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

    if site.name == "Pomerol":
        cases = [(url, text) for url, text, _, error in pages if "/case-studies/" in url and not error]
        pairs = similarity_pairs(cases)
        report.extend([
            "Case-page similarity screen:",
            "",
            f"- Case-study pages checked: **{len(cases)}**",
            f"- Page pairs above Jaccard {SIMILARITY_THRESHOLD:.2f}: **{len(pairs)}**",
            "- This lexical overlap screen flags candidates for editorial review; it does not prove duplication or predict a search penalty.",
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
