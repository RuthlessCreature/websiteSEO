# Cloudflare 三站 AI/搜索爬虫七日复核（2026-10-10）

## 范围与口径

2026-10-10 在 Cloudflare AI Crawl Control 的 Metrics 面板分别查看 `xiaodu.tech`、`staychina.org` 与 `pomerol.trade`，时间选择为过去 7 天。本文为控制台的聚合请求统计，不是搜索引擎索引、排名、访问者或 AI 答案引用报告。User-Agent 分类可用于排查线索，但不能独立验证请求确实来自标签所代表的运营方。

## 三站汇总

| Zone | 请求总量 | Allowed | Failed | Googlebot | BingBot | OAI-SearchBot | 主要观察 |
|---|---:|---:|---:|---:|---:|---:|---|
| xiaodu.tech | 约 3k | 约 2k | 452 | 335 | 未单独复核 | 330 | 200：约 2.25k；301：85；403：367、404：71。4xx 热门路径主要是 `.env`、凭据文件、开发环境与内部 API 探测，符合自动化扫描特征；汇总面板不能证明这些请求来自搜索爬虫。 |
| staychina.org | 约 5k | 约 3k | 约 1k | 502 | 522 | 426 | 200：约 1.77k；301：9、307：683、308：822；403：543、404：717、499：2。用户此前明确要求保持该站挑战策略开启，本轮未更改。 |
| pomerol.trade | 约 6k | 约 6k | 139 | 613 | 525 | 464 | 200：约 5.16k；301：243、304：1、308：857；403：2、404：137。`/en/` 有 1,024 次请求；`/sitemap.xml` 有 117 次。 |

Xiaodu 的请求分类还显示 Meta-ExternalAgent 503、Applebot 457、Claude-SearchBot 224；Pomerol 显示 Meta-ExternalAgent 约 1.78k、Applebot 约 1.2k。StayChina 的主要内容路径包括 `/en`（827）、`/en/china-setup`（79）、`/en/contact`（50）、`/en/institutions`（41）、`/en/foreign-teachers`（37）及 `/zh-cn/contact`（32）。路径请求数代表边缘请求，不等于独立访问或搜索曝光。

## 解读与行动

1. 三个 Zone 都持续接收被 Cloudflare 标为搜索或 AI 的爬虫请求，证明有请求到达边缘；不能据此声称 URL 已收录、排名上升或被 AI 答案引用。
2. StayChina 的 Googlebot 汇总筛选显示 774 次请求：727 allowed、47 failed；状态为 200：502、3xx：225、403：4、404：43。该筛选只说明 Googlebot 标签在这个窗口中的聚合状态，不足以证明挑战策略对所有真实 Google 请求均无影响。保持当前挑战设置不变，并在 Search Console 对照重要 URL 的抓取与索引情况。
3. StayChina 总体 403/404 较高，但聚合数据没有给出足够的 crawler × path × security rule 关联，不能把失败都归因给搜索引擎。尤其 404 需区分已发布内容死链与不存在的探测路径。
4. Xiaodu 的高 403 主要路径看起来是凭据、环境配置及开发服务探测（这是基于路径名称的判断），不应为了降低 4xx 而开放这些地址。仅在安全事件日志能确认真实搜索 crawler 被挑战且目标为有效内容 URL 时，才考虑逐条修复。
5. Pomerol 的 137 个 404 值得之后以 Cloudflare 路径明细核对是否存在站内引用的旧 URL；目前仅有状态聚合，不能认定为真实死链。
6. 将 Cloudflare 请求指标与 Google Search Console、Bing Webmaster 的索引、展现及查询数据分开记录。Bing Webmaster 当前浏览器页面不可访问；本次不把它记作已验证或已导入。

## 配置变更

本轮仅查看面板，没有修改三站的 DNS、Worker、WAF、Crawler Hints、Bot Preference Sync 或其他 Zone 设置。StayChina 继续按用户先前指示保持爬虫挑战策略。Cloudflare 的 7 日数字会随滚动窗口变化，未来比较必须记录准确时间窗，并且不能把本表不同观测日的聚合数直接解释成增长或下降。
