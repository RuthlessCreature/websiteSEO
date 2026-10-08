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
