# Cloudflare 与 AI 搜索爬虫可见度核查

核查日期：2026-10-07  
范围：`xiaodu.tech`、`staychina.org`、`pomerol.trade` 线上 `robots.txt` 与 `llms.txt`，以及 Cloudflare、Google 对 AI 搜索可见度的公开说明。  
目的：让希望获得的 AI 搜索与答案引用爬虫能读取公开页面，同时保留对模型训练爬虫的现有限制；不把技术文件或提交回执误当成排名保证。

## 结论

- 三个站的 `robots.txt`、`llms.txt` 均返回 HTTP 200。三站都声明 `search=yes`、`ai-input=yes`、`ai-train=no`；显式允许主要 AI 搜索/访问爬虫，并对 GPTBot、ClaudeBot、Applebot-Extended 设置 `Disallow: /`。
- OpenAI 把 `OAI-SearchBot`（自动搜索抓取）与 `ChatGPT-User`（用户触发的页面访问）用途分开。若目标是 ChatGPT 搜索结果中的摘要和引用，关键是允许 `OAI-SearchBot` 并让它通过 Cloudflare；仅允许 `ChatGPT-User` 不等于可进入 ChatGPT 搜索结果。三站当前 robots 已允许 `OAI-SearchBot`。
- 这套 robots 规则把“搜索/回答时取用页面”和“训练语料抓取”分开，方向符合当前希望争取引用、同时不开放训练抓取的偏好。仅有 `Allow` 规则不保证实际抓取、索引或引用；Cloudflare WAF、自定义规则、Bot Fight Mode 或挑战页仍可能拦截请求。
- StayChina 根域实际转向 `www`；robots 声明的 sitemap 为 `https://www.staychina.org/sitemap.xml`，检查返回 200 且最终主机为 `www.staychina.org`，与规范主机一致。
- Google 官方说明：生成式搜索功能沿用基础搜索技术要求与有帮助、可靠、以用户为先的内容原则；没有专门的 AI schema 或理想字数。Google 也说明 `llms.txt` 不会帮助或损害 Google 搜索可见度。因此，`llms.txt` 应作为其他工具的可选导航文件，SEO 投入优先放在可索引正文、可靠来源、独特经验、内部链接和 Search Console 诊断。
- Cloudflare AI Crawl Control 免费方案可以按 User-Agent 识别已知 AI 爬虫并显示最近 24 小时数据；升级 Bot Management 才能使用更深入的检测 ID。它适合边缘层观察与策略管理，不等于搜索引擎站长平台，也不证明页面已被索引。

## 三站线上文件抽查

| 网站 | robots / llms | AI 搜索与访问爬虫 | 模型训练爬虫 | Sitemap |
|---|---|---|---|---|
| Xiaodu | 两者 HTTP 200 | 明确允许 `OAI-SearchBot`、`ChatGPT-User`、`Claude-SearchBot`、`Claude-User`、`PerplexityBot`、`Perplexity-User`、`Applebot`，并允许 Google、Bing 等搜索爬虫 | 明确禁止 `GPTBot`、`ClaudeBot`、`Applebot-Extended` | `https://xiaodu.tech/sitemap.xml` |
| StayChina | 两者 HTTP 200 | 同上；`/api/` 被禁止，公开页面允许 | 同上 | `https://www.staychina.org/sitemap.xml`，200；最终主机为 `www.staychina.org` |
| Pomerol | 两者 HTTP 200 | 同上；公开页面允许 | 同上 | `https://pomerol.trade/sitemap.xml` |

注：User-Agent 规则是爬虫自我声明的访问约定，不是鉴权机制。Cloudflare 的免费 AI 爬虫分类也主要依据 User-Agent 字符串；不应把它当作对伪装爬虫的强身份验证。

## Cloudflare 建议配置

