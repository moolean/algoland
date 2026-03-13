#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
step="${1:-1}"
score=0
expected_best="$(awk '{split($3,a,"=");v=a[2]+0;if(NR==1||v<min){min=v;line=$0}} END{print line}' "$ROOT/levels/L1_git_terminal/lab/experiments.log")"
expected_top2="$(awk '/\[error\]/{cnt[$2]++} END {for (k in cnt) print k, cnt[k]}' "$ROOT/levels/L1_git_terminal/lab/train.err.log" | sort -k2,2nr -k1,1 | head -n2)"
case "$step" in
  1)
    [[ -f "$ROOT/submissions/L1/best_run.txt" ]] && diff -u <(echo "$expected_best") <(sed 's/[[:space:]]*$//' "$ROOT/submissions/L1/best_run.txt") >/dev/null && score=100
    ;;
  2)
    [[ -f "$ROOT/submissions/L1/error_top2.txt" ]] && diff -u <(echo "$expected_top2") <(sed 's/[[:space:]]*$//' "$ROOT/submissions/L1/error_top2.txt") >/dev/null && score=100
    ;;
  3)
    [[ -f "$ROOT/submissions/L1/model_fixed.yaml" ]] && grep -q '^lr: 0.001$' "$ROOT/submissions/L1/model_fixed.yaml" && grep -q '^batch_size: 32$' "$ROOT/submissions/L1/model_fixed.yaml" && score=100
    ;;
  4)
    b="$(git -C "$ROOT" branch --show-current || true)"
    c="$(git -C "$ROOT" log --oneline --grep='L1' | wc -l | tr -d ' ')"
    if [[ "$b" == "feat/onboarding-l1" ]] && [[ "$c" -ge 2 ]] && git -C "$ROOT" log --oneline -n 30 | grep -q 'L1 complete'; then score=100; fi
    ;;
esac
mkdir -p "$ROOT/.state"
echo "$score" > "$ROOT/.state/L1.step${step}.score"
[[ $score -ge 70 ]]
