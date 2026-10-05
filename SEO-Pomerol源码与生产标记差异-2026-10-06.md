# Pomerol SEO 源码与生产标记差异

核查日期：2026-10-06  
范围：只读核对 Pomerol SEO 生成器、仓库中的静态英文首页，以及线上英文首页的 Organization 联系点。未修改 Pomerol 网站仓库，也未触发部署。

## 观察结果

| 位置 | Organization 的 ContactPoint | 结果 |
|---|---|---|
| [SEO 生成器](https://github.com/RuthlessCreature/pWebsiteExport/blob/main/scripts/build_seo.py)（blob `c9a597fc67d10212c7f9af17b9a52e981f52b0eb`） | 生成 `contact@pomerol.trade` 与 Yusuf Gmail 两个 ContactPoint | 生成逻辑包含两个邮箱 |
| [仓库静态英文首页](https://github.com/RuthlessCreature/pWebsiteExport/blob/main/public/en/index.html)（blob `301093e6ac0adcae88c6caa74f05670b1f6976af`） | Organization 仅有 Gmail ContactPoint | 与生成器结果不一致 |
| [线上英文首页](https://pomerol.trade/en/) | HTTP 200；Organization 含两个邮箱 ContactPoint | 当前生产标记正确 |

因此这是**仓库中的生成后静态文件与生成器不一致**，并非当前线上联系邮箱缺失。SEO 专项仓库的实体审计以线上页面为对象，当前生产检查通过；但若后续部署直接使用未重新生成的静态文件，可能把旧的单联系人标记带回生产。

## 后续维护动作

下一次有权限更新 Pomerol 网站源码时：

1. 先核对生成器输入和构建/部署工作流。
2. 用仓库规定的 SEO 构建步骤重新生成页面，并比较英文首页的 JSON-LD 是否包含两个 ContactPoint。
3. 加一项源码产物一致性检查，防止生成器与提交的静态输出再次漂移。
4. 部署后复核线上首页和联系页，再记录新的生产回执。

本记录只用于 SEO 运维跟踪，不代表已修改网站源码或已部署修复。
