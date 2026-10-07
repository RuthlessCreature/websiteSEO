# Xiaodu：GSC 定向抓取请求记录（2026-10-08）

## 核查结果

本记录补充 GSC 网域属性 `sc-domain:xiaodu.tech` 的实时 URL Inspection。检查针对一条此前出现在“已发现 - 尚未编入索引”示例中的商业行业页，并对照一条已收录的解决方案页。

| URL | GSC URL Inspection / 实时测试 | 采取的动作 |
|---|---|---|
| https://xiaodu.tech/en/solutions/robotic-automation/ | URL Inspection 显示已编入索引；Googlebot Smartphone 于 2026-10-03 20:09:58 抓取成功；抓取和索引许可均为是；Google 选择该 URL 为规范页；来源 sitemap 为 `https://xiaodu.tech/sitemap.xml`。 | 未重复提交。 |
| https://xiaodu.tech/en/industries/mining-bulk-materials/ | URL Inspection 初始状态为 Google 尚不识别该 URL，抓取日期及规范数据为空。实时测试于 GSC 显示时间 2026-10-08 01:44:50 完成：URL 可编入索引、抓取许可为是、抓取成功、索引许可为是；用户声明规范页为自身。 | 已请求编入索引。GSC 确认 URL 已加入优先抓取队列。 |

## 解读与后续

- 索引报告（2026-10-04 更新）中的示例归类为“已发现 - 尚未编入索引”，但该行业 URL 的实时检查初始界面显示 Google 不认识它，且未列出 sitemap 或引用页。两者是不同视图、不同时间的 GSC 证据；不能据此断言 Google 已经抓取。
- 该页实时测试的抓取与索引技术条件均通过，且线上 sitemap/站内链接图也包含该页，因此已提交一次定向抓取请求。
- GSC 提交回执说明，多次提交同一 URL 不会改变队列顺序或优先级；不重复请求同一 URL。
- 收到请求回执只代表进入抓取队列，不代表 Google 已抓取、已收录或取得排名。后续在 GSC URL Inspection/索引报告复查状态变化，并以搜索表现报告观察曝光、点击与查询；本次没有证明排名变化。

## 可复核入口

- [Xiaodu GSC 网页索引报告](https://search.google.com/search-console/index?resource_id=sc-domain%3Axiaodu.tech)
- [待抓取页面](https://xiaodu.tech/en/industries/mining-bulk-materials/)
- [已收录对照页](https://xiaodu.tech/en/solutions/robotic-automation/)
- [未索引样本及站内链接图复核](SEO-%E5%B0%8F%E5%BA%A6-GSC%E6%9C%AA%E7%B4%A2%E5%BC%95%E6%A0%B7%E6%9C%AC%E4%B8%8E%E5%86%85%E9%93%BE%E5%A4%8D%E6%A0%B8-2026-10-08.md)

