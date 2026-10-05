#!/usr/bin/env python3
"""Read-only semantic consistency check for homepage JSON-LD entity graphs."""

from __future__ import annotations

from dataclasses import dataclass
from html.parser import HTMLParser
import json
import os
import re
import sys
import urllib.parse
import urllib.request

MAX_RESPONSE_BYTES = 4_000_000
USER_AGENT = "websiteSEO-schema-entity-audit/1.0 (+https://github.com/RuthlessCreature/websiteSEO)"
EXPECTED_PHONE_DIGITS = "8613242694270"


@dataclass(frozen=True)
class Site:
    name: str
    homepage: str
    host: str
    email_domain: str


SITES = (
    Site("Xiaodu", "https://xiaodu.tech/", "xiaodu.tech", "xiaodu.tech"),
    Site("StayChina", "https://www.staychina.org/en", "www.staychina.org", "staychina.org"),
    Site("Pomerol", "https://pomerol.trade/en", "pomerol.trade", "pomerol.trade"),
)


class JsonLdParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[str] = []
        self.canonicals: list[str] = []
        self._buffer: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.casefold(): (value or "") for key, value in attrs}
        if tag.casefold() == "link" and "canonical" in values.get("rel", "").casefold().split():
            if values.get("href"):
                self.canonicals.append(values["href"])
        if tag.casefold() == "script" and values.get("type", "").split(";")[0].strip().casefold() == "application/ld+json":
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._buffer is not None:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.casefold() == "script" and self._buffer is not None:
            self.blocks.append("".join(self._buffer))
            self._buffer = None


