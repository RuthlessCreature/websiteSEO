# Pomerol 规范主机与 www 别名复核（2026-10-10）

## 生产探测

使用普通 HTTP GET 读取六种主机入口根路径，并对 Pomerol 核心服务页额外复核：

| 主机入口 | 最终 URL / 状态 | 规范化结论 |
|---|---|---|
| `www.xiaodu.tech/` | HTTP 200，最终 URL 为 `https://xiaodu.tech/zh-cn/` | www 别名已跳到裸域 |
| `xiaodu.tech/` | HTTP 200 | 裸域主站 |
| `staychina.org/` | HTTP 200，最终 URL 为 `https://www.staychina.org/en` | 裸域已跳到 www 主站 |
| `www.staychina.org/` | HTTP 200 | www 主站 |
| `www.pomerol.trade/` | HTTP 200，最终仍为 www | 仍可用的重复主机别名 |
| `pomerol.trade/` | HTTP 200 | 裸域主站 |

核心页 `https://www.pomerol.trade/china-sourcing-agent/` 也返回 HTTP 200，页面 canonical 指向 `https://pomerol.trade/china-sourcing-agent/`。公开搜索样本还返回带 `www` 的 Pomerol 核心页 URL。这意味着 canonical 有声明，但请求端仍能以两个主机获得 200；对三站统一 host 信号而言，应把 Pomerol 的 `www` 请求直接 301 到裸域。

StayChina 的 `/en/china-setup` 在线页面现已显示 Yusuf 联系方式且未发现 Nicole/旧电话/163.com 标记，但公开搜索样本仍出现旧摘要。此前该 URL 的 GSC 重抓取请求已排队，本轮不重复提交。

## 推荐的 Cloudflare Redirect Rule

在 `pomerol.trade` Zone 建一条 Single Redirect：

- 匹配表达式：`http.host eq "www.pomerol.trade"`
- 目标 URL：`concat("https://pomerol.trade", http.request.uri.path)`
- 状态码：`301`
- 保留查询字符串：开启

这会把 `www` 全路径永久归并到已声明 canonical 的裸域，并保留原 path/query。Cloudflare 官方示例说明可将一个主机的所有路径 301 到另一 HTTPS 主机并保留路径及查询参数：[Redirect requests to a different hostname](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/)。

## 状态与验收

本轮已确认缺口并整理了规则配置，但**尚未创建或启用 Cloudflare 规则**。当前浏览器中的 Cloudflare 账号可打开 Zone 页面，但本轮界面控制在展开导航步骤超时，故没有声称规则已应用。

规则应用后应抽查 `www.pomerol.trade/`、`www.pomerol.trade/china-sourcing-agent/` 与带查询参数的 URL：均应返回 301 至 `pomerol.trade` 对应 URL；裸域目标应返回 200 且 canonical 自指。随后复跑三站主机/canonical 全站审计。
