# 三站 robots、sitemap 与联系入口即时复核

复核时间：2026-10-27 约 03:00–03:08（Asia/Shanghai）  
方法：对生产站点执行只读 HTTPS GET；检查 robots.txt、sitemap.xml 与下表中的核心页面 HTTP 状态、canonical、可见联系信息和 `tel:`/`mailto:` 链接。没有修改生产配置或提交表单。

## 抓取控制与 sitemap

| 主机 | robots.txt | sitemap.xml | 唯一 URL 数 | 摘要 |
|---|---:|---:|---:|---|
| `xiaodu.tech` | 200 | 200 | 170 | sitemap 为 URL set；与另外两站合计 349 个 URL |
| `www.staychina.org` | 200 | 200 | 24 | sitemap 含 hreflang alternate；主机与当前 sitemap 主机一致 |
| `pomerol.trade` | 200 | 200 | 155 | sitemap 为 URL set；与 10-25 全站审计的 155 条一致 |

三站 robots.txt 均声明：`Content-Signal: search=yes, ai-input=yes, ai-train=no`。均允许 Googlebot、Bingbot、YandexBot、Baiduspider、360、Sogou 等搜索爬虫，也允许 OAI-SearchBot、ChatGPT-User、Claude-SearchBot、Claude-User、PerplexityBot、Perplexity-User 和 Applebot；GPTBot、ClaudeBot、Applebot-Extended 被禁止。三个 robots 文件都将 `/api/` 排除，并声明对应 sitemap URL。

Pomerol 当前 sitemap 的条目不含 `lastmod`；该字段不是 sitemap 必填项，因此不作为错误处理，只表示不能从 sitemap 推断页面修改时间。其 URL 数从 10-08 历史快照的 154 增至 10-25 审计记录的 155，当前请求仍为 155；增量已在 10-25 审计中出现，不是本轮的新索引变化。

robots.txt 是站点发布的抓取指令，不证明 Cloudflare 安全规则对每个请求的实际处理，也不证明搜索引擎已抓取、收录或 AI 产品已引用页面。StayChina 的现有 crawler challenge 选择未变更。

## 页面状态与联系信息

以下 7 个页面本次均返回 HTTP 200，并有指向自身规范 URL 的 canonical：

| 页面 | 标题 | 规范 URL | 可见联系人/电话/邮箱 | `mailto:` 与 `tel:` |
|---|---|---|---|---|
| [Xiaodu English 首页](https://xiaodu.tech/en/) | Industrial Automation & Smart Manufacturing \| Zhuhai Xiaodu | `https://xiaodu.tech/en/` | Yusuf、+86 132 4269 4270、Yusuf Gmail | `abd.yusuf.ibrahim.mustafa@gmail.com`、`contact@xiaodu.tech`；`tel:+8613242694270` |
| [Xiaodu English 联系页](https://xiaodu.tech/en/contact/) | Tell us about your project \| Zhuhai Xiaodu | `https://xiaodu.tech/en/contact/` | 同上 | 同上 |
| [StayChina English 首页](https://www.staychina.org/en) | China company setup, work permit & residence support \| StayChina | `https://www.staychina.org/en` | Yusuf、+86 132 4269 4270、Yusuf Gmail | `abd.yusuf.ibrahim.mustafa@gmail.com`、`contact@staychina.org`；`tel:+8613242694270` |
| [StayChina English 联系页](https://www.staychina.org/en/contact) | Contact Yusuf \| China company, work permit & residence \| StayChina | `https://www.staychina.org/en/contact` | 同上 | 同上 |
| [StayChina China setup 页](https://www.staychina.org/en/china-setup) | China Company Setup & Work Permit \| StayChina | `https://www.staychina.org/en/china-setup` | 同上 | 同上 |
| [Pomerol 服务页](https://pomerol.trade/services/) | China Sourcing Services \| Pomerol International | `https://pomerol.trade/services/` | Yusuf、+86 132 4269 4270、Yusuf Gmail | `abd.yusuf.ibrahim.mustafa@gmail.com`、`contact@pomerol.trade`；`tel:+8613242694270` |
| [Pomerol 联系页](https://pomerol.trade/contact/) | Contact Pomerol International \| Start an RFQ | `https://pomerol.trade/contact/` | 同上 | 同上 |

页面源码中出现的 `17920888140`、`15232407956`、`15310580203` 字符串均出现在 Cloudflare Insights 脚本路径或 Unsplash 图片资源 ID，而不是页面电话链接；电话链接均为 Yusuf 当前号码。表单中的 `name@example.com` 属于占位示例，不是联系邮箱。

## 后续动作

1. 记录 robots 与 sitemap 的 AI/search 指令；只要实际抓取/索引未验证，不将“允许”写成“已收录”或“已引用”。
2. Pomerol sitemap 的 155 条已与 10-25 审计一致；无需以 10-08 的旧快照重复追查该增量。
3. GSC 同窗 query/page 导出仍需单独完成。此次生产页检查不能代替搜索性能证据。
4. 所有请求均为只读 GET；没有部署、DNS、Crawler Hints 或邮件更改。
