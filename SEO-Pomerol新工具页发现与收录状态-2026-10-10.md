# Pomerol 新工具页发现与收录状态（2026-10-10）

## 线上页面核验

直接读取生产 URL 与 sitemap：

| 检查 | 结果 |
|---|---|
| `https://pomerol.trade/tools/china-supplier-verification-kit/` | HTTP 200，未重定向 |
| 规范链接 | 自指 canonical 与目标 URL 一致 |
| robots meta | `index,follow` |
| 页面主题 | 标题和 H1 均为 China Supplier Verification Checklist & Evidence Tracker |
| sitemap | `https://pomerol.trade/sitemap.xml` HTTP 200，包含该工具 URL |

这些信号说明页面当前具备被抓取和索引的基本条件；它们不代表 Google 已编入索引或已产生排名。

## Search Console 当前证据

在已登录的 Pomerol GSC 效果报表中，当前可读取的图表数据仍截至 **2026-10-06**（报表上次更新约 32.5 小时前）：全站 157 次展示、1 次点击、平均排名 72.6。可见宽词主题中，`china supplier verification` 有 12 次展示、0 次点击；这不是新工具页的 URL 索引证据，也不能从全站平均排名推断该页或该词的位置。

### Google 抓取请求

2026-10-09 已在 GSC URL Inspection 中检查该工具页：首次状态为“网址尚未收录到 Google”，未显示 sitemap/引荐页或抓取记录；同日实时测试显示 URL 可编入索引并检测到 1 项有效 Breadcrumbs，随后已请求一次编入索引。GSC 明确回执“已将网址添加到优先抓取队列中”。这证明请求已进入队列，不证明 Google 已重新抓取或收录。详见 [非品牌宽词与 Pomerol 索引差距记录](SEO-非品牌宽词复核与Pomerol索引差距-2026-10-09.md)。

本次复核中直接拼接 GSC URL 检查链接返回通用 404；这不是索引结论，也不覆盖前述 GSC 确认回执。**当前 Google 收录状态需要通过 GSC 正常 URL 检查界面后续复核；在队列结果出来前不重复请求。**

### IndexNow 通知

Pomerol Cloudflare Worker 部署运行 [#37755603958](https://github.com/RuthlessCreature/pWebsiteExport/actions/runs/37755603958)（2026-10-08 09:17 UTC）实际验证了公开 key 文件，并在 `api.indexnow.org/indexnow` 对 155 个 sitemap URL 分批收到 HTTP 200，日志明确写明“IndexNow submission accepted for 155 URLs”。工具页在当时的 155 URL sitemap 中，因此包含在该批通知中。该回执证明 IndexNow endpoint 接受 URL 列表，不证明 Bing、Naver 等参与方已抓取、收录或排名。

## 下一步动作

1. 等待已排队的 GSC 请求处理后，用 GSC 正常 URL 检查界面复核抓取时间与最终索引状态；不要重复提交同一请求。
2. GSC 确认索引后，在 `china supplier verification` 查询过滤下检查页面维度。当前 12 次展示主要说明主题已获得有限搜索需求信号，并不证明新工具页承接了这 12 次展示。
3. Bing Webmaster 的 URL Inspection 当前浏览器页无法访问；部署日志证明 IndexNow 已接受这 155 个 URL，但不证明 Bing 已抓取或收录。待 Bing 页面可访问时核对 IndexNow history 与该 URL 的索引状态。

## 边界

本记录区分了页面可索引性、Google 队列回执、IndexNow endpoint 回执、实际索引和排名。尚无证据证明该工具页已由 Google/Bing 收录，或让 `china supplier verification` 进入前 20。要争取宽词排名，仍需围绕工具实际提供的验证步骤、证据清单、风险解释与执行边界获得真实使用/引用信号。
