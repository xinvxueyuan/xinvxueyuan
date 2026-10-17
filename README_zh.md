> 🌐 **[English](https://github.com/xinvxueyuan/xinvxueyuan#readme) | [中文](README_zh.md)**

# 你好，我是 新v学员 · Xin Xue Yuan

**AI Agent 工具作者** — 让模型真正干活：MCP 服务、Agent Skill、运行时插件。

```text
Agent  ·  MCP  ·  图像工具  ·  机器人生态  ·  Windows / Linux
```

<p align="center">
  <a href="https://github.com/xinvxueyuan"><img src="https://img.shields.io/badge/GitHub-xinvxueyuan-4c8bf5?style=for-the-badge&logo=github&logoColor=white" alt="GitHub: xinvxueyuan"/></a>
  <a href="https://www.xinvstar.xyz"><img src="https://img.shields.io/badge/Blog-xinvstar.xyz-4c8bf5?style=for-the-badge&logo=safari&logoColor=white" alt="blog"/></a>
  <img src="https://img.shields.io/badge/Location-China-4c8bf5?style=for-the-badge&logo=github&logoColor=white" alt="location"/>
  <img src="https://img.shields.io/badge/OS-Windows%20%7C%20Debian-4c8bf5?style=for-the-badge&logo=windows&logoColor=white" alt="os"/>
</p>

<!-- AUTO:BIO:START -->
> *“你好，亲爱的同胞。你今天过得怎么样？我嘛，目前没有进行交配仪式的兴趣。我的睡眠循环很快就要到了，所以我很快就会失去意识。要进行交配的话，就等以后再说吧。”*
<!-- AUTO:BIO:END -->

---

<!-- 下方 AUTO 标记区由 scripts/generate_profile.py 每日自动重写：卡片类型标签取自仓库
     topics，语言与星数取自 GitHub API，描述取自 profile.config.json 里的分语言映射。
     标记区以外的文案均为手写，脚本不会改动。 -->

## Agent 工具链

把 AI Agent 接到真实系统上 —— 图像生成、GitHub API、安全执行。

<!-- AUTO:CARDS:agent-tooling:START -->
<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/NovelAI-Image-MCP"><b>NovelAI-Image-MCP</b></a><br>
<sub>MCP · Python · ★ 11 · v0.5.1</sub><br><br>
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
<sub>Cordis 插件 · TypeScript · v0.2.0</sub><br><br>
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
<sub>NoneBot2 · Python · ★ 3 · v0.8.0</sub><br><br>
基于 NoneBot2 的插件化 QQ 群管理机器人，涵盖群管理、命令处理、配置、存储与异步数据访问。
</td>
<td width="50%"></td>
</tr>
</table>
<!-- AUTO:CARDS:bot-ecosystem:END -->

## Web 与应用

<!-- AUTO:CARDS:web-apps:START -->
<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/xinvxueyuan.github.io"><b>xinvxueyuan.github.io</b></a><br>
<sub>博客 · TypeScript</sub><br><br>
个人博客
</td>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/winux"><b>winux</b></a><br>
<sub>CLI · Rust</sub><br><br>
Rust 打造的 Windows 类 Linux CLI 工作流管理器。
</td>
</tr>
</table>
<!-- AUTO:CARDS:web-apps:END -->

## 更多公开项目

<!-- AUTO:CATALOG:START -->
- [cordis-plugin-local-dream](https://github.com/xinvxueyuan/cordis-plugin-local-dream) — Cordis / DeepSeek Harness plugin — drive the Android Local Dream Stable Diffusion app over its HTTP backend (LAN-first, USB/adb fallback) with automatic device connection management
- [cordis-plugin-loop](https://github.com/xinvxueyuan/cordis-plugin-loop) — DSH /loop: run a task now, then keep running it on a fixed cadence or a self-paced one
- [cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) — Cordis / DeepSeek Harness plugin — the agent asks the human for a secret in an inline conversation card and only ever receives an opaque session-scoped DSH\_SECRET\_\* name, never the value
- [docs](https://github.com/xinvxueyuan/docs)
- [github-readme-stats](https://github.com/xinvxueyuan/github-readme-stats)
- [nonebot-plugin-auto-unmute-superuser](https://github.com/xinvxueyuan/nonebot-plugin-auto-unmute-superuser) — NoneBot2 插件（qbot 子模块）· 超级用户被群禁言时自动解禁（事件驱动 + 周期轮询兜底）
- [nonebot-plugin-ciyuan-image](https://github.com/xinvxueyuan/nonebot-plugin-ciyuan-image) — NoneBot2 插件（qbot 子模块）· 栗次元（t.alcy.cc）随机图片，18 个分类，超过 3 张自动合并转发
- [nonebot-plugin-info](https://github.com/xinvxueyuan/nonebot-plugin-info) — NoneBot2 插件（qbot 子模块）· 功能菜单：扫描全部已加载插件的 \_\_plugin\_meta\_\_.extra，按分类出菜单图与详情（htmlkit 出图，失败回退纯文本）
- [nonebot-plugin-lingchu-bot](https://github.com/xinvxueyuan/nonebot-plugin-lingchu-bot)
- [nonebot-plugin-lottery](https://github.com/xinvxueyuan/nonebot-plugin-lottery) — NoneBot2 插件（qbot 子模块）· 抽奖（禁言小助手）：群里命中匹配词的人会被随机禁言，超阈值的定时自动解禁
- [nonebot-plugin-merge-forward](https://github.com/xinvxueyuan/nonebot-plugin-merge-forward) — NoneBot2 插件（qbot 子模块）· 合并群消息转发工具库（抽取自 zhenxun\_bot），提供 OneBot V11 合并转发 node 构造与发送 API，供其他插件 import 调用
- [nonebot-plugin-message-reaction](https://github.com/xinvxueyuan/nonebot-plugin-message-reaction) — NoneBot2 插件（qbot 子模块）· 消息表态（emoji reaction）工具库：三态表态 message\_reaction 与 with\_reaction 装饰器，供其他插件 import 调用
- [nonebot-plugin-pixiv-illust](https://github.com/xinvxueyuan/nonebot-plugin-pixiv-illust) — NoneBot2 插件（qbot 子模块）· pixiv 插画/漫画订阅推送：按群订阅画师新作、多页推送（\>3 页合并转发）、R18 可打码
- [nonebot-plugin-pixiv-novel](https://github.com/xinvxueyuan/nonebot-plugin-pixiv-novel) — NoneBot2 插件（qbot 子模块）· pixiv 小说订阅推送：按群订阅作者新作自动推送 + 拉取单篇全文
- [nonebot-plugin-waifu](https://github.com/xinvxueyuan/nonebot-plugin-waifu) — NoneBot2 插件（qbot 子模块）· 从群内活跃成员里抽一位当「今日老婆」，支持换一只/确认/娶老婆/离婚/超管指婚
- [picx-images-hosting](https://github.com/xinvxueyuan/picx-images-hosting) — PicX images hosting repository
- [proxy-rules](https://github.com/xinvxueyuan/proxy-rules) — 自用分流规则：一份自持数据编译成 Clash(mihomo) rule-provider 与 Xray geosite/geoip dat，CI 定时构建+真内核校验
<!-- AUTO:CATALOG:END -->

## 技术栈

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,rust,typescript,go,java,c,cpp,react,vue,nextjs,svelte,spring,electron,mariadb,redis,postgres,mongodb,docker,kubernetes,gitlab" alt="tech stack" />
</p>

## 数据

<!-- AUTO:STATS:START -->
- 公开仓库: **56**
- 非 Fork 仓库: **27**
- 获星数（非 Fork）: **14**
- 被 Fork 数（非 Fork）: **3**
- 关注者: **7**
- 按非 Fork 仓库数量统计的主要语言：Python (16), TypeScript (5), JavaScript (2), MDX (1), Rust (1)
_来源：GitHub 公开 API，不含私有数据；语言按仓库计数，不代表代码字节占比。_
<!-- AUTO:STATS:END -->

<div align="center">

[![GitHub stats](https://github-readme-state.xinvstar.xyz/api?username=xinvxueyuan&show_icons=true&count_private=true&hide_border=true&bg_color=0D1117&title_color=4c8bf5&icon_color=4c8bf5&text_color=c9d1d9&ring_color=4c8bf5)](https://github.com/xinvxueyuan)
[![Top Langs](https://github-readme-state.xinvstar.xyz/api/top-langs/?username=xinvxueyuan&layout=compact&langs_count=6&hide_border=true&bg_color=0D1117&title_color=4c8bf5&text_color=c9d1d9)](https://github.com/xinvxueyuan)

</div>

## 最新文章

<!-- AUTO:POSTS:START -->
- [一步步用 Google AI Studio 做出并部署自己的 Android 应用](https://www.xinvstar.xyz/posts/2026-10-17-google-ai-studio-personal-android-apps/) — 2026-10-17
- [2026年开源安全威胁态势全景报告](https://www.xinvstar.xyz/posts/2026-07-07-%E5%BC%80%E6%BA%90%E5%AE%89%E5%85%A8%E5%A8%81%E8%83%81%E6%80%81%E5%8A%BF%E6%8A%A5%E5%91%8A/) — 2026-07-07
- [一封封号邮件里的 1×1 像素：Claude 邮件追踪器技术分析与争议](https://www.xinvstar.xyz/posts/2026-07-05-claude-%E5%B0%81%E7%A6%81%E9%82%AE%E4%BB%B6-%E8%BF%BD%E8%B8%AA%E5%83%8F%E7%B4%A0%E5%88%86%E6%9E%90/) — 2026-07-05
- [深度源码解析：Claude Code 隐藏的反向代理检测与隐写标记机制](https://www.xinvstar.xyz/posts/2026-07-04-claude-code-%E9%9A%90%E5%86%99%E6%A0%87%E8%AE%B0-%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90/) — 2026-07-04
- [Next.js 14 App Router 完全指南](https://www.xinvstar.xyz/posts/2026-03-29-nextjs-14-app-router%E5%AE%8C%E5%85%A8%E6%8C%87%E5%8D%97/) — 2026-03-29
<!-- AUTO:POSTS:END -->

## 近况

<!-- AUTO:NOW:START -->
- **[NovelAI-Image-MCP](https://github.com/xinvxueyuan/NovelAI-Image-MCP)** · v0.5.1 — 将 NovelAI 图像生成接入 AI Agent 的 MCP 服务。 · 推送于 2026-10-17 18:31:47 UTC
- **[nonebot-plugin-fanqie-verify](https://github.com/xinvxueyuan/nonebot-plugin-fanqie-verify)** · v0.4.0 — NoneBot2 番茄读书群入群验证插件：新成员发送本人书评详情页截图，视觉/OCR 识别通过后自动放行；支持延期审核、漏验补验、引用回复，异常自动转管理员决策 · 推送于 2026-10-17 18:02:16 UTC
- **[xinvxueyuan.github.io](https://github.com/xinvxueyuan/xinvxueyuan.github.io)** — 个人博客 · 推送于 2026-10-17 17:33:31 UTC
<!-- AUTO:NOW:END -->

## 最近维护

<!-- AUTO:MAINTENANCE:START -->
配置仓库最近更新的 100 条已关闭 PR 中，最近合并的记录：

- [lingchu-bot #79](https://github.com/xinvxueyuan/lingchu-bot/pull/79) — ⬆️ build(deps): Bump typescript in webui from 5.9.3 to 6.0.3 · 2026-10-12
- [lingchu-bot #88](https://github.com/xinvxueyuan/lingchu-bot/pull/88) — ⬆️ build(deps): Bump npm minor packages · 2026-10-12
- [lingchu-bot #92](https://github.com/xinvxueyuan/lingchu-bot/pull/92) — ⬆️ build(deps): Bump Mako and multidict · 2026-10-12
<!-- AUTO:MAINTENANCE:END -->

## 联系

- **博客** —— [xinvstar.xyz](https://www.xinvstar.xyz)
- **GitHub** —— [@xinvxueyuan](https://github.com/xinvxueyuan)
- **公司** —— xinvStar.Inc

---

<p align="center">
  <i>欢迎在 Agent 工具、MCP 与机器人方向交流合作 —— let's build 🌱</i>
</p>
