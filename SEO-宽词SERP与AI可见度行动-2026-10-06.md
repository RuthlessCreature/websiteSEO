# 三站宽词 SERP 与 AI 可见度行动（2026-10-06）

## 本轮证据

对三类宽主题进行了当前公开搜索抽查：

| 主题 | 当前搜索样本 | 可确认结论 | 不可推断事项 |
|---|---|---|---|
| `China sourcing agent` | 结果包含 Pomerol 的 [China Sourcing Agent 页面](https://pomerol.trade/china-sourcing-agent/) | 页面可被当前公开搜索发现；摘要呈现采购需求、流程与服务环节 | 搜索工具未提供可复现地区、设备和精确位置；不能确认是否进入 Google 前 20，也不能代表所有查询或地区 |
| `industrial automation system integrator China` | 样本突出显示 [SENTRADO 系统集成页](https://sentrado.com/industrial-automation-integrator) | 竞争页面明确展示技术栈、Siemens 授权、工程团队、行业和交付证据 | 没有证据证明 Xiaodu 固定排名或完全未收录 |
| `company setup in China for foreigners` | 样本显示 China Briefing、TKEG、政府入口及有明确流程/费用/时效的服务商 | 竞争主题更新频繁，法规来源与决策流程覆盖较深 | 没有证据证明 StayChina 固定排名或完全未收录 |

样本不是排名追踪。是否达到前 20，应以同一国家/语言/日期窗口的 GSC、Bing 查询位置或可复现的 SERP 记录核验。

## 三站下一步执行顺序

### 1. Pomerol：把宽词曝光转为可核验的采购方法

- 保留 `/china-sourcing-agent/` 作为 `China sourcing agent` 的唯一主要商业着陆页；指南、服务页、RFQ 工具和案例资源向它提供清楚的上下文链接，避免多个商业页重复争同一主词。
- 强化现有 RFQ Builder 的独特信息：每个字段如何减少报价假设差异，买方应提供哪些证据，如何记录 revision、样品偏差、验收标准与交货责任。页面要说明模板用途与边界，避免将工具页面做成仅有表单的薄页。
- 公开一套空白、可下载的报价可比矩阵、供应商核验记录、样品版本变更单和出货交接清单；标注由买方、供应商或 Pomerol 协调方填写。没有授权的实际项目继续标示为匿名化或示意，不用它们暗示可独立核验的客户业绩。
- 后续衡量该主页面的非品牌宽词展示、点击、平均位置、询盘和 AI 引用页数；不要把单次 SERP 出现等同于前两页。

### 2. Xiaodu：以工程可信证据竞争，而非堆叠集成关键词

- 为 `industrial automation system integrator` 保持一个主商业入口，并在其页面直接说明确实承接的控制平台、协议、服务地区、设计/编程/柜体/现场集成/调试/维护范围及不承接事项。
- 把可公开的工程方法做成一份核心材料：脱敏 I/O 清单、测试验收表、控制柜/HMI 图解或从需求到调试的流程图。每项须经业务负责人确认和发布授权；未核实的品牌授权、团队规模、行业客户、产能和案例不发布。
- 将一手材料与相关指南、服务页和联系入口互链。没有可验证材料前，不以新增地区页或机械替换关键词扩张页面数量。

### 3. StayChina：用官方来源和复核责任建立决策型内容

- 将 `company setup in China for foreigners` 作为主要主题入口，按外国个人/境外公司、业务活动、城市、经营地址和运营需求组织路径；每个高风险规则点链接政府或法规原文，说明适用地区、最后复核日期和具体限制。
- 为投资准入、登记、银行开户、税务/发票、招聘、工作许可/居留等主题指定复核责任；明确哪些是信息整理与协调服务，哪些必须由政府、律师、会计或许可服务方确认。
- 优先补足读者下一步决策需要的文件准备清单、流程分歧、地区差异和更新日志，而不是只重复通用定义。法规页面需在官方规则变化后复核。

## AI 可见度：按官方数据测量

- **Bing / Copilot：** Bing Webmaster Tools 已提供 AI Performance 报告，可查看被引用 URL、引用变化和 grounding queries。为三站逐一核对已验证资源的报告入口并保存相同时间窗导出；报告没数据就记录为尚无可见引用数据。该报告记录引用活动，不是排名或流量的替代指标。[Bing AI Performance 文档](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c)
- **Google AI 搜索：** 按 Search Console 的 Generative AI performance 报告记录页面、国家和日期范围，并与传统搜索查询分开。符合索引和摘要展示资格仍是前提。[Google AI 搜索指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **内容方式：** 用独有的一手方法、证据和行业知识回答真实决策问题；保持页面可抓取、可索引、正文清晰，主张有来源，必要时配真实图像/视频。FAQ、短段落或结构化数据本身不是排名捷径。
- **文件边界：** 可继续维护 `llms.txt` 作为给其他工具的辅助索引，但 Google 官方说明 Google Search 不使用 `llms.txt`，不会因该文件获得额外搜索可见度。投入优先级应放在真实内容、收录资格、外部可信提及及 Search Console/Bing 数据上。
- **Cloudflare 边缘核验：** `robots.txt` 的允许规则和普通 HTTP 200 不足以证明真实验证爬虫通过 Cloudflare。对 Googlebot、Bingbot、Baiduspider、OAI-SearchBot、PerplexityBot 等，需从 Cloudflare 安全事件/爬虫分析确认实际行为。保持已确认的 StayChina 挑战策略；先读真实事件证据，不因 AI SEO 主张自动放宽防护。

## 内容规模与质量边界

可借鉴大型垂直站的主题分类、内链、工具、视频和规律更新，不能照搬其页面体量或用批量低价值页面冲量。Google 当前 AI 搜索指南仍要求 people-first 的独特价值，并明确反对为覆盖查询变体而制造缺乏价值的大量页面；`llms.txt`、机械化 FAQ 和非真实外链提及都不能替代质量。[Google AI 搜索指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) [Google Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies)

## 后续每周记录表

每个域名按固定的国家、语言、设备和 28 天窗口记录：

1. GSC/Bing 非品牌宽主题查询的 impressions、clicks、CTR、average position 和 landing URL。
2. 索引异常 URL 数、canonical 选择、抓取错误与 sitemap 对账差异。
3. Bing AI Performance 的 citations、cited pages、grounding queries；Google AI performance 中可用的生成式 AI 展示数据。
4. Cloudflare verified crawler 的实际请求/挑战/拦截事件；不要只按 user-agent 字符串下结论。
5. 外部目录/社媒状态分别记为草稿、已提交、审核中、已公开、失败；不把账号创建或提交回执当作排名。

这轮公开抽样只确认 Pomerol 的一个目标页出现在一份宽词结果样本中。Xiaodu、StayChina 的前 20 目标仍缺少可复现位置证据；三站目标排名均未达成验证。

## 2026-10-06 核心着陆页与标题生产复核

05:58（Asia/Shanghai）对三站宽主题入口做 HTTP/HTML 核对，均返回 HTTP 200，title、description 与 H1 清楚对应主题：

| 站点 | 核心 URL | Title / H1 检查 |
|---|---|---|
| Xiaodu | `https://xiaodu.tech/en/solutions/` | Title 和 H1 都是 “Industrial Automation System Integrator in China”；description 说明 Zhuhai-based 系统集成范围 |
| StayChina | `https://www.staychina.org/en/china-setup` | Title “China Company Setup & Work Permit | StayChina”；H1 指向外籍创办人的 China company setup 路径 |
| Pomerol | `https://pomerol.trade/china-sourcing-agent/` | Title “China Sourcing Agent for Overseas Buyers | Pomerol International”；H1 是对应 China sourcing agent 的主要服务入口 |

本次也抽查了两个 Pomerol illustrative scenario 页。现网 title 分别为 “Machine-vision BOM and motion-control | Pomerol International” 和 “CNC machined parts with dimensional | Pomerol International”，末尾关键名词 “sourcing” 与 “inspection” 被省掉。原因是生成器新增了 “China Sourcing Scenario” 后缀，而最后的 70 字符 title 整理仅处理旧 “China Sourcing Case” 后缀。草稿 PR [#41](https://github.com/RuthlessCreature/pWebsiteExport/pull/41) 增加对新旧后缀的统一处理；按当前 36 个案例标题对生成逻辑作静态比较，预计其中 2 个 title 会恢复完整的产品/验收词。PR 仍待仓库验证及合并，尚未部署。

以上 title/H1 核对是页面元数据检查，不能证明目标关键词达到前 20；宽词排名仍以各站 GSC/Bing 固定市场与日期范围内的 query-page 数据为准。


## 2026-10-06 搜索快照与线上联系信息复核

新一轮公开搜索工具曾返回 StayChina 英文页的旧摘要，摘要中显示旧品牌联系人 “Nicole” 与旧邮箱，且结果标注为上月抓取。为避免把缓存误判为线上故障，今天直接打开线上英文首页、`/en/china-setup` 和 `/en/contact` 复核：三页正文都显示 Yusuf、+86 132 4269 4270、abd.yusuf.ibrahim.mustafa@gmail.com；联系页也列出 contact@staychina.org。公司设立页的标题为 “China Company Setup & Work Permit | StayChina”，H1 为 “China company setup for foreign founders should start with the route, not the licence.”

**判断与动作：**联系人已在当前线上正文统一；旧搜索摘要是过期快照，本轮不改站点代码。继续观察后续搜索摘要是否更新；若主要页面已重新抓取仍展示旧实体信息，再检查缓存/索引状态和页面结构化实体数据。该公开搜索视图没有提供可复现的排名位置，因此不能据此判断目标词排名。

