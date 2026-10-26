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

## 补充生产复核（2026-10-27 05:50 Asia/Shanghai）

本次使用 HTTPS GET 和未通过字段校验的空 POST，对主机跳转、联系页及表单 API 做一次只读式复核。空 POST 在服务端校验失败后停止；没有创建线索、写入业务表、发送通知邮件或变更线上设置。

### 主机规范化与抓取入口

| 站点 | 主机检查 | Sitemap 页面 URL 主机 | 结论 |
|---|---|---:|---|
| Xiaodu | `http://xiaodu.tech/` → HTTPS；`www` 和 apex 首页均 308 到 `https://xiaodu.tech/zh-cn/` | 170/170 `xiaodu.tech` | canonical、首页跳转和 sitemap 对齐 |
| StayChina | apex HTTPS 308 到 `www`；`www` 首页 307 到 `/en` | 24/24 `www.staychina.org` | `www` 是已实施的规范主机，旧 GSC 页面行混杂不能归因于 DNS/重定向故障 |
| Pomerol | HTTP → HTTPS；`www` 首页 308 到 `https://pomerol.trade/en/` | 155/155 `pomerol.trade` | canonical、首页跳转和 sitemap 对齐 |

三个 robots.txt 与 sitemap.xml 均返回 HTTP 200。AI/search 指令仍为 `search=yes, ai-input=yes, ai-train=no`；指定搜索与 AI 搜索 user-agent 获准抓取，训练 user-agent 仍按当前产品策略被禁止。robots 许可本身仍不证明已抓取、收录或 AI 引用。

### 联系入口及表单路由

| 站点 | 当前生产入口 | 在线检查结果 | 邮件交付证据边界 |
|---|---|---|---|
| Xiaodu | [英文联系页](https://xiaodu.tech/en/contact/) | HTTP 200，自 canonical；表单前端提交到 `POST /api/inquiry`。`/__health` 返回 HTTP 200 和版本 `redirect-loop-fix-20260930`；空表单 API 请求按预期返回 400 `validation_error`。 | 当前 GitHub `main` 的 Worker 在 `EMAIL.send` 可用时发到 Yusuf Gmail；`wrangler.jsonc` 声明 `EMAIL` 绑定。页面另含失败后手动邮件 fallback 文案。配置/路由存在不等于本次证明了生产环境绑定或成功投递；未做会创建真实线索的有效表单提交。 |
| StayChina | [英文联系页](https://www.staychina.org/en/contact)；[公司设立咨询表单](https://www.staychina.org/en/china-setup) | 联系页 HTTP 200、自 canonical，并展示 Yusuf、电话、Gmail 和 `contact@staychina.org`；联系页没有 HTML 表单。`/en/china-setup` 有表单，提交到 `POST /api/growth/leads`；空 JSON 请求按预期返回 400 `Invalid form submission`。 | 当前 GitHub `main` 的 Worker 使用 `PORTAL_EMAIL`、`PORTAL_ADMIN_EMAIL` 和 `PORTAL_EMAIL_REPLY_TO`，配置目标为 Yusuf。API 校验通过后的真实投递未由本轮确认；没有提交有效数据或写入线索记录。 |
| Pomerol | [联系/RFQ 页面](https://pomerol.trade/contact/) | HTTP 200、自 canonical；存在询价表单，`POST /api/inquiry` 的空 JSON 请求按预期返回 400 `validation_error`。工具页仅本地生成 RFQ 草稿，不提交或保存买家字段。 | 当前 GitHub `main` Worker 有 `EMAIL.send` 时发到 Yusuf Gmail；`wrangler.jsonc` 声明对应绑定。空请求只验证路由和字段校验；本轮没有证明生产环境邮件送达，也未制造测试线索。 |

三个联系页的公开联系信息均是 Yusuf、`+86 132 4269 4270`、对应站点的 `contact@域名` 和 Gmail。实际收到业务表单通知仍以 Gmail 实收为准；本轮检查未使用虚构数据触发真实邮件，故不把“配置指定收件箱”写成“端到端收件成功”。

### 后续执行

1. 搜索/AI 抓取方面：无需因主机混杂样本改 DNS、canonical 或 sitemap；保留 sitemap 监测，并继续争取取得 GSC 同口径 query × page 导出。
2. 表单方面：联系入口、API 路由与配置目标已核实，下一步只在出现真实提交时核对对应邮件是否进入 Yusuf 收件箱；若实际未投递，再按站点查看 Cloudflare Worker 邮件 binding 与生产日志，不制造假线索。
3. 联系入口本身已足够清楚，暂不做网站改动；页面优化继续由 GSC 查询/落地页证据驱动。
