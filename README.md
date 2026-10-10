# websiteSEO

SEO implementation notes and operational materials for three Cloudflare-hosted websites:

- **Xiaodu Intelligent** — [xiaodu.tech](https://xiaodu.tech/)
- **StayChina** — [staychina.org](https://staychina.org/)
- **Pomerol International** — [pomerol.trade](https://pomerol.trade/)

The live website code remains in each site's own repository. This repository holds cross-site SEO documentation, directory-submission materials, and social publishing drafts. It excludes website source copies, deployment bundles, credentials, environment files, and private inquiry records.

## Automated monitoring

- [Weekly production audit workflow](.github/workflows/seo-live-audit.yml) checks crawl signals, sitemap reachability/URL consistency, llms.txt, representative page metadata, and stale contact markers.
- [Weekly mobile Lighthouse audit workflow](.github/workflows/lighthouse-audit.yml) checks three representative production pages for mobile Performance, Accessibility, Best Practices, and SEO signals; stores raw Lighthouse reports plus a Markdown summary as 90-day workflow artifacts. These are lab diagnostics, not field Core Web Vitals or ranking evidence.\n- [Weekly full-site audit workflow](.github/workflows/seo-full-site-audit.yml) checks every sitemap URL for status, final host, self-canonical equality with its sitemap URL, `<html lang>` against the site's URL-language map, title/H1/noindex, legacy contact markers, JSON-LD syntax, duplicate titles, hreflang targets/return links, and social preview tags. It maps every locale prefix currently present in the Xiaodu and Pomerol production sitemaps (including Chinese, Spanish, Portuguese, Japanese, and Russian routes), and checks that unsupported StayChina locale aliases return 404/410, redirect to the English fallback, or serve a `noindex` page canonicalized to that fallback; the fallback's `<html lang>` is also checked against the language of its canonical target. Missing `og:image`, `twitter:image`, or a large-image Twitter card is reported as a warning, separate from crawl/indexing errors.
- [Weekly audit script](seo-tools/seo_live_audit.py), [full-site audit script](seo-tools/seo_full_site_audit.py), [English body-depth/editorial triage](seo-tools/seo_content_triage.py), and [structured-data entity audit](seo-tools/seo_schema_entity_audit.py) contain the read-only checks for all three production domains. The full-site audit validates locale metadata and known unsupported-locale fallbacks in addition to sitemap and hreflang integrity. The weekly audit checks the expected primary sitemap separately from any supplemental sitemap index and reports mismatches or advertised indexes with empty child sitemaps as warnings; the monthly workflow checks homepage Organization → WebSite → WebPage references and contact aliases. Each workflow writes results to the GitHub Actions run summary and saves Markdown reports as downloadable workflow artifacts for 90 days.

## Latest verified checkpoints

- [Google Search Console search and AI performance (2026-10-10)](SEO-GSC%E4%B8%89%E7%AB%99%E6%90%9C%E7%B4%A2%E4%B8%8EAI%E8%A1%A8%E7%8E%B0-2026-10-10.md)
- [Three-site full production SEO audit (2026-10-10)](SEO-%E4%B8%89%E7%AB%99%E5%85%A8%E7%AB%99%E7%BA%BF%E4%B8%8A%E5%AE%A1%E8%AE%A1-2026-10-10.md)

- [Free mobile Lighthouse weekly audit and first run (2026-10-08)](SEO-Lighthouse-免费移动端周审计-2026-10-08.md)

- [Contact details live but search result stale; refresh checklist (2026-10-08)](SEO-%E4%B8%89%E7%AB%99%E8%81%94%E7%B3%BB%E6%96%B9%E5%BC%8F%E7%B4%A2%E5%BC%95%E6%BB%9E%E5%90%8E%E5%A4%8D%E6%A0%B8%E4%B8%8E%E5%88%B7%E6%96%B0%E6%B8%85%E5%8D%95-2026-10-08.md)

- [Three-site broad-keyword page updates and production verification (2026-10-08)](SEO-%E4%B8%89%E7%AB%99%E5%AE%BD%E8%AF%8D%E9%A1%B5%E9%9D%A2%E4%BC%98%E5%8C%96%E4%B8%8E%E4%B8%8A%E7%BA%BF%E8%AE%B0%E5%BD%95-2026-10-08.md)
- [Xiaodu brand entity differentiation and search visibility (2026-10-08)](SEO-Xiaodu-%E5%AE%9E%E4%BD%93%E5%8C%BA%E5%88%86%E4%B8%8E%E6%A3%80%E7%B4%A2%E4%BC%98%E5%8C%96-2026-10-08.md)

These reports separate technical crawl health, search-engine indexing evidence, public discovery samples, and third-party publishing status. A clean crawl or an accepted sitemap does not prove rankings.

- [Three-site search entry points and AI crawler rules (2026-10-08)](SEO-%E4%B8%89%E7%AB%99%E6%90%9C%E7%B4%A2%E5%85%A5%E5%8F%A3%E4%B8%8EAI%E6%8A%93%E5%8F%96%E8%A7%84%E5%88%99%E7%BA%BF%E4%B8%8A%E5%A4%8D%E6%A0%B8-2026-10-08.md)
- [Live technical SEO audit (2026-10-08)](SEO-%E5%AE%9E%E6%97%B6%E5%B7%A1%E6%A3%80-2026-10-08.md)
- [Latest production crawl and directory status (2026-10-07)](SEO-%E7%94%9F%E4%BA%A7%E5%A4%8D%E6%A0%B8%E4%B8%8E%E7%9B%AE%E5%BD%95%E7%8A%B6%E6%80%81-2026-10-07.md)
- [Cloudflare AI crawler readiness and live robots.txt check (2026-10-07)](SEO-Cloudflare-AI%E7%88%AC%E8%99%AB%E5%8F%AF%E8%A7%81%E5%BA%A6%E6%A0%B8%E6%9F%A5-2026-10-07.md)
- [Google indexing validation notices and live sitemap audit (2026-10-07)](SEO-GSC%E6%9C%80%E6%96%B0%E7%B4%A2%E5%BC%95%E9%AA%8C%E8%AF%81%E7%8A%B6%E6%80%81-2026-10-07.md)
- [Xiaodu targeted GSC crawl request record (2026-10-08)](SEO-Xiaodu-GSC-%E5%AE%9A%E5%90%91%E6%8A%93%E5%8F%96%E8%AF%B7%E6%B1%82%E8%AE%B0%E5%BD%95-2026-10-08.md)
- [Three-site GSC search and generative AI performance (2026-10-08)](SEO-GSC%E4%B8%89%E7%AB%99%E6%90%9C%E7%B4%A2%E4%B8%8E%E7%94%9F%E6%88%90%E5%BC%8FAI%E8%A1%A8%E7%8E%B0-2026-10-08.md)
- [Cloudflare three-site AI crawler traffic review (2026-10-08)](SEO-Cloudflare-%E4%B8%89%E7%AB%99AI%E7%88%AC%E8%99%AB%E5%AE%9E%E6%B5%81%E9%87%8F%E6%A0%B8%E6%9F%A5-2026-10-08.md)
- [Xiaodu Industrial Automation Integrators directory request (2026-10-08)](SEO-Xiaodu-Industrial-Automation-Integrators-%E7%9B%AE%E5%BD%95%E7%94%B3%E8%AF%B7-2026-10-08.md)
- [Pomerol China Supply Chain Directory registration review (2026-10-08)](SEO-Pomerol-China-Supply-Chain-Directory-%E5%A4%8D%E6%A0%B8-2026-10-08.md)
- [Pomerol pre-shipment inspection broad-keyword page expansion plan (2026-10-08)](SEO-Pomerol-%E5%87%BA%E8%B4%A7%E5%89%8D%E6%A3%80%E9%AA%8C%E5%AE%BD%E8%AF%8D%E9%A1%B5%E9%9D%A2%E6%89%A9%E5%B1%95%E6%96%B9%E6%A1%88-2026-10-08.md)
- [Pomerol GSC index and sitemap check (2026-10-08)](SEO-Pomerol-GSC%E7%B4%A2%E5%BC%95%E4%B8%8Esitemap%E5%A4%8D%E6%A0%B8-2026-10-08.md)
- [StayChina broad-query discovery and content gaps (2026-10-08)](SEO-StayChina-%E5%AE%BD%E8%AF%8D%E5%85%AC%E5%BC%80%E5%8F%91%E7%8E%B0%E4%B8%8E%E5%86%85%E5%AE%B9%E5%B7%AE%E8%B7%9D-2026-10-08.md)
- [Broad-query public discovery sample (2026-10-07)](SEO-%E5%AE%BD%E8%AF%8D%E5%85%AC%E5%BC%80%E5%8F%91%E7%8E%B0%E6%A0%B7%E6%9C%AC-2026-10-07.md)
- [YouTube brand-channel visibility check (2026-10-07)](SEO-YouTube%E5%93%81%E7%89%8C%E9%A2%91%E9%81%93%E7%8A%B6%E6%80%81-2026-10-07.md)
- [Live technical audit and broad-keyword baseline (2026-10-07)](SEO-%E5%AE%9E%E6%97%B6%E5%B7%A1%E6%A3%80%E4%B8%8E%E5%AE%BD%E8%AF%8D%E5%9F%BA%E7%BA%BF-2026-10-07.md)

## Start here

- [Contact details live but search result stale; refresh checklist (2026-10-08)](SEO-%E4%B8%89%E7%AB%99%E8%81%94%E7%B3%BB%E6%96%B9%E5%BC%8F%E7%B4%A2%E5%BC%95%E6%BB%9E%E5%90%8E%E5%A4%8D%E6%A0%B8%E4%B8%8E%E5%88%B7%E6%96%B0%E6%B8%85%E5%8D%95-2026-10-08.md)

- [Live technical SEO audit (2026-10-08)](SEO-%E5%AE%9E%E6%97%B6%E5%B7%A1%E6%A3%80-2026-10-08.md)
- [Xiaodu targeted GSC crawl request record (2026-10-08)](SEO-Xiaodu-GSC-%E5%AE%9A%E5%90%91%E6%8A%93%E5%8F%96%E8%AF%B7%E6%B1%82%E8%AE%B0%E5%BD%95-2026-10-08.md)
- [Three-site GSC search and generative AI performance (2026-10-08)](SEO-GSC%E4%B8%89%E7%AB%99%E6%90%9C%E7%B4%A2%E4%B8%8E%E7%94%9F%E6%88%90%E5%BC%8FAI%E8%A1%A8%E7%8E%B0-2026-10-08.md)
- [Pomerol pre-shipment inspection broad-keyword page expansion plan (2026-10-08)](SEO-Pomerol-%E5%87%BA%E8%B4%A7%E5%89%8D%E6%A3%80%E9%AA%8C%E5%AE%BD%E8%AF%8D%E9%A1%B5%E9%9D%A2%E6%89%A9%E5%B1%95%E6%96%B9%E6%A1%88-2026-10-08.md)
- [Pomerol GSC index and sitemap check (2026-10-08)](SEO-Pomerol-GSC%E7%B4%A2%E5%BC%95%E4%B8%8Esitemap%E5%A4%8D%E6%A0%B8-2026-10-08.md)
- [Cloudflare AI crawler readiness and live robots.txt check (2026-10-07)](SEO-Cloudflare-AI%E7%88%AC%E8%99%AB%E5%8F%AF%E8%A7%81%E5%BA%A6%E6%A0%B8%E6%9F%A5-2026-10-07.md)
- [Live technical audit and broad-keyword baseline (2026-10-07)](SEO-%E5%AE%9E%E6%97%B6%E5%B7%A1%E6%A3%80%E4%B8%8E%E5%AE%BD%E8%AF%8D%E5%9F%BA%E7%BA%BF-2026-10-07.md)
- [Latest production crawl and broad-query sample (2026-10-07)](SEO-%E7%94%9F%E4%BA%A7%E5%B7%A1%E6%A3%80%E4%B8%8E%E5%AE%BD%E8%AF%8D%E6%90%9C%E7%B4%A2%E5%BF%AB%E7%85%A7-2026-10-07-2.md)
- [StayChina China company setup pillar-page publication draft](StayChina-China-Company-Setup-%E5%AE%BD%E8%AF%8D%E6%94%AF%E6%9F%B1%E9%A1%B5%E5%8F%91%E5%B8%83%E7%A8%BF.md)
- [Content-depth and case-distinctiveness review (2026-10-07)](SEO-%E5%86%85%E5%AE%B9%E6%B7%B1%E5%BA%A6%E4%B8%8E%E6%A1%88%E4%BE%8B%E5%8C%BA%E5%88%86%E5%A4%8D%E6%A0%B8-2026-10-07.md)

- [Three-site SEO status](SEO-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%96%B9%E6%A1%88-%E5%85%AC%E5%BC%80%E6%91%98%E8%A6%81.md)
- [Live technical audit and broad-keyword baseline (2026-10-07)](SEO-%E5%AE%9E%E6%97%B6%E5%B7%A1%E6%A3%80%E4%B8%8E%E5%AE%BD%E8%AF%8D%E5%9F%BA%E7%BA%BF-2026-10-07.md)
- [Current three-site live audit (2026-10-06)](SEO-%E5%AE%9E%E6%97%B6%E7%94%9F%E4%BA%A7%E5%B7%A1%E6%A3%80-2026-10-06.md)
- [Search-engine and AI crawler receipts (2026-10-07)](SEO-%E4%B8%89%E7%AB%99%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E%E4%B8%8EAI%E6%8A%93%E5%8F%96%E5%9B%9E%E6%89%A7-2026-10-07.md)
- [Full-site production recheck (2026-10-06)](SEO-%E5%85%A8%E7%AB%99%E5%A4%8D%E6%A0%B8-2026-10-06.md)
- [Search and generative AI visibility baseline (2026-10-06)](SEO-%E6%90%9C%E7%B4%A2%E4%B8%8E%E7%94%9F%E6%88%90%E5%BC%8FAI%E5%8F%AF%E8%A7%81%E5%BA%A6%E5%9F%BA%E7%BA%BF-2026-10-06.md)
- [Cloudflare crawler edge probe (2026-10-06)](SEO-Cloudflare%E7%88%AC%E8%99%AB%E8%BE%B9%E7%BC%98%E6%8A%BD%E6%9F%A5-2026-10-06.md)
- [StayChina GSC indexing check (2026-10-06)](GSC-%E7%B4%A2%E5%BC%95%E6%A0%B8%E6%9F%A5-2026-10-06.md)
- [Search-console and AI visibility report (2026-10-06)](SEO-%E7%AB%99%E9%95%BF%E5%B9%B3%E5%8F%B0%E4%B8%8EAI%E6%95%88%E6%9E%9C%E6%A0%B8%E6%9F%A5-2026-10-06.md)
- [Public search and brand signal audit (2026-10-06)](SEO-%E5%85%AC%E5%BC%80%E6%90%9C%E7%B4%A2%E4%B8%8E%E5%93%81%E7%89%8C%E4%BF%A1%E5%8F%B7%E6%A0%B8%E6%9F%A5-2026-10-06.md)
- [Broad-keyword competitive gaps and content routes (2026-10-06)](SEO-%E5%AE%BD%E8%AF%8D%E7%AB%9E%E4%BA%89%E7%BC%BA%E5%8F%A3%E4%B8%8E%E5%86%85%E5%AE%B9%E8%B7%AF%E7%BA%BF-2026-10-06.md)
- [Broad-keyword SERP and AI visibility actions (2026-10-06)](SEO-%E5%AE%BD%E8%AF%8DSERP%E4%B8%8EAI%E5%8F%AF%E8%A7%81%E5%BA%A6%E8%A1%8C%E5%8A%A8-2026-10-06.md)
- [Broad-keyword search sample and content gaps (2026-10-06)](SEO-%E5%AE%BD%E8%AF%8D%E6%90%9C%E7%B4%A2%E6%A0%B7%E6%9C%AC%E4%B8%8E%E5%86%85%E5%AE%B9%E5%B7%AE%E8%B7%9D-2026-10-06.md)
- [Main-content depth and template similarity triage (2026-10-06)](SEO-%E6%AD%A3%E6%96%87%E6%B7%B1%E5%BA%A6%E4%B8%8E%E6%A8%A1%E6%9D%BF%E7%9B%B8%E4%BC%BC%E5%BA%A6%E5%88%9D%E7%AD%9B-2026-10-06.md)
- [Broad-keyword baseline and competitive gaps](SEO-%E5%AE%BD%E8%AF%8D%E5%9F%BA%E7%BA%BF%E5%92%8C%E7%AB%9E%E4%BA%89%E5%B7%AE%E8%B7%9D-2026-10.md)
- [Full sitemap page audit](SEO-%E5%85%A8%E9%87%8F%E7%AB%99%E7%82%B9%E5%B7%A1%E6%A3%80-2026-10.md)
- [Structured-data entity audit](SEO-%E7%BB%93%E6%9E%84%E5%8C%96%E6%95%B0%E6%8D%AE%E5%AE%9E%E4%BD%93%E5%AF%B9%E9%BD%90-2026-10.md)
- [Pomerol SEO source/output drift (2026-10-06)](SEO-Pomerol%E6%BA%90%E7%A0%81%E4%B8%8E%E7%94%9F%E4%BA%A7%E6%A0%87%E8%AE%B0%E5%B7%AE%E5%BC%82-2026-10-06.md)
- [Directory submission roadmap](SEO-%E7%9B%AE%E5%BD%95%E6%8F%90%E4%BA%A4%E8%B7%AF%E7%BA%BF%E5%9B%BE-2026-10.md)
- [Directory submission pack](SEO-%E4%B8%89%E7%AB%99%E7%9B%AE%E5%BD%95%E6%8F%90%E4%BA%A4%E5%8C%85-2026-10.md)
- [Xiaodu Automation-List draft](SEO-%E7%9B%AE%E5%BD%95%E6%8F%90%E4%BA%A4%E8%8D%89%E7%A8%BF-2026-10.md)
- [Social launch materials](%E7%A4%BE%E5%AA%92%E5%90%AF%E5%8A%A8%E7%B4%A0%E6%9D%90-2026-10.md)
- [First social posts](%E7%A4%BE%E5%AA%92%E9%A6%96%E5%8F%91%E5%86%85%E5%AE%B9%E5%8C%85.md)

Submission drafts are not evidence of registration, approval, indexing, or ranking. Follow each platform's current rules and publish only verified business information.

- [Xiaodu Automation List submission profile](SEO-Xiaodu-Automation-List-申请资料-2026-10.md) — prepared from verifiable production-site claims; pending required acceptance of the directory listing guidelines.


