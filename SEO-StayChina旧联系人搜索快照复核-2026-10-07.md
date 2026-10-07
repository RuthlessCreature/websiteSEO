# StayChina 旧联系人搜索快照复核（2026-10-07）

## 结论

公开网页搜索仍返回 StayChina 旧联系人信息，但直接读取生产页面的服务器返回 HTML 已确认联系人已统一更新为 Yusuf。现有证据支持“搜索索引/摘要尚未刷新”，不支持“生产页面仍显示旧联系人”。

## 生产页面核验

2026-10-07 直接请求以下页面，全部返回 HTTP 200；响应 HTML 均包含 Yusuf 联系方式 `+86 132 4269 4270`、`abd.yusuf.ibrahim.mustafa@gmail.com`，均未命中旧姓名 Nicole、旧号码 `13923387986` 或 `163.com`：

| 页面 | HTTP | 旧联系人字符串 | 新联系人字符串 |
|---|---:|---|---|
| [英文首页](https://www.staychina.org/en) | 200 | 未发现 | 已发现 |
| [公司设立页](https://www.staychina.org/en/china-setup) | 200 | 未发现 | 已发现 |
| [联系页](https://www.staychina.org/en/contact) | 200 | 未发现 | 已发现 |
| [中文幼儿园外教招聘页](https://www.staychina.org/zh-cn/kindergarten-foreign-teacher-recruitment) | 200 | 未发现 | 已发现 |

## 搜索快照证据

2026-10-07 的公开搜索抽查仍将旧联系人展示在以下已收录 URL 的正文/摘要中：

- `https://www.staychina.org/en`
- `https://www.staychina.org/en/china-setup`
- `https://www.staychina.org/en/contact`
- `https://www.staychina.org/en/products`
- `https://www.staychina.org/en/institutions`
- `https://www.staychina.org/zh-cn/kindergarten-foreign-teacher-recruitment`

搜索工具给这些结果标注的抓取时间为约一个月前（中文招聘页约三个月前）。这是搜索索引快照，不是当前生产 HTML。页面仍可能在特定查询中显示旧摘要，直到搜索引擎重新抓取并更新索引。

## 后续动作与状态

1. 在 Google Search Console 对仍显示旧联系内容的规范 URL 使用“网址检查”并申请重新编入索引；申请后记录提交回执，并在后续核对 Google 选定 canonical、最后抓取时间和实际索引正文。
2. 在 Bing Webmaster Tools 对相同规范 URL 使用 URL Inspection / 提交 URL；以平台确认的抓取或索引状态为证，不把提交动作记成已更新。
3. 搜索缓存清除前，不通过临时改 URL、批量重定向或另建重复页面来试图刷新摘要。
4. 2026-10-07 当前浏览器中的 GSC 检查页未能由自动化接口稳定打开，本轮没有成功提交 Google 重新抓取请求。故搜索快照刷新状态仍未解决，保留为后续事项。

## SEO 影响

旧联系人摘要可能削弱品牌实体一致性和询盘可信度。由于生产页面已经正确，应优先推动搜索引擎刷新规范 URL 的索引；同时确保 sitemap 的 `lastmod` 与真实内容更新时间一致，但不可虚构更新时间。
