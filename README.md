# websiteSEO

SEO implementation notes and operational materials for three Cloudflare-hosted websites:

- **Xiaodu Intelligent** — [xiaodu.tech](https://xiaodu.tech/)
- **StayChina** — [staychina.org](https://staychina.org/)
- **Pomerol International** — [pomerol.trade](https://pomerol.trade/)

The live website code remains in each site's own repository. This repository holds cross-site SEO documentation, directory-submission materials, and social publishing drafts. It excludes website source copies, deployment bundles, credentials, environment files, and private inquiry records.

## Automated monitoring

- [Weekly production audit workflow](.github/workflows/seo-live-audit.yml) checks crawl signals, sitemap reachability/URL consistency, llms.txt, representative page metadata, and stale contact markers.
- [Monthly full-site audit workflow](.github/workflows/seo-full-site-audit.yml) checks every sitemap URL for status/canonical/title/H1/noindex, legacy contact markers, JSON-LD syntax, duplicate titles, and hreflang targets/return links.
- [Weekly audit script](seo-tools/seo_live_audit.py) and [full-site audit script](seo-tools/seo_full_site_audit.py) contain the read-only checks for all three production domains. Each workflow writes its results to the GitHub Actions run summary.

## Start here

- [Three-site SEO status](SEO-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%96%B9%E6%A1%88-%E5%85%AC%E5%BC%80%E6%91%98%E8%A6%81.md)
- [Broad-keyword baseline and competitive gaps](SEO-%E5%AE%BD%E8%AF%8D%E5%9F%BA%E7%BA%BF%E5%92%8C%E7%AB%9E%E4%BA%89%E5%B7%AE%E8%B7%9D-2026-10.md)
- [Full sitemap page audit](SEO-%E5%85%A8%E9%87%8F%E7%AB%99%E7%82%B9%E5%B7%A1%E6%A3%80-2026-10.md)
- [Structured-data entity audit](SEO-%E7%BB%93%E6%9E%84%E5%8C%96%E6%95%B0%E6%8D%AE%E5%AE%9E%E4%BD%93%E5%AF%B9%E9%BD%90-2026-10.md)
- [Directory submission roadmap](SEO-%E7%9B%AE%E5%BD%95%E6%8F%90%E4%BA%A4%E8%B7%AF%E7%BA%BF%E5%9B%BE-2026-10.md)
- [Directory submission pack](SEO-%E4%B8%89%E7%AB%99%E7%9B%AE%E5%BD%95%E6%8F%90%E4%BA%A4%E5%8C%85-2026-10.md)
- [Xiaodu Automation-List draft](SEO-%E7%9B%AE%E5%BD%95%E6%8F%90%E4%BA%A4%E8%8D%89%E7%A8%BF-2026-10.md)
- [Social launch materials](%E7%A4%BE%E5%AA%92%E5%90%AF%E5%8A%A8%E7%B4%A0%E6%9D%90-2026-10.md)
- [First social posts](%E7%A4%BE%E5%AA%92%E9%A6%96%E5%8F%91%E5%86%85%E5%AE%B9%E5%8C%85.md)

Submission drafts are not evidence of registration, approval, indexing, or ranking. Follow each platform's current rules and publish only verified business information.
