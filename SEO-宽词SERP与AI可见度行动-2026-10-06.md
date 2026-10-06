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

## 2026-10-06 09:25 当前宽词搜索样本补充

用公开网页搜索对三组商业宽词再次抽样。工具没有提供可复现的引擎、国家、语言界面、设备或排名位置，因此只记搜索结果样本与竞争内容特征，不记名次，也不推断未显示即未收录。

| 宽主题 | 本次样本可见结果 | 可采取的内容动作 | 证据边界 |
|---|---|---|---|
| China sourcing agent | YunSource、Sourcing Agent China、NovaLink 等服务商结果；本次可见列表未出现 Pomerol | 在主服务页提供可核验的服务范围、采购决策步骤、质量/物流交接边界和原创空白工具；只有业务资料能证明的团队、订单数、国家覆盖或检测能力才可公开 | 竞争者的团队、客户和订单数字是各自网站自述，不是第三方核验，也不是可复制的文案 |
| China industrial automation system integrator | 出现 RevenueBase 的中国集成商目录，说明其匹配会读取公司自己的公开描述、网站和 LinkedIn；样本没有呈现可确认的 Xiaodu 名次 | 统一官网和 LinkedIn 的公司简介，准确写出实际系统集成类别、控制平台、项目边界与服务地区；如目录资料不准确，用其公开纠错渠道处理，不购买数据产品来制造排名信号 | RevenueBase 的列表按其追踪到的团队规模排序，且只展示 824 家中的前 25；未展示 Xiaodu 不足以判断是否被收录 |
| company setup in China for foreigners | 上海市政府登记服务入口、TKEG 外籍人士设立指南等结果；TKEG 页面显示 2026-09-30 更新并引用官方规则 | StayChina 重点补强法规原文链接、适用主体/城市、最近复核日期、文件与流程决策路径，并清晰区分信息整理、协调服务和主管机关/专业服务方的决定 | 搜索样本不能证明 StayChina 固定排名。TKEG 对流程、成本和时限的描述属于该页面内容，须逐项以官方来源核实 |

