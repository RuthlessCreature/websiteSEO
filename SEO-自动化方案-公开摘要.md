# 三站 SEO 当前状态摘要

更新时间：2026-10-06

本文件概述三站的统一 SEO 技术基线、已完成的可验证工作和仍待外部平台确认的事项。详细运营日志保留在本地工作区，不在公开仓库发布。

## 站点与业务

| 品牌 | 规范域名 | 主体主题 |
|---|---|---|
| Xiaodu Intelligent | <https://xiaodu.tech/> | 中国工业自动化与系统集成 |
| StayChina | <https://staychina.org/> | 外籍人士在华创业、工作与居留信息/服务 |
| Pomerol International | <https://pomerol.trade/> | 面向海外买家的中国采购与供应链协调 |

`pomerol.in` 已弃用，不作为 Pomerol 的当前 SEO 域名。

## 统一技术基线

- 三站部署于 Cloudflare；生产页面由 Cloudflare 提供。
- 生产页面使用各自规范 URL、可抓取 sitemap、robots.txt 与结构化数据；多语言站点需要按真实语言版本配置自指 canonical 和相互对应的 hreflang。
- 三站提供 `/llms.txt` 作为机器导航文件。它可以给支持该格式的工具提供背景，但 Google 明确表示 `llms.txt` 不会提升或损害 Google 搜索可见度；不要把文件存在本身当作排名或 AI 引用信号。
- 三站 robots.txt 允许 Google、Bing、Baidu 及所声明的 AI 搜索/检索爬虫访问公开页面，并阻止 GPTBot、ClaudeBot 和 Applebot-Extended 的模型训练抓取。robots 声明只表达站点规则；Cloudflare WAF、速率限制或挑战仍可能拦住请求，需结合 Search Console、Bing Webmaster 与真实抓取日志验证。
- 2026-10-05 公开检查三站 `robots.txt` 均返回 HTTP 200，均声明 `Content-Signal: search=yes, ai-input=yes, ai-train=no`，并列出 Google、Bing、百度、Yandex 及 OAI/Claude/Perplexity 搜索相关爬虫允许规则。Cloudflare 官方说明 AI Crawl Control 在所有套餐可用，可查看 AI 爬虫活动及逐爬虫管理访问；三个 Zone 的后台活动和挑战/阻断记录本轮未核实，因此 robots 允许不等于边缘实际放行。见 [Cloudflare AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)。
- Cloudflare Crawler Hints 已启用；它可用缓存变化信号通知支持的搜索引擎/IndexNow 参与方内容有更新，不保证抓取、收录或排名。
- 通过 Cloudflare Email Routing 配置三个 `contact@` 地址转发至站点负责人。路由规则、已验证目标地址、公网 MX/SPF 与独立发件端到端测试均已核验。
- 三站联系入口公开姓名、电话、Gmail 和各自域名邮箱；生产页面抽查通过。

## 最新只读生产审计（2026-10-06）

