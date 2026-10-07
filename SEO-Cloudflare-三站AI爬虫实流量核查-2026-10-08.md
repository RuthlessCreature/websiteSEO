# Cloudflare 三站 AI/搜索爬虫实流量核查（2026-10-08）

## 核查范围

2026-10-08 登录 Cloudflare 控制台，分别查看 `xiaodu.tech`、`staychina.org` 与 `pomerol.trade` 的 AI Crawl Control Overview；时间筛选为控制台显示的“过去 7 天”。另查看 StayChina 的 Metrics 与 Security 面板。本文记录控制台聚合数值，不是独立抓包或引擎索引报告。面板显示的 AI/搜索爬虫标签在 Cloudflare Free 方案下主要依赖 User-Agent 识别，不能当作来源 IP 或运营方身份的密码学验证。[Cloudflare：管理 AI 爬虫](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)

## 三站概览

| Zone | AI crawler 请求 | HTTP 200 | Allowed（概数） | Unsuccessful（概数） | 面板观察 |
|---|---:|---:|---:|---:|---|
| xiaodu.tech | 2.29k | 2.1k | 约 2k | 165 | Google 爬虫访问约 3.19 MB HTML；`xiaodu.tech/` 为最常访问路径，697 次成功请求；面板较前期显示 +7813.8%，基数较小时百分比会被放大。 |
| staychina.org | 4.25k | 约 1.6k | 约 3k | 约 1k | Microsoft 爬虫读取约 5.64 MB HTML；`www.staychina.org/` 为最常访问路径，925 次成功请求；OAI-SearchBot 494 次请求。 |
| pomerol.trade | 5.44k | 4.52k | 约 5k | 139 | Meta 爬虫读取约 83.82 MB 图片；`pomerol.trade/` 为最常访问路径，949 次成功请求。Meta 图片抓取不等于被 AI 搜索或回答引用。 |

Cloudflare 计数以面板当时显示为准；“约”标记来自卡片四舍五入。`Unsuccessful` 可能由其他安全规则或源站响应错误造成，不等于 AI Crawl Control 明确封锁；状态码需结合筛选查看。[Cloudflare：分析 AI 流量](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/)

## 允许列表信号（过去 7 天）

以下是 Overview 的 crawler 汇总面板所列的 allowed 请求数。不同实体可能包含“+1/+2”附加 UA 归并项；这不是各公司真实爬虫身份核验。

| 爬虫标签 | Xiaodu | StayChina | Pomerol |
|---|---:|---:|---:|
| Googlebot | 348 | 731（另有 1 个合并项） | 684（另有 1 个合并项） |
| BingBot | 176 | 797 | 659 |
| OAI-SearchBot | 178（另有 2 个合并项） | 505（另有 2 个合并项） | 549（另有 2 个合并项） |
| Claude-SearchBot | 389（另有 2 个合并项） | 296（另有 2 个合并项） | 711（另有 2 个合并项） |
| PerplexityBot | 162（另有 1 个合并项） | 195（另有 1 个合并项） | 314（另有 1 个合并项） |
| Applebot | 299 | 107 | 445 |
| Baidu | 71 | 161 | 103 |
| Meta-ExternalAgent | 516 | 未列入当前 Overview 前列 | 1.91k |
| Bytespider | 4（另有 1 个合并项） | 0 | 0 |

### StayChina 状态与内容路径

Metrics 面板的状态码聚合可见：HTTP 200 约 1.6k、204 为 3、403 为 686、404 为 743、307 为 801、308 为 423。3xx 不一定是错误，需看目标 URL 与 canonical；4xx 中包含大量非站点内容路径探测，因此不能把全部失败归因于已收录内容页面或真实搜索引擎。

主要成功内容路径包括 `/en`（853 次 allowed）、`/en/china-setup`（66）、`/zh-cn`（45）、`/en/contact`（42）、`/en/institutions`（31）、`/zh-cn/contact`（30）、`/zh-cn/products`（28）、`/zh-cn/china-setup`（27）、`/zh-cn/foreign-teachers`（25）和 `/en/foreign-teachers`（22）。这些访问说明页面正在接收边缘请求，不等于 Search Console 收录或搜索排名。

Security 面板当前显示 Googlebot、BingBot、OAI-SearchBot、Claude-SearchBot、PerplexityBot、Baidu 与 Applebot 有 allowed 请求；Claude-User、ClaudeBot、CCBot、GPTBot、Bytespider 等若干训练/助手类标签显示被阻止。该状态与公开 robots 声明的区分意图一致，但 UA 标签本身不能证明来源。`Unsuccessful` 计数可能来自响应错误、重定向、安全规则等，不可直接解释为 AI Crawl Control 拒绝。[Cloudflare：管理 AI 爬虫](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)

Metrics 的 4xx 过滤中可见疑似扫描器探测的环境变量、配置文件与开发服务器路径。这里仅记录其位于 4xx 聚合，不将它们公开解释为被 Google 或 AI 公司访问，也不据此开放 API 或调整 WAF。若要归属真实请求，应在安全日志中核对来源 IP、时间、路径及规则事件。

## 当前 Cloudflare 设置观察

- 三个 Zone 的 **Bot Preference Sync** 在 Overview 中均显示开启；本轮未修改任何设置。
- **Markdown for agents** 显示为 Pro 方案功能，不属于当前免费配置；本轮未升级或启用。
- 本轮没有更改 DNS、WAF、robots.txt、Crawler Hints、Zone 设置、Worker 或站点部署。

## SEO 解读与下一步

1. 三站都观察到 Cloudflare 标记为搜索/AI 爬虫的实际请求，证明流量确实到达边缘；不能据此推断收录、排名、模型训练或 AI 答案引用。需要分别用 Google Search Console、Bing Webmaster Tools、Yandex Webmaster 的页面与查询数据核验结果。
2. StayChina 的 `/en/china-setup` 和联系/机构页已出现数十次 allowed 请求；下一轮应结合 GSC 页面索引和查询表现，优先改善已被抓取但没有展示/点击的核心服务页，并观察 `/en/guides` 是否得到稳定抓取。
3. 对 307/308，只为 sitemap 中的重要 canonical 页面逐条检查跳转目标与最终 canonical；不要把所有重定向或 4xx 自动视为 SEO 缺陷。
4. 对 scanner 风格 4xx 保持边缘保护；只有能用安全事件日志定位到真实搜索爬虫访问了 sitemap 目标 URL，才进一步排查挑战或 Worker 路由。
5. 在下个周期按同一筛选记录三站的 allowed、HTTP 状态、主要 URL 与 Search Console 索引变化。用同一时间窗比较，不以单次流量峰值宣称 SEO 改善。

Cloudflare 指标定义与免费计划身份限制见官方文档：[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)、[管理 AI 爬虫](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)、[分析 AI 流量](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/)。

