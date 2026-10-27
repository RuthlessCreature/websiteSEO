# 三站 robots、sitemap 与 canonical 线上复核

复核时间：2026-10-27（Asia/Shanghai）。通过终端对线上 URL 发起 GET 请求。

| 站点 | robots.txt | sitemap | sitemap URL 数 | 页面样例 canonical |
|---|---|---|---:|---|
| xiaodu.tech | HTTP 200 | `https://xiaodu.tech/sitemap.xml` | 170 | `https://xiaodu.tech/en/` |
| staychina.org | HTTP 200 | `https://www.staychina.org/sitemap.xml` | 24 | `https://www.staychina.org/en` |
| pomerol.trade | HTTP 200 | `https://pomerol.trade/sitemap.xml` | 155 | `https://pomerol.trade/en/` |

三个 robots 文件都声明 `Content-Signal: search=yes, ai-input=yes, ai-train=no`，允许常见搜索引擎与 AI 搜索爬虫（如 Googlebot、Bingbot、Baiduspider、Sogou、OAI-SearchBot、ChatGPT-User、Claude-SearchBot、PerplexityBot），并拒绝 GPTBot、ClaudeBot、Applebot-Extended 等训练爬虫；同时屏蔽 `/api/`。robots.txt 只表达站点方的抓取偏好，不能证明 Cloudflare WAF 实际放行，也不能证明页面已经收录或被 AI 引用。还需结合 Cloudflare 请求/安全事件和 GSC/Bing 收录数据核验。