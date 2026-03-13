#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SESSION="terminal-quest"

if ! command -v tmux >/dev/null 2>&1; then
  echo "❌ 需要 tmux 才能运行真实上下分屏 TUI"
  echo "macOS 可安装：brew install tmux"
  exit 1
fi

"$ROOT/scripts/quest" sync >/dev/null 2>&1 || true

tmux kill-session -t "$SESSION" 2>/dev/null || true

tmux new-session -d -s "$SESSION" -c "$ROOT"
tmux send-keys -t "$SESSION" "python3 scripts/lesson_viewer.py" Enter
tmux split-window -v -t "$SESSION" -c "$ROOT"
tmux select-pane -t "$SESSION" -U
rows=$(tmux display-message -p -t "$SESSION" '#{window_height}' 2>/dev/null || echo 40)
upper=$(( rows / 2 ))
if [[ $upper -lt 16 ]]; then upper=16; fi
tmux resize-pane -t "$SESSION" -y "$upper" 2>/dev/null || true
tmux select-pane -t "$SESSION" -D

tmux send-keys -t "$SESSION" "clear" Enter
tmux send-keys -t "$SESSION" "printf '\n🎯 欢迎来到真实终端操作区\n\n'" Enter
tmux send-keys -t "$SESSION" "printf '上半屏是常驻讲义；下半屏是真实操作区。\n'" Enter
tmux send-keys -t "$SESSION" "printf '切到上半屏：Ctrl-b 然后 ↑\n切回下半屏：Ctrl-b 然后 ↓\n\n'" Enter
tmux send-keys -t "$SESSION" "printf '提交当前步骤：./quest submit\n查看整体进度：./quest status\n常用短路径：lab/  out/  lesson.md\n\n'" Enter

LANG_MODE="${ALGOLAND_LANG:-en}"
if [[ "$LANG_MODE" == "en" ]]; then
cat <<'MSG'
🧵 AlgoLand split-terminal mode is ready:
- Top pane: permanent scrollable lesson viewer
- Bottom pane: real shell (vim / python -m pdb / ssh all work here)

Recommended flow:
1. Read the operation hints in the bottom pane first
2. Switch to the lesson pane with: Ctrl-b then ↑
3. Read with j/k, PgUp/PgDn, g/G, { / }
4. Switch back with: Ctrl-b then ↓
MSG
elif [[ "$LANG_MODE" == "zh" ]]; then
cat <<'MSG'
🧵 已启动 AlgoLand 终端分屏模式：
- 上半屏：常驻可滚动讲义阅读器
- 下半屏：真实 shell（可直接运行 vim / python -m pdb / ssh）

建议这样用：
1. 先在下半屏看操作提示
2. 想读讲义时：Ctrl-b 然后 ↑
3. 在上半屏用 j/k、PgUp/PgDn、g/G、{ / } 阅读
4. 做题时：Ctrl-b 然后 ↓
MSG
fi

exec tmux attach -t "$SESSION"
