# Bing Webmaster Tools 独立验证与 AI 可见度闭环（2026-10-08）

## 目的与权限边界

为 `xiaodu.tech`、`staychina.org`、`pomerol.trade` 建立 Bing 自有站长平台数据基线，并查看 Bing 搜索及 Copilot 的 AI Performance 报告。此前已撤销 Bing 对 Yusuf Google Search Console 的 OAuth 读取连接；本方案不恢复该连接，不导入 GSC 站点、sitemap 或分析数据。

## 当前已知状态

- 2026-10-06 的运维记录称 Bing 已处理三站 sitemap，合计 338 个发现 URL；StayChina 切换到直接 sitemap 后的新提交/处理状态当时尚待复核。该历史值不能代替当前 Bing 后台的“最后读取、成功/错误、索引”状态。
- Bing 搜索曾为 StayChina 报告少量搜索展示，但三站当前的 Bing 查询、页面、国家、位置和 AI Performance 数据尚未形成同一时间窗的完整截图/记录。
- 2026-10-08 从已登录浏览器导航到 Bing Webmaster Tools 后，页面标题显示“Home - Bing Webmaster Tools”；本轮浏览器读取接口连续超时，无法验证具体账号、站点属性或报告内容。未连接 Google OAuth、未提交站点或改 DNS。
- 三站公开 sitemap 与 robots 入口均可访问，且 sitemap 已由 robots.txt 声明；公开可访问不能证明 Bing 后台已验证或持续处理站点地图。
- Bing 官方帮助页列出的所有权验证方式包括 Domain Connect（若 DNS 服务支持）、自定义 XML 文件、meta tag 和 DNS CNAME。staychina.org 首页曾见到 `msvalidate.01`；xiaodu.tech 与 pomerol.trade 的首页抽样未见常见验证 meta，但可能已用 XML/DNS 或其他验证方式，不能据此判断未验证。

## 只用 Bing 自身权限的操作顺序

1. 在 Bing Webmaster Tools 中核对三站是否已存在，并记录每站的账户内验证状态、验证方法和最后验证时间。不要选“从 Google Search Console 导入”。
2. 对缺少有效所有权验证的站点，优先使用 Bing 页面为该属性生成的专属 DNS CNAME 或 XML 验证文件；如采用 meta tag，使用 Bing 当次生成的精确值。不得复制、猜测或在站点间复用 token。
3. 验证后检查 Bing Sitemaps：Xiaodu `https://xiaodu.tech/sitemap.xml`、StayChina `https://www.staychina.org/sitemap.xml`、Pomerol `https://pomerol.trade/sitemap.xml`。逐站记录提交状态、最后读取时间、发现 URL 数、错误详情及索引覆盖；发现数不等于已索引数。
4. 打开 Bing Search Performance 与 **AI Performance**，以固定 3 个月窗口记录 impressions、clicks、CTR、平均排名，以及 query × page × country 维度。AI Performance 当前仍为公开预览，单独说明其覆盖 Copilot、Bing AI summaries 与参与合作的体验；不能外推为 ChatGPT、Claude 或全部 AI 搜索的引用数据。
5. 与 Cloudflare 对照同一窗口的 Bingbot/AI crawler 边缘事件。只有 Cloudflare Verified Bot 或 Bing 官方诊断才能进一步验证爬虫身份；仅凭 UA 名称及 HTTP 200 不构成真实身份或收录证明。

## 提交与效果口径

- Microsoft 当前推荐 IndexNow 通知参与平台上的 URL 更新；它与 sitemap 的全站发现作用不同。三站已有部署记录显示部分 IndexNow 请求被接收，但 HTTP 200/接收回执不代表已抓取、收录、排名或 AI 引用。
- Bing Webmaster Tools 的 sitemap 报告才可核实 Bing 侧提交/处理状态；IndexNow Insights 可用于查看提交、抓取与索引之间的差异。
- Microsoft 文档提示旧 SOAP/POX Webmaster API 将于 **2026-08-31** 退役；若未来做自动化，应使用官方当前 REST 接口，不依赖旧 SDK/接口。
- 不要把全站平均排名当作目标商业查询位置。最终排名目标要按站点、查询、国家、设备和固定周期核实；第 1–2 页是否达到必须由具体目标查询证据支持。

## 官方资料

- [Bing: Add and Verify a Site](https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b)
- [Bing: Start Using Webmaster Tools to Improve Site Visibility](https://blogs.bing.com/webmaster/2025/6/Start-Using-Bing-Webmaster-Tools-to-Improve-Your-Site-Visibility/)
- [Bing: Introducing AI Performance in Public Preview](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/)
- [Bing: Keeping Content Discoverable with Sitemaps in AI Powered Search](https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/)
- [Bing: IndexNow Insights](https://blogs.bing.com/webmaster/2024/3/Optimize-your-Impact-with-IndexNow-Insights/)

## 待闭环

Bing Webmaster Tools 的账户内页面读取接口恢复后，逐站完成“验证 → sitemap 状态 → Search Performance → AI Performance → Cloudflare 边缘事件”并记录实际数值。若属性已由直接验证保留，则无需重复添加。此项目前是账户数据未复核，不是公开 sitemap/robots 技术故障。
