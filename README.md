<div align="center">

# AlgoLand

**English** · [中文](./README.zh-CN.md)

<p>
  <strong>A playful terminal onboarding world for algorithm engineers.</strong><br/>
  Learn by playing: terminal, Git, Python envs, PDB, SSH, and LLM APIs.
</p>

<p>
  <a href="#quick-start">Quick Start</a> ·
  <a href="#what-you-learn">Curriculum</a> ·
  <a href="#image--preview">Preview</a> ·
  <a href="./README.zh-CN.md">中文介绍</a>
</p>

<p>
  <img alt="stage count" src="https://img.shields.io/badge/stages-6-7C3AED?style=for-the-badge" />
  <img alt="ui" src="https://img.shields.io/badge/interface-tmux%20split%20ui-06B6D4?style=for-the-badge" />
  <img alt="learning mode" src="https://img.shields.io/badge/learning-patch%20%2B%20debug%20%2B%20play-10B981?style=for-the-badge" />
</p>

</div>

---

## What is AlgoLand?

AlgoLand is an open-source terminal game for algorithm engineers and research interns.
Instead of reading a long tutorial first, you **enter the world, read the lesson in the top pane, and patch or complete real tasks in the bottom pane**.

It is built for people who:
- are new to terminal workflows
- prefer hands-on onboarding over passive docs
- learn better by debugging and modifying existing code
- want a faster path into real engineering basics

## Why it feels different

| Traditional onboarding | AlgoLand |
|---|---|
| Read first | Play first |
| Static docs | Split terminal UI |
| Toy demos | Real patch/debug tasks |
| Delayed feedback | Immediate step validation |

## What you learn

1. **L0 — Vim + terminal basics**
2. **L1 — Terminal + Git**
3. **L2 — Python environments**
4. **L3 — Debugging with PDB**
5. **L4 — SSH basics**
6. **L5 — LLM API basics**

## Image / Preview

> Replace the placeholder below with your screenshot or GIF.  
> Suggested path: `assets/algoland.png`

<p align="center">
  <img src="./assets/algoland.png" alt="AlgoLand split terminal preview" width="100%" />
</p>

Recommended preview ideas:
- the startup screen
- top lesson pane + bottom shell pane
- a learner fixing code and submitting a step

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

## Design philosophy

AlgoLand teaches the way many engineers actually learn:
- understand a task
- patch something real
- run it
- observe the result
- level up step by step

So the lessons try to:
- explain the core principle
- avoid giving away the full answer
- reduce fear for beginners
- let learners succeed through guided patching and debugging

## Suggested GitHub description

**A playful terminal onboarding world for algorithm engineers. Learn by patching, debugging, and playing.**

## Suggested GitHub topics

`terminal` `onboarding` `education` `algorithms` `cli` `tmux` `git` `debugging` `ssh` `llm` `api` `learn-by-doing` `game-based-learning`
