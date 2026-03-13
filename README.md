# AlgoLand

**English** | [中文](./README.zh-CN.md)

> A playful terminal onboarding world for algorithm engineers.  
> Learn by playing: terminal, Git, Python envs, PDB, SSH, and LLM APIs.

---

## What is AlgoLand?

AlgoLand is an open-source terminal game for algorithm engineers and research interns.
Instead of reading a long tutorial first, you **enter the world, read the lesson in the top pane, and patch or complete real tasks in the bottom pane**.

It is built for people who:
- are new to terminal workflows
- prefer hands-on onboarding over passive docs
- learn better by debugging and modifying existing code
- want a faster path into real engineering basics

## Why it is different
- **Playable** — every step is an interactive task
- **Terminal-first** — learn in the real environment, not screenshots
- **Beginner-friendly** — lessons explain concepts without dumping the full answer
- **Patch-oriented** — you mostly modify existing code instead of writing everything from scratch
- **Fast feedback** — the game checks your progress as you go
- **Built for algorithm engineers** — later stages focus on debugging, data scripts, SSH, and LLM APIs

## What you learn
1. **L0 — Vim + terminal basics**
2. **L1 — Terminal + Git**
3. **L2 — Python environments**
4. **L3 — Debugging with PDB**
5. **L4 — SSH basics**
6. **L5 — LLM API basics**

## Quick start
```bash
cd onboarding-game
./start
```

If executable permissions are missing:
```bash
cd onboarding-game
bash start
```

On startup, AlgoLand will ask you:
- language (`中文` / `English`)
- whether to **Resume** or start a **New game**

You can also force progress mode:
```bash
./start --resume
./start --fresh
```

## Controls
**Lesson pane**
- `j / k` — scroll
- `PgUp / PgDn` — page up/down
- `{ / }` — jump between sections
- `g / G` — top/bottom

**tmux pane switching**
- `Ctrl-b` then `↑` — focus lesson pane
- `Ctrl-b` then `↓` — focus shell pane

**Game commands**
```bash
./quest submit
./quest status
./quest goto L3 1
./quest reset
```

## Requirements
- `podman`
- `tmux`
- `git` (recommended)

macOS example:
```bash
brew install podman tmux git
```

## Image placeholder

> Add a split-terminal screenshot or GIF here.

Recommended assets:
- startup screen
- top lesson pane + bottom shell pane
- a learner fixing code and submitting a step

## Suggested GitHub description

**A playful terminal onboarding world for algorithm engineers. Learn by patching, debugging, and playing.**

## Suggested GitHub topics

`terminal` `onboarding` `education` `algorithms` `cli` `tmux` `git` `debugging` `ssh` `llm` `api` `learn-by-doing` `game-based-learning`
