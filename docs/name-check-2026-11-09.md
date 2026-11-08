# 名称核查 / Name screening

日期：2026-11-09。用途：面向中英文用户的免费开源机票研究 Skill，主要地区：中国、新加坡。本记录是公开名称初筛，未完成官方商标清查，不保证不侵权或可以注册。

## 新工作名称：FareTally · 票价有数

仓库及 Skill 标识：`fare-tally`。

英文由 fare（票价）和 tally（合计、核算）组成，强调把票价和额外开销算清楚，不承诺最低价。中文借用“心中有数”，比“航价”更口语化，适合价格、时段、行李和实际花费的权衡。局限是英文可能被理解为票价计算器，中文也可能涵盖其他交通票价；应配合“flight research skill／低价机票研究”说明。

以上是编辑判断，不是商标显著性或法律风险评级。两个英文词均为常用词，中文也有描述意味；完整组合的在先权利仍须独立查询。

## 公开名称及项目查询

| 范围 | 实际查询与观察 | 限制 |
| --- | --- | --- |
| 网页完整英文 | `"FareTally"`，以及附加 flight、software、app、trademark 的查询 | 未核实到以此为名的直接同名产品；不覆盖未索引、未公开或地区性使用。 |
| 英文变体 | `"Fare Tally" flight`、`"Fare-Tally" flight software` | 返回分词或正文描述。例如 App Store 的 TripListPlanner 文案出现普通短语“fare tally”，其标题不是 FareTally；未把它当成同名品牌，也不能据此排除近似权利。 |
| 中文网页 | `"票价有数"`、`"票價有數"`，以及软件／项目／机票限定 | 未核实到直接同名产品；放宽分词的无关结果不计作同名项目。 |
| GitHub 原生仓库搜索 | 浏览器实际读取 [FareTally 查询](https://github.com/search?q=FareTally&type=repositories) | 页面显示 **0 repositories**；不覆盖私有仓库或全部代码文件。 |
| GitHub 中文完整词 | 浏览器读取 [“票价有数”查询](https://github.com/search?q=%22%E7%A5%A8%E4%BB%B7%E6%9C%89%E6%95%B0%22&type=repositories) | 页面显示 **0 repositories**。未加引号时出现50条分字匹配的股票等结果，不能称为50个同名项目。 |
| GitHub AI resources | FareTally 相关建议共11条，已查看两页 | 条目标题为 Tallyfy、Follore、TapTax、Finn、Trailmark、Truthifi、Cashly、Territory Report、Avalara、To Tickets、NAV Tie-Out，未见同名标题。相关建议数不等于同名项目数。 |

网页抓取器未能读取 GitHub 搜索页，shell 的 API 请求也因 DNS 失败；上述结果来自随后在浏览器实际读取的页面，没有使用失败请求推断零结果。未完成 Gitee、GitLab、各地区应用商店内部搜索、域名或社交账号占用的完整核查。

## 为什么替换 FareMosaic · 航价拼图

原名表达“组合机场与日期”，中英文含义协调。不过，航空领域已有 Mosaic 产品：

- [Sabre 官方 Flight Shop Lite 文档](https://developer.sabre.com/rest-api/flightshoplite-api/v1/index.html)使用 **Sabre Mosaic® Flight Shop Lite**，用于发现可用低价、比较航班与行程，和本 Skill 的用途接近。搜索引擎可读取官方文档正文，直接抓取文档壳页仅返回脚本框架；未核实其在中国或新加坡的注册范围与状态。
- [JetBlue 官方页面](https://www.jetblue.com/help/mosaic)把 **Mosaic** 用于 TrueBlue 高级会员等级。
- GitHub 原生 [FareMosaic 仓库查询](https://github.com/search?q=FareMosaic&type=repositories)显示0条。网页初筛也未核实到 FareMosaic／航价拼图 的直接同名项目。

完整名没有同名项目，不等于没有近似名称问题；共同包含 Mosaic，也不自动构成侵权。改名是为了减少已经发现的同行业品牌联想，不是认定旧名侵权，也不是证明新名已获商标许可。旧 `fare-mosaic` 目录和压缩包保留，未删除或覆盖。

更早的 FareLens 也不沿用：[Hatch 产品原页](https://whatsinmydata.com/project/farelens/)已经使用该名称。此前 GitHub FareLens 索引线索直接打开返回404，不能认定该仓库当前公开。

## 官方商标检索尚未完成

此前在 IPOS Digital Hub 查询旧候选名时遇到 reCAPTCHA，未取得有效查询结果。**没有完成 FareTally、Fare Tally、票价有数及近似名称的新加坡官方检索；中国官方注册库也没有取得有效结果。** 网页搜索加上 trademark 不能替代注册库检索。

[IPOS 注册指南](https://www.ipos.gov.sg/about-ip/trade-marks/how-to-register/)要求关注相同及近似标记，提供 Similar Mark Search；[国家知识产权局近似判断答复](https://www.cnipa.gov.cn/jact/front/mailpubdetail.do?sysid=13&transactId=427132)指向《商标审查审理指南》的相同、近似审查。判断须结合完整名称、读音含义、实际商品服务和目标地区，而非仅看 GitHub 或一个共同英文词。

后续若要把名称作为长期品牌使用或申请商标，建议补做中国、新加坡的专业近似检索：完整英文、空格／连字符变体、简繁中文及近似音义，核对权利人、申请／注册状态和核定商品服务。软件及服务类别须按实际提供方式确认；未来若扩展售票或旅行服务，重新评估范围。免费开源、MIT 许可和无关联声明均不自动消除名称权利问题。

**结论：采用 FareTally／票价有数作为公开初筛后的工作名称；未发现直接同名项目的有效证据，未取得商标可用或不侵权保证。** 网站工作仍搁置，没有执行 GitHub 或网站发布。

## English

The new working name is **FareTally / 票价有数** (`fare-tally`). Fare + tally conveys checking fares and total costs; the Chinese name suggests understanding what a ticket really costs. Add a “flight research skill” descriptor to distinguish it from a calculator or other ticketing tools.

Public web searches did not establish a directly same-named product. GitHub's native public repository search visibly returned zero repositories for FareTally and the quoted Chinese name on 9 November 2026. Related AI-resource suggestions were inspected and did not have the same title. This is a bounded observation, not proof of worldwide uniqueness; private/unindexed projects, internal app-store listings and domains were not comprehensively checked.

FareMosaic was replaced because Sabre uses Mosaic in flight-shopping software and JetBlue uses it for loyalty status. Shared words alone do not establish infringement. No usable China or Singapore registry clearance was obtained for either language of the new name. Open-source licensing does not grant rights to third-party brands. Review relevant registers, similar marks and actual goods/services before relying on this as a cleared or registered brand.
