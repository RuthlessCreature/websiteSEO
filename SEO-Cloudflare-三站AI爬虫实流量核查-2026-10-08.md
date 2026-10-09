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



## 2026-10-08 公共页面 Cloudflare 缓存头抽查

从外部 HTTP 请求抽查三站的重要服务页与 AI 摘要文件，全部目标返回 HTTP 200，响应头可见 Server: cloudflare。主要 HTML 响应呈现不同的缓存策略：

| 页面 | 观测到的响应头 | 能确认的内容 |
|---|---|---|
| Xiaodu `/en/solutions/` | `Cache-Control: public, max-age=600`；未返回 `CF-Cache-Status` | 浏览器/缓存客户端可缓存 10 分钟；本次无法从响应头确认边缘 HIT/MISS。 |
| StayChina `/en/china-setup` | `Cache-Control: s-maxage=31536000`；未返回 `CF-Cache-Status` | 声明共享缓存新鲜期 365 天；响应头未提供 Cloudflare HIT/MISS 或 Age，不能单凭它断定 Cloudflare 实际缓存命中。上线后页面内容变更时应确认 purge/失效链路。 |
| Pomerol `/china-sourcing-agent/` | `CF-Cache-Status: HIT`、`Cache-Control: public, max-age=0, must-revalidate` | 本次 Cloudflare 明确返回 HIT，但 Cache-Control 要求复核；不表示浏览器可长期本地缓存。 |

三站 `/llms.txt` 抽查均 HTTP 200 且 Cloudflare 标记 HIT。该信号证明相应请求当前由边缘响应缓存，不代表 AI 机器人已读取或引用该文件。当前生产页面的缓存头不一致；先确认 Worker/Cache Rules 的真实缓存策略与部署 purge，再统一静态资源和 HTML 的规则，避免 StayChina 的一年共享缓存声明在无失效保障时长期提供旧联系或服务信息。不要在未确认缓存清除机制前盲目延长 HTML TTL。


## 2026-10-08 Cloudflare Cache Rules 与 Workers 响应策略交叉核对

已在三站 Zone 的 Cloudflare Dashboard 只读查看 Cache Rules 页面：Xiaodu、StayChina、Pomerol 均显示未创建 Cache Rules，也未创建 Cache Response Rules。结合已测响应头，三站页面缓存差异来自 Worker/框架返回，而不是当前 Zone Cache Rule：

- Xiaodu 的主解决方案 Worker 路由在当前 GitHub main 源码中明确为 HTML 响应设置 `Cache-Control: public, max-age=600`。
- StayChina 主公司设立页的线上响应为 `s-maxage=31536000`；当前 main 的 app/middleware 源码未发现该长 TTL 的直接声明，具体由构建/Next-on-Workers 运行时产生的头仍待核实。
- Pomerol Worker 对静态页面调用 `env.ASSETS.fetch(request)`，线上 HTML 响应为 `public, max-age=0, must-revalidate` 并显示 CF-Cache-Status HIT。

