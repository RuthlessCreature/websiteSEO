# Pomerol：GSC 索引与 sitemap 定向复核（2026-10-08）

## 结果摘要

在 Google Search Console 网域属性 `sc-domain:pomerol.trade` 对照核心出货前检验指南、质量检验服务页和 sitemap 报告：两页均已收录、均由 Googlebot 手机版成功抓取、均获准抓取与索引，Google 均选择自身为规范页。2026-10-08 内容更新后，针对出货前检验指南提交了一次新的 URL 重新抓取请求，页面明确确认已加入优先抓取队列；此前的基线记录未重复提交。

| 页面 | GSC 索引状态 | 最近抓取 | 规范网址 | GSC 发现信息 |
|---|---|---|---|---|
| `https://pomerol.trade/resources/guides/china-pre-shipment-inspection-guide/` | 已收录 | 2026-10-04 04:26:49；Googlebot 智能手机版；抓取成功；抓取/索引许可均为是 | 用户声明与 Google 选定均为该 URL | sitemap 与引荐来源均为 `https://pomerol.trade/sitemap.xml` |
| `https://pomerol.trade/china-quality-inspection/` | 已收录 | 2026-10-04 02:49:42；Googlebot 智能手机版；抓取成功；抓取/索引许可均为是 | 用户声明与 Google 选定均为该 URL | URL 检查的 sitemap 发现字段显示“临时处理错误”；同时列出引荐页面 `https://pomerol.trade/case-studies/20-custom-pendant-lighting-for-hospitality-interiors/` |

Pomerol 属性概览显示 **140 个网页已收录、22 个网页未收录**。GSC 的 sitemap 专页显示 `https://pomerol.trade/sitemap.xml` 状态为 **成功**，上次读取 2026-10-07，发现 154 个网页、0 个视频。

## 解读

- 两个商业落地页都已收录且 canonical 正确，不应为了提高排名而重复提交。
- 质量检验页的单 URL 检查出现 sitemap 字段“临时处理错误”，但该页面已经收录、成功抓取，且 GSC sitemap 报告整体状态成功并发现 154 个页面。这是 URL 检查的单页发现信息与 sitemap 汇总报告不一致；当前不足以断定 sitemap 全站故障。
- 该质量检验页在 GSC 同时有来自案例页的引荐记录，说明除 sitemap 外还有一条报告可见的发现路径。后续检查 sitemap 状态时优先观察该单页提示是否刷新，不要重提整个 sitemap 或批量再次请求已收录页面。
- 已收录只证明页面可出现在搜索结果，并不证明对应宽词排名、点击率或转化已达目标。

## 后续动作

1. 不要再次提交同一 URL；等待 Google 处理此次队列请求，并在后续 GSC 检查中查看新的抓取日期和搜索表现。
2. 保持指南至质量检验服务页的上下文内链，并从质量检验、工厂审核、供应商核验等相关页面反向链接到指南；每条链接锚文本应描述页面主题。
3. 不重新提交当前成功的主 sitemap。若 sitemap 专页后续转为失败，先读错误详情并通过线上 XML 核验 HTTP、XML 结构、canonical host 和 URL 清单，再处理具体错误。
4. 按页面和查询交叉查看 PSI / `china quality inspection` 相关展示、位置与点击。资源整体平均排名不能代替单查询、单 URL 排名。

## 2026-10-08 11:16（Asia/Shanghai）宽词查询与 URL 检查续核

在 Search Console 的搜索效果报告中筛选精确查询 `pre shipment inspection china`，再切换至“网页”维度：该查询只对应到指南 URL `https://pomerol.trade/resources/guides/china-pre-shipment-inspection-guide/`。筛选视图显示 5 次展示、0 次点击、平均位置 89；图表日期为 2026-09-30 至 2026-10-05，报告提示约 22 小时前更新。未筛选报告表中同一查询行当时仍显示 3 次展示，因此本记录保留筛选视图的查询—网页交叉值，并注明两种表格渲染存在差异；不把 5 次展示解释为排名改善或趋势变化。

随后从该 URL 的 GSC“检查网址”入口读取正式索引详情：页面已编入索引；Googlebot 智能手机版于 2026-10-04 04:26:49 成功抓取；允许抓取与编入索引；用户声明 canonical 与 Google 选择的 canonical 均为目标指南自身；发现及引荐来源均显示 `https://pomerol.trade/sitemap.xml`。生产 HTML 的 `dateModified` 为 2026-10-08，晚于最后一次已记录抓取日，因此本次提交一次重新抓取请求，Google UI 确认“已将网址添加到优先抓取队列中”。这是请求受理回执，不代表已重新抓取、重新编入索引或提升排名；没有再次提交。

## 可复核入口

- [Pomerol GSC 概览](https://search.google.com/search-console?resource_id=sc-domain%3Apomerol.trade)
- [Pomerol sitemap 报告](https://search.google.com/search-console/sitemaps?resource_id=sc-domain%3Apomerol.trade)
- [Pomerol 搜索效果](https://search.google.com/search-console/performance/search-analytics?resource_id=sc-domain%3Apomerol.trade)
- [出货前检验指南](https://pomerol.trade/resources/guides/china-pre-shipment-inspection-guide/)
- [质量检验服务页](https://pomerol.trade/china-quality-inspection/)
- [Pomerol 出货前检验宽词页面扩展方案](SEO-Pomerol-%E5%87%BA%E8%B4%A7%E5%89%8D%E6%A3%80%E9%AA%8C%E5%AE%BD%E8%AF%8D%E9%A1%B5%E9%9D%A2%E6%89%A9%E5%B1%95%E6%96%B9%E6%A1%88-2026-10-08.md)