来源： [上海市政府公司登记入口](https://english.shanghai.gov.cn/en-Business-BusinessSetup-CompanyRegistration/)、[TKEG 外籍投资者设立指南](https://tkegexpat.com/guide/cn/china-company-incorporation)、[RevenueBase 中国工业自动化集成商列表](https://revenuebase.ai/companies/industrial-automation-system-integrators/china)、[YunSource 中国采购服务](https://www.yunsource.com/)、[Sourcing Agent China](https://www.sourcingagentchina.org/)。

本轮没有新的 Search Console/Bing Webmaster 查询位置或 AI citations 数据；三站目标宽词是否进入前 20 仍未验证。



## 2026-10-06 16:02（Asia/Shanghai）宽主题复抽样

通过公开网页搜索分别抽查 `China sourcing agent`、`industrial automation system integrator China`、`company setup in China for foreigners` 与 `teach English in China jobs`。搜索工具没有固定国家/地区、语言界面、设备或可复现 SERP 序号；以下是本轮返回样本，不是排名报告。

| 宽主题 | 本轮样本页面 | 对三站的实际差距与下一步 |
|---|---|---|
| China sourcing agent | [YunSource](https://www.yunsource.com/)、[Sourcing Agent China](https://www.sourcingagentchina.org/)、[JiangSourcing](https://jiangsourcing.com/) | 多家页面把供应商筛选、报价、QC、物流、响应流程连成一条可理解的执行路径，并展示其自述运营规模。Pomerol 应强化真实可验证的步骤、费用/职责边界、供应商决策工具和来源清楚的原创证据；不能抄用对方的订单量、客户数、团队规模或认证，也不能把 illustrative case 写成已交付客户项目。本轮返回项未出现 Pomerol，不能据此断言未收录或固定排名。 |
| Industrial automation system integrator China | [SENTRADO](https://sentrado.com/)、[苏州高西自动化](https://www.sipem.cn/)、[正泰自动化](https://www.chintautomation.com/about/)、[Actemium China](https://www.actemium.cn/) | 结果把工程系统、技术栈、服务范围、认证/组织证据和交付环节写得具体。Xiaodu 应优先发布经业务方确认的实际集成技术、工程流程、测试/调试材料、售后边界和所在地；若没有凭证，不添加第三方品牌授权、产能、团队规模或项目数字。本轮样本没有提供 Xiaodu 可复现位置。 |
| Company setup in China for foreigners | [Asomerit](https://asomerit.com/)、[Supro](https://suprocorpservice.com/)、[上海市政府英文登记入口](https://english.shanghai.gov.cn/en-Business-BusinessSetup-CompanyRegistration/) | 商业服务页细分设立、银行、税务和合规阶段；政府资源提供权威流程入口。StayChina 应在宽主题主页面显著区分信息支持/协调与政府或持牌专业人士的决定，并给关键步骤加官方原始来源和复核日期。本轮样本未提供 StayChina 可复现位置。 |
| Teach English in China jobs | [ESL Careers](https://www.esl.careers/teach-in/china)、[TEFL Org](https://www.tefl.org/teach-english-abroad/teach-english-in-china/)、[TES jobs](https://www.tes.com/jobs/browse/english-as-a-foreign-language-china)、[OlaChina](https://olachina.org/recruiting-english-teachers/) | 招聘目录拥有职位库存，TEFL 站点拥有资格/流程指南，招聘机构拥有实际岗位入口。StayChina 如继续争取此宽词，需先界定真实招聘职责，并提供有授权的真实岗位或独有的资格、雇主准备与合规路径信息；没有在招职位时不能把站点包装成职位聚合平台。本轮样本未提供 StayChina 可复现位置。 |

该复抽样揭示的是内容与信任证据模式，不证明这些竞争者数字真实，也不能推出目标站点排名变化。搜索曝光、实际收录、地区化位置、AI 引用和询盘仍须用各平台的 URL/query/country 报表分别验证；公开网页搜索结果只能作发现线索。


## 2026-10-06 23:24（Asia/Shanghai）品牌宽词页面公开发现抽样

以公开搜索抽查三个站点的主要商业主题页。当前返回结果中，Pomerol 的 `https://pomerol.trade/china-sourcing-agent/` 明确出现，页面标题为 “China Sourcing Agent for Overseas Buyers”；摘要呈现供应商筛选、报价比较、样品与变更、质量检查规划和出口交接等流程，搜索工具标记该页面两天前抓取。[Pomerol China sourcing agent 页面](https://pomerol.trade/china-sourcing-agent/)

本轮搜索样本没有返回 Xiaodu 的 system integrator 主页面或 StayChina 的 company setup 主页面。这只说明它们没有出现在本次工具结果中，不代表未被索引，也不代表固定排名。该搜索工具没有提供可复现的国家、语言界面、设备、自然结果序号或完整结果页，因此不据此判定三站进入前 20/前 10。

下一步证据优先级：在 Bing Webmaster 的 Search Performance 数据可用后读取每站非品牌查询、页面、国家/地区和平均位置；Google Search Console 采用同样的 query-page-country 切片；再用指定国家和语言的普通搜索结果作单独快照。Pomerol 已有一次公开发现信号，仍需靠稳定曝光、点击及询盘证明宽词竞争进展。

## 2026-10-07 品牌限定宽词公开发现复查

按三个核心商业主题分别检索并限定自有域名。公开搜索工具返回了 Pomerol 的 [China sourcing agent 服务页](https://pomerol.trade/china-sourcing-agent/)，抓取标记为 2 天前；结果正文能读到服务范围、六步执行路径与 illustrative/pseudonymized 案例说明。当前这是一项页面被搜索工具发现并可抽取内容的证据，但工具没有给出 Google/Bing 引擎、国家、自然排名序号或稳定 SERP，**不能据此判断已进前 20**。

本轮结果没有返回 staychina.org 对应的 company setup in China 主页，也没有返回 xiaodu.tech 对应的 industrial automation system integrator 主页。这只是本工具、本次查询下未出现，不证明未索引或未进入其他国家/个性化结果。新返回的竞争页面强调的差异包括完整服务阶段、可核查的办事范围/时限、定价或主体证据；三站需要继续依托业务事实建立这种证明力，不复制竞争者未经第三方核验的数字。

后续可比较的量化信号仍是各站 Search Console/Bing Webmaster 的非品牌 query × country × landing page × 日期窗报表。本轮没有站长平台的目标词位置数据。
