# 免费 Lighthouse 周度 SEO 与体验诊断

日期：2026-10-08

## 变更记录

公共仓库新增 Lighthouse 周度移动端审计，按周检查三个生产页面的 Performance、Accessibility、Best Practices、SEO 类别，以及 LCP、CLS、TBT、Speed Index 等实验室指标。报告通过 GitHub Actions 作为 workflow artifact 保存 90 天；不写回站点仓库，也不触发 Cloudflare Worker 部署。

- Xiaodu：`https://xiaodu.tech/en/solutions/`
- StayChina：`https://www.staychina.org/en/china-setup`
- Pomerol：`https://pomerol.trade/resources/guides/china-pre-shipment-inspection-guide/`

公开仓库的 GitHub Actions 标准托管 runner 可免费使用。工作流固定 Lighthouse 版本并运行在移动端配置，减少版本变化带来的噪声。首轮 GitHub Actions 运行 [37708232369](https://github.com/RuthlessCreature/websiteSEO/actions/runs/37708232369) 已完成，工作流结果为 success，三条 Lighthouse CLI 调用均执行完成，并上传了包含原始 JSON 与 Markdown 汇总的 artifact（保留 90 天）。该结果只证明审计作业完成；Cloudflare 可能向 CI 返回挑战页，需查看报告中的最终页面响应与各项数据，不把作业 success 视为每个页面内容均可抓取。分数不抄录进此记录，以免把一次波动的 lab 样本当成长期基线。

## 如何解读

Lighthouse 是一次合成实验室测试，受 runner、网络、缓存及页面响应影响。单次分数不是实际用户的 Core Web Vitals、搜索名次、索引状态或排名保证。将按同一页面的多周趋势查看，并结合 Search Console 的实际体验/搜索数据判断。LCP、CLS 等单次 lab 数值不能替代 CrUX field data。

StayChina Cloudflare 对部分未验证的 crawler User-Agent 曾产生挑战响应。GitHub runner 上的 Lighthouse 若遇到边缘挑战，报告反映的是该 runner 当次可见的响应，不代表 Google/Bing 验证爬虫的真实抓取结果；工作流保留报告供诊断，不会把挑战页面得分当成正常内容页表现。

## 为什么新增本地审计

本轮匿名 PageSpeed Insights API 请求触发 Google API 的 HTTP 429，返回的项目每日查询额度为 0。这是匿名 API 项目配额限制，不能解读为站点故障。改为在公开 SEO 仓库使用开源 Lighthouse CLI 与公开仓库 Actions，避免依赖 PageSpeed API 配额，也不需要付费密钥。

## 参考

- [Lighthouse v13.5.0 release](https://github.com/GoogleChrome/lighthouse/releases/tag/v13.5.0)
- [GitHub Actions 托管 runner 说明及公开仓库免费用量](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job)
- [Google PageSpeed Insights API 入门](https://developers.google.com/speed/docs/insights/v5/get-started?hl=en)

## 2026-10-08 首轮原始 Lighthouse 报告发现

读取首次周审计原始 JSON（GitHub Actions run `37708824335`，Lighthouse `13.5.0`）后，确认三条命令都执行成功之外，页面还存在以下真实改进项。它们是一轮移动端实验室样本，需在修复后用同一配置复测；不能代替 CrUX 现场数据或 Search Console 排名证据。

| 页面 | Performance | Accessibility | Best Practices | SEO | 主要发现 |
|---|---:|---:|---:|---:|---|
| Xiaodu `/en/solutions/` | 94 | 78 | 73 | 100 | 三处文字对比度低于 Lighthouse 检查值；卡片 `h3` 出现标题层级跳级；语言选择器没有可访问名称；浏览器记录一个 404 资源错误（本 JSON 未定位具体 URL）；Pexels 图片估算可节省约 388 KiB。 |
| StayChina `/en/china-setup` | 77 | 97 | 81 | 100 | LCP 3.6 秒、TBT 490 毫秒、TTI 4.7 秒；主线程 JavaScript 执行约 2.3 秒。报告归因包含 Cloudflare `/cdn-cgi/challenge-platform/scripts/jsd/main.js` 与 Next.js chunk；Unsplash 主图估算可节省约 126 KiB。 |
| Pomerol 出货前检验指南 | 96 | 95 | 92 | 100 | 两处低对比度文字、页脚标题层级跳级、首屏图片显示比例与实际比例不一致且分辨率不足；图片估算可节省约 91 KiB。 |

### 实施顺序

1. **StayChina：先拆解慢交互来源。** 先对 Next.js 页面 bundle 与 Cloudflare JavaScript Detections/挑战注入分别做归因，确认 Lighthouse 普通浏览器请求的 `jsd` 脚本是否来自现有安全配置、适用范围和实际访客触发比例；不为拿分直接绕过挑战或降低边缘保护。并优先压缩/裁剪首页图片、减少非关键客户端 JavaScript，再以同一 Lighthouse 配置复测。
2. **Xiaodu：修复可直接定位的无障碍项。** 提升低对比度文字颜色；为语言选择器添加明确标签；理顺页面标题层级；优先提供尺寸匹配、压缩后的同源图片。404 需从下一轮浏览器网络日志定位后再改。
3. **Pomerol：修复图片比例/分辨率与对比度。** 给首屏图片匹配自然比例并生成合适尺寸/格式变体；调整日期与品牌小字的对比度；把页脚标题级别接入连续的页面层级。

相关节点来自原始 Lighthouse JSON：Xiaodu 对比度分别测得 2.17、4.09、2.54（该小号正文需满足更高的可读对比标准）；StayChina 两个主要执行项为 Cloudflare 挑战平台脚本与 Next.js chunk；Pomerol 对比度最低为 2.82，图片自然比例与指定显示尺寸不符。修复应落在对应网站源码/Cloudflare配置后再复测；本报告更新只记录诊断，不代表生产站已修复或排名已提升。
