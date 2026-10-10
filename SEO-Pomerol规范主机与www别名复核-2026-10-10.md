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
- 搜索索引快照仍可见 StayChina 首页旧联系人 Nicole、旧电话号码和 163 邮箱；该快照标记为约一个月前抓取，且网站品牌显示为 “StayChina · Pomerol International”。这与本轮 Googlebot UA 直接读取线上页面的结果不同，应视为索引快照滞后，不能据此认定当前线上联系信息错误。本轮未访问 GSC，因此没有重新请求抓取。
- 三站 `/robots.txt`、`/sitemap.xml`、`/llms.txt` 均返回 200。当前 `robots.txt` 明确允许 OAI-SearchBot、Claude-SearchBot、PerplexityBot、Applebot 等 AI 搜索抓取，且都设置 `Content-Signal: search=yes, ai-input=yes, ai-train=no`；这是允许搜索索引、同时声明不用于训练的组合。

## 推荐的 Cloudflare Redirect Rule

在 `pomerol.trade` Zone 建一条 Single Redirect：

- 匹配表达式：`http.host eq "www.pomerol.trade"`
- 目标 URL：`concat("https://pomerol.trade", http.request.uri.path)`
- 状态码：`301`
- 保留查询字符串：开启

这会把 `www` 全路径永久归并到已声明 canonical 的裸域，并保留原 path/query。Cloudflare 官方示例说明可将一个主机的所有路径 301 到另一 HTTPS 主机并保留路径及查询参数：[Redirect requests to a different hostname](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/)。

## 状态与验收

缺少可用的 Cloudflare API 凭据和 Wrangler 登录配置；本轮桌面自动化又无法可靠确认当前浏览器 URL，因此**尚未创建或启用 Cloudflare 规则**。

规则应用后应抽查 `www.pomerol.trade/`、`www.pomerol.trade/china-sourcing-agent/` 与带查询参数的 URL：均应永久重定向至 `pomerol.trade` 对应 URL，路径和查询参数保留；裸域目标应返回 200 且 canonical 自指。随后复跑三站主机/canonical 全站审计。
