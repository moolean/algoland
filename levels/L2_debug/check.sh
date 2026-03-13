#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
mkdir -p "$ROOT/.state"
score=0

root_line_file="$ROOT/submissions/L2/root_cause_line.txt"
run_out_file="$ROOT/submissions/L2/run_output.txt"
expected_root="$(grep 'TypeError:' "$ROOT/levels/L2_debug/lab/train_crash.log" | tail -n 1 | sed -e 's/[[:space:]]*$//')"

if [[ -f "$root_line_file" ]] && diff -u <(echo "$expected_root") <(sed -e 's/[[:space:]]*$//' "$root_line_file") >/dev/null; then
  score=$((score+25))
fi

TARGET_PY="$ROOT/player/current/broken_train.py"
if [[ ! -f "$TARGET_PY" ]]; then
  TARGET_PY="$ROOT/levels/L2_debug/broken_train.py"
fi

if LEARNING_RATE=0.001 python "$TARGET_PY" 2>/dev/null | grep -q 'training ok'; then
  score=$((score+45))
fi

if [[ -f "$run_out_file" ]] && grep -q 'training ok' "$run_out_file"; then
  score=$((score+10))
fi

branch="$(git -C "$ROOT" branch --show-current || true)"
[[ "$branch" == "feat/onboarding-l2" ]] && score=$((score+10))

git -C "$ROOT" log --oneline -n 30 | grep -q 'L2 complete' && score=$((score+10))

echo "$score" > "$ROOT/.state/L2.score"
echo "L2 得分: $score/100"
if [[ $score -ge 70 ]]; then
  echo "🏅 通过！你获得徽章：Debug Ranger"
else
  echo "未通过。请先用命令提取 root cause，再修复脚本并保存运行输出。"
fi
