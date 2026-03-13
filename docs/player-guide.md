# Player Guide

[中文](../README.zh-CN.md) | **English**

## Start
- Run directly: `./start`
- If progress exists, AlgoLand will ask:
  - `Resume` your previous progress
  - `New game` from the beginning

You can also force a mode:
- `./start --resume`
- `./start --fresh`

Language:
- launch and choose interactively on startup
- or preset with `ALGOLAND_LANG=en ./start`
- or preset with `ALGOLAND_LANG=zh ./start`

## Core loop
1. read the lesson in the top pane
2. work in the bottom shell pane
3. run `./quest submit`
4. get feedback and move to the next step
5. use `./quest status` for overall progress

## Lesson pane
- `j / k` — scroll
- `PgUp / PgDn` — page up/down
- `{ / }` — jump between sections
- `g / G` — top/bottom

## Pane switching
- focus lesson pane: `Ctrl-b` then `↑`
- focus shell pane: `Ctrl-b` then `↓`

## Debug and jump
- `./quest goto L3 1`
- `./quest goto L5 2`
- `./quest reset`
