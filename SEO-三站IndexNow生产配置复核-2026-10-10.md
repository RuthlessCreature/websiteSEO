# 三站 IndexNow 生产配置复核

复核日期：2026-10-10  
范围：`xiaodu.tech`、`www.staychina.org`、`pomerol.trade` 的线上 IndexNow 验证文件、sitemap 入口，以及网站 `main` 分支部署工作流。

## 结论

三站都已公开提供与源码配置匹配的 IndexNow 验证文件。三站各自的生产部署工作流均在部署成功后运行 IndexNow 通知脚本；StayChina 还要求生产 SEO smoke check 成功后才通知。该链路属于免费 URL 更新通知，不代表搜索引擎承诺抓取、收录或排名。

## 线上核查

| 站点 | 验证文件 | Sitemap | 结果 |
|---|---|---|---|
| Xiaodu | `https://xiaodu.tech/6ef27e4a81efe1ff6c679ee852d012f2.txt` 返回 HTTP 200，正文与脚本密钥一致 | `https://xiaodu.tech/sitemap.xml` 返回 HTTP 200；抽取到 170 个本站 URL | 通过 |
| StayChina | `https://www.staychina.org/6ef27e4a81efe1ff6c679ee852d012f2.txt` 返回 HTTP 200，正文与脚本密钥一致 | `https://www.staychina.org/sitemap-index.xml` 返回 HTTP 200；索引列出子 sitemap，脚本会递归读取 | 通过；本次未统计递归后的 URL 总数 |
| Pomerol | `https://pomerol.trade/6ef27e4a81efe1ff6c679ee852d012f2.txt` 返回 HTTP 200，正文与脚本密钥一致 | `https://pomerol.trade/sitemap.xml` 返回 HTTP 200；抽取到 155 个本站 URL | 通过 |

线上查询只读取公开验证文件和 sitemap，没有向 IndexNow 提交额外通知，也没有改动 Cloudflare 或网站仓库。

## 部署自动通知代码

- [Xiaodu 部署 workflow](https://github.com/RuthlessCreature/xWebsite/blob/main/.github/workflows/deploy.yml) 在 Worker 部署成功后运行 `node scripts/notify-indexnow.mjs`；[通知脚本](https://github.com/RuthlessCreature/xWebsite/blob/main/scripts/notify-indexnow.mjs) 会核验线上 key，读取本站 sitemap，并向 IndexNow API 提交通知。
- [StayChina 部署 workflow](https://github.com/RuthlessCreature/pWebsite/blob/main/.github/workflows/deploy-production.yml) 部署并通过生产 smoke check 后运行通知脚本；[通知脚本](https://github.com/RuthlessCreature/pWebsite/blob/main/scripts/notify-indexnow.mjs) 会核验 key，递归读取 sitemap index 与子 sitemap，再提交本站 canonical URL。
- [Pomerol 部署 workflow](https://github.com/RuthlessCreature/pWebsiteExport/blob/main/.github/workflows/deploy-cloudflare.yml) 部署并通过 SEO smoke check 后运行 `python scripts/notify_indexnow.py`；脚本会核验线上 key、解析 sitemap，并向 IndexNow 端点发送 URL 通知。

## 后续监测

1. 在每次成功生产部署后，查看对应 GitHub Actions 的 IndexNow 步骤是否完成。三个 workflow 对通知失败采用允许部署继续的策略，因此需单独看步骤日志。
2. 用 Google Search Console、Bing Webmaster Tools 中的索引报告观察抓取和收录结果；IndexNow HTTP 接受只代表通知被接受。
3. 排名和流量结论以各站 Search Console / Webmaster Tools 的实际查询数据为准。当前这次复核没有取得站长平台后台数据，也没有声称任何关键词排名或收录数量提升。
