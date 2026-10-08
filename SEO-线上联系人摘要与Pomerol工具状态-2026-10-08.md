# 线上联系人摘要与 Pomerol 工具状态

检查时间：2026-10-08（Asia/Shanghai）  
范围：公开搜索摘要、生产联系页、Pomerol 新工具 URL。只读核查。

## 结果

| 项目 | 线上结果 | 含义 |
|---|---|---|
| StayChina 英文联系页 | HTTP 200；标题和正文为 Yusuf，公开电话 `+86 13242694270`，地址为 `abd.yusuf.ibrahim.mustafa@gmail.com` 和 `contact@staychina.org` | 生产联系入口正确。网页搜索曾返回旧 Nicole/163 邮箱摘要，但打开当前 URL 后已是 Yusuf；这是搜索摘要滞后，不应据此改动已正确的页面。 |
| Pomerol 联系页 | HTTP 200；Yusuf、`+86 132 4269 4270`、Gmail 和 `contact@pomerol.trade` 均显示 | 生产联系入口正确。 |
| Pomerol 供应商证据追踪器 `/tools/china-supplier-verification-kit/` | HTTP 404 | 本地实现尚未部署，不能把该页描述为已上线、可提交索引或已带来 SEO 流量。 |
| Pomerol sitemap | HTTP 200 | 当前线上 sitemap 可读取；新增工具页还未出现在生产站点中。 |

## 搜索与 AI 可见性处理

1. 不为消除旧搜索摘要而改写已正确的 StayChina 联系页。待摘要刷新后再核查；如旧联系方式持续影响用户，优先检查 Search Console 中该 URL 的最新抓取和重新抓取状态。
2. Pomerol 工具页目前只存在于本地 `pWebsiteExport` 快照，连同生成脚本、样式、浏览器端交互、sitemap、`llms.txt` 与上下文内链变更。生产返回 404，故尚未形成可供搜索引擎或 AI 抓取的页面。
3. 按本轮操作范围，仅更新和推送 `websiteSEO` 文档仓库；没有推送 `xWebsite`、`pWebsite` 或 `pWebsiteExport`，也没有触发站点部署。
4. 页面未来正式上线后，先从生产复查 HTTP 200、canonical、robots、页面正文、sitemap 与 `llms.txt`，再通过现有站点通知流程提交；回执只代表通知端接受，不代表收录或排名。

## 证据链接

- [StayChina 当前英文联系页](https://www.staychina.org/en/contact)
- [Pomerol 当前联系页](https://pomerol.trade/contact/)
- [Pomerol 供应商证据追踪器（当前 404）](https://pomerol.trade/tools/china-supplier-verification-kit/)
- [Pomerol 当前 sitemap](https://pomerol.trade/sitemap.xml)

本记录描述的是检查时的生产状态，不构成页面已收录、排名提升、AI 引用或询盘增长的证据。
