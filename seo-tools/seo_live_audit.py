#!/usr/bin/env python3
"""Read-only SEO availability and crawl-policy audit for the three production sites."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from html.parser import HTMLParser
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


USER_AGENT = "websiteSEO-live-audit/1.0 (+https://github.com/RuthlessCreature/websiteSEO)"
MAX_SITEMAPS = 30
MAX_URLS = 10_000
MAX_RESPONSE_BYTES = 4_000_000


@dataclass(frozen=True)
class Site:
    name: str
    robots_url: str
    sitemap_url: str
    robots_sitemap_url: str
    llms_url: str
    canonical_host: str
    sample_paths: tuple[str, ...]


SITES = (
    Site(
        "Xiaodu",
        "https://xiaodu.tech/robots.txt",
        "https://xiaodu.tech/sitemap.xml",
        "https://xiaodu.tech/sitemap.xml",
        "https://xiaodu.tech/llms.txt",
        "xiaodu.tech",
        ("/en/", "/en/contact/"),
    ),
    Site(
        "StayChina",
        "https://staychina.org/robots.txt",
        "https://www.staychina.org/sitemap-index.xml",
        "https://www.staychina.org/sitemap.xml",
        "https://www.staychina.org/llms.txt",
        "www.staychina.org",
        ("/en/", "/en/contact", "/en/china-setup"),
    ),
    Site(
        "Pomerol",
        "https://pomerol.trade/robots.txt",
        "https://pomerol.trade/sitemap.xml",
        "https://pomerol.trade/sitemap.xml",
        "https://pomerol.trade/llms.txt",
        "pomerol.trade",
        ("/en/", "/contact/", "/china-sourcing-agent/"),
    ),
)

SEARCH_BOTS = (
    "Googlebot",
    "Bingbot",
    "Baiduspider",
    "OAI-SearchBot",
    "ChatGPT-User",
    "Claude-SearchBot",
    "Claude-User",
    "PerplexityBot",
    "Perplexity-User",
)
TRAINING_BOTS = ("GPTBot", "ClaudeBot", "Applebot-Extended")
LEGACY_CONTACT_MARKERS = ("Nicole", "13923387986", "163.com")


@dataclass
class Result:
    rows: list[tuple[str, str, str]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def add(
        self,
        site: str,
        check: str,
        outcome: str,
        error: bool = False,
        warning: bool = False,
    ) -> None:
        self.rows.append((site, check, outcome))
        if error:
            self.errors.append(f"{site}: {check}: {outcome}")
        if warning:
            self.warnings.append(f"{site}: {check}: {outcome}")


def fetch(url: str) -> tuple[int, str, bytes]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xml,text/plain,*/*;q=0.8",
            "Accept-Encoding": "identity",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = response.read(MAX_RESPONSE_BYTES + 1)
            if len(data) > MAX_RESPONSE_BYTES:
                raise ValueError(f"response exceeds {MAX_RESPONSE_BYTES} bytes")
            return response.status, response.geturl(), data
    except urllib.error.HTTPError as error:
        return error.code, error.geturl(), error.read(MAX_RESPONSE_BYTES)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def parse_robots(text: str) -> list[tuple[list[str], list[tuple[str, str]]]]:
    groups: list[tuple[list[str], list[tuple[str, str]]]] = []
    agents: list[str] = []
    rules: list[tuple[str, str]] = []

    def finish() -> None:
        nonlocal agents, rules
        if agents:
            groups.append((agents, rules))
        agents, rules = [], []

    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            if agents and rules:
                finish()
            continue
        if ":" not in line:
            continue
        name, value = (part.strip() for part in line.split(":", 1))
        if name.casefold() == "user-agent":
            if agents and rules:
                finish()
            agents.append(value.casefold())
        elif name.casefold() in ("allow", "disallow") and agents:
            rules.append((name.casefold(), value))
    finish()
    return groups


def robots_allows(groups: list[tuple[list[str], list[tuple[str, str]]]], bot: str, path: str = "/") -> bool:
    bot = bot.casefold()
    exact = [rules for agents, rules in groups if bot in agents]
    selected = exact or [rules for agents, rules in groups if "*" in agents]
    if not selected:
        return True
    candidates = [rule for rules in selected for rule in rules if rule[1] and path.startswith(rule[1])]
    if not candidates:
        return True
    candidates.sort(key=lambda rule: (len(rule[1]), rule[0] == "allow"), reverse=True)
    return candidates[0][0] == "allow"


def parse_sitemap(start_url: str, result: Result, site: str) -> tuple[list[str], list[str]]:
    queue = [start_url]
    seen_sitemaps: set[str] = set()
    page_urls: list[str] = []
    sitemap_urls: list[str] = []
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
        if urllib.parse.urlsplit(final_url).hostname != urllib.parse.urlsplit(start_url).hostname:
            raise ValueError(f"sitemap redirected to an unexpected host: {final_url}")
        root = ET.fromstring(body)
        root_type = local_name(root.tag)
        if root_type == "sitemapindex":
            queue.extend(
                (element.text or "").strip()
                for sitemap in root
                if local_name(sitemap.tag) == "sitemap"
                for element in sitemap
                if local_name(element.tag) == "loc" and (element.text or "").strip()
            )
            continue
        if root_type != "urlset":
            raise ValueError(f"unexpected sitemap root element: {root_type}")
        sitemap_urls.append(sitemap_url)
        page_urls.extend(
            (element.text or "").strip()
            for url_element in root
            if local_name(url_element.tag) == "url"
            for element in url_element
            if local_name(element.tag) == "loc" and (element.text or "").strip()
        )
        if len(page_urls) > MAX_URLS:
            raise ValueError(f"sitemap contains more than {MAX_URLS} URLs")
    return page_urls, sitemap_urls


class PageMetadata(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.h1: list[str] = []
        self.canonicals: list[str] = []
        self.meta_robots: list[str] = []
        self._in_title = False
        self._in_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {key.casefold(): (value or "") for key, value in attrs}
        tag = tag.casefold()
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
            self.h1.append("")
        elif tag == "link" and attributes.get("rel", "").casefold() == "canonical":
            self.canonicals.append(attributes.get("href", ""))
        elif tag == "meta" and attributes.get("name", "").casefold() in ("robots", "googlebot"):
            self.meta_robots.append(attributes.get("content", "").casefold())

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


def page_checks(site: Site, path: str, result: Result) -> None:
    url = f"https://{site.canonical_host}{path}"
    try:
        status, final_url, body = fetch(url)
    except Exception as error:  # noqa: BLE001
        result.add(site.name, f"page {path}", str(error), error=True)
        return
    if status != 200:
        result.add(site.name, f"page {path}", f"HTTP {status}", error=True)
        return
    parser = PageMetadata()
    parser.feed(body.decode("utf-8", "replace"))
    if not parser.title.strip():
        result.add(site.name, f"page {path}", "missing title", error=True)
    if not any(value.strip() for value in parser.h1):
        result.add(site.name, f"page {path}", "missing H1", error=True)
    if len(parser.canonicals) != 1:
        result.add(site.name, f"page {path}", f"{len(parser.canonicals)} canonical tags", error=True)
    else:
        canonical_host = urllib.parse.urlsplit(parser.canonicals[0]).hostname
        if canonical_host != site.canonical_host:
            result.add(site.name, f"page {path}", f"canonical host {canonical_host!r}", error=True)
    for marker in LEGACY_CONTACT_MARKERS:
        if marker.casefold() in body.decode("utf-8", "replace").casefold():
            result.add(site.name, f"page {path}", f"legacy contact marker {marker!r} found", error=True)
    if any("noindex" in content for content in parser.meta_robots):
        result.add(site.name, f"page {path}", "page is marked noindex", error=True)
    result.add(site.name, f"page {path}", f"HTTP 200; title, H1 and canonical present; final {final_url}")


def audit_site(site: Site) -> Result:
    result = Result()
    try:
        robots_status, _, robots_body = fetch(site.robots_url)
        if robots_status != 200:
            result.add(site.name, "robots.txt", f"HTTP {robots_status}", error=True)
            return result
        robots = robots_body.decode("utf-8", "replace")
        signals = re.sub(r"\s+", "", robots).casefold()
        for signal in ("search=yes", "ai-input=yes", "ai-train=no"):
            if signal not in signals:
                result.add(site.name, "Content-Signal", f"missing {signal}", error=True)
        if all(signal in signals for signal in ("search=yes", "ai-input=yes", "ai-train=no")):
            result.add(site.name, "Content-Signal", "search and AI input allowed; AI training not permitted")
        groups = parse_robots(robots)
        blocked = [bot for bot in SEARCH_BOTS if not robots_allows(groups, bot)]
        if blocked:
            result.add(site.name, "search/AI retrieval bots", f"blocked: {', '.join(blocked)}", error=True)
        else:
            result.add(site.name, "search/AI retrieval bots", "Google, Bing, Baidu and AI retrieval bots allowed at /")
        unblocked_training = [bot for bot in TRAINING_BOTS if robots_allows(groups, bot)]
        if unblocked_training:
            result.add(site.name, "AI training bots", f"not explicitly blocked: {', '.join(unblocked_training)}")
        else:
            result.add(site.name, "AI training bots", "GPTBot, ClaudeBot and Applebot-Extended blocked at /")

        sitemap_directives = re.findall(r"(?im)^\s*sitemap\s*:\s*(\S+)", robots)
        if site.robots_sitemap_url not in sitemap_directives:
            result.add(
                site.name,
                "robots primary sitemap",
                f"expected {site.robots_sitemap_url}; found {', '.join(sitemap_directives) or 'none'}",
                warning=True,
            )
        else:
            result.add(site.name, "robots primary sitemap", f"declares {site.robots_sitemap_url}")
        if site.sitemap_url != site.robots_sitemap_url and site.sitemap_url in sitemap_directives:
            result.add(
                site.name,
                "robots supplemental sitemap index",
                "index is also advertised; confirm every child sitemap contains at least one URL",
                warning=True,
            )

        pages, leaf_sitemaps = parse_sitemap(site.sitemap_url, result, site.name)
        unique_pages = list(dict.fromkeys(pages))
        duplicates = len(pages) - len(unique_pages)
        wrong_hosts = sorted(
            {
                urllib.parse.urlsplit(url).hostname or ""
                for url in unique_pages
                if urllib.parse.urlsplit(url).hostname != site.canonical_host
            }
        )
        if duplicates:
            result.add(site.name, "sitemap URLs", f"{duplicates} duplicates", error=True)
        if wrong_hosts:
            result.add(site.name, "sitemap host", f"unexpected hosts: {', '.join(wrong_hosts)}", error=True)
        if not unique_pages:
            result.add(site.name, "sitemap URLs", "empty", error=True)
        else:
            result.add(
                site.name,
                "sitemap URLs",
                f"{len(unique_pages)} unique URLs across {len(leaf_sitemaps)} sitemap file(s)",
            )

        llms_status, _, llms_body = fetch(site.llms_url)
        if llms_status != 200 or not llms_body.strip():
            result.add(site.name, "llms.txt", f"HTTP {llms_status} or empty", error=True)
        else:
            result.add(site.name, "llms.txt", f"HTTP 200; {len(llms_body)} bytes")

        for path in site.sample_paths:
            page_checks(site, path, result)
    except Exception as error:  # noqa: BLE001
        result.add(site.name, "audit", f"{type(error).__name__}: {error}", error=True)
    return result


def main() -> int:
    result = Result()
    with ThreadPoolExecutor(max_workers=len(SITES)) as pool:
        futures = {pool.submit(audit_site, site): site for site in SITES}
        for future in as_completed(futures):
            site_result = future.result()
            result.rows.extend(site_result.rows)
            result.errors.extend(site_result.errors)
            result.warnings.extend(site_result.warnings)

    lines = [
        "# Three-site SEO live audit",
        "",
        "Read-only production checks for robots/content signals, sitemap reachability and URL consistency, llms.txt, and representative page metadata.",
        "",
        "| Site | Check | Result |",
        "|---|---|---|",
    ]
    for site, check, outcome in result.rows:
        safe_outcome = outcome.replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {site} | {check} | {safe_outcome} |")
    lines.extend(["", f"Warnings: **{len(result.warnings)}**", f"Errors: **{len(result.errors)}**"])
    summary = "\n".join(lines) + "\n"
    print(summary)

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as output:
            output.write(summary)
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())

