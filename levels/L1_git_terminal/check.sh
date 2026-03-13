#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
mkdir -p "$ROOT/.state"
score=0

best_file="$ROOT/submissions/L1/best_run.txt"
err_file="$ROOT/submissions/L1/error_top2.txt"
fixed_file="$ROOT/submissions/L1/model_fixed.yaml"

expected_best="$(awk '{
  split($3,a,"="); v=a[2]+0;
  if (NR==1 || v<min){ min=v; line=$0 }
} END { print line }' "$ROOT/levels/L1_git_terminal/lab/experiments.log")"

expected_top2="$(awk '/\[error\]/{cnt[$2]++} END {for (k in cnt) print k, cnt[k]}' "$ROOT/levels/L1_git_terminal/lab/train.err.log" | sort -k2,2nr -k1,1 | head -n 2)"

# 1) best run
if [[ -f "$best_file" ]] && diff -u <(echo "$expected_best") <(sed -e 's/[[:space:]]*$//' "$best_file") >/dev/null; then
  score=$((score+30))
fi

# 2) top2 errors
if [[ -f "$err_file" ]] && diff -u <(echo "$expected_top2") <(sed -e 's/[[:space:]]*$//' "$err_file") >/dev/null; then
  score=$((score+30))
fi

# 3) fixed yaml
if [[ -f "$fixed_file" ]] \
  && grep -q '^lr: 0.001$' "$fixed_file" \
  && grep -q '^batch_size: 32$' "$fixed_file"; then
  score=$((score+15))
fi

# 4) git workflow
branch="$(git -C "$ROOT" branch --show-current || true)"
if [[ "$branch" == "feat/onboarding-l1" ]]; then
  score=$((score+5))
fi

commit_count="$(git -C "$ROOT" log --oneline --grep='L1' | wc -l | tr -d ' ')"
if [[ "$commit_count" -ge 2 ]]; then
  score=$((score+10))
fi

if git -C "$ROOT" log --oneline -n 30 | grep -q 'L1 complete'; then
  score=$((score+10))
fi

echo "$score" > "$ROOT/.state/L1.score"
echo "L1 得分: $score/100"
if [[ $score -ge 70 ]]; then
  echo "🏅 通过！你获得徽章：Terminal Scout"
else
  echo "未通过。建议：用真实命令从 lab 数据生成结果，再完成 git 分支与提交。"
fi
