# 三站统一 SEO 与 Cloudflare 索引信号复核 — 2026-10-06

## 生产端只读核查

通过 `seo-tools/seo_live_audit.py` 对三个生产域名执行只读请求：错误 0。

| 站点 | sitemap URL 数 | llms.txt | robots 搜索/AI 检索 | AI 训练策略 | 样例页 |
|---|---:|---|---|---|---|
| xiaodu.tech | 170 | HTTP 200 | Google、Bing、Baidu 与 AI retrieval 允许 | GPTBot、ClaudeBot、Applebot-Extended 屏蔽 | `/en/`、`/en/contact/` 均 HTTP 200，title、H1、canonical 存在 |
| staychina.org | 24 | HTTP 200 | Google、Bing、Baidu 与 AI retrieval 允许 | GPTBot、ClaudeBot、Applebot-Extended 屏蔽 | `/en/`、`/en/contact`、`/en/china-setup` 均 HTTP 200，title、H1、canonical 存在 |
| pomerol.trade | 144 | HTTP 200 | Google、Bing、Baidu 与 AI retrieval 允许 | GPTBot、ClaudeBot、Applebot-Extended 屏蔽 | `/en/`、`/contact/`、`/china-sourcing-agent/` 均 HTTP 200，title、H1、canonical 存在 |

该巡检证明端点可访问及当前抓取政策，不证明搜索引擎已完整收录、排名变化或 Cloudflare Crawler Hints 账户设置仍为开启。

## 结构化实体抽样

从三个英文首页读取 JSON-LD：

- **Xiaodu**：`Organization` 为 “Zhuhai Xiaodu Intelligent Technology Co., Ltd.”；`WebSite` 与 `WebPage` 使用 Zhuhai Xiaodu 品牌，并关联公开 YouTube 频道。公开搜索抽样没有找到足以核实该英文法定名称的权威企业记录。珠海市市场监督管理局提供官方企业信用信息查询入口，但本轮站外搜索不能替代按统一社会信用代码在官方系统中完成核验。故该名称、注册状态及实体关系应标为“待业务证件核实”，不可当作外部认证或已验证经营资质推广。参见[珠海市市场监督管理局企业信息查询](https://ssgs.zhuhai.gov.cn/modes/xxcx.html)。
- **StayChina**：`Organization.name` 为 StayChina，`legalName` 为 Pomerol International Trade (Zhuhai) Co., Ltd.，主品牌与运营法人明确区分，方向正确；公开搜索仍有旧联系人、旧站名摘要，需要 GSC 侧确认重抓/canonical 选取。
- **Pomerol**：`Organization.name` 为 Pomerol International，`legalName` 为 Pomerol International Trade (Zhuhai) Co., Ltd.，与站点品牌和运营关系一致。

所有站点 JSON-LD 均抽取到 Yusuf 的邮箱、电话和珠海地址；联系方式真实一致性仍以业务主体资料及站内联系页为准。实体标记不应自行增加未经验证的 `sameAs`、资质、客户或业绩。

## Cloudflare 与搜索引擎提交路线

- Cloudflare 官方将 Crawler Hints 列为所有套餐可用的功能，并说明它会依据 cache MISS 信号把潜在内容变化通知 IndexNow；该机制帮助及时重抓，但不保证抓取、收录或排名。[Cloudflare Crawler Hints 文档](https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/)
- 本轮没有重新登录 Cloudflare API，因此不能把以前的控制台操作当作今日的账户设置复验结果。下一次有可读 API 凭据时，逐 zone 只读检查 `crawler_hints`，不更改其他安全设置。
- Bing Webmaster Tools 官方推荐 IndexNow 用于变更 URL 通知，并说明可在 IndexNow 报告中查看提交与收录状态；提交成功本身不等于已收录。[Bing URL Submission](https://www.bing.com/webmasters/help/url-submission-62f2860b)、[Bing IndexNow](https://www.bing.com/webmasters/help/indexnow-0z209wby)
- Google Indexing API 仅适用于包含 `JobPosting` 或 `VideoObject` + `BroadcastEvent` 的页面，不应拿它批量推送一般营销页；常规站点继续使用 sitemap 与 Search Console URL 检查。[Google Indexing API 限定](https://developers.google.com/search/apis/indexing-api/v3/quickstart)
- GSC 本轮无法通过当前桌面浏览器的辅助功能接口安全读取；StayChina 旧联系人 URL 的索引状态仍未确认，也没有再次提交已在队列的 `/en/contact`。

## 本次可执行优先级

1. 先用官方登记资料核实 Xiaodu 的法定主体英文/中文名称与登记状态；核实后再统一 JSON-LD、页脚、`llms.txt` 与公开资料。不应为了 SEO 把未核实信息填成肯定事实。
2. 在可访问的 GSC 中核查 StayChina 旧摘要 URL 的 live test、selected canonical、last crawl；观察已有重抓队列的 `/en/contact`，不重复提交。
3. 在 Bing Webmaster Tools 读取三站的 IndexNow 提交历史和 URL inspection，确认 Cloudflare 或部署流水线通知被接收；当前公开页面能被搜索工具抽取，不替代这个状态。
4. 后续用各站目标服务的广义、高意图词分别做非品牌词表现跟踪；不把 `site:` 查询、搜索摘要或索引请求状态写成目标词排名。
