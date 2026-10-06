# Cloudflare 搜索与 AI 爬虫边缘抽查（2026-10-06）

## 请求结果

从当前网络出口对三站英文首页发送只读 GET 请求，每站分别使用以下六种 User-Agent：Googlebot、ChatGPT-User、OAI-SearchBot、PerplexityBot、Claude-SearchBot、Baiduspider。

| 站点 | UA 探测数 | HTTP 200 | Cloudflare Challenge 标记 | 结果 |
|---|---:|---:|---|---|
| Xiaodu | 6 | 6 | 未见 cf-mitigated: challenge | 通过 |
| StayChina | 6 | 6 | 未见 cf-mitigated: challenge | 通过 |
| Pomerol | 6 | 6 | 未见 cf-mitigated: challenge | 通过 |
| **合计** | **18** | **18** | 未见 | **通过** |

响应中可见 Cloudflare server 与 cf-ray 标头，探测出口显示 HKG。Googlebot 与 ChatGPT-User 的请求也在同一轮全部返回 HTTP 200。该抽查证明三站首页在这个出口与这些自报 User-Agent 组合下没有明显的全站挑战/拦截。

## 证据边界

这不是 Cloudflare 对真实爬虫身份的认证。命令行请求可以伪造 User-Agent；本轮没有使用搜索引擎或 AI 公司的真实爬虫 IP，也未访问 Cloudflare AI Crawl Control 后台的真实 crawler 活动、robots 合规或 WAF 安全事件。HTTP 200 不证明 URL 已被收录、排名、被模型抓取或被 AI 回答引用。

