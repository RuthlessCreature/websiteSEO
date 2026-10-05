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
- Automation-List：Xiaodu 免费档案资料已准备；尚无提交/确认回执，不能记作已上线。表单的必选指南确认尚未执行。

## 目录与社媒状态

- Industrial Automation Integrators 已收到 Xiaodu 的编辑审核请求；尚未确认公开档案已经上线。
- YouTube：Xiaodu 与 StayChina 的品牌频道页面可访问；Pomerol 的 `@PomerolTrade` 返回 HTTP 404，因此不把 Pomerol 频道记为已创建。
- 目录和社媒注册只提交真实、获准公开的公司信息。目录申请、平台审核、索引通知、搜索排名和 AI 引用是不同结果，逐项记录证据。

## 可信度与资料保护

- 不公开客户询盘、凭据、内部运营日志或未经授权的私人资料。
- 不虚构客户案例、业绩、认证、经营资质、合作伙伴或排名。
- 免费提交不等于获批；被抓取不等于收录；收录不等于排名；AI 导航文件不等于 AI 推荐。
