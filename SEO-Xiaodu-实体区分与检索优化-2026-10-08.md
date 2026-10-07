# Xiaodu 实体区分与检索优化（2026-10-08）

## 当前证据

### 生产首页公开实体

直接读取 `https://xiaodu.tech/en/`：

- HTTP 200。
- Title：`Industrial Automation & Smart Manufacturing | Zhuhai Xiaodu`。
- H1：`Industrial automation solutions shaped around your production process`。
- Organization 的 `name` 与 `legalName` 均为 `Zhuhai Xiaodu Intelligent Technology Co., Ltd.`；`alternateName` 为 `珠海小度智能科技有限公司`。
- Organization `sameAs` 当前只包含 YouTube `@XiaoduAutomation`。
- WebSite 名称使用 `Zhuhai Xiaodu Intelligent Technology`。

因此页面已说明工业自动化主题，结构化数据也有完整法定实体；但消费者可识别的英文品牌名 `Xiaodu Automation` 尚未进入 Organization 的 `alternateName`。单独使用 `Xiaodu` 的区分度弱。

### 公开搜索发现样本

2026-10-08 对四组公开查询抽样：

- `Xiaodu Automation industrial automation Zhuhai`
- `"Zhuhai Xiaodu Intelligent Technology"`
- `site:xiaodu.tech "Xiaodu Automation"`
- `小度 自动化 珠海 小度智能 工业自动化`

该搜索服务的返回结果中未出现 `xiaodu.tech` 或法定公司名对应页面；结果包含珠海其他自动化服务商，以及一个名为“小度全屋智能”、内容涉及百度 AI 生态的页面。这个返回集没有完整分页、地域参数和可复现 SERP 位置，因此只说明**当前搜索样本未发现 Xiaodu 官网，且存在品牌词歧义信号**；不能当作 Google/Bing 未收录证明，也不能推导固定排名。

## 判断

主要缺口不是首页缺少工业自动化主题，而是独特品牌实体的站外佐证不足：

1. `Xiaodu` / `小度` 会与知名消费电子/AI品牌及其他同名企业发生词义竞争。
2. 法定实体名与 YouTube 英文频道名目前没有在 Organization 结构化数据里形成明确的英文别名关系。
3. 除 YouTube 外，当前实体 `sameAs` 没有其他已核验的公开公司档案。
4. 当前公开搜索样本没有返回 Xiaodu 官网；现有 GSC 数据报告截至 2026-10-04 显示零展示，但该数据窗口较短且不是本轮实时刷新。

## 实体强化稿

### 对外名称规范

在可编辑的公开资料中统一采用：

- **展示品牌**：Xiaodu Automation
- **法定名称**：Zhuhai Xiaodu Intelligent Technology Co., Ltd.
- **中文名称**：珠海小度智能科技有限公司
- **地区识别**：Zhuhai, Guangdong, China
- **业务类别**：Industrial automation systems integration

目录的公司法定名称字段继续使用网站公开的法定英文名称；简介首句可使用：

> Xiaodu Automation is the English brand used by Zhuhai Xiaodu Intelligent Technology Co., Ltd., an industrial automation systems integrator based in Zhuhai, China.

这句只整合网站目前公开的品牌、法律实体、地点与服务类别，不加入未验证客户、授权、认证、员工数或项目成果。若公司希望将英语品牌与法定实体写成不同关系，应先以业务主体实际登记/使用情况为准，再调整措辞。

### 网站代码后续实施稿

当前工作边界只更新 `websiteSEO` 仓库，本轮未修改或推送 xWebsite。日后获授权进入站点源码时，优先考虑：

1. 保留 `Organization.name` 与 `legalName` 为完整法定名称。
2. 把英文品牌 `Xiaodu Automation` 纳入 `alternateName`；继续保留中文法定别名。
3. 只有加入经验证的公司官方外部档案后，才把对应 URL 加入 `sameAs`。频道、档案必须代表同一实体。
4. 评估首页标题是否要明确“system integrator”与“Xiaodu Automation”，但先用 GSC 国家/查询/页面数据确认真实展示机会；不要仅为宽词匹配而批量生成地区页。
5. 首页首屏用一句话清楚交代“品牌名 + 法定实体 + 珠海 + 工业自动化集成”，保持和真实业务主体一致。

### 站外档案优先级

1. 已存在且可核验的 YouTube `@XiaoduAutomation` 频道，持续补充原创建议/实机演示内容后再加更多社交链接。
2. Automation-List 免费集成商档案仍未得到有效提交回执；正式表单填报资料已准备，待其可正常提交并完成邮箱核验后再视为公开实体档案。
3. Industrial Automation Integrators 的公司申请页面此前显示已接收，但公开搜索仍为 0 profiles；继续以目录公开档案页是否出现为验收标准。
4. 不创建同名的多份低质量简介，不使用未经授权的客户案例，不购买无法证明受众和收录价值的链接。

## 衡量标准

每两周抽查同一搜索服务的品牌精确词与行业宽词，并记国家、语言、查询文本、实际返回 URL 和抓取日期；不要以搜索结果工具的不完整列表替代 GSC/Bing Webmaster 指标。阶段性成功需同时具备：

- 品牌精确查询返回官网或官方档案；
- 公司全称、英文品牌、中文名与官方简介在多个可信来源一致；
- GSC 中目标查询具有真实展示，且目标页是相关规范页面；
- 若要求前 1–2 页，必须用目标国家和宽主题查询的 Search Console / 搜索跟踪数据验证，不能用网站可访问或关键词长尾结果代替。