def fetch_page(url: str) -> tuple[int, str, bytes]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,*/*;q=0.8",
            "Accept-Encoding": "identity",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        body = response.read(MAX_RESPONSE_BYTES + 1)
        if len(body) > MAX_RESPONSE_BYTES:
            raise ValueError(f"response exceeds {MAX_RESPONSE_BYTES} bytes")
        return response.status, response.geturl(), body


def types_of(value: object) -> set[str]:
    if not isinstance(value, dict):
        return set()
    raw = value.get("@type", [])
    if isinstance(raw, str):
        return {raw.casefold()}
    if isinstance(raw, list):
        return {item.casefold() for item in raw if isinstance(item, str)}
    return set()


def collect_nodes(value: object, output: list[dict]) -> None:
    if isinstance(value, dict):
        if types_of(value):
            output.append(value)
        for child in value.values():
            collect_nodes(child, output)
    elif isinstance(value, list):
        for child in value:
            collect_nodes(child, output)


def reference_id(value: object) -> str:
    if isinstance(value, dict):
        return str(value.get("@id", ""))
    return ""


def digit_string(value: object) -> str:
    return re.sub(r"\D", "", str(value or ""))


def audit_site(site: Site) -> tuple[list[str], str]:
    errors: list[str] = []
    status, final_url, body = fetch_page(site.homepage)
    if status != 200:
        raise ValueError(f"homepage returned HTTP {status}: {final_url}")
    if urllib.parse.urlsplit(final_url).hostname != site.host:
        errors.append(f"homepage redirected to unexpected host: {final_url}")

    parser = JsonLdParser()
    parser.feed(body.decode("utf-8", "replace"))
    if len(parser.canonicals) != 1:
        errors.append(f"expected one canonical link, found {len(parser.canonicals)}")
        canonical = ""
    else:
        canonical = urllib.parse.urljoin(final_url, parser.canonicals[0])
        if urllib.parse.urlsplit(canonical).hostname != site.host:
            errors.append(f"canonical uses unexpected host: {canonical}")
    if not parser.blocks:
        return errors + ["no application/ld+json blocks found"], "none"

    roots: list[object] = []
    for index, raw in enumerate(parser.blocks, start=1):
        try:
            roots.append(json.loads(raw))
        except (json.JSONDecodeError, TypeError) as error:
            errors.append(f"invalid JSON-LD block {index}: {error}")
    nodes: list[dict] = []
    for root in roots:
        collect_nodes(root, nodes)

    organizations = [node for node in nodes if "organization" in types_of(node)]
    websites = [node for node in nodes if "website" in types_of(node)]
    webpages = [node for node in nodes if "webpage" in types_of(node)]
    if not organizations:
        errors.append("missing Organization node")
    if not websites:
        errors.append("missing WebSite node")
    if not webpages:
        errors.append("missing WebPage node")
    if not organizations or not websites or not webpages:
        return errors, ", ".join(sorted({kind for node in nodes for kind in types_of(node)})) or "none"

    organization = next((node for node in organizations if str(node.get("@id", "")).endswith("#organization")), organizations[0])
    website = next((node for node in websites if str(node.get("@id", "")).endswith("#website")), websites[0])
    webpage = next((node for node in webpages if node.get("url") == canonical), webpages[0])
    organization_id = str(organization.get("@id", ""))
    website_id = str(website.get("@id", ""))

    for label, node in (("Organization", organization), ("WebSite", website), ("WebPage", webpage)):
        node_id = str(node.get("@id", ""))
        if not node_id:
            errors.append(f"{label} is missing @id")
        elif urllib.parse.urlsplit(node_id).hostname != site.host:
            errors.append(f"{label} @id uses unexpected host: {node_id}")
        node_url = str(node.get("url", ""))
        if node_url and urllib.parse.urlsplit(node_url).hostname != site.host:
            errors.append(f"{label} url uses unexpected host: {node_url}")
    if not organization.get("name"):
        errors.append("Organization is missing name")
    if not organization.get("legalName"):
        errors.append("Organization is missing legalName")
    if reference_id(website.get("publisher")) != organization_id:
        errors.append("WebSite.publisher does not reference the Organization @id")
    if reference_id(webpage.get("isPartOf")) != website_id:
        errors.append("WebPage.isPartOf does not reference the WebSite @id")
    if reference_id(webpage.get("about")) != organization_id:
        errors.append("WebPage.about does not reference the Organization @id")

    contact_points = organization.get("contactPoint", [])
    if isinstance(contact_points, dict):
        contact_points = [contact_points]
    if not isinstance(contact_points, list):
        contact_points = []
    names = [str(item.get("name", "")).casefold() for item in contact_points if isinstance(item, dict)]
    phones = [digit_string(item.get("telephone")) for item in contact_points if isinstance(item, dict)]
    emails = [str(item.get("email", "")).casefold() for item in contact_points if isinstance(item, dict)]
    if not any(name == "yusuf" for name in names):
        errors.append("no Yusuf ContactPoint found")
    if EXPECTED_PHONE_DIGITS not in phones:
        errors.append("expected business phone not found in ContactPoint")
    if f"contact@{site.email_domain}" not in emails:
        errors.append(f"domain contact alias contact@{site.email_domain} missing from ContactPoint")
    return errors, ", ".join(sorted({kind for node in nodes for kind in types_of(node)}))


def main() -> int:
    lines = [
        "# Homepage structured-data entity audit",
        "",
        "Read-only semantic checks for the Organization -> WebSite -> WebPage graph on one production homepage per site. This verifies published markup only; it does not prove search engines adopted the entities.",
        "",
        "| Site | Schema types | Result |",
        "|---|---|---|",
    ]
    all_errors: list[str] = []
    for site in SITES:
        try:
            errors, schema_types = audit_site(site)
        except Exception as error:  # noqa: BLE001
            errors, schema_types = [f"{type(error).__name__}: {error}"], "unavailable"
        result = "PASS" if not errors else f"FAIL ({len(errors)} issue(s))"
        lines.append(f"| {site.name} | {schema_types} | {result} |")
        all_errors.extend(f"{site.name}: {error}" for error in errors)
    lines.extend(["", f"Total issues: **{len(all_errors)}**"])
    if all_errors:
        lines.extend(["", "## Issues", ""])
        lines.extend(f"- {error}" for error in all_errors)
    report = "\n".join(lines) + "\n"
    print(report)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as output:
            output.write(report)
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())

