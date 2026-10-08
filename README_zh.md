> 🌐 **[English](https://github.com/xinvxueyuan/xinvxueyuan#readme) | [中文](README_zh.md)**

# 你好，我是 新v学员 · Xin Xue Yuan

**AI Agent 工具作者** — 让模型真正干活：MCP 服务、Agent Skill、运行时插件。

```text
Agent  ·  MCP  ·  图像工具  ·  机器人生态  ·  Windows / Linux
```

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=xinvxueyuan&style=for-the-badge&color=4c8bf5&label=profile+views" alt="profile views"/>
  <a href="https://www.xinvstar.xyz"><img src="https://img.shields.io/badge/Blog-xinvstar.xyz-4c8bf5?style=for-the-badge&logo=safari&logoColor=white" alt="blog"/></a>
  <img src="https://img.shields.io/badge/Location-China-4c8bf5?style=for-the-badge&logo=github&logoColor=white" alt="location"/>
  <img src="https://img.shields.io/badge/OS-Windows%20%7C%20Debian-4c8bf5?style=for-the-badge&logo=windows&logoColor=white" alt="os"/>
</p>

> *资以乐其无涯之生*

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
<sub>MCP · Python · ★ 6</sub><br><br>
将 NovelAI 图像生成接入 AI Agent 的 MCP 服务 —— 11 个工具、双传输、文档与 Docker。
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
<sub>Cordis 插件 · TypeScript</sub><br><br>
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
<sub>NoneBot2 · OneBot 11 · Python</sub><br><br>
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
<sub>NoneBot2 · Python · ★ 3</sub><br><br>
插件化架构的 QQ 群管理机器人。
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
<a href="https://github.com/xinvxueyuan/lty-moe"><b>lty-moe</b></a><br>
<sub>Web · TypeScript · ★ 1</sub><br><br>
洛天依同人作品档案与社区投稿站点
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/orbital-marketplace"><b>orbital-marketplace</b></a><br>
<sub>SPA · React Router · JavaScript</sub><br><br>
Orbital — 应用商城 SPA（React Router v7 + FastAPI）：应用下载、许可证、更新、订阅、发卡机制与文档站。MIT OR Apache-2.0 双许可。
</td>
<td width="50%" valign="top">
<a href="https://github.com/xinvxueyuan/winux"><b>winux</b></a><br>
<sub>CLI · Rust</sub><br><br>
Rust 打造的 Windows 类 Linux CLI 工作流管理器。
</td>
</tr>
</table>
<!-- AUTO:CARDS:web-apps:END -->

## 技术栈

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,rust,typescript,go,java,c,cpp,react,vue,nextjs,svelte,spring,electron,mariadb,redis,postgres,mongodb,docker,kubernetes,gitlab" alt="tech stack" />
</p>

## 数据

<div align="center">

[![GitHub stats](https://github-readme-state.xinvstar.xyz/api?username=xinvxueyuan&show_icons=true&count_private=true&hide_border=true&bg_color=0D1117&title_color=4c8bf5&icon_color=4c8bf5&text_color=c9d1d9&ring_color=4c8bf5)](https://github.com/xinvxueyuan)
[![Top Langs](https://github-readme-state.xinvstar.xyz/api/top-langs/?username=xinvxueyuan&layout=compact&langs_count=6&hide_border=true&bg_color=0D1117&title_color=4c8bf5&text_color=c9d1d9)](https://github.com/xinvxueyuan)

</div>

## 最新文章

<!-- AUTO:POSTS:START -->
- [2026年开源安全威胁态势全景报告](https://www.xinvstar.xyz/posts/2026-07-07-%E5%BC%80%E6%BA%90%E5%AE%89%E5%85%A8%E5%A8%81%E8%83%81%E6%80%81%E5%8A%BF%E6%8A%A5%E5%91%8A/) — 2026-07-07
- [一封封号邮件里的 1×1 像素：Claude 邮件追踪器技术分析与争议](https://www.xinvstar.xyz/posts/2026-07-05-claude-%E5%B0%81%E7%A6%81%E9%82%AE%E4%BB%B6-%E8%BF%BD%E8%B8%AA%E5%83%8F%E7%B4%A0%E5%88%86%E6%9E%90/) — 2026-07-05
- [深度源码解析：Claude Code 隐藏的反向代理检测与隐写标记机制](https://www.xinvstar.xyz/posts/2026-07-04-claude-code-%E9%9A%90%E5%86%99%E6%A0%87%E8%AE%B0-%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90/) — 2026-07-04
- [Next.js 14 App Router 完全指南](https://www.xinvstar.xyz/posts/2026-03-29-nextjs-14-app-router%E5%AE%8C%E5%85%A8%E6%8C%87%E5%8D%97/) — 2026-03-29
- [CI/CD 实战：GitHub Actions 自动化工作流](https://www.xinvstar.xyz/posts/2026-03-22-cicd%E5%AE%9E%E6%88%98-github-actions/) — 2026-03-22
<!-- AUTO:POSTS:END -->

## 近况

<!-- AUTO:NOW:START -->
- 🚀 **[lingchu-bot](https://github.com/xinvxueyuan/lingchu-bot)** `v0.7.0` — 插件化架构的 QQ 群管理机器人。 · _50 分钟前_
- 🚀 **[nonebot-plugin-fanqie-verify](https://github.com/xinvxueyuan/nonebot-plugin-fanqie-verify)** `v0.4.0` — NoneBot2 番茄读书群入群验证插件：新成员发送本人书评详情页截图，视觉/OCR 识别通过后自动放行；支持延期审核、漏验补验、引用回复，异常自动转管理员决策 · _1 小时前_
- 🚀 **[cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret)** `v0.4.1` — Cordis / DeepSeek Harness plugin — the agent asks the human for a secret in an inline conversation card and only ever receives an opaque session-scoped DSH_SECRET_* name, never the value · _4 小时前_
<!-- AUTO:NOW:END -->

## 联系

- **博客** —— [xinvstar.xyz](https://www.xinvstar.xyz)
- **GitHub** —— [@xinvxueyuan](https://github.com/xinvxueyuan)
- **公司** —— xinvStar.Inc

---

<p align="center">
  <i>欢迎在 Agent 工具、MCP 与机器人方向交流合作 —— let's build 🌱</i>
</p>
