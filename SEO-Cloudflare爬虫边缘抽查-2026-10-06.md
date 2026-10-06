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
