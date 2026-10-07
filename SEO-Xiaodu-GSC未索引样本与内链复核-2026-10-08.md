# Xiaodu：GSC 未索引样本与站内链接图复核（2026-10-08）

## Google Search Console 当前证据

Xiaodu 的网域属性索引报告在 **2026-10-04** 更新，显示 75 个已编入索引、105 个未编入索引。其中 90 个属于“已发现 - 尚未编入索引”，12 个属于“已抓取 - 尚未编入索引”；其余为规范替代、Google 选择不同规范页和 1 个正在验证的 robots.txt 阻挡。

GSC 对“已发现 - 尚未编入索引”的原因详情显示 90 个受影响页面。当前页面展示的前 10 个 URL 示例如下，样本的“上次抓取日期”均为“不适用”：

| 类型 | GSC 示例 URL |
|---|---|
| 案例索引 | https://xiaodu.tech/en/cases/ |
| 案例页 | https://xiaodu.tech/en/cases/conveyor-robot-retrofit/ |
| 案例页 | https://xiaodu.tech/en/cases/flexible-robotic-workstation/ |
| 案例页 | https://xiaodu.tech/en/cases/laboratory-robotic-automation/ |
| 案例页 | https://xiaodu.tech/en/cases/production-equipment-data-platform/ |
| 案例页 | https://xiaodu.tech/en/cases/remote-monitoring-service/ |
| 案例页 | https://xiaodu.tech/en/cases/robot-machine-tending-inspection/ |
| 案例页 | https://xiaodu.tech/en/cases/warehouse-vision-handling/ |
| 联系页 | https://xiaodu.tech/en/contact/ |
| 行业索引 | https://xiaodu.tech/en/industries/ |

随后将 GSC 表格切换为每页 100 行，报告显示全部 90 条示例；这 90 条的“上次抓取日期”均为“不适用”。按 URL 路径归类如下：

| 语言路径 | 数量 |
|---|---:|
| en | 19 |
| es | 12 |
| ja | 9 |
| pt | 15 |
| ru | 14 |
| zh-cn | 8 |
| zh-tw | 13 |

| 页面路径类型 | 数量 |
|---|---:|
| cases（含案例索引） | 26 |
| industries（含行业索引） | 30 |
| solutions（含解决方案索引） | 28 |
| contact | 5 |
| 本地化首页 | 1 |

84/90 条（约 93%）集中在案例、行业、解决方案路径，且分布于七种语言。这代表当前 GSC 示例中的主要发现/抓取队列集中在三类页面，不代表网站全站的收录比例，也不能单凭这个分布判定重复内容。结合全部示例的抓取日期均为“不适用”，目前更符合 Google 尚未抓取这些 URL，而非已抓取后判定内容不足。

## 站内链接图与正文深度复核

只读脚本对 Xiaodu sitemap 的 170 个 URL 抓取 HTML 并统计站内 HTML 链接：

- sitemap URL 纳入链接图：170
- 获取或正文提取错误：0
- 没有站内 HTML 入链的 sitemap URL：0
- 只有一个来源页面入链的 sitemap URL：0

因此当前证据不支持把这些页面归因于完全孤立或 sitemap 缺失。GSC 样本仍未被抓取，说明存在站内链接并不保证 Google 会及时安排抓取；首页、解决方案、行业和案例索引之间的上下文链接及重要性信号仍值得强化。

英文/默认语言的 24 个非联系页中，有 12 个低于本地审计的 300 英文词人工复核提示线。该线不是 Google 的最低字数要求，也不是删除或 noindex 建议：

| 页面 | 英文词数 |
|---|---:|
| /en/industries/logistics-warehousing/ | 151 |
| /en/industries/precision-manufacturing/ | 151 |
| /en/industries/laboratory-automation/ | 166 |
| /en/industries/mining-bulk-materials/ | 176 |
| /en/solutions/machine-vision/ | 196 |
| /en/solutions/custom-equipment-integration/ | 205 |
| /en/solutions/automated-sampling-lab/ | 213 |
| /en/industries/process-heavy-industry/ | 221 |
| /en/solutions/robotic-automation/ | 221 |
| /en/solutions/intelligent-workflow-automation/ | 222 |
| /en/solutions/industrial-software-data/ | 246 |
| /en/cases/ | 270 |

## SEO 优先级

1. 先逐页增强与宽词直接相关的解决方案和行业落地页：补充可核验的交付范围、适用边界、典型输入与输出、集成方式、地区服务能力和常见采购问题。没有真实案例证据时不写成已完成的客户项目。
2. 在首页、解决方案索引、行业索引和案例索引中增加更明确的上下文链接，指出哪些服务页解决哪些行业问题；不要只依赖通用导航链接。
3. 已将 GSC 当前展示的 90 条 URL 按页面类型和语言分组。优先复核英语行业/解决方案索引页与服务页的独立决策信息，再检查其余语言版本是否准确、完整地保留相同的业务边界；不要为案例示例页批量请求索引。
4. 对 12 个低词数页面进行人工内容审阅。只要信息完整、目的明确且真实有用，可以保留；不要按字数批量删除、合并或设置 noindex。
5. GSC 的“已抓取 - 尚未编入索引”12 页需要单独逐页看主内容、canonical、重复模板和搜索需求，不要与“尚未抓取”的 90 页混为一谈。

## 限制与可复核链接

- GSC 报告最后更新时间：2026-10-04。
- sitemap 链接图是当前 HTML 中的站内 anchor 统计，不测量 Google 实际发现路径、链接权重或真实抓取优先级。
- 这轮三站正文 triage 中，StayChina 与 Pomerol 在抓取过程中连续遇到 TLS EOF；脚本未能给出这两站的链接图/正文统计。另一个实时首页及代表页探测正常，不等于该抓取批次成功。

- [Xiaodu GSC 网页索引报告](https://search.google.com/search-console/index?resource_id=sc-domain%3Axiaodu.tech)
- [Xiaodu 当前 sitemap](https://xiaodu.tech/sitemap.xml)
- [三站实时巡检（2026-10-08）](SEO-%E5%AE%9E%E6%97%B6%E5%B7%A1%E6%A3%80-2026-10-08.md)
- [现有审计脚本：英文正文及内链图](seo-tools/seo_content_triage.py)
