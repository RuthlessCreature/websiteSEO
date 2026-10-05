#!/usr/bin/env python3
"""Monthly, read-only audit of every URL in the three public production sitemaps."""

from __future__ import annotations

from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from html.parser import HTMLParser
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

USER_AGENT = "websiteSEO-full-crawl-audit/1.0 (+https://github.com/RuthlessCreature/websiteSEO)"
MAX_SITEMAPS = 30
MAX_URLS = 10_000
MAX_RESPONSE_BYTES = 4_000_000
MAX_WORKERS = 12
RETRIES = 2


@dataclass(frozen=True)
class Site:
    name: str
    sitemap_url: str
    canonical_host: str


SITES = (
    Site("Xiaodu", "https://xiaodu.tech/sitemap.xml", "xiaodu.tech"),
    Site("StayChina", "https://www.staychina.org/sitemap-index.xml", "www.staychina.org"),
    Site("Pomerol", "https://pomerol.trade/sitemap.xml", "pomerol.trade"),
)


@dataclass
class Page:
    url: str
    status: int | None = None
    final_url: str = ""
    title: str = ""
    h1: list[str] | None = None
    canonicals: list[str] | None = None
    robots: list[str] | None = None
    alternates: list[tuple[str, str]] | None = None
    error: str = ""


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.h1: list[str] = []
        self.canonicals: list[str] = []
        self.robots: list[str] = []
        self.alternates: list[tuple[str, str]] = []
        self._in_title = False
        self._in_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.casefold(): (value or "") for key, value in attrs}
        tag = tag.casefold()
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
            self.h1.append("")
        elif tag == "meta" and values.get("name", "").casefold() in ("robots", "googlebot"):
            self.robots.append(values.get("content", "").casefold())
        elif tag == "link":
            rels = set(values.get("rel", "").casefold().split())
            if "canonical" in rels and values.get("href"):
                self.canonicals.append(values["href"])
            if "alternate" in rels and values.get("hreflang") and values.get("href"):
                self.alternates.append((values["hreflang"].casefold(), values["href"]))

    def handle_endtag(self, tag: str) -> None:
        if tag.casefold() == "title":
            self._in_title = False
        elif tag.casefold() == "h1":
            self._in_h1 = False

    def handle_data(self, data: str) -> None:
        value = data.strip()
        if not value:
            return
        if self._in_title:
            self.title += " " + value
        if self._in_h1 and self.h1:
            self.h1[-1] += " " + value


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].casefold()


