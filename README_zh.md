> 🌐 **[English](https://github.com/xinvxueyuan/xinvxueyuan#readme) | [中文](README_zh.md)**

# 你好，我是 新v学员 · Xin Xue Yuan

**Agent 工具链、机器人，以及一个自建博客。**

<p align="center">
  <a href="https://github.com/xinvxueyuan"><img src="https://img.shields.io/badge/GitHub-xinvxueyuan-4c8bf5?style=for-the-badge&logo=github&logoColor=white" alt="GitHub: xinvxueyuan"/></a>
  <!-- AUTO:BLOG_BADGE:START -->
<a href="https://blog.hikarilink.org"><img src="https://img.shields.io/badge/Blog-blog.hikarilink.org-4c8bf5?style=for-the-badge&logo=safari&logoColor=white" alt="blog"/></a>
<!-- AUTO:BLOG_BADGE:END -->
  <img src="https://img.shields.io/badge/Location-China-4c8bf5?style=for-the-badge&logo=github&logoColor=white" alt="location"/>
  <img src="https://img.shields.io/badge/OS-Windows%20%7C%20Debian-4c8bf5?style=for-the-badge&logo=windows&logoColor=white" alt="os"/>
</p>

我是新v学员，一名开发者，在做让 AI Agent 真正接上外部服务的小工具，也把过程写在博客上。

- **MCP 服务** — NovelAI-Image-MCP 让 MCP 客户端可以调用 NovelAI 图像生成。
- **Agent Skill** — github-api-skill 与 json-safe-skill：把 GitHub API 参考和 JSON 校验规则交给 Agent。
- **Cordis 插件**（DeepSeek Harness）— GitHub 工具、Local Dream 图像后端、`/loop` 与密钥处理。
- **NoneBot2 / OneBot 11 插件** — 入群验证、状态告警、群管理，跑在真实的 QQ 群里。
- **自建博客** — 记录同一批工作的技术笔记与长文。

---

<!-- 下方 AUTO 标记区由 scripts/generate_profile.py 每日自动重写：卡片类型标签取自仓库
     topics，语言与星数取自 GitHub API，描述取自 profile.config.json 里的分语言映射；
     博客与统计图链接同样由该文件中的站点地址渲染，换域名只改配置。
     标记区以外的文案均为手写，脚本不会改动。 -->

## Agent 工具链

把 AI Agent 接到真实系统上 —— 图像生成、GitHub API、安全执行。

<!-- AUTO:CARDS:agent-tooling:START -->
<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/NovelAI-Image-MCP"><b>NovelAI-Image-MCP</b></a><br>
<sub>MCP · Python · ★ 12 · v0.7.0</sub><br><br>
将 NovelAI 图像生成接入 AI Agent 的 MCP 服务。
</td>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/github-api-skill"><b>github-api-skill</b></a><br>
<sub>Agent Skill · JavaScript</sub><br><br>
权威 GitHub API 参考（REST + GraphQL + 安全规则），别再猜端点。
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/cordis-plugin-github"><b>cordis-plugin-github</b></a><br>
<sub>Cordis 插件 · TypeScript · v0.3.0 · 已归档</sub><br><br>
为 Cordis / DeepSeek Harness 提供规范化 GitHub 工具 —— 默认走 gh CLI，自动 HTTP 回退。
</td>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/json-safe-skill"><b>json-safe-skill</b></a><br>
<sub>Agent Skill</sub><br><br>
面向 Node REPL / run_code / JSON-RPC 的安全手写 JSON 技能 —— 发送前先校验。
</td>
</tr>
</table>
<!-- AUTO:CARDS:agent-tooling:END -->

## 机器人生态

每天跑在生产 QQ 群里的 NoneBot2 / OneBot 插件。

<!-- AUTO:CARDS:bot-ecosystem:START -->
<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/nonebot-plugin-fanqie-verify"><b>nonebot-plugin-fanqie-verify</b></a><br>
<sub>NoneBot2 · OneBot 11 · Python · v0.4.0</sub><br><br>
NoneBot2 番茄读书群入群验证插件：新成员发送本人书评详情页截图，视觉/OCR 识别通过后自动放行；支持延期审核、漏验补验、引用回复，异常自动转管理员决策
</td>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/nonebot-plugin-llbot-alert"><b>nonebot-plugin-llbot-alert</b></a><br>
<sub>NoneBot2 · OneBot 11 · Python</sub><br><br>
LLBot 状态告警插件：从 OneBot 心跳抽取账号状态检测账号异常，并在连接断开/心跳静默时检测服务异常，通过 SMTP 发送告警与恢复邮件
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/lingchu-bot"><b>lingchu-bot</b></a><br>
<sub>NoneBot2 · Python · ★ 3 · v0.10.0.dev1</sub><br><br>
基于 NoneBot2 的插件化 QQ 群管理机器人，涵盖群管理、命令处理、配置、存储与异步数据访问。
</td>
<td width="50%"></td>
</tr>
</table>
<!-- AUTO:CARDS:bot-ecosystem:END -->

## 命令行工具

<!-- AUTO:CARDS:cli-tools:START -->
<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/winux"><b>winux</b></a><br>
<sub>CLI · Rust</sub><br><br>
Rust 打造的 Windows 类 Linux CLI 工作流管理器。
</td>
<td width="50%"></td>
</tr>
</table>
<!-- AUTO:CARDS:cli-tools:END -->

## 更多公开项目

<!-- AUTO:CATALOG:START -->
- [cordis-plugin-local-dream](https://github.com/xinvxueyuan/cordis-plugin-local-dream) — Cordis / DeepSeek Harness plugin — drive the Android Local Dream Stable Diffusion app over its HTTP backend (LAN-first, USB/adb fallback) with automatic device connection management
- [cordis-plugin-loop](https://github.com/xinvxueyuan/cordis-plugin-loop) — DSH /loop: run a task now, then keep running it on a fixed cadence or a self-paced one
- [cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) — Cordis / DeepSeek Harness plugin — the agent asks the human for a secret in an inline conversation card and only ever receives an opaque session-scoped DSH\_SECRET\_\* name, never the value
- [docs](https://github.com/xinvxueyuan/docs)
- [github-readme-stats](https://github.com/xinvxueyuan/github-readme-stats)
- [hataraku](https://github.com/xinvxueyuan/hataraku)
- [nonebot-plugin-auto-unmute-superuser](https://github.com/xinvxueyuan/nonebot-plugin-auto-unmute-superuser) — NoneBot2 插件（qbot 子模块）· 超级用户被群禁言时自动解禁（事件驱动 + 周期轮询兜底）
- [nonebot-plugin-checkin](https://github.com/xinvxueyuan/nonebot-plugin-checkin) — 群签到：每日签到攒积分，连续签到有加成，群内积分排行（htmlrender 出图，失败回退纯文本）
- [nonebot-plugin-ciyuan-image](https://github.com/xinvxueyuan/nonebot-plugin-ciyuan-image) — NoneBot2 插件（qbot 子模块）· 栗次元（t.alcy.cc）随机图片，18 个分类，超过 3 张自动合并转发
- [nonebot-plugin-info](https://github.com/xinvxueyuan/nonebot-plugin-info) — NoneBot2 插件（qbot 子模块）· 功能菜单：扫描全部已加载插件的 \_\_plugin\_meta\_\_.extra，按分类出菜单图与详情（htmlkit 出图，失败回退纯文本）
- [nonebot-plugin-lottery](https://github.com/xinvxueyuan/nonebot-plugin-lottery) — NoneBot2 插件（qbot 子模块）· 抽奖（禁言小助手）：群里命中匹配词的人会被随机禁言，超阈值的定时自动解禁
- [nonebot-plugin-merge-forward](https://github.com/xinvxueyuan/nonebot-plugin-merge-forward) — NoneBot2 插件（qbot 子模块）· 合并群消息转发工具库（抽取自 zhenxun\_bot），提供 OneBot V11 合并转发 node 构造与发送 API，供其他插件 import 调用
- [nonebot-plugin-message-reaction](https://github.com/xinvxueyuan/nonebot-plugin-message-reaction) — NoneBot2 插件（qbot 子模块）· 消息表态（emoji reaction）工具库：三态表态 message\_reaction 与 with\_reaction 装饰器，供其他插件 import 调用
- [nonebot-plugin-pixiv-illust](https://github.com/xinvxueyuan/nonebot-plugin-pixiv-illust) — NoneBot2 插件（qbot 子模块）· pixiv 插画/漫画订阅推送：按群订阅画师新作、多页推送（\>3 页合并转发）、R18 可打码
- [nonebot-plugin-pixiv-novel](https://github.com/xinvxueyuan/nonebot-plugin-pixiv-novel) — NoneBot2 插件（qbot 子模块）· pixiv 小说订阅推送：按群订阅作者新作自动推送 + 拉取单篇全文
- [nonebot-plugin-waifu](https://github.com/xinvxueyuan/nonebot-plugin-waifu) — NoneBot2 插件（qbot 子模块）· 从群内活跃成员里抽一位当「今日老婆」，支持换一只/确认/娶老婆/离婚/超管指婚
- [picx-images-hosting](https://github.com/xinvxueyuan/picx-images-hosting) — PicX images hosting repository
- [proxy-rules](https://github.com/xinvxueyuan/proxy-rules) — 自用分流规则：一份自持数据编译成 Clash(mihomo) rule-provider 与 Xray geosite/geoip dat，CI 定时构建+真内核校验
- [qbot](https://github.com/xinvxueyuan/qbot) — QBot —— 原生 NoneBot2 宿主（12 个插件以 git 子模块管理）
<!-- AUTO:CATALOG:END -->

## 技术栈

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,rust,typescript,go,java,c,cpp,react,vue,nextjs,svelte,spring,electron,mariadb,redis,postgres,mongodb,docker,kubernetes,gitlab" alt="tech stack" />
</p>

## 数据

<!-- AUTO:STATS:START -->
- 公开仓库: **59**
- 非 Fork 仓库: **28**
- 获星数（非 Fork）: **15**
- 被 Fork 数（非 Fork）: **3**
- 关注者: **7**
- 按非 Fork 仓库数量统计的主要语言：Python (17), TypeScript (5), JavaScript (2), MDX (1), Rust (1)
_来源：GitHub 公开 API，不含私有数据；语言按仓库计数，不代表代码字节占比。_
<!-- AUTO:STATS:END -->

<div align="center">

<!-- AUTO:STATS_IMAGES:START -->
[![GitHub stats](https://readme-stats.hikarilink.org/api?username=xinvxueyuan&show_icons=true&count_private=true&hide_border=true&bg_color=0D1117&title_color=4c8bf5&icon_color=4c8bf5&text_color=c9d1d9&ring_color=4c8bf5)](https://github.com/xinvxueyuan)
[![Top Langs](https://readme-stats.hikarilink.org/api/top-langs/?username=xinvxueyuan&layout=compact&langs_count=6&hide_border=true&bg_color=0D1117&title_color=4c8bf5&icon_color=4c8bf5&text_color=c9d1d9&ring_color=4c8bf5)](https://github.com/xinvxueyuan)
<!-- AUTO:STATS_IMAGES:END -->

</div>

## 最新文章

<!-- AUTO:POSTS:START -->
- [Windows 上纯 Agent Vibe Coding：先把 Git 的 autocrlf 设为 input](https://blog.hikarilink.org/blog/40) — 2026-10-23
- [一步步用 Google AI Studio 做出并部署自己的 Android 应用](https://blog.hikarilink.org/blog/39) — 2026-10-17
- [2026年开源安全威胁态势全景报告](https://blog.hikarilink.org/blog/38) — 2026-07-07
- [一封封号邮件里的 1×1 像素：Claude 邮件追踪器技术分析与争议](https://blog.hikarilink.org/blog/37) — 2026-07-05
- [深度源码解析：Claude Code 隐藏的反向代理检测与隐写标记机制](https://blog.hikarilink.org/blog/36) — 2026-07-04
<!-- AUTO:POSTS:END -->

## 近况

<!-- AUTO:NOW:START -->
- **[proxy-rules](https://github.com/xinvxueyuan/proxy-rules)** — 自用分流规则：一份自持数据编译成 Clash(mihomo) rule-provider 与 Xray geosite/geoip dat，CI 定时构建+真内核校验 · 推送于 2026-10-29 23:07:47 UTC
- **[lingchu-bot](https://github.com/xinvxueyuan/lingchu-bot)** · v0.10.0.dev1 — 基于 NoneBot2 的插件化 QQ 群管理机器人，涵盖群管理、命令处理、配置、存储与异步数据访问。 · 推送于 2026-10-29 22:34:04 UTC
- **[nonebot-plugin-message-reaction](https://github.com/xinvxueyuan/nonebot-plugin-message-reaction)** — NoneBot2 插件（qbot 子模块）· 消息表态（emoji reaction）工具库：三态表态 message\_reaction 与 with\_reaction 装饰器，供其他插件 import 调用 · 推送于 2026-10-29 06:17:37 UTC
<!-- AUTO:NOW:END -->

## 最近维护

<!-- AUTO:MAINTENANCE:START -->
配置仓库最近更新的 100 条已关闭 PR 中，最近合并的记录：

- [lingchu-bot #102](https://github.com/xinvxueyuan/lingchu-bot/pull/102) — chore(deps): bump certifi in uv.lock to 2026.10.19 for GHSA-6q48-6c7w-9gw2 · 2026-10-27
- [lingchu-bot #101](https://github.com/xinvxueyuan/lingchu-bot/pull/101) — ⬆️ build(deps): Bump vitest from 4.1.12 to 5.0.5 · 2026-10-27
- [lingchu-bot #100](https://github.com/xinvxueyuan/lingchu-bot/pull/100) — ⬆️ build(deps): Bump the npm-minor group with 18 updates · 2026-10-27
<!-- AUTO:MAINTENANCE:END -->

## 联系

<!-- AUTO:BLOG:START -->
- **博客** —— [blog.hikarilink.org](https://blog.hikarilink.org) · [RSS](https://blog.hikarilink.org/rss.xml)
<!-- AUTO:BLOG:END -->
- **GitHub** —— [@xinvxueyuan](https://github.com/xinvxueyuan)
- **公司** —— xinvStar.Inc

---

<p align="center">
  <i>欢迎在 Agent 工具、MCP 与机器人方向交流合作 —— let's build 🌱</i>
</p>
