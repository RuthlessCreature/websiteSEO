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

## 部署流水线与 IndexNow 运行证据（2026-10-06）

本轮通过 GitHub Actions REST 元数据检查公开可读的两个生产仓库最近运行：

- [Xiaodu run 37418374232](https://github.com/RuthlessCreature/xWebsite/actions/runs/37418374232)，提交 `2ee3c679`，2026-10-06 05:24 UTC 完成成功；步骤 `Deploy Workers Static Assets`、`Verify all production sites`、`Notify IndexNow` 均为 success。
- [Pomerol run 37421595583](https://github.com/RuthlessCreature/pWebsiteExport/actions/runs/37421595583)，提交 `6c039751`，2026-10-06 06:02 UTC 完成成功；构建/SEO gate、`Deploy Worker`、`Verify production SEO and contact routes`、`Verify and notify IndexNow` 均为 success。之前同日 run `37421010573` 的生产路由复核失败，IndexNow 步骤被跳过；随后成功的 run 重新完成了验证及通知。
- [websiteSEO run 37410796850](https://github.com/RuthlessCreature/websiteSEO/actions/runs/37410796850) 的三站生产巡检成功。
- GitHub 公共 Actions API 对 StayChina 源码仓库返回 404，无法从匿名数据核实其 Actions 日志；这不等于仓库或线上站点不存在。StayChina 生产连通性仍由本文件上面的实时 HTTP 巡检证明，IndexNow 通知是否执行需要在有权限的站点流水线/Bing Webmaster 中核实。

成功执行 IndexNow 通知只证明站点部署脚本运行完成，不等于每个 URL 都被 Bing、Naver 或其他参与方抓取/收录，也不提供宽泛关键词排名证据。Bing Webmaster 的 IndexNow 报告和 URL Inspection 才是后续确认提交历史、抓取和索引状态的依据。

## 手动补发变更 URL 的 IndexNow 接收回执（2026-10-06）

对 sitemap 中仍公开、当前返回 HTTP 200 且域名根目录 IndexNow 校验文件与密钥内容匹配的 URL，直接向 `api.indexnow.org/indexnow` 发送小批量变更通知。三站分别返回 HTTP 200：

- Xiaodu：42 个含 `/industries/` 路径的当前 sitemap URL。该筛选包含行业栏目与相关行业内容页，范围比单一栏目首页更广；这 42 个请求已被 IndexNow endpoint 接受。
- StayChina：3 个已更正的联系/招聘说明 URL：`/en/contact`、`/zh-cn/contact`、`/zh-cn/kindergarten-foreign-teacher-recruitment`。
- Pomerol：6 个当前 sitemap 中的多语言联系页。

本次没有把密钥写入本记录。HTTP 200 是 IndexNow 接收回执，不等于 Bing/Naver/Seznam 等已抓取、已收录或排名变化。Google 不参与 IndexNow；Google 侧仍需依赖 sitemap 和 Search Console 的索引报告/URL 检查。Bing 官方也说明 IndexNow 通知不保证收录，后续应查看 Bing Webmaster Tools 的 IndexNow 与 URL Inspection 报告。

### 对 Actions 步骤状态的证据修正

复查两个公开部署 workflow 后发现 IndexNow 步骤设置了 `continue-on-error: true`；即使通知脚本异常，部署 job 仍可成功。GitHub 日志下载接口本轮返回 HTTP 403，无法读取脚本的逐条提交回执。因此前文 `Notify IndexNow` / `Verify and notify IndexNow` 的 Actions `conclusion: success` 只证明 job 未被该步骤阻断，**不能单独证明 endpoint 接收**。本轮另行直连 `api.indexnow.org/indexnow`，已对上面三组页面分别取得 HTTP 200；这些才是本轮 URL 通知被 IndexNow endpoint 接受的证据。

## Cloudflare 控制台只读复核（StayChina，2026-10-06）

通过已登录的 Cloudflare 控制台查看 `staychina.org`：Caching → Configuration 中 `Crawler Hints Beta` 当前为开启状态。AI Crawl Control → Signals 显示 robots 偏好同步已开启；最近 7 天 `www.staychina.org/robots.txt` 成功读取 97 次、失败 0 次，根域 `staychina.org/robots.txt` 成功读取 38 次、失败 0 次，两个端点均由 Cloudflare 托管并声明内容信号。

同一信号页记录到 BingBot 请求 `/api/social-image/...` 路径，并因 robots.txt 的 `Disallow: /api/` 被判为 robots violation；出现于 contact、products 等页面路径。这是 Bing 声称的 crawler 活动与 robots 合规事件，不能据此确认请求身份或断言分享预览已损坏。后续应核对线上 Open Graph 图片声明与这些图片 URL 的实际抓取需要，再决定是否为特定公开图片路径添加最窄的 robots Allow；保持其他 `/api/` 私有接口不开放。

该次只读复核没有更改 Zone、机器人规则、robots.txt 或部署。随后在 Cloudflare 三个 Zone 的 Caching → Configuration 页面逐一核对，`Crawler Hints Beta` 均显示已开启：`xiaodu.tech`、`staychina.org`、`pomerol.trade`。AI Crawl Control → Signals 的机器人请求、robots violations 与 robots 偏好同步明细本次仍只在 StayChina 核查；不能把 StayChina 的 signals 数据外推到另外两站。

## 社交预览抓取抽查（公开生产页面，2026-10-06）

从三站英文联系页各读取一个样例，并对页面声明的 Open Graph 图片进行只读 HEAD 请求：

| 站点/页面 | `og:image` 声明 | 图片响应 | 观察 |
|---|---|---|---|
| StayChina `/en/contact` | `/api/social-image/en/contact` | HTTP 200，`image/png` | 声明与公开端点均可用；robots 对 `/api/social-image/` 有更具体的 Allow，但 Cloudflare 最近 7 天仍记录到 BingBot 访问此类 URL 的 robots violation。需用 Bing robots tester 并观察下一轮 Cloudflare 信号确认是否为历史记录或解析差异。 |
| Xiaodu `/en/contact/` | 无 `og:image`；仅 `twitter:card=summary` | 不适用 | 该样例没有大图社交预览标签。源代码中已有其他分支实现了动态分享图标签，但当前生产页面仍未呈现；需要在 Xiaodu 当前发布源码中统一生成 `og:image`、`twitter:image` 与 `summary_large_image`，再部署并回验。 |
| Pomerol `/contact/` | `/assets/photos/product-development.jpg` | HTTP 200，`image/jpeg` | 声明的静态社交图片端点可用。 |

这是每站各一个页面的抽样，不代表所有 sitemap URL 的分享图片覆盖情况。Bing 官方说明，针对 Bingbot 的专属 robots 组会覆盖通用 `User-agent: *` 指令，并支持用 `Allow` 放行被目录规则覆盖的路径；因此排查时要同时看匹配的专属规则组与路径，而不是只看通用规则。[Bing robots.txt 指南](https://www.bing.com/webmasters/help/how-to-create-a-robots-txt-file-cb7c31ec)。本次只改动此 SEO 仓库中的记录，没有改站点代码或部署。

## 全站社交预览标签巡检（2026-10-06）

将 `og:image`、`twitter:image`、`twitter:card=summary_large_image` 纳入每月全 sitemap 检查，并以独立提醒呈现，不与 HTTP 状态、canonical、noindex 等可索引性问题混在一起。对当前 338 个 sitemap URL 的只读检查结果：

| 站点 | 页面数 | 既有 SEO 检查问题 | 社交预览标签提醒 |
|---|---:|---:|---:|
| Xiaodu | 170 | 0 | 28 页缺少 `og:image` / `twitter:image`，且卡片为摘要类型 |
| StayChina | 24 | 0 | 0 |
| Pomerol | 144 | 0 | 46 页有提醒：45 个资源页缺少 Twitter 图片/大图卡片字段；`/sitemap/` 工具页缺全部三个字段 |

检查仅确认 HTML 标签与图片 URL 是否声明为 HTTPS，未对全部 338 个图片 URL 逐一发请求，也不证明社交平台当前已生成预览。此前三页 HEAD 抽查只证实 StayChina 联系页动态 PNG 与 Pomerol 首页素材 JPEG 返回 200。需要在站点源码中统一分享标签后部署，再抽查主要页面的 Open Graph debugger / 社媒预览，并观察下一轮月度覆盖率变化。


## 2026-10-07 00:02（Asia/Shanghai）三站 IndexNow 校验与 sitemap 新鲜度

从三个生产站直接读取 sitemap 与 IndexNow 校验文件，结果如下：

| 站点 | 规范页面 URL | sitemap 最近 lastmod | 公网 IndexNow key file |
|---|---:|---|---|
| Xiaodu | 170 | 2026-10-05（170 项均有 lastmod） | HTTP 200，正文与该站配置值匹配 |
| StayChina | 24 | 2026-10-05（24 项均有 lastmod） | HTTP 200，正文与该站配置值匹配 |
| Pomerol | 144 | sitemap 未提供 lastmod | HTTP 200，正文与该站配置值匹配 |

通过 GitHub Actions API 查看 2026-10-06 的最新公开部署运行：Xiaodu run [37443093920](https://github.com/RuthlessCreature/xWebsite/actions/runs/37443093920) 与 Pomerol run [37443324993](https://github.com/RuthlessCreature/pWebsiteExport/actions/runs/37443324993) 中 IndexNow 步骤显示 `conclusion: success`。两个 workflow 均配置 `continue-on-error: true`，所以该字段不能排除步骤内部失败；不把它当作新的 endpoint 接收证明。StayChina 的私有仓库运行日志无法从公开 Actions API 读取，但此前三条已更新 URL 已单独取得 IndexNow HTTP 200 回执。当前没有发现 2026-10-06 之后的 sitemap lastmod 更新，也没有重复提交全站 URL。

结论：三站当前具备可验证的 IndexNow key 文件；已变更 URL 的历史 endpoint 接收回执按原记录保留。校验文件可达、部署步骤结束或 endpoint 接收都不表示 Bing/Naver/其他参与端已抓取或收录。下一步需在 Bing Webmaster 的 IndexNow history / URL inspection 对照具体 URL；Google 不参与 IndexNow，继续以 GSC sitemap、URL 检查与抓取统计为准。Pomerol 若后续依赖 lastmod 增量判断，应先补上准确页面更新时间；不能编造或在无内容变化时批量改写日期。