def fetch(url: str) -> tuple[int, str, bytes]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xml,*/*;q=0.8",
            "Accept-Encoding": "identity",
            "Connection": "close",
        },
    )
    last_error: Exception | None = None
    for attempt in range(RETRIES + 1):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                body = response.read(MAX_RESPONSE_BYTES + 1)
                if len(body) > MAX_RESPONSE_BYTES:
                    raise ValueError(f"response exceeds {MAX_RESPONSE_BYTES} bytes")
                return response.status, response.geturl(), body
        except urllib.error.HTTPError as error:
            return error.code, error.geturl(), error.read(MAX_RESPONSE_BYTES)
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            last_error = error
            if attempt < RETRIES:
                time.sleep(0.5 * (attempt + 1))
    raise RuntimeError(f"request failed after {RETRIES + 1} attempts: {last_error}")


def load_sitemap(site: Site) -> list[str]:
    queue = [site.sitemap_url]
    seen_sitemaps: set[str] = set()
    pages: list[str] = []
    while queue:
        sitemap_url = queue.pop(0)
        if sitemap_url in seen_sitemaps:
            continue
        seen_sitemaps.add(sitemap_url)
        if len(seen_sitemaps) > MAX_SITEMAPS:
            raise ValueError(f"sitemap tree exceeds {MAX_SITEMAPS} files")
        status, final_url, body = fetch(sitemap_url)
        if status != 200:
            raise ValueError(f"sitemap returned HTTP {status}: {sitemap_url}")
        if urllib.parse.urlsplit(final_url).hostname != site.canonical_host:
            raise ValueError(f"sitemap redirected to unexpected host: {final_url}")
        root = ET.fromstring(body)
        root_type = local_name(root.tag)
        if root_type == "sitemapindex":
            queue.extend(
                (node.text or "").strip()
                for entry in root
                if local_name(entry.tag) == "sitemap"
                for node in entry
                if local_name(node.tag) == "loc" and (node.text or "").strip()
            )
        elif root_type == "urlset":
            pages.extend(
                (node.text or "").strip()
                for entry in root
                if local_name(entry.tag) == "url"
                for node in entry
                if local_name(node.tag) == "loc" and (node.text or "").strip()
            )
            if len(pages) > MAX_URLS:
                raise ValueError(f"sitemap contains more than {MAX_URLS} URLs")
        else:
            raise ValueError(f"unexpected sitemap root: {root_type}")
    return pages


def inspect_page(url: str) -> Page:
    page = Page(url=url)
    try:
        page.status, page.final_url, body = fetch(url)
        if page.status != 200:
            return page
        parser = MetadataParser()
        parser.feed(body.decode("utf-8", "replace"))
        page.title = " ".join(parser.title.split())
        page.h1 = [" ".join(value.split()) for value in parser.h1]
        page.canonicals = parser.canonicals
        page.robots = parser.robots
        page.alternates = [
            (lang, urllib.parse.urljoin(url, href))
            for lang, href in parser.alternates
        ]
    except Exception as error:  # noqa: BLE001
        page.error = f"{type(error).__name__}: {error}"
    return page


def audit_site(site: Site) -> tuple[list[str], int]:
    errors: list[str] = []
    try:
        urls = load_sitemap(site)
    except Exception as error:  # noqa: BLE001
        return [f"{site.name}: sitemap: {type(error).__name__}: {error}"], 0

    duplicates = len(urls) - len(set(urls))
    if duplicates:
        errors.append(f"{site.name}: sitemap contains {duplicates} duplicate URL(s)")
    url_set = set(urls)
    unexpected_hosts = sorted({
        urllib.parse.urlsplit(url).hostname or ""
        for url in urls
        if urllib.parse.urlsplit(url).hostname != site.canonical_host
    })
    if unexpected_hosts:
        errors.append(f"{site.name}: sitemap has unexpected hosts: {', '.join(unexpected_hosts)}")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(inspect_page, url): url for url in url_set}
        pages = [future.result() for future in as_completed(futures)]

    titles: dict[str, list[str]] = defaultdict(list)
    pages_by_url = {page.url: page for page in pages}
    for page in pages:
        label = f"{site.name}: {page.url}"
        if page.error:
            errors.append(f"{label}: {page.error}")
            continue
        if page.status != 200:
            errors.append(f"{label}: HTTP {page.status} -> {page.final_url}")
            continue
        if urllib.parse.urlsplit(page.final_url).hostname != site.canonical_host:
            errors.append(f"{label}: final host is {urllib.parse.urlsplit(page.final_url).hostname}")
        if not page.title:
            errors.append(f"{label}: missing title")
        else:
            titles[page.title.casefold()].append(page.url)
        if not page.h1 or not any(page.h1):
            errors.append(f"{label}: missing H1")
        canonicals = page.canonicals or []
        if len(canonicals) != 1:
            errors.append(f"{label}: expected one canonical, found {len(canonicals)}")
        elif urllib.parse.urlsplit(urllib.parse.urljoin(page.url, canonicals[0])).hostname != site.canonical_host:
            errors.append(f"{label}: canonical host is not {site.canonical_host}")
        if any("noindex" in value for value in (page.robots or [])):
            errors.append(f"{label}: meta robots/googlebot contains noindex")

        alternates = page.alternates or []
        languages = [lang for lang, _ in alternates]
        repeated = sorted(lang for lang, count in Counter(languages).items() if count > 1)
        if repeated:
            errors.append(f"{label}: duplicate hreflang value(s): {', '.join(repeated)}")
        for lang, target in alternates:
            if urllib.parse.urlsplit(target).hostname != site.canonical_host:
                errors.append(f"{label}: hreflang {lang} target uses unexpected host: {target}")
            elif target not in url_set:
                errors.append(f"{label}: hreflang {lang} target is not in sitemap: {target}")
            elif target != page.url:
                target_page = pages_by_url.get(target)
                if target_page and not any(back == page.url for _, back in (target_page.alternates or [])):
                    errors.append(f"{label}: hreflang target does not link back: {target}")

    duplicate_titles = {title: urls for title, urls in titles.items() if len(urls) > 1}
    for title, matching_urls in duplicate_titles.items():
        errors.append(
            f"{site.name}: duplicate title ({len(matching_urls)} pages): "
            + ", ".join(matching_urls[:5])
            + f" — {title[:120]}"
        )
    return errors, len(pages)


def main() -> int:
    summaries: list[tuple[str, int, int]] = []
    all_errors: list[str] = []
    for site in SITES:
        errors, count = audit_site(site)
        summaries.append((site.name, count, len(errors)))
        all_errors.extend(errors)

    lines = [
        "# Monthly full-site SEO audit",
        "",
        "Read-only audit of every URL in each production sitemap: status, final/canonical host, title, H1, noindex, duplicate titles, and hreflang targets/return links.",
        "",
        "| Site | Sitemap pages checked | Issues |",
        "|---|---:|---:|",
    ]
    for name, count, issue_count in summaries:
        lines.append(f"| {name} | {count} | {issue_count} |")
    lines.extend(["", f"Total issues: **{len(all_errors)}**"])
    if all_errors:
        lines.extend(["", "## Issues", ""])
        lines.extend(f"- {message}" for message in all_errors[:200])
        if len(all_errors) > 200:
            lines.append(f"- Output truncated; {len(all_errors) - 200} additional issue(s) omitted.")
    report = "\n".join(lines) + "\n"
    print(report)

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as output:
            output.write(report)
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
