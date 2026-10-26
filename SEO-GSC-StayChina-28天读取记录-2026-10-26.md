# StayChina Search Console 读取记录 — 2026-10-26

## 读取范围

- 资源：`sc-domain:staychina.org`，登录账号 Yusuf Gmail。
- 报告：Google Search Console「效果 → 搜索结果」，搜索类型「网络」。
- 日期：选择「最近 28 天」，界面图表范围显示 2026-09-27 至 2026-10-24；页面提示数据上次更新约 3.5 小时前。
- 这是 UI 读取记录，尚未导出 CSV。查询维度和网页维度分开浏览，**未取得 query × page 交叉归因**。

## 总览

- 点击：2
- 展现：50
- CTR：4%
- 平均排名：9

## 查询维度（界面显示的 5 行）

| 查询 | 点击 | 展现 |
|---|---:|---:|
| stay china | 1 | 3 |
| yusuf china | 0 | 3 |
| it support china | 0 | 2 |
| guide to teaching in china | 0 | 1 |
| hengqin | 0 | 1 |

可见行展现总数只占总展现的一部分；不要将其视为完整查询列表或全量归因。当前页面可确认品牌词 `stay china` 有 1 次点击；不能凭单独的 query 与 page 表推断“guide to teaching in china”落在哪个 URL。

## 网页维度（首屏前 10 行；表格共 13 行）

| 页面 | 点击 | 展现 |
|---|---:|---:|
| `https://www.staychina.org/en/contact` | 1 | 10 |
| `http://www.staychina.org/` | 1 | 5 |
| `https://www.staychina.org/en/china-setup` | 0 | 19 |
| `https://www.staychina.org/zh-cn/china-setup` | 0 | 6 |
| `https://www.staychina.org/en/guides` | 0 | 3 |
| `https://www.staychina.org/en` | 0 | 3 |
| `https://www.staychina.org/` | 0 | 2 |
| `https://www.staychina.org/zh-cn/contact` | 0 | 2 |
| `https://www.staychina.org/zh-cn` | 0 | 1 |
| `https://www.staychina.org/en/products` | 0 | 1 |

### 核对限制

页面维度可见首屏数据合计展现数已超过总览 50，且同一根路径同时显示 HTTP/HTTPS 与不同主机/路径形式。可能是页面尚未完整加载、动态报表读数更新不同步，或当前抽取没有完整捕获报告条件；因此该页表在导出并复核前只作为初步观察，**不能作为已审计的精确页面排名表**。暂不据此修改 canonical、重定向或页面内容。

## 后续动作

1. 重新打开报告并用同一日期范围、同一搜索类型导出完整 query、page 报表；核对指标总数与维度行是否一致。
2. 确认相似 URL、HTTP/HTTPS 行的完整归一化与索引状态。
3. 通过报告内交互取得代表性查询对应页面；完成后再确定 StayChina 优先修改页。
4. Xiaodu 与 Pomerol 使用完全相同窗口和过滤条件建立对应快照。

## 结论

当前只能确认 StayChina 最近 28 天总览是 2 clicks / 50 impressions / 4% CTR / average position 9，以及报告列出的查询和页面候选。搜索主题和落地页的交叉归因仍缺证据；未据此改站或请求重新编入索引。
