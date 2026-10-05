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
- 三站提供 `/llms.txt` 作为可选机器导航文件。该文件不应被当作 Google 排名开关；AI 可见度仍依赖抓取、索引、清楚且可信的页面内容和外部引用。
- 通过 Cloudflare Email Routing 配置三个 `contact@` 地址转发至站点负责人。路由规则、已验证目标地址及公网 MX/SPF 配置已核验；邮件端到端收件测试尚未获得确认收件证据。
- robots 对搜索与 AI 搜索用途提供可抓取信号，并分别声明模型训练爬虫的站点策略。应定期复核 Cloudflare 安全规则，避免误拦正规搜索爬虫。

## 已验证的收录通知与页面检查

- 三站生产 sitemap 页面数量基线：Xiaodu 170，StayChina 24，Pomerol 144。历史全量巡检曾验证页面状态码、标题、H1、描述、canonical 和可索引性；部署后仍须对变更 URL 做回验。
- IndexNow 曾接受 Xiaodu 170、StayChina 24、Pomerol 144 个 URL 的通知。API 接收不代表搜索引擎已抓取、收录或排名提升。
- SEO 专项仓库已启用每周一次的免费 GitHub Actions 线上审计。2026-10-05 首次运行成功，三站爬取信号、sitemap、`llms.txt` 和代表页面检查均为 0 错误；结果可在 [Actions run](https://github.com/RuthlessCreature/websiteSEO/actions/runs/37325202926) 复核。
- StayChina sitemap 的 `lastmod` 日期已与对应页面更新对齐，并在生产 sitemap 回验。
- Pomerol 示意场景已明确标注为示例，不作为已交付客户案例、业绩或第三方背书。

## 外部搜索可见度状态

2026-10-05 的公开宽词抽样未见三站出现在对应搜索结果样本中。此抽样不是固定国家/地区、语言、设备和搜索引擎下的排名报告；因此当前没有证据证明三站已进入宽词前两页。目标需要通过 Search Console 与 Bing Webmaster 查询数据持续量测，不能承诺具体名次。

优先使用有真实需求的宽主题支柱页，补充第一手工程/业务流程证据、负责人和企业信息、真实可公开案例与行业引用。不要批量生成近似地域词页、伪造客户或购买低质量链接。

## 当前外部渠道待办

- Google Search Console：核查 sitemap 处理状态、旧摘要 URL 和宽词曝光；浏览器控制恢复后完成 URL 检查。
- Bing Webmaster Tools：核查 sitemap、IndexNow 活动与 AI Performance 查询引用；只有接口接受记录不算收录证明。
- Yandex Webmaster：添加并验证需要覆盖的站点，再提交 sitemap。
- 百度站长平台：根据实际登录账号与官方当前准入流程核验站点验证及 sitemap 提交能力。
- Automation-List：Xiaodu 免费档案资料已准备；尚无提交/确认回执，不能记为已上线。

## 可信度与资料保护

- 所有目录、社媒资料只填写网站公开或有凭证的事实。
- 不公开未授权的客户询盘、私人联系信息、凭据、内部运营日志或未发布账户数据。
- 免费提交不等于获批；收录通知不等于排名；AI 导航文件不等于 AI 推荐。
