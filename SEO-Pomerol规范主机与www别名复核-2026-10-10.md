# Pomerol 规范主机与 www 别名复核（2026-10-10）

## 生产探测

使用普通 HTTP GET 读取六种主机入口根路径，并对 Pomerol 核心服务页额外复核：

| 主机入口 | 最终 URL / 状态 | 规范化结论 |
|---|---|---|
| `www.xiaodu.tech/` | HTTP 200，最终 URL 为 `https://xiaodu.tech/zh-cn/` | www 别名已跳到裸域 |
| `xiaodu.tech/` | HTTP 200 | 裸域主站 |
| `staychina.org/` | HTTP 200，最终 URL 为 `https://www.staychina.org/en` | 裸域已跳到 www 主站 |
| `www.staychina.org/` | HTTP 200 | www 主站 |
| `www.pomerol.trade/` | HTTP 308，跳到 `https://pomerol.trade/en/` | 首页别名已永久跳到裸域 |
| `pomerol.trade/` | HTTP 200 | 裸域主站 |

核心页 `https://www.pomerol.trade/china-sourcing-agent/` 和带 `?seo_probe=1` 的版本都返回 HTTP 200，页面 canonical 指向裸域路径。说明首页已有永久主机归一化，但深层路径仍能从 www 访问，会保留双主机入口。公开搜索样本也出现带 `www` 的 Pomerol 核心页 URL。需为 Pomerol 的 www 主机补充全路径永久重定向；现有根路径行为是 308，建议统一规则可用 301。

StayChina 的 `/en/china-setup` 在线页面现已显示 Yusuf 联系方式且未发现 Nicole/旧电话/163.com 标记，但公开搜索快照仍出现旧摘要。此前该 URL 的 GSC 重抓取请求已排队，本轮不重复提交。

## 2026-10-10 补充复核

- Pomerol www 首页直接响应 `308 Location: https://pomerol.trade/en/`；www 的 `/china-sourcing-agent/` 路径及带查询参数版本仍为 `200`，规范 URL 为裸域。缺口只在深层路径，不应再描述为首页也未归一化。
- 三站已复查的主要入口均返回 200，并输出正确联系资料：Xiaodu 英文 solutions、StayChina 英文首页/公司设立页/联系页、Pomerol sourcing 服务页均显示 Yusuf 和新电话/邮箱；StayChina 同时显示 `contact@staychina.org`。
- 搜索结果中仍有旧缓存：`/en/contact` 结果显示 Nicole/旧电话/163 邮箱（标记约一个月前抓取），中文 `/zh-cn/kindergarten-foreign-teacher-recruitment` 结果也显示旧联系人（标记约三个月前）。但同一搜索服务打开 StayChina 首页时已返回 Yusuf 新资料，且最近抓取的英语指南摘要也已更新。进一步按当前 sitemap 对全部 24 个 StayChina URL 逐一用 Googlebot UA 直连：24/24 均返回成功，源码均含 Yusuf、新电话和新 Gmail，未发现 Nicole、旧电话或 163 邮箱。综合证据表明，旧信息只存在于尚未刷新的一部分搜索快照；本轮未访问 GSC，因此没有重复请求抓取。
- 三站 `/robots.txt`、`/sitemap.xml`、`/llms.txt` 均返回 200。当前 `robots.txt` 明确允许 OAI-SearchBot、Claude-SearchBot、PerplexityBot、Applebot 等 AI 搜索抓取，且都设置 `Content-Signal: search=yes, ai-input=yes, ai-train=no`；这是允许搜索索引、同时声明不用于训练的组合。

## 已部署的 Cloudflare Redirect Rule

已在 `pomerol.trade` Zone 部署 Single Redirect，规则 ID：`53ca05df4fc6450984512acc8f2ff0f3`，规则名称 `Pomerol WWW paths to apex`：

- 匹配表达式：`http.host eq "www.pomerol.trade" and http.request.uri.path ne "/"`
- 目标 URL：`concat("https://pomerol.trade", http.request.uri.path)`
- 状态码：`301`
- 保留查询字符串：开启
- Cloudflare 控制台状态：活动

此规则将非根路径的 `www` 请求永久归并到已声明 canonical 的裸域，并保留原 path/query。根路径刻意排除，因此首页继续由原有规则以 308 跳转到 `https://pomerol.trade/en/`。Cloudflare 官方示例说明可将一个主机的路径 301 到另一 HTTPS 主机并保留路径及查询参数：[Redirect requests to a different hostname](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/)。

## 状态与验收

部署后以不自动跟随重定向的外部 HTTP GET 验证：

| 请求 | 响应 | 验收 |
|---|---|---|
| `https://www.pomerol.trade/china-sourcing-agent/?seo_probe=cf-rule` | HTTP 301，`Location: https://pomerol.trade/china-sourcing-agent/?seo_probe=cf-rule` | 深层路径与查询参数均保留 |
| `https://www.pomerol.trade/` | HTTP 308，`Location: https://pomerol.trade/en/` | 原有首页语言跳转保持有效 |
| `https://pomerol.trade/china-sourcing-agent/?seo_probe=cf-rule` | HTTP 200；canonical 为 `https://pomerol.trade/china-sourcing-agent/` | 裸域目标正常且 canonical 自指 |

随后从当前 Pomerol sitemap 逐个取出 **155 个 URL**，将每个路径映射到 `www.pomerol.trade` 并发送不自动跟随重定向的 HTTP 请求：**155/155 均返回预期 301 到相同裸域 path，0 异常**。网站首页 `/` 不在 sitemap URL 集中，已单独确认其仍按原规则 308 到 `/en/`。这证明当前全部 sitemap 页面路径均已覆盖到该主机归一规则。

主机别名问题已修复。后续可复跑三站主机/canonical 全站审计，并通过 GSC 的后续抓取与 canonical 报告观察 Google 是否已处理 www 重定向；这项 HTTP 验收本身不代表 Google 已重新抓取或排名已提升。

