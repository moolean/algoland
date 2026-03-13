#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
mkdir -p "$ROOT/.state"
score=0

[[ -x "$ROOT/submissions/L4/.venv/bin/python" ]] && score=$((score+25))

if [[ -f "$ROOT/submissions/L4/eval_result.json" ]] \
  && grep -q '"status": "PASS"' "$ROOT/submissions/L4/eval_result.json" \
  && grep -q '"threshold": 0.85' "$ROOT/submissions/L4/eval_result.json"; then
  score=$((score+45))
fi

if [[ -f "$ROOT/submissions/L4/pip_freeze.txt" ]] \
  && grep -qi '^rich==13.7.1' "$ROOT/submissions/L4/pip_freeze.txt" \
  && grep -qi '^PyYAML==6.0.2' "$ROOT/submissions/L4/pip_freeze.txt"; then
  score=$((score+30))
fi

echo "$score" > "$ROOT/.state/L4.score"
echo "L4 得分: $score/100"
