# AlgoLand

[English](./README.md) | **中文**

> 一个给算法同学边玩边学的终端入门世界：在真实终端里学习 terminal、Git、Python 环境、PDB、SSH 和 LLM API。

---

## AlgoLand 是什么？

AlgoLand 是一个面向算法工程师和研究实习生的开源终端闯关项目。
它不是让你先啃一大堆文档，而是让你：
**直接进入一个可玩的终端世界，在上半屏看讲义，在下半屏修改代码、执行命令、一步步过关。**

它适合这样的人：
- 刚开始接触终端工作流
- 不喜欢被动看文档，更喜欢边做边学
- 更擅长通过 debug、patch 现有代码来理解系统
- 想更快进入真实工程基础能力

## 它和普通 onboarding 的区别
- **可玩**：每一步都是一个真实的小任务
- **终端优先**：直接在真实环境里学习，不靠截图
- **对新手友好**：讲原理，但不直接把答案喂给你
- **以 patch 为主**：大部分时候是在修改已有代码，而不是从零开始写
- **反馈快**：每一步都可以即时验收
- **贴近算法同学**：后面的关卡会覆盖排障、数据脚本、SSH 和 LLM API

## 你会学到什么
1. **L0 — Vim + 终端基础**
2. **L1 — Terminal + Git**
3. **L2 — Python 环境**
4. **L3 — PDB 排障**
5. **L4 — SSH 基础**
6. **L5 — LLM API 基础**

## 快速开始
```bash
cd onboarding-game
./start
```

如果没有保留可执行权限：
```bash
cd onboarding-game
bash start
```

启动后系统会先询问：
- 语言（中文 / English）
- 是否 `Resume` 继续上次进度
- 或 `New game` 从头开始

也可以显式指定：
```bash
./start --resume
./start --fresh
```

## 操作方式
**讲义区**
- `j / k`：上下滚动
- `PgUp / PgDn`：翻页
- `{ / }`：按段跳转
- `g / G`：跳到头尾

**tmux pane 切换**
- `Ctrl-b` 然后 `↑`：切到上半屏
- `Ctrl-b` 然后 `↓`：切回下半屏

**常用命令**
```bash
./quest submit
./quest status
./quest goto L3 1
./quest reset
```

## 依赖
- `podman`
- `tmux`
- `git`（推荐）

macOS 示例：
```bash
brew install podman tmux git
```

## 截图预留位

> 建议在这里放一张上下分屏截图，或者一段 5~10 秒的 GIF。

推荐素材：
- 启动画面
- 上半屏讲义 + 下半屏 shell
- 正在修代码并提交过关的过程
