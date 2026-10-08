#!/usr/bin/env python3
"""Summarize Lighthouse JSON reports for the weekly three-site SEO audit."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REPORTS = {
    "Xiaodu — industrial automation solutions": "lighthouse-reports/xiaodu-solutions.json",
    "StayChina — China company setup": "lighthouse-reports/staychina-setup.json",
    "Pomerol — pre-shipment inspection guide": "lighthouse-reports/pomerol-psi-guide.json",
}
CATEGORIES = (
    ("performance", "Performance"),
    ("accessibility", "Accessibility"),
    ("best-practices", "Best Practices"),
    ("seo", "SEO"),
)
METRICS = (
    ("largest-contentful-paint", "LCP (lab)"),
    ("cumulative-layout-shift", "CLS (lab)"),
    ("total-blocking-time", "TBT (lab)"),
    ("speed-index", "Speed Index (lab)"),
)


def score_text(value: object) -> str:
    if not isinstance(value, (int, float)):
        return "n/a"
    return str(round(value * 100))


def cell(value: object) -> str:
    return str(value if value not in (None, "") else "n/a").replace("|", "\\|").replace("\n", " ")


def main() -> None:
    rows: list[str] = []
    details: list[str] = []
    missing: list[str] = []

    for label, report_path in REPORTS.items():
        path = Path(report_path)
        if not path.exists():
            missing.append(report_path)
            continue

        report = json.loads(path.read_text(encoding="utf-8"))
        categories = report.get("categories", {})
        audits = report.get("audits", {})
        values = [score_text(categories.get(key, {}).get("score")) for key, _ in CATEGORIES]
        metric_values = [audits.get(audit_id, {}).get("displayValue", "n/a") for audit_id, _ in METRICS]
        rows.append("| " + " | ".join([label, *values, *(cell(value) for value in metric_values)]) + " |")

        lighthouse_version = report.get("lighthouseVersion", "unknown")
        details.append(f"### {label}\n\nLighthouse {lighthouse_version}.")
        seo_refs = categories.get("seo", {}).get("auditRefs", [])
        seo_failures = []
        for ref in seo_refs:
            audit = audits.get(ref.get("id"), {})
            score = audit.get("score")
            if isinstance(score, (int, float)) and score < 1 and audit.get("scoreDisplayMode") in {"binary", "numeric"}:
                seo_failures.append(f"- {audit.get('title', ref.get('id'))}: {audit.get('displayValue', 'needs review')}")
        details.append(
            "\n".join(["SEO-category audits below full score:", *(seo_failures[:8] or ["- None reported"])])
        )

        opportunities = []
        for audit in audits.values():
            savings = audit.get("details", {}).get("overallSavingsMs")
            if audit.get("details", {}).get("type") == "opportunity" and isinstance(savings, (int, float)) and savings > 0:
                opportunities.append((savings, audit.get("title", "Opportunity"), audit.get("displayValue", "")))
        opportunities.sort(reverse=True)
        if opportunities:
            details.append(
                "\nLargest lab opportunities:\n"
                + "\n".join(f"- {title}: {display} (estimated {round(savings)} ms)" for savings, title, display in opportunities[:3])
            )

    table_header = "| Page | Performance | Accessibility | Best Practices | SEO | LCP (lab) | CLS (lab) | TBT (lab) | Speed Index (lab) |"
    separator = "|---|---:|---:|---:|---:|---:|---:|---:|---:|"
    lines = [
        "# Weekly mobile Lighthouse audit",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        table_header,
        separator,
        *(rows or ["| No Lighthouse reports were produced | — | — | — | — | — | — | — | — |"]),
        "",
        "This is a single mobile lab run per representative page. Scores and timings can vary with the runner, cache, and network; they are diagnostics, not field Core Web Vitals, rankings, or a guarantee of search visibility. Do not compare runs unless the Lighthouse version and strategy are recorded.",
        "",
        *details,
    ]
    if missing:
        lines.extend(["", "## Missing reports", "", *(f"- {path}" for path in missing)])
    Path("lighthouse-reports/summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
