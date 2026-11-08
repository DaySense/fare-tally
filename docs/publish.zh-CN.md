# 把 Skill 发布到 GitHub：新手步骤

本教程发布代码和使用说明，不会把机票研究接到一个实时订票网站。你之前的私人 Ticket Helper 目录不是要上传的仓库；这里只上传独立的 **fare-tally 发布包内容**。

## 1. 准备干净文件夹

解压 `fare-tally-github-v0.1.2.zip`，打开里面的 fare-tally 文件夹。根目录应看到 README.md、README.zh-CN.md、LICENSE，以及 skills、docs、tests、tools 等文件夹。

不要把整个 ZIP 当成源码上传，GitHub 不会替你解压。也不要上传父目录中的机票报告、截图、账号信息、cookie、.env 或本地运行记录。

## 2. 核对安装链接里的用户名

本项目发布在 `DaySense/fare-tally`，README 中已填写真实地址。若你 Fork 后独立发布，再把 README.md 和 README.zh-CN.md 中 URL 的 `DaySense` 换成你的 GitHub 用户名。用户名可在 GitHub 头像菜单的个人资料网址中看到；它不是必须与显示昵称相同。

如果仓库采用其他名字，同时修改 URL 中的 `fare-tally` 仓库名；后面的 `skills/fare-tally` 是 Skill 所在文件夹，不随仓库改名自动改变。

请保留两个完整段落：**如何安装**以及**如何调用**。README.md 是默认展示的英文介绍，README.zh-CN.md 是通过顶部链接打开的中文介绍；不用把两种语言硬塞进同一长文。GitHub 会展示仓库根目录的 README，可用相对链接连接其他说明。[README 官方说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

## 3. 创建仓库

1. 登录 GitHub，打开 [New repository](https://github.com/new)。
2. Repository name 建议填 `fare-tally`。
3. Description 可填：`Bilingual flight-research skill: flexible dates, nearby airports, verified fares and real trip costs. 中英双语低价机票研究。`
4. 选择 **Public**，方便免费开源分享。
5. 因为文件包已包含 README、.gitignore 和 MIT LICENSE，这里不重复勾选生成它们。
6. 点击 **Create repository**。

这些是 GitHub 网页建库的标准步骤；界面按钮可能随版本调整。[创建仓库官方指南](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)

## 4. 上传源码

在空仓库的提示中点 **uploading an existing file**；已有文件的仓库可用 **Add file → Upload files**。

把发布文件夹**里面的文件和子文件夹**拖进去，而不是把 fare-tally 外层文件夹再套一层。预览中至少确认：

```text
README.md
README.zh-CN.md
LICENSE
skills/fare-tally/SKILL.md
skills/fare-tally/agents/openai.yaml
skills/fare-tally/references/...
skills/fare-tally/scripts/search_matrix.py
```

提交说明可写 `Add FareTally flight research skill`。按页面提示 Commit changes／Propose changes；若进入分支流程，创建并合并 PR。网页上传支持文件夹，应该保留目录结构。[上传文件官方指南](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

## 5. 检查别人能安装

在仓库中打开 `skills/fare-tally/SKILL.md`，确认链接路径存在。然后新开一个 Codex 对话，使用你 README 里的真实安装提示：

```text
$skill-installer 请从 https://github.com/DaySense/fare-tally/tree/main/skills/fare-tally 安装这个 Skill。
```

把用户名替换好；若默认分支不是 main，也应改成实际分支。安装后新一轮输入：

```text
用 $fare-tally 帮我查低价机票，请先问清日期、机场、行李和中转条件。
```

它应先澄清需求，而不是直接报未经核实的价格。如果找不到 Skill，检查是否多嵌套一层、是否漏传 references/scripts，及当前 Codex 的 Skill 目录；必要时重启。官方支持用 skill-installer 从其他仓库安装，本地目录说明见 [OpenAI Skill 指南](https://learn.chatgpt.com/docs/build-skills)。

## 6. 在 README 里修改／补充安装说明

打开仓库 README.md，点编辑按钮，在 `## Install` 下面保留可直接复制的 Codex 提示、手动复制目录方法和调用示例。用 **Preview** 看代码块和中文链接是否正确，再提交。中文文档在 README.zh-CN.md 的安装段落同步更新。不要只写“下载即可”，因为 Skill 文件夹放错位置就不会被发现。

只复制安装说明不会为使用者提供浏览器或携程登录。保留前置条件与登录说明，避免新手误以为这是自动订票接口。

## 7. 可选：添加下载版

仓库的 Download ZIP 已可下载源码。若另做 Release，可将 `fare-tally-skill-v0.1.2.zip` 作为安装包附件；这个压缩包内应是 `fare-tally/SKILL.md` 和完整资源。GitHub 源码包与单 Skill 安装包用途不同，文件名已区分。

名称仍属初筛候选。MIT 是代码许可，不表示授予第三方商标权。公开前核对[名称记录](name-check-2026-11-09.md)、许可与署名。这是可供后续复用的发布教程，不是部署记录；本项目的实际发布状态以 GitHub 仓库和 Releases 页面为准。网站未随仓库一起发布。