1. 在每个 Zone 的 **AI Crawl Control → Crawlers** 检查实际请求量与动作。至少单独核对 `OAI-SearchBot`、`ChatGPT-User`、`Claude-SearchBot`、`Claude-User`、`PerplexityBot`、`Perplexity-User` 和 `Applebot`。对用于搜索发现、回答取用或带来引用的爬虫设为允许；训练用途爬虫继续按当前 robots 策略处理。OpenAI 明确指出 `OAI-SearchBot` 控制 ChatGPT Search 内容发现；`ChatGPT-User` 是用户触发访问，不能替代前者。
2. 检查 **AI Crawl Control → Directives** 中三站 robots 的可用状态、响应码和 Content Signals；同时查看 **Security → Events** 是否有这些爬虫命中自定义 WAF、托管规则、速率限制或挑战。允许 robots.txt 但边缘仍持续挑战，实际效果依然是爬虫无法取正文。
3. 对 StayChina 特别检查此前要求保留的爬虫挑战策略。挑战普通自动化流量可以保留；若规则按“所有非浏览器请求”或宽泛 User-Agent 直接挑战，需将经过核验的搜索/AI 搜索爬虫从挑战规则中排除，否则会抵消 robots 的 `Allow`。
4. Free 方案 Metrics 仅保留 24 小时窗口，应固定每周同一时间记录各爬虫请求、状态码、路径和 robots violation；如需较长时间序列，用导出或自有日志保存，不要假设免费面板提供历史趋势。
5. 当前已启用的 Crawler Hints / IndexNow 信号继续作为快速发现辅助。IndexNow 受理不保证抓取、收录或排名；Google 仍以 sitemap、内部链接、Search Console URL 检查与实际索引状态为主。

## 逐站优先动作

- **Xiaodu**：边缘规则重点放行 OAI/Claude/Perplexity 的 Search 与 User 爬虫；训练抓取器保留阻止。继续把工业自动化解决方案、行业页、真实可核验项目资料和清晰询盘路径作为正文优化重点。
- **StayChina**：先验证首页和 `/en/china-setup` 这类核心页面没有被挑战。该站明确服务对象和政府来源比额外堆叠 AI 文件更重要。中文服务页面与英文页面应各自可索引、互相有清楚语言链接。
- **Pomerol**：优先保护 `/china-sourcing-agent/`、采购服务支柱页、行业页与 RFQ 工具的可抓取性。案例库已声明为示例流程，不应在社媒或目录内容中包装成真实客户业绩。

## 验证边界

- 本次线上文件检查使用普通 HTTP GET，三个域名的六个文件均返回 200；这证明文件可由本次检查读取，不证明所有搜索机器人或 AI 爬虫从 Cloudflare 边缘都能无挑战读取。
- 未读取到 Cloudflare AI Crawl Control 的 Zone 面板事件数据。本报告不声称已经完成逐爬虫放行，也不声称本次边缘规则复核已通过。
- 之前发出的 IndexNow 通知与 GitHub Actions 的 sitemap 通知有重叠，收到 HTTP 200 仅代表端点接受请求，不代表收录或排名。

## 官方依据

- [Google Search：AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) — AI 搜索功能沿用基础 SEO；无特殊技术门槛，须可索引并可展示摘要。
- [Google Search：Optimizing your website for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) — 强调独特、有帮助、可靠内容；没有专用 schema 或理想字数；Google 忽略 `llms.txt`。
- [Cloudflare：AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) — 可观察并管理 AI 服务访问，适用所有方案。
- [Cloudflare：Manage AI crawlers](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/) — 可逐爬虫允许或阻止；免费识别依赖 User-Agent。
- [Cloudflare：Directives](https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/) — 可检查 robots.txt 状态、内容信号和违规。
- [Cloudflare：AI crawler reference](https://developers.cloudflare.com/ai-crawl-control/reference/bots/) — 爬虫类别、User-Agent 与运营方映射。
- [OpenAI：Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) — `OAI-SearchBot` 用于 ChatGPT Search，`GPTBot` 用于潜在模型训练，`ChatGPT-User` 用于用户触发访问，各自的 robots 设置互相独立。