SEO 专项仓库的 [月度全站审计](https://github.com/RuthlessCreature/websiteSEO/actions/runs/37345205039) 已成功运行，覆盖全部生产 sitemap URL；同一工作流还运行了首页实体关系检查。

| 站点 | Sitemap 页面检查 | 有效 JSON-LD 块 | 问题 |
|---|---:|---:|---:|
| Xiaodu | 170 | 503 | 0 |
| StayChina | 24 | 48 | 0 |
| Pomerol | 144 | 144 | 0 |
| **总计** | **338** | **695** | **0** |

三个首页的 Organization → WebSite → WebPage 实体引用及 Yusuf 联系信息检查均为 PASS，0 个问题。详见 [实体关系巡检日志](https://github.com/RuthlessCreature/websiteSEO/actions/runs/37345205039)。

### IndexNow 通知回执

- **Xiaodu：**[生产部署日志](https://github.com/RuthlessCreature/xWebsite/actions/runs/37309444760)显示 IndexNow 接受 170 个 sitemap URL，HTTP 200。
- **StayChina：**2026-10-06 重新读取 sitemap-index 及其 2 个子 sitemap，共发现 24 个规范域 URL；验证公钥文件匹配后提交给 IndexNow，HTTP 200。
- **Pomerol：**[生产部署日志](https://github.com/RuthlessCreature/pWebsiteExport/actions/runs/37297913047)显示 IndexNow 接受 144 个 sitemap URL，HTTP 200。

IndexNow 的 HTTP 200 只证明通知端接受了 URL 列表，不证明搜索引擎已抓取、收录或提升排名。全站巡检也不覆盖 Google/Bing 私有索引状态、固定地域排名、Cloudflare 安全事件日志或 AI 产品是否引用内容。StayChina sitemap 的 `lastmod` 日期已与对应页面更新对齐。

## AI 搜索与内容策略

Google 的官方生成式 AI 搜索指南说明，AI Overviews/AI Mode 延续常规搜索的抓取、索引和质量要求；页面需要可抓取、已收录并符合在 Google Search 展示摘要的资格。指南没有要求 AI 专用标记或特殊 schema，且指出 Google Search 忽略 `llms.txt`。因此优先级是：

1. 让重要商业页面可抓取、返回正常状态码、使用正确 canonical，并在 sitemap 和站内链接中可发现。
2. 页面给出直接、可核实的服务范围、适用条件、流程、负责人和来源；真实案例只在有证据且获准公开时使用。
3. 建立清楚的实体信息与有用的结构化数据，但结构化数据须与用户可见事实一致。
4. 在行业相关的真实社区、视频与专业目录中提供原创信息和可靠品牌提及；不购买垃圾链接、不制造虚假背书。
5. 不批量生成只替换城市名、同义词或问句的近似页面，也不为操纵搜索/AI 回答而规模化生成无独立价值内容。

官方依据：[Google AI 搜索优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)、[Google Search Essentials](https://developers.google.com/search/docs/essentials)、[Google 生成式 AI 内容指南](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)、[Google Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies)、[Cloudflare Crawler Hints](https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/)。

## 外部搜索可见度状态

近期公开宽词搜索样本没有证明三站已经稳定进入竞争性宽词前两页。网页搜索抽样会受国家/地区、语言、时间和个性化影响，不能作为固定排名报告。当前还没有足够的 Search Console/Bing 查询数据来声称宽词达到前 1–2 页；应以各站查询、展示、点击、平均排名、目标国家和对应落地页为基线持续比较。排名取决于搜索引擎，不能承诺具体名次。

优先做有真实需求的宽主题支柱页，补充第一手工程/业务流程证据、信息完整度、内链和可信行业引用。不要虚构客户、业绩或资质。

## 当前外部渠道待办

- Google Search Console（2026-10-05 只读核验）：三站已提交 sitemap 均显示成功；发现 URL 数为 Xiaodu 170、StayChina 24、Pomerol 144，这不等于已收录。StayChina 的 `/en/china-setup` URL 检查显示已收录；索引报告仍列有未收录页面。Xiaodu 与 Pomerol 的索引报告正在处理。当前数据不足以证明竞争性宽词稳定进入前 20；公开搜索仍可能显示 StayChina 的旧品牌/联系人摘要，而实时页面已显示 Yusuf。联系页和首页的 GSC 重新抓取请求尚未提交。
- Bing Webmaster Tools：核查 sitemap、IndexNow 活动、查询表现与 AI Performance 引用；只有通知接受记录不算收录证明。
- Yandex Webmaster：添加并验证需要覆盖的站点，再提交 sitemap。
- 百度站长平台：按官方当前准入流程核验站点验证及 sitemap 提交能力。
- Automation-List：Xiaodu 免费档案资料已准备；表单曾返回 “Unable to submit listing”。2026-10-07 已发邮件至官方 `contact@automation-list.com` 核实是否进入审核队列；尚无对方回复、提交回执或公开档案链接，不能记作已上线。表单的必选指南确认尚未执行。

## 目录与社媒状态

- Industrial Automation Integrators 已收到 Xiaodu 的编辑审核请求；尚未确认公开档案已经上线。
- YouTube：Xiaodu 与 StayChina 的品牌频道页面可访问；Pomerol 的 `@PomerolTrade` 返回 HTTP 404，因此不把 Pomerol 频道记为已创建。
- 目录和社媒注册只提交真实、获准公开的公司信息。目录申请、平台审核、索引通知、搜索排名和 AI 引用是不同结果，逐项记录证据。

## 可信度与资料保护

- 不公开客户询盘、凭据、内部运营日志或未经授权的私人资料。
- 不虚构客户案例、业绩、认证、经营资质、合作伙伴或排名。
- 免费提交不等于获批；被抓取不等于收录；收录不等于排名；AI 导航文件不等于 AI 推荐。


## 2026-10-07 生产修复与 AI 搜索跟踪补充

以下记录更新本文件此前的巡检与通知状态：

- StayChina 已部署多语言根布局修复。生产 `/zh-cn`、`/zh-cn/contact` 返回 HTTP 200，根 HTML 语言为 `zh-CN`，页面自规范且允许索引；`/en` 为 `en`。部署工作流 [#37513527528](https://github.com/RuthlessCreature/pWebsite/actions/runs/37513527528) 的 Worker 发布、生产 SEO/联系入口检查和 IndexNow 步骤均通过。
- 部署后 SEO 全站审计 [#37514644759](https://github.com/RuthlessCreature/websiteSEO/actions/runs/37514644759) 覆盖三站共 338 个 sitemap URL：Xiaodu 170、StayChina 24、Pomerol 144；有效 JSON-LD 分别为 503、48、144；页面与实体关系审计均为 0 问题。该结果检查生产可访问性和页面技术规则，不代表搜索引擎已全部收录。
- 最新生产工作流分别记录 Xiaodu 170 个 URL、StayChina 24 个 URL、Pomerol 144 个 URL 的 IndexNow 请求被接受（HTTP 200）。这只代表通知端接受 URL，后续抓取和收录仍须在各搜索引擎站长平台确认。
- Bing Webmaster Tools 的 [AI Performance 报告](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c)可查看被 AI 回答引用的页面、引用趋势及 grounding queries，涵盖 Microsoft Copilot、Bing AI 摘要和部分合作体验。它显示的是聚合引用活动，不是排名、权威度或业务效果。本轮浏览器读取报告遇到连接超时，因此尚无三站引用数量或查询数据可记录；应在浏览器恢复后分别选择三站导出/记录 30 天区间的总引用、被引 URL 与 grounding query。
- Google 当前的[生成式 AI 搜索指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)仍把标准抓取、索引、独特且有帮助的内容作为基础，并明确建议优先有效 SEO，而非所谓 AEO/GEO 技巧、无必要的内容切块或不真实提及。Google 的[有帮助内容指南](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)强调原创信息、第一手经验和相对搜索结果的实质增值。故下一轮内容工作优先补充可核验的第一手流程和证据、官方来源及清楚的服务边界；不继续堆叠同义词页或未证实案例。
- Search Console 的固定日期宽词表现和索引状态本轮未能重新读取，不能据此宣称 Google 收录已变化或排名上升；继续以站长平台实际报告为准。



## 2026-10-07 Pomerol 联系入口线上修复

- 线上抽查发现 `/china-sourcing-agent/` 页脚把 “Business email” 显示两遍；部分非英语联系页页脚也缺少统一电话/邮箱标签和 `contact@pomerol.trade`。
- 已把本地化页脚规范化移到所有语言页面生成步骤之后，并让它对标点/空格差异不重复插入标签。生产烟测现在逐项检查六种语言联系页及 China Sourcing Agent 支柱页的电话、个人邮箱和业务邮箱链接；Cloudflare 部署状态仅在生产烟测也成功后标绿。
- Pomerol 主分支部署提交 [6f0d3c7](https://github.com/RuthlessCreature/pWebsiteExport/commit/6f0d3c7b18540c66c01eef4969dd6afac0d994a4) 的 `cloudflare-worker` 状态为 success。生产烟测通过；自动 IndexNow 步骤仅在烟测通过后运行。
- 只读回验：`/zh/contact/`、`/es/contact/` 和 `/china-sourcing-agent/` 均 HTTP 200；中文、西班牙语页脚各自显示一份本地化电话、直邮、业务邮箱标签；采购代理页的 “Business email” 恰好出现一次。
- 这是联系入口与部署校验质量修复，不代表索引、AI 引用或关键词排名已有变化。

## 2026-10-08 当前增长与复测状态（覆盖较早快照）

### 当前技术与搜索引擎证据

- Cloudflare 已在三个 Free Zone 开启 Always Use HTTPS。HTTP apex/www 首页及 Pomerol 三个历史 HTTP URL 的抽样请求均最终到达 HTTPS 规范主机并返回 200；每周 SEO 巡检已纳入 6 个 apex/www 入口回归检查。
- 最新生产全量审计覆盖 348 个 sitemap URL（Xiaodu 170、StayChina 24、Pomerol 154），707 个有效 JSON-LD 区块，0 issue、0 warning。它证明公开页面在审计时可抓取和解析，不证明引擎已收录或已排名。
- 最新部署日志记录 IndexNow 接受 Xiaodu 170、StayChina 24、Pomerol 154 个 URL 的 HTTP 200 回执；通知接受不保证后续抓取、收录或排序。
- Google 索引报告（最后更新 2026-10-04）：Xiaodu 75 indexed / 105 not indexed；StayChina 27 / 51；Pomerol 140 / 22。非索引原因需按 URL 和页面价值区分，不能把所有未索引计数都当作修复缺陷。
- 目前可见的 Google 搜索效果快照：StayChina 2 clicks / 50 impressions / 平均位置 24.3；Pomerol 1 / 31 / 62.6；Xiaodu 在当前可见报告窗口为 0 / 0。窗口数据截止 2026-10-04，之后的趋势尚不能据此判断。

### 查询与页面优先级

- **StayChina：**GSC 当前筛选状态中，`company setup in china` 显示 2 次展示、平均位置 35.5，页面拆分落在 `/es`。该 URL 是英文回退页，保持 noindex 并 canonical 到英文首页；不应为获取这两个低量展示而开放它索引。真正的 `/en/china-setup` 已编入索引，最近成功抓取时间为 2026-10-07。继续通过该页面本身的标题、摘要和相关内链加强商业意图，并以之后累积的 query × page × country 数据复测。教师指南的 `guide to teaching in china` 有 28 展示，但本轮无法重新读取其页面拆分，不把旧窗口数说成实时值。
- **Pomerol：**围绕出货前检验和采购主页面持续观察查询×页面，而不是复制近似词页。GSC 尚未证明目标宽词进入前 20；现有报告平均位置 62.6。
- **Xiaodu：**英文 `/en/solutions/` 已索引且 2026-10-06 抓取成功，但当前报告窗口无展示数据。优先积累可公开、可核验的工程流程和验收材料，再从核心解决方案页建立主题内链。

### 目录与品牌实体

- YouTube 公开核验：Xiaodu（Channel ID `UCQYlG-WsgjLUaZUruqAsrVA`）与 StayChina（`UCejnhaXLiO9fpdnXfeSt1Kw`）About 页 HTTP 200；Pomerol `@PomerolTrade` HTTP 404，不能写入站点社交链接或结构化实体，需先在账号内完成公开创建并验证。
- Xiaodu 在 Industrial Automation Integrators 的档案申请显示已收到，但站内搜索仍为 0 profiles；不重复提交，待出现公开档案后再补核链接。
- 社媒与目录执行顺序：先完成各品牌官方账号资料、准确站点链接和简介，再逐个平台核对免费/付费条件与用户协议；优先发布原创、可验证的行业内容，把用户带回相应支柱页。公开发帖与接受平台法律条款须在具体平台操作前按其实际内容处理，不以注册成功当作曝光或 SEO 成果。

### 下一轮免费复测顺序

1. GSC：按同一日期窗口分别读取三个站的查询、页面、国家和设备；先复测 StayChina `company setup in china` 的真实展示 URL，再记录教师指南和两个站的商业查询变化。数据刷新前保留报告日期。
2. Bing Webmaster Tools：在连接可用时复核 Sitemap、Search Performance、IndexNow URL 抓取/索引报告和 AI Performance；不得把通知回执替代索引/引用数据。
3. Yandex 与百度：核对站点是否已验证、sitemap 状态、抓取/索引和关键词报告；没有后台数据时只记录公开结果样本并注明地区、语言及查询条件。
4. 第三方目录：优先检查已提交申请是否出现公开档案；不为数量重复创建条目，也不购买垃圾外链。
5. Cloudflare：保留当前 HTTPS 规范化与 Crawler Hints；StayChina 的挑战偏好维持用户此前选择，后续通过真实安全事件/已验证爬虫数据评估抓取影响，而不是用可伪造的 User-Agent 测试推断机器人身份。

以上是当前证据和待办，不承诺排名、收录、流量、询盘或 AI 引用结果。

### Cloudflare 真实处置日志补充（2026-10-08）

最近 7 天只读 Security Events 查询发现：StayChina 对声称为 PerplexityBot、Claude-SearchBot、Bingbot、OAI-SearchBot、Googlebot 的请求累计记录 **309 条 Bot Fight Mode managed challenge**，并有 23 条 ClaudeBot 及 5 条其他匹配 UA 的 block；Xiaodu 有 10 条 ClaudeBot 与 1 条 Baiduspider block；Pomerol 有 2 条 ClaudeBot block。StayChina 的 Claude-SearchBot/PerplexityBot 标签多天反复访问首页。

这证明规则正在对相应 User-Agent 声称请求执行 challenge/block，但不证明对方属于真实官方爬虫。当前 Cloudflare Free GraphQL 可按 User-Agent 过滤，不能用 Bot Management 的可靠 bot detection ID 验证身份。由于用户此前明确要求 StayChina 继续 challenge，本次保留原设置；此项仍是搜索/AI抓取风险待核实点，需与 Cloudflare 可靠身份信号及站长平台抓取结果交叉确认。详见[完整事件核查](SEO-实时巡检-2026-10-08.md)。

