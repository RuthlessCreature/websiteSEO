# Pomerol PSI 生产页与源码差异复核

复核时间：2026-10-27 04:06–04:10（Asia/Shanghai）  
目的：核实 PSI 指南所引用的 ISO 标准是否需要改动，并确认后续编辑应进入哪个部署源。

## 生产页只读复核

生产页：[Pre-Shipment Inspection in China: A Buyer’s Checklist Before Shipment](https://pomerol.trade/resources/guides/china-pre-shipment-inspection-guide/)。页面当前使用标题“Pre-Shipment Inspection in China Checklist | Pomerol International”，H1 为“Pre-Shipment Inspection in China: A Buyer’s Checklist Before Shipment”，正文覆盖 12 个检查步骤，并明确抽样检查不保证整批每件无缺陷。2026-10-27 日期更新已实际部署并在线复核。页面已链接：

- [ISO 2859-1:2026](https://www.iso.org/standard/2859-1)：ISO 页面显示 2026 年 1 月发布，第三版。
- [ISO 28590:2017](https://www.iso.org/standard/64622.html)：ISO 页面显示 2024 年复核确认，当前仍有效。

因此，指南使用的标准版本和一手链接已经正确；生产页现显示 `Official references checked: 2026-10-27` 与 `Guide last reviewed: 2026-10-27`。本轮已重新核对两项官方目录。未改抽样数值或采样建议；任何具体 sampling plan / AQL 值仍须质量专业人员根据实际订单和标准正文确认。

## 本地源文件对照

| 本地副本 | 当前状态 | PSI 页面与生产页的差异 |
|---|---|---|
| `E:\GitHub\SEO\pWebsiteExport\public\resources\guides\china-pre-shipment-inspection-guide\index.html` | `main` 工作目录有其他 SEO 相关未提交修改；本轮未编辑 | 标题仍是 “What Buyers Should Control”，无 ISO 2859-1:2026/ISO 28590:2017 引用，正文短于线上生产页 |
| `E:\GitHub\SEO\_pWebsiteExport-seo-work\public\resources\guides\china-pre-shipment-inspection-guide\index.html` | `main`，工作区干净，HEAD `0ba4b18` | 有 12 步指南和当前 ISO 链接，但使用 “A Buyer’s Checklist Before Shipment” 旧副标题，并保留 2026-10-08 核查日期；与生产 HTML 仍不完全一致 |
| `E:\GitHub\SEO\pWebsiteExport\_worktrees\pomerol-seo-livefix-20261007\public\resources\guides\china-pre-shipment-inspection-guide\index.html` | `seo/full-site-quality-20261007`，有大量未提交文件改动；本轮未编辑 | 页面为 “decision gate” 旧版，未包含当前生产页的两个 ISO 引用；不应清理、覆盖或重置其改动 |

## 部署源追溯结果（2026-10-27 后续核实）

Cloudflare Worker 的实际发布链路现已确认：生产仓库为 `RuthlessCreature/pWebsiteExport`，部署分支为 `main`，Worker 为 `pwebsite-export`，路由为 `pomerol.trade/*`，静态资产目录为 `public`。GitHub Actions 成功运行 #130 对应 `a0e2357cb9814209e61ea8cad1c78344d91a1fc9`；工作流执行 SEO 页面构建、验证、Wrangler 部署和生产 SEO/联系入口 smoke check。对比该 revision 的构建结果与生产页，指南 `<main>` 正文文本一致；差异集中在生成资源、页脚和 Cloudflare beacon。源文件是 `scripts/guide_overrides.json`，其中维护 `dateModified` 与 `referencesCheckedOn`，构建脚本会把它们输出到页面可见的复核日期。

根目录 `pWebsiteExport` checkout 当前落后于 origin/main 且有未提交改动；本轮没有修改、清理或覆盖它。为隔离改动，从 `origin/main` revision `a0e2357cb9814209e61ea8cad1c78344d91a1fc9` 创建独立 detached worktree：`E:\GitHub\SEO\_pWebsiteExport-review-20261027`。其中只把两个日期字段从 `2026-10-08` 更新到 `2026-10-27`，反映本轮对生产内容及官方 ISO 来源的复核。此段记录的是 04:10 的工作区状态；日期更新随后以 `ac13a6609e94612a70943e629e57d33d1e95090f` 推送并部署，生产验证见下方记录。之后另有 smoke-check 脚本修复提交 `ebd9d4d1e3f0378be14dc4e9f050375b18520881`。

## 本轮决策

1. 生产内容及标准引用无需改写；本轮仅更新两个可见复核日期。
2. 部署源已映射到 `origin/main` 的 `scripts/guide_overrides.json`。仅在干净隔离 worktree 中审阅该两行改动；不得覆盖生产 HTML 或触碰其他 checkout 的未提交内容。
3. 截至本复核初始阶段 04:10，隔离改动尚未推送；之后的提交、部署及线上回验见下方发布记录。

## 发布进度（2026-10-27 04:33 Asia/Shanghai）

已将隔离 worktree 中的两项相关改动提交并推送到 `main`：commit `ac13a6609e94612a70943e629e57d33d1e95090f`（`chore(seo): refresh PSI guide review date`）。除 `scripts/guide_overrides.json` 的两个日期字段外，同步修改 `.github/workflows/deploy-cloudflare.yml` 中对应的两条日期断言。GitHub Actions run #131（ID `40396655862`）构建、静态验证与 `Deploy Worker` 均成功，Worker 版本为 `593a9a5b-6a9f-42c0-97dc-f5ef73bc0c6e`，路由为 `pomerol.trade/*` 及 `www.pomerol.trade`。生产 smoke check 的首页重定向断言失败：检查脚本要求 www `/index.html` 返回 308 并直接到 `/en/`，实际是既有链式规范化先返回 301 到根域 `/index.html`。这是 smoke-check 断言与生产重定向链不一致；部署已经完成。随后以 HTTP 200 读取生产 PSI 页面，确认两个可见日期都是 `2026-10-27`。根域及指南实际内容均正常；仍需将 smoke 检查改为验证完整重定向链，而不是把这次部署记成失败。


## 04:39 后续验证

GitHub Actions #131 的 Wrangler 部署成功，Worker 版本 `593a9a5b-6a9f-42c0-97dc-f5ef73bc0c6e` 已提供新日期。原 smoke check 把 www→apex 的 301 规范化和应用后续 308 误判为单跳失败。我已在 `scripts/seo_live_check.py` 加入完整链路校验，并于 04:39 用同一脚本直接检查生产环境；结果通过：robots、llms、155 个 sitemap 页面、唯一标题、H1、description、canonical、可索引性、联系入口和搜索意图检查均通过。修复提交 `ebd9d4d1e3f0378be14dc4e9f050375b18520881`。由于 workflow 将此脚本列入 `paths-ignore`，该修复没有触发新 Actions run；下一次含部署路径变化的运行将自动使用新检查器。Actions #131 的历史 run 结论仍为 failure，但 Worker 部署和手动生产 smoke 均成功。
