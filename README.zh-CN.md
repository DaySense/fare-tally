# FareTally · 航价笔记

简体中文 · [English](README.md)

[![skills.sh 安装统计](https://skills.sh/b/daysense/fare-tally)](https://skills.sh/daysense/fare-tally/fare-tally)

一个免费开源的低价机票研究 Skill。它帮助 AI 助手先问清需求，再比较灵活航班方案，说明实际花费和取舍。

![FareTally 10 秒动态预览：先问清需求、展开方案、比较总成本](https://github.com/user-attachments/assets/bac18abe-49a2-4a4a-b6a4-527ddf9ea801)

[观看 48 秒中文项目介绍](https://github.com/user-attachments/assets/738bbf65-39ad-4467-ab57-37547711fde9)。视频为流程示意，价格是示例数字，不是实时机票报价。

## 它能做什么

- **先确认需求**：周边机场、去程和返程的日期与时段、每站停留、最晚抵达时间、人数舱位、行李、廉航、中转及特殊要求。
- **记录查询范围**：覆盖约定范围内的前后日期、日期窗口两端、回程日期、机场组合和不同路线；没有查完或被阻挡的部分会明确列出。
- **比较整套票价**：支持单程、往返、多程和缺口程；换一段航班后重新核对整套价格。
- **比较实际花费**：考虑必要行李、强制费用、机场交通、中转住宿及不理想时刻；未知费用保持未知。
- **核对关键细节**：实际当地抵达日期、酒店预订晚数、时区、所需行李、票价条款及会员或优惠资格。
- **支持中英文**：使用你熟悉的语言和订票平台；可以查携程，但不会默认任何平台永远最便宜。

可接受的机场、日期越多，越有机会发现低价；但额外交通费和不便时刻可能抵消省下的钱。不知道机场代码也没关系，告诉它城市和可接受的地面交通范围即可。

## 使用条件

需要支持本地 Skill 的 Codex，以及可用的浏览／搜索工具或合适的授权机票查询连接器。Skill 提供研究流程，不自带实时库存、浏览器、订票接口或平台账号。Python 3.10+ 仅用于可选的离线覆盖检查工具。

## 安装

把下面这段**发送到 Codex 对话框**，不是终端：

```text
$skill-installer 请从 https://github.com/DaySense/fare-tally/tree/main/skills/fare-tally 安装这个 Skill。
```

[最新发布版](https://github.com/DaySense/fare-tally/releases/latest) · [下载 Skill 安装包](https://github.com/DaySense/fare-tally/releases/download/v0.1.3/fare-tally-skill-v0.1.3.zip)

### 使用 skills CLI 安装

另一种方式：先安装 Node.js 22.20+、npm 和 Git，再在**想使用这个 Skill 的项目目录中打开终端**，运行：

```bash
npx skills add DaySense/fare-tally --skill fare-tally --agent codex
```

按提示确认安装。默认仅安装到当前项目；添加 `--global` 可供不同项目使用。安装后，在 Codex 的下一轮对话尝试 `$fare-tally`。

这个 CLI 会发送用于 skills.sh 统计的匿名安装数据；设置环境变量 `DISABLE_TELEMETRY=1` 可退出统计。参见 [CLI 文档](https://github.com/vercel-labs/skills)及 [FareTally 目录页](https://skills.sh/daysense/fare-tally/fare-tally)。被目录收录不代表兼容全部 AI 助手，本项目的使用说明与验证以 Codex 为目标。

### 手动安装

1. 下载并解压 **Skill 安装包**，里面直接是 `fare-tally` 文件夹。如果使用仓库的 **Code → Download ZIP**，则找到解压内容中的 `skills/fare-tally`。
2. 将这个 **完整 Skill 文件夹**复制到当前 Codex 的 Skill 目录：个人使用可放 `~/.agents/skills/`，仅供某项目使用可放该项目的 `.agents/skills/`。
3. 最终路径应为 `<Skill目录>/fare-tally/SKILL.md`，旁边保留 `agents`、`references`、`scripts` 和 `examples`，不要额外套一层仓库文件夹。
4. 下一轮对话尝试调用 `$fare-tally`。没有出现时，检查文件夹并重启 Codex。更新时先备份已安装的文件夹，再整体替换。

安装目录以当前 Codex 版本为准，优先让自带的安装器处理版本差异。参见[官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。仅下载 GitHub 文件，不会在普通 ChatGPT 聊天中自动安装 Skill。

macOS 可在 Finder 的“前往 → 前往文件夹”中输入目录；其他系统可使用文件管理器打开相应用户或项目目录。

## 开始使用

```text
用 $fare-tally 帮我查便宜的往返机票。日期可以前后调整两天，需要托运行李，最好白天出发。请先确认周边机场和中转条件，再开始查价。
```

不用一次提供全部信息。助手应分几轮问清相关需求、确认会影响查询的条件，再给出含票价、航班详情、优缺点和待查项的候选清单。

如果平台需要登录，助手应解释原因及正在使用哪个浏览器。请自行输入密码、验证码并完成验证，不要把凭据发到聊天中。查价不代表授权下单、锁票或付款。

## 查询限制与隐私

结果是“已查范围内已核实的低价”，不保证全市场最低。完成一个查询，也不代表查过所有航班或确认了旅客的全部要求。舱位、行李或过境条件缺少证据时，方案会标为附条件候选；会员价和优惠券价格另行注明。

请把真实行程、报价、截图和浏览器信息保存在仓库之外的私人目录，不要放进公开 Issue。附带示例使用虚构查询日期，没有真实机票报价。

## 可选的离线辅助工具

[覆盖检查工具](skills/fare-tally/references/coverage.md)用于展开已同意的机场／日期组合，并检查查询记录。它不联网、不抓取机票、不验证酒店入住安排。普通用户可以让助手管理，不必自己运行脚本；对话流程本身不强制要求 Python。

开发检查及打包方法见[验证说明](docs/validation.md)。

## 许可

[MIT](LICENSE)。
