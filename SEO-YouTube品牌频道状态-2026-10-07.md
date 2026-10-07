# YouTube 品牌频道公开状态复核（2026-10-07）

按桌面 Chrome User-Agent 直接请求三个频道的公开 About 页面：

| 品牌 | 公开 URL | HTTP 与页面元数据 | 结论 |
|---|---|---|---|
| Xiaodu | https://www.youtube.com/@XiaoduAutomation/about | HTTP 200；title 为 “Xiaodu Automation - YouTube”；description 以 Xiaodu 的工业自动化介绍开头 | 公开频道页面可访问，元数据与品牌基本匹配 |
| StayChina | https://www.youtube.com/@StayChinaOrg/about | HTTP 200；title 为 “StayChina - YouTube”；description 以 StayChina 在华设立与专业人士指南介绍开头 | 公开频道页面可访问，元数据与品牌基本匹配 |
| Pomerol | https://www.youtube.com/@PomerolTrade/about | HTTP 404 | 该 handle 尚无可访问的公开频道页面；不能记为创建完成 |

PowerShell 默认 User-Agent 收到过 YouTube 通用语言页；本记录使用桌面 Chrome User-Agent 重取后，Xiaodu / StayChina 返回完整频道元数据。Pomerol 在相同 Chrome User-Agent 下仍返回 404。该公开端点结果不能说明账号登录态、视频发布、频道主邮箱归属或 Google 搜索对这些页面的收录状态。

## SEO 影响与后续

- Xiaodu 和 StayChina 已有两个可公开核验的品牌实体页面，但之前资料显示尚无视频；需要后续发布有实用信息的原创视频，并将真实频道链接纳入各自的结构化 `sameAs` 和站点社交链接，后者涉及网站仓库，本轮不触碰。
- Pomerol 的频道尚未建成，当前没有可添加的真实 YouTube 频道实体链接。此前已完成电话验证步骤，但公开频道地址仍返回 404；在能够恢复 YouTube 登录 UI 后需从账号内确认是否创建成功。不要将预约 handle 或生成的 URL 当作上线证明。
- 上传与公开发布内容前，应检查视频中业务主张、素材权利和描述链接；账号状态、发布与搜索引擎收录分开记录。

## YouTube 频道再次复核（2026-10-08）

使用桌面 Chrome User-Agent 重新请求三条 `/about` 页面：

| 品牌 | 当前公开状态 | 可验证信息 |
|---|---|---|
| Xiaodu | HTTP 200 | Channel ID `UCQYlG-WsgjLUaZUruqAsrVA`；标题 `Xiaodu Automation - YouTube`；描述以面向制造、矿业、实验室和物流的工业自动化方案开头 |
| StayChina | HTTP 200 | Channel ID `UCejnhaXLiO9fpdnXfeSt1Kw`；标题 `StayChina - YouTube`；描述涵盖在华设立及工作许可/居留信息 |
| Pomerol | HTTP 404 | 没有公开频道元数据；`@PomerolTrade` 仍未创建或未公开可访问 |

近期通过电话验证码只证明某个 YouTube 验证步骤完成，不能证明 Pomerol 品牌频道创建成功。针对“创建 Pomerol 频道”的浏览器会话在页面读取阶段超时，本轮没有发出创建请求，也没有接受新的 YouTube 服务条款；不把 404 的 handle 写入 Pomerol 网站或结构化数据。后续应在账号页面可正常操作时创建并确认公开频道，再将已验证的频道 URL 加入 Pomerol 官网社交链接和 `sameAs`。
