# 三站非品牌宽词搜索复核（2026-10-09）

## 今日线上证据

本日用公开搜索服务复核三组主要商业主题：industrial automation integrator China、teaching jobs in China、China sourcing agent / China supplier verification。结果用于了解当前返回的页面类型和品牌是否出现在样本中；公开搜索服务未固定 Google/Bing、地点、设备、个性化或完整结果集，**不作为精确名次报告**。

- **Xiaodu — industrial automation integrator China：**样本显示中国工业自动化集成商目录及竞争公司的集成服务页（包括 RevenueBase 中国目录与 SENTRADO 页面），未显示 xiaodu.tech。相关结果将授权资质、工程范围、交付阶段与可核实证据放在显著位置。Xiaodu 技术站点审计全绿、核心页可访问，仍不能替代真实第三方工程证据与行业引用；不要复制对手未经核验的认证、客户数或项目数。
- **StayChina — teaching jobs in China：**搜索结果主要由实时职位列表与招聘平台承接，含 Expat.com、Teast 和招聘品牌；StayChina 当前能在指南型查询样本中被发现，但没有当前真实在招岗位的证据，不能把指南页说成职位列表，也不能加虚构职位或 JobPosting 标记。短期宽词策略继续以 teaching in China / employer hiring preparation / work-permit fit 的信息意图为主，同时将教学指南和任何未来真实岗位严格区分。
- **Pomerol — China sourcing agent / supplier verification：**宽词 sourcing agent 样本以可说明实际流程和运营范围的采购服务页为主；supplier verification 样本出现独立核验内容与工具。Pomerol 新发布的供应商证据追踪器是具体的买家工具资产，但本日样本尚未证明其出现在宽词结果。继续补充可复用的真实买方交付物、来源与服务责任边界，避免将其描述成官方核验或供应商认证。

### 本次搜索参考

- [RevenueBase：中国工业自动化系统集成商目录](https://revenuebase.ai/companies/industrial-automation-system-integrators/china)
- [SENTRADO：工业自动化系统集成商服务页](https://sentrado.com/)
- [Expat.com：中国教学职位列表](https://www.expat.com/en/jobs/asia/china/social-teaching.html)
- [Teast：中国教学职位列表](https://teast.co/jobs/china)
- [StayChina：教学指南中心](https://www.staychina.org/en/guides)
- [YunSource：中国采购代理服务页](https://www.yunsource.com/)
- [AskChinaSuppliers：中国供应商核验指南](https://askchinasuppliers.com/supplier-verification/china-supplier-verification/)

以上对手页面里的认证、团队、项目数、业绩或客户案例均为其自述，本次未独立核实，不应移植到三个网站。

## 新页面索引发现：Pomerol

### 已确认

- 2026-10-09 通过生产 HTTP 请求读取 sitemap：Xiaodu 170 URL、StayChina 24 URL、Pomerol 155 URL；三个 sitemap 均返回 HTTP 200。
- 当前 Pomerol sitemap 已包含 https://pomerol.trade/tools/china-supplier-verification-kit/。
- 生产工具页此前已验证 HTTP 200，规范 URL、站内上下文链接、llms.txt 与 sitemap 条目均已随部署上线。
- 已登录 Google Search Console 的 Pomerol「站点地图」报告当前显示同一 sitemap.xml 的状态为“成功”，上次读取为 **2026-10-07**，发现 154 个网页。该读取时间早于新工具上线，且比当前 sitemap URL 数少 1；因此目前只能证明 Google 曾成功处理旧版本 sitemap，**不能证明新工具 URL 已被 Google 发现或收录**。
- 本轮尝试从该 GSC 页面继续进行 URL Inspection 时，浏览器交互没有完成；没有请求新页面索引，也没有重复提交 sitemap。下一步仍是用 GSC 的正式 URL Inspection 检查新工具页，只有显示可编入索引后才请求一次索引，并等待后续抓取报告回验。

## 对排名目标的结论

今日公开样本没有证明三个站点的非品牌商业宽词稳定进入搜索结果前 20。此前可读取的 GSC 基线仍分别显示 Xiaodu 无网页搜索展示、StayChina 指南查询约在 25 位附近、Pomerol 出货前检验查询约在 70–89 位区间；这些是不同日期的历史后台数据，不能把今天的搜索样本解释成排名增长。

当前直接影响宽词的最大差距仍是可核验的行业背书与真实业务证据，而不是再增加 sitemap、schema 或同义关键词页。后续应继续以站长平台的 query × page × country 数据判定落地页，把实质更新后的 URL 提交一次，再通过索引状态与成熟查询数据验证结果。

## 搜索样本引用

- 今日网络搜索样本：industrial automation integrator China、teaching jobs in China、China sourcing agent、China supplier verification。
- 对同一查询的搜索结果可能随地区、语言、账号、设备和时间变化；本记录不宣称 Google 或 Bing 的固定位置。

## 2026-10-09 GSC URL Inspection：StayChina 首页与 Pomerol 工具页

### StayChina 英文首页

在已登录的 GSC `sc-domain:staychina.org` 属性检查 `https://www.staychina.org/en`：
- 状态为“网址已收录到 Google”。Googlebot 智能手机版于 2026-10-07 17:56:53 成功抓取；允许抓取与索引；用户声明 canonical 为 `https://www.staychina.org/en`。
- 当前生产首页、联系页与新教学指南均 HTTP 200、canonical 自指向，并包含 Yusuf 姓名/联系方式；三页均不含旧联系人 Nicole、旧电话或 163 邮箱。
- 第三方搜索结果仍出现旧联系信息，但 GSC 已在最近两天抓取当前首页，且生产正文已更新。该搜索摘录不能作为当前 HTML 错误的证据；本轮不重复请求已收录且近期抓取的首页。

### Pomerol 供应商核验工具

在已登录的 GSC `sc-domain:pomerol.trade` 属性检查 `https://pomerol.trade/tools/china-supplier-verification-kit/`：
- 检查前状态为“网址尚未收录到 Google：Google 无法识别此网址”；GSC 未检测到引荐 sitemap、引荐页面，且没有抓取记录。
- 同日实时测试于 2026-10-09 11:26 完成，结果为“网址可编入 Google 索引”；增强功能检测到 1 项有效 Breadcrumbs。随后现场 HTTP 复核为 200、自指 canonical、无 noindex，并且当前 sitemap 含此 URL。
- 实时测试通过后，本次只提交一次 GSC 索引请求。GSC 明确确认“已将网址添加到优先抓取队列中”。这只证明已进入队列，不证明 Google 已重新抓取或收录；不要重复请求同一 URL。

### 同一时点的 GSC 概览数字

- StayChina 概览卡显示 27 个已编入索引、51 个未编入索引、2 次网页搜索点击。
- Pomerol 概览卡显示 140 个已编入索引、22 个未编入索引、1 次网页搜索点击。
- 这些是当时概览卡上的汇总数，没有在本次快照中读取其统一的统计时间窗；不能与上一轮的不同日期/时间范围直接比较，也不代表目标宽词排名改善。

下一次回验重点：重新打开该工具 URL Inspection 查看 Google 最近抓取与索引状态；再用同一 GSC 属性、相同过滤条件读取 query × page 报告。索引和宽词排名仍是两个不同的状态。