Cloudflare 官方 Workers 缓存说明明确：Zone 级 Cache Rules、Cache Response Rules 和默认缓存等级不控制 Workers Cache；Worker 响应中的 Cache-Control 才是 Workers Cache 的主要控制面。[Workers Cache 官方文档](https://developers.cloudflare.com/workers/cache/)；[Workers 与 Cache Rules 的优先级](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers-cache-rules/)。因此本轮没有为了“统一”而新建 Zone Cache Rules；这类规则不能可靠解决上述 Worker 返回头差异。

若要统一缓存行为，应在三套 Worker 源码/构建策略中统一公共 HTML 与静态端点的 Cache-Control，单独保持 API/个性化/表单请求为 no-store，并明确部署版本、静态资源哈希和页面更新的失效策略。StayChina 的一年 s-maxage 与 Pomerol 的 max-age=0 策略各自都需要先确认部署后缓存版本/更新路径，再决定改动；不能简单把所有 HTML 改成相同的高 TTL。

## 2026-10-09 Cloudflare AI 检索设置与 7 日流量复核

### 设置状态

逐个打开三站 Cloudflare Dashboard 的 Caching → Configuration 与 AI Crawl Control：

- 三站 **Crawler Hints Beta 均为启用**；这是用户先前已授权的免费 Zone 设置，本轮仅核查，未修改。
- 三站 **Bot Preference Sync 均为启用**，由 Cloudflare 将当前爬虫偏好同步到 robots.txt。
- AI Crawl Control 的 **Markdown for Agents 开关均因套餐要求 Pro 而禁用**。另以 `Accept: text/markdown` 对三个真实 HTML 页面发起只读请求，返回类型均为 `text/html`；没有发生 Markdown 转换。
- Cloudflare 当前官方文档将 Markdown for Agents 列为 Pro、Business 与 Enterprise 功能；用户已明确不充值，因此保持免费功能，不尝试升级。三站继续通过语义化 HTML、JSON-LD、robots Content-Signal 和 llms.txt 支持机器发现。[Cloudflare Markdown for Agents 文档](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/)
- Crawler Hints 官方文档说明，该功能通过缓存更新信号通知 crawler，并支持 IndexNow；Cloudflare 将发生变化的 URL 信号提交给参与的搜索引擎。该机制帮助发现更新，不保证收录或排名。[Cloudflare Crawler Hints 文档](https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/)，[Cloudflare IndexNow 公告](https://blog.cloudflare.com/cloudflare-now-supports-indexnow/)

### AI Crawl Control 最近 7 天概览

| Zone | AI crawler 总请求 | HTTP 200 | Allowed（概数） | Unsuccessful（概数） | 其他面板信号 |
|---|---:|---:|---:|---:|---|
| xiaodu.tech | 2.92k | 2.54k | 约 3k | 302 | OpenAI crawler 读取 3.78 MB HTML；首页 `/` 有 742 次成功请求。Googlebot 395、OAI-SearchBot 366、BingBot 207、PerplexityBot 187、Baidu 81 次 allowed。 |
| staychina.org | 5.29k | 1.92k | 约 4k | 约 2k | OpenAI crawler 读取 6.48 MB HTML；`/` 有 986 次成功请求，OAI-SearchBot 请求 801 次。BingBot 865、OAI-SearchBot 852、Googlebot 746、Claude-SearchBot 352、PerplexityBot 270、Baidu 181 次 allowed。 |
| pomerol.trade | 6.32k | 5.21k | 约 6k | 139 | Meta crawler 读取 83.82 MB 图片；`/` 有 1.02k 次成功请求。Googlebot 768、Claude-SearchBot 763、OAI-SearchBot 718、BingBot 695、PerplexityBot 333、Baidu 114 次 allowed。 |

数值来自每个 Zone 页面中的“过去 7 天”聚合卡片，计数和更新时刻以当次控制台为准。AI Crawl Control 按 User-Agent/Cloudflare 分类标签统计；这些数是边缘请求量，既不代表独立访客，也不证明模型引用、搜索曝光或合法来源身份。Meta 的大量图片请求也不能当作 AI 搜索引用。

### StayChina 失败响应与安全策略复核

StayChina 的 7 日 Metrics 显示 HTTP 200 1.92k、204 3；403 为 804、404 为 978、499 为 2；307 为 856、308 为 720、301 为 3。4xx 路径表出现 `/.env`、`/src/.env`、`/firebase-config.json`、`/process.env` 和开发服务器文件路径探测。它们应继续由现有 404/WAF 边界保护，不要为了 AI 抓取而放开这些路径。表中 `/` 也有 279 次 4xx，但聚合图无法归因具体爬虫或规则，不能单凭该数字认定首页阻挡搜索引擎。

Security 面板过去 24 小时对关键检索 UA 显示的动作开关：Googlebot、BingBot、OAI-SearchBot、ChatGPT-User、Claude-SearchBot、PerplexityBot 与 Perplexity-User 未勾选阻止；GPTBot、ClaudeBot、CCBot、Amazonbot 等部分训练/归档 UA 显示被阻止。Xiaodu 与 Pomerol 面板的关键开关一致。OAI-SearchBot、Googlebot、BingBot、Claude-SearchBot、PerplexityBot 的“允许”策略与其 robots 声明一致；部分 User-Agent 的 unsuccessful 计数仍需依具体路径/状态码分析，不能直接归因为 AI Crawl Control 拒绝。

### SEO 决策

1. 保持三站 Crawler Hints、Bot Preference Sync 与搜索/AI 检索 UA 允许状态；训练爬虫策略沿用当前阻止设置。本轮没有改 WAF，也没有放开未知路径。
2. 保留 Cloudflare Free 方案，不启用 Pro 专属 Markdown for Agents。这个功能不是获得 AI 引用的必要条件，当前语义化 HTML、结构化数据和可读内容仍可被爬取。
3. 三站每周记录 AI Crawl Control 的请求量与成功状态；若失败量变化，再用 status code × crawler × path 逐层定位，避免把扫描器 404、训练爬虫拒绝或普通重定向误认成搜索检索故障。
4. 把请求流量与 GSC/Bing 的索引、展现、查询报告分开衡量。当前数据证明 Google/Bing 与 AI Search crawler 确实到达 Cloudflare 边缘，但不能据此声称站点已出现在 AI 回答中。
