# Xiaodu 已发现未索引 URL：第一轮 sitemap 对照（2026-10-08）

## 权威现状

Google Search Console 的 Xiaodu 网域索引报告（最近更新 2026-10-04）显示：

- 已编入索引：75
- 未编入索引：105，其中 90 个“已发现 - 尚未编入索引”
- 已抓取 - 尚未编入索引：12
- 备用网页（规范页已适当标记）：1
- Google 选择的规范页与用户指定不同：1
- robots.txt 屏蔽：1（报告当时验证已开始）

当前 GSC 搜索效果报告选择“过去 3 个月”，但图表可见日期只有 2026-09-30 至 2026-10-04，显示 0 次展示、0 次点击。不要据此声称此前完整三个月没有展示。

## 当前线上 Sitemap 与语言版本

2026-10-08 直接读取 `https://xiaodu.tech/sitemap.xml` 成功，XML 中共有 170 个页面 `<loc>`，按语言分布如下：

- `en`：25
- `zh-cn`：25
- `zh-tw`、`ja`、`es`、`pt`、`ru`：各 24

也就是约 24–25 个同主题路径跨七种语言提供版本，另有一篇项目清单资源目前只出现于英文和简体中文。Search Console 10 月 4 日报告记录 180 个已知页面，和 10 月 8 日线上 sitemap 的 170 个页面不完全相等；因为报告日期不同，这只是需要核对的差额，不足以证明有 10 个失联页面。

对 `/solutions/` 的七种语言版本做了实时 HTML 抽查：

- 每个样本的 canonical 指向自身语言版本。
- 每个样本带 8 个 alternate/hreflang 链接（七个语言版本及默认版本）。
- H1 与页面主标题随语言变化。提取的页面文本约 1,821 至 4,208 字符，表面上不是空页；字符量不等同于翻译质量或独立搜索价值。
- 这一轮只抽查解决方案索引页，不代表其余 169 个 sitemap 页面都已逐个核验。

## 结论

当前证据不支持把 90 个未收录 URL 一概归因于多语言重复：GSC 对“alternate canonical”只报告 1 个，样本服务页也使用自指 canonical 和成组 hreflang。

更可能需要优先区分的是各 URL 类型的索引价值、内容独特性、内部链接深度及 Google 是否已抓取。90 个“已发现”表示 Google 知道 URL，但该报告原因本身不能说明具体页面或原因；不能通过批量重提 sitemap 解决未知的内容质量问题。

## 下一步执行

1. 从 GSC 的“已发现 - 尚未编入索引”原因详情导出示例 URL。按语言、页面类型（首页、服务、行业、场景案例、联系页、资源页）、是否在当前 sitemap 中、内部链接深度分组。
2. 先检查同时出现在 sitemap、但没有被编入索引的商业意图页面；逐页复核主内容是否在翻译后保留了具体行业、输入/输出、适用条件、交付边界和可验证证据。
3. 对同一主题的多语言页核对真实翻译质量和 hreflang 返回闭环；不要因为 URL 多就合并确有当地语言需求的页面。
4. 将薄弱的示例型案例明确标注为 illustrative scenario，补充能公开核实的技术细节；没有获准的一手客户证据时，不将其包装成真实案例。
5. 只有重要、可索引、canonical 正确且有足够原创价值的页面才保留在 sitemap 并请求重新抓取；重定向、noindex、规范替代及低价值重复页按各自情况处理。

## 可复核入口

- Sitemap：https://xiaodu.tech/sitemap.xml
- 解决方案页：https://xiaodu.tech/en/solutions/
- GSC 索引报告：https://search.google.com/search-console/index?resource_id=sc-domain%3Axiaodu.tech
- GSC 搜索效果：https://search.google.com/search-console/performance/search-analytics?resource_id=sc-domain%3Axiaodu.tech