Cloudflare 官方说明，AI Crawl Control 可以查看 AI 服务的访问情况并按爬虫设置规则；其免费方案主要根据 User-Agent 识别已知 AI 爬虫。Free 级别的自报 UA 抽查适合筛查明显阻断，但必须和后台真实活动数据交叉核实。见 [AI Crawl Control 概览](https://developers.cloudflare.com/ai-crawl-control/)、[管理 AI 爬虫](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)。

## 后续 Cloudflare 核查

1. 为每个 Zone 分别记录 AI Crawl Control 的时间范围、爬虫名称/类别、allowed/unsuccessful 请求、HTTP 状态分布和 robots violation。
2. 对搜索/引用型爬虫逐项确认当前操作是 Allow 还是 Challenge/Block；对训练型爬虫按 Yusuf 的既定偏好检查 robots 与边缘规则是否一致。
3. 检查 WAF、Bot Fight Mode/机器人规则及自定义规则顺序，确认它们没有意外覆盖搜索爬虫的 Allow 规则。
4. 保存后台截图或导出数据，再与 GSC、Bing Webmaster、IndexNow 及公开查询表现合并分析。不要把伪造 UA 返回 200 当作真实 crawler 验证。

本轮没有更改 Cloudflare Zone、WAF、robots.txt、网站代码或部署状态。


## 2026-10-06 搜索型 AI UA 与 robots 规则复核

本轮对三个生产域名重新读取 `robots.txt`，并以只读 GET 检查公开 URL：

- Googlebot 与 Bingbot：每站的 `/robots.txt`、`/llms.txt`、`/en/` 均返回 HTTP 200。
- OAI-SearchBot、Claude-SearchBot 与 PerplexityBot：三站的 `/en/` 均返回 HTTP 200；响应包含 Cloudflare `cf-ray`，没有 `cf-mitigated: challenge`。
- 所有三站的 `robots.txt` 均返回 HTTP 200，并声明 `Content-Signal: search=yes, ai-input=yes, ai-train=no`；搜索型爬虫 UA 允许访问站点页面并仅排除 `/api/`。
- `GPTBot`、`ClaudeBot` 与 `Applebot-Extended` 在三站 robots 规则中明确 `Disallow: /`。这与允许 OAI-SearchBot、Claude-SearchBot、PerplexityBot 抓取形成区分：可供搜索/回答使用，不开放训练型爬虫抓取。
- 这次没有更改 Cloudflare 设置、robots.txt、站点代码或部署。

| 站点 | Googlebot | Bingbot | OAI-SearchBot | Claude-SearchBot | PerplexityBot | robots.txt | llms.txt（Google/Bing UA） |
|---|---:|---:|---:|---:|---:|---:|---:|
| Xiaodu | 200 | 200 | 200 | 200 | 200 | 200 | 200 |
| StayChina | 200 | 200 | 200 | 200 | 200 | 200 | 200 |
| Pomerol | 200 | 200 | 200 | 200 | 200 | 200 | 200 |

UA 探测只能证明这些自报 UA 从本次出口访问时得到的响应，不能认证请求来自对应公司的真实爬虫 IP，也不能证明平台已抓取、引用或收录。真实爬虫到访及边缘挑战状态仍需在 Cloudflare AI Crawl Control / Security Events 与各站长平台中核实。robots 对 User-Agent 的声明才是训练爬虫应遵守的可见策略；不要用伪装成被禁止 UA 的请求来推断合法搜索型爬虫状态。


## 2026-10-06 22:30（Asia/Shanghai）Cloudflare 已验证爬虫活动复核

在 Cloudflare 控制台逐 Zone 查看 Crawler Hints 和 AI Crawl Control：三站 `Crawler Hints Beta` 开关均为开启。AI Crawl Control 安全页选择“过去 7 天”，该页面所列为 Cloudflare 识别的爬虫实体活动，不是本地伪造 UA 测试。下表分别记录“允许请求 / 未成功请求”；未成功请求不等于该爬虫在 AI Crawl Control 被封锁，Cloudflare 将其定义为其他规则或响应错误也可能导致的失败。

| Zone | Googlebot | BingBot | OAI-SearchBot | Claude-SearchBot | PerplexityBot | Baidu |
|---|---:|---:|---:|---:|---:|---:|
| Xiaodu | 292 / 13 | 151 / 3 | 145 / 7 | 349 / 6 | 125 / 8 | 63 / 20 |
| StayChina | 584 / 69 | 689 / 29 | 398 / 42 | 175 / 231 | 125 / 193 | 151 / 62 |
| Pomerol | 624 / 4 | 590 / 0 | 396 / 0 | 642 / 0 | 269 / 0 | 100 / 0 |

三个 Zone 的上表搜索/检索爬虫阻止开关均为关闭（即允许）；Xiaodu、StayChina、Pomerol 的 GPTBot 与 ClaudeBot 阻止开关均为开启，符合当前区分 AI 搜索/回答与训练用途的策略。StayChina 还阻止 Claude-User；这是独立的 AI 助手访问策略，robots.txt 中该 UA 的声明与 Cloudflare 控制台应继续保持一致复核。此次没有修改任何 Cloudflare 开关。

StayChina 指标页近 7 天显示约 4k AI 爬虫总请求、约 2k 允许、约 1k 未成功。状态码分布可见 2xx 约 1.35k（另有 3 个 204）、3xx 约 1.1k（307 为 761、308 为 341）、4xx 约 1.4k（403 为 657、404 为 741）。热门路径中 `/en` 有 724 次允许请求，`/en/china-setup` 有 47 次，`/en/contact` 有 37 次。该面板没有在本轮筛选到逐爬虫的状态码/URL 对应关系，因此目前不能确认 403 是否来自 Cloudflare Challenge、WAF、robots 不合规、上游响应或其他规则，也不能将全部 404 归因于某个爬虫。后续应在指标页以爬虫和状态码过滤，再用 Security Events 对应时间、主机、路径与规则 ID 定位；只针对确认误拦截的检索爬虫调整规则。

Cloudflare 官方定义：安全页“未成功”可以由任何规则或响应错误造成，不仅限于 AI Crawl Control 的 Block 操作；指标页的状态码分布用于区分 2xx、3xx、4xx（包含 403 和 402）与 5xx。[管理 AI 爬虫](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)、[分析 AI 流量](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/)。本轮没有更改 WAF、Bot Fight Mode、爬虫允许/封锁状态或站点部署。


## 2026-10-06 23:35（Asia/Shanghai）StayChina Googlebot 标签的状态码与路径复核

在 Cloudflare Free Zone `staychina.org` 的 AI Crawl Control > Metrics 中选 “Googlebot” 和 “过去 7 天”，图表覆盖 2026-09-30 至 2026-10-06。指标为 653 次请求：584 allowed、69 unsuccessful。状态分布完整相加为 388 个 HTTP 200、174 个 307、22 个 308、69 个 404；本筛选中没有 403 或 5xx。因而这 69 次 unsuccessful 与 Cloudflare 显示的 69 个 404 数量一致；它们不是 Cloudflare Challenge/Block 的证据。

4xx 路径榜前列包括 `/test.php`、`/.git/config`、`/api/.env.bak`、`/dist../.env`、`/push_config.json`、`/.aws/credentials`、`/.env.sample`、`/pt/id_ecdsa` 和 `/pt/telescope/requests`，还出现指向 `:8080`、`:8443` 的主机项。它们是漏洞扫描式路径，不是站点公开 sitemap 页面。3xx 路径榜约 165/196 条为根路径 `/` 的重复分组；榜中还出现 `/dist../.env`、`/.ssh/config`、随机字符串路径以及非标准端口探测。普通只读 GET 复核中，规范域根路径 `/` 返回 307 并指向 `/en`；`/en/` 返回 308 并指向 `/en`。所以可见的根路径和语言尾斜杠跳转与预期主机/路径归一化相符；其余 3xx 仍不能逐条从聚合面板确定目标。

**身份边界：**此 Zone 当前为 Cloudflare Free。Cloudflare 文档说明 User-Agent 过滤值可被伪造，可靠验证需 Bot Management 的 detection ID；因此本页标注 “Googlebot” 不能单独证明请求来自 Google。Google 官方也提醒 Googlebot User-Agent 经常被伪装，并建议用来源 IP 的反向 DNS 或其公布 IP 段验证。故不能将这批扫描式 404 归为 Google 的真实索引抓取问题，也不能据此封锁或放宽 Googlebot。参考：[Cloudflare GraphQL Analytics API](https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/)、[Cloudflare 管理 AI 爬虫](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)、[Googlebot 验证说明](https://developers.google.com/search/docs/crawling-indexing/googlebot)、[Google Search Console Crawl Stats](https://support.google.com/webmasters/answer/9679690?hl=en)。

后续低风险核验顺序：先以 GSC Crawl Stats 的 Google 爬取历史/响应类别为准；若需要逐请求归属，再从可用安全日志取得来源 IP 并按 Google 官方方法校验。只有确认是 Google 来源且是索引目标 URL 的失败，才考虑调整重定向或边缘规则。本轮没有更改 DNS、WAF、爬虫策略或网站部署。
