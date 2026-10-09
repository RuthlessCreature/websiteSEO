# 三站全量 sitemap 审计与免费目录复核（2026-10-09）

## 全站生产抓取审计

使用仓库内 `seo-tools/seo_full_site_audit.py` 对三个线上 sitemap 中的全部 URL 做只读巡检，核对 HTTP 状态与跳转、canonical 主机、标题和描述、H1、robots、旧联系人标记、JSON-LD 语法/实体名、hreflang 互返、社交预览元数据和重复标题。

| 站点 | Sitemap 页面数 | 有效 JSON-LD 块 | 空 alt 图片（信息项） | 问题 | 警告 |
|---|---:|---:|---:|---:|---:|
| Xiaodu | 170 | 505 | 560 | 0 | 0 |
| StayChina | 24 | 48 | 0 | 0 | 0 |
| Pomerol | 155 | 155 | 155 | 0 | 0 |
| **合计** | **349** | **708** | **715** | **0** | **0** |

空 alt 是合法的装饰图片用法，审计将其作为信息项；未发现缺少 alt 的图片、旧联系人、不可用 canonical、错误实体或 sitemap 页面元数据警告。此项证明的是当前被 sitemap 列出的页面技术健康状态，不代表搜索引擎已经索引这些页面或宽词已排名。

## 免费目录复核

### Xiaodu — Automation-List 仍是最匹配的免费目录

官方提交页与指南仍面向真正设计、构建或集成工业自动化系统的企业，系统集成、机器视觉和机器人集成都属于可选类别；页面声明免费档案需人工审核，目录发布不等于排名保证。[提交页](https://www.automation-list.com/en/submit-listing) · [Listing Guidelines](https://www.automation-list.com/en/listing-guidelines)

本轮核对到必填项包含 `I have read and agree to the listing guidelines`，以及公司、网站、工作邮箱、国家、服务类别等字段。历史资料显示相同表单曾返回 `Unable to submit listing.`，且没有可确认回执。因此本轮没有重复提交，也不把隐藏的“Listing submitted”成功状态当回执。下一步应解决真实表单错误，之后以实际确认邮件或公开档案 URL 作为完成证据。

### Industrial Automation (Netherlands) — 暂不填报

官方页面宣传免费企业索引，但当前必填完整邮编、门牌号、街道、城市、国家与商务邮箱；三站公开资料仅能核实到珠海、广东、中国的城市级地点，没有可确认的完整街道地址。故不猜填地址，也不提交不完整或错误 NAP 信息。[官方注册表](https://industrialautomation.nl/en/sign-up/)

### China Business Directory — 不作为优先免费外链

该站称中国企业可免费建立档案，但其免费方案的官网字段不提供可点击网站链接；带有可点击官网链接的方案需要一次性付费。当前注册还要求建立账户并同意服务条款。因此这轮不为一条非点击链接创建新账号，也不把付费档案列为免费 SEO 资源。[官方首页](https://businessdirectorychina.com/) · [免费注册/方案说明](https://businessdirectorychina.com/register.php)

### StayChina / The Helpful Panda — 保持资格排除

The Helpful Panda 的免费目录明确只接受专门从事中国教师招聘的机构，并免费档案不提供可点击网站链接。StayChina 官网公开的当前服务边界为岗位需求指南与早期沟通协调，不应包装为招聘机构；此前错误申请已撤回，本次不重新提交。[目录资格说明](https://thehelpfulpanda.com/directory/china-teacher-recruitment-agencies/)

## 当前 SEO 判断

- 三站 sitemap 中的生产页面技术信号整体一致且健康，本轮未发现需立刻修复的全站级抓取/结构化数据错误。
- 技术合规消除了阻碍，但不能替代真实经验、独立案例、外部提及和目标查询的内容竞争力；也不能据此宣称宽词已到前 20。
- 下轮优先级转为：Automation-List 表单错误的可核实诊断；三站核心宽词页的独立经验/证据增量；按 GSC/Bing 的目标查询和目标国家跟踪实际排名及展示变化。

