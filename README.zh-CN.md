# FareTally · 航价笔记

简体中文 · [English](README.md)

一个免费开源的机票研究 Skill：先聊清楚需求，再组合比较机场、日期、时段、行李和实际花费，寻找适合你的低价机票。

## 它会怎么帮你

1. **先问再查**：出发地及周边机场、去程日期和时间、每站停留、返程日期和时间、必须抵达的截止时间、人数舱位、手提和托运行李、廉航、中转、特殊要求。
2. **系统覆盖**：前后相邻日期、日期窗口两端、回程日期、机场组合和不同路线都有记录，避免只查中间几天。范围太大会说明取舍，不偷偷截断。
3. **重核整套票**：多程／缺口程按实际整套报价比较，换一段后重新核价，不把不同组合的单程价随意相加。
4. **不只盯票面价**：比较行李费、机场交通、中转住宿和不理想时刻；未知费用会注明，不编造“最低总成本”。
5. **讲清依据**：区分起价、逐段选择价和最后一程报价，检查实际抵达日期、午夜入住、酒店晚数、过境条件，并说明哪些没查完。

可接受的机场越多，越有机会找到低票价；但远机场可能增加交通费和时间。你不用提前懂机场代码，告诉它城市和可接受的交通范围即可。

## 使用前需要什么

需要支持本地 Skill 的 Codex，以及能实时访问机票页面的浏览器／搜索工具或合适的授权连接器。**只装 Skill 不会自动获得携程接口、实时库存或登录权限。** 本包没有附带订票连接器。Python 3.10+ 仅用于可选的离线组合／覆盖检查工具。

普通 ChatGPT 聊天不会因为你下载了这个仓库就自动安装 Skill。其他兼容 Agent 可参考 SKILL.md，但需要各自的安装与浏览能力；本包主要按 Codex 的本地 Skill 方式提供。

## 安装：推荐方法

将下面这段**发到 Codex 对话框**，即可从已发布的仓库安装：

```text
$skill-installer 请从 https://github.com/DaySense/fare-tally/tree/main/skills/fare-tally 安装这个 Skill。
```

这不是终端命令。链接已填写本项目的真实仓库地址。如果你的环境没有 skill-installer，用下面的手动方法。

[下载单 Skill 安装包](https://github.com/DaySense/fare-tally/releases/download/v0.1.2/fare-tally-skill-v0.1.2.zip) · [最新发布版](https://github.com/DaySense/fare-tally/releases/latest)

## 安装：手动方法，不需要终端

1. 在 GitHub 仓库点击 **Code → Download ZIP**，解压。
2. 找到里面的 `skills/fare-tally` 文件夹，**整个复制**，不要只复制 SKILL.md。
3. 放进你当前 Codex 版本使用的 Skill 目录。现行官方文档的用户目录是 `~/.agents/skills/`，单项目目录是 `.agents/skills/`。
4. 确认最后路径是 `<Skill目录>/fare-tally/SKILL.md`，旁边仍有 agents、references、scripts 和 examples。不要多套一层仓库文件夹。
5. 下一轮对话尝试调用；没有出现时重启 Codex，检查安装位置。旧环境的目录可能不同，优先让自带 skill-installer 处理，避免在多个位置装重复版本。

macOS 可在 Finder 的“前往 → 前往文件夹”中输入目录；Windows 用户在自己的用户文件夹下寻找或建立 `.agents/skills`。安装位置以当前产品文档及版本为准。[官方 Skill 指南](https://learn.chatgpt.com/docs/build-skills)；[官方目录示例](https://developers.openai.com/api/reference/cli)。

## 开始使用

```text
用 $fare-tally 帮我查机票。我想尽量便宜，但不想凌晨出发。请先确认机场、日期、停留、行李和中转条件，再开始搜。
```

```text
Use $fare-tally to find cheaper flights. My dates are flexible, but I want reasonable departure times. Please clarify airport, baggage and connection options before searching.
```

如果查价需要登录携程或其他平台，它会解释原因及使用哪个浏览器，请你自己输入密码、短信验证码和完成验证。你另一个浏览器的登录状态不一定共享；不要把凭据发给 Agent。查票不代表授权下单、锁票或付款。

## 查价范围与隐私

只能承诺“已查范围内已核实的低价”，不能保证全市场最低。匿名／会员／优惠券价格会区别记录。过境签以具体航班和证件条件核对；未知状态不会写成免签。

实际行程、报价记录、截图和浏览器信息应保存在仓库之外的私人目录。不要把它们提交到公开仓库或公开 Issue。本包示例均为虚构，不含创建者的私人查票记录。

## 可选的防漏查工具

Skill 内附 Python 标准库脚本，展开日期和机场组合、列出未完成查询。它**不联网、不抓取携程、不生成机票报价**，也不根据出发日期差假定实际住宿晚数。超过设定组合上限时会报错，不静默只做前几条。

用法和数据格式见 [coverage.md](skills/fare-tally/references/coverage.md)。普通使用者直接让 Agent 按 Skill 工作即可，不必自己操作脚本。

## 发布与许可

[GitHub 新手发布教程](docs/publish.zh-CN.md)包含 README 安装段落的修改方法。已附 MIT 许可证，发布前请核对版权署名；可按需要更换许可。

**新工作名称为 FareTally／航价笔记**。原名 FareMosaic 因航空领域已有 Mosaic 产品而调整，旧版本保留。公开初筛未发现直接同名项目，但中国、新加坡的官方商标清查尚未完成；不保证可注册或不侵权。中文名本轮由“票价有数”改为“航价笔记”，参见[中文名称更新记录](docs/chinese-name-check-2026-11-09.md)及[之前的英文名称核查记录](docs/name-check-2026-11-09.md)。[验证记录](docs/validation.md)区分离线检查和未进行的真实票价测试。
