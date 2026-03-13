#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
step="${1:-1}"
score=0
case "$step" in
  1)
    [[ -x "$ROOT/submissions/L2/.venv/bin/python" ]] && score=100
    ;;
  2)
    [[ -f "$ROOT/submissions/L2/eval_result.json" ]] && grep -q '"status": "PASS"' "$ROOT/submissions/L2/eval_result.json" && grep -q '"threshold": 0.85' "$ROOT/submissions/L2/eval_result.json" && score=100
    ;;
  3)
    [[ -f "$ROOT/submissions/L2/pip_freeze.txt" ]] && grep -qi '^rich==13.7.1' "$ROOT/submissions/L2/pip_freeze.txt" && grep -qi '^PyYAML==6.0.2' "$ROOT/submissions/L2/pip_freeze.txt" && score=100
    ;;
esac
mkdir -p "$ROOT/.state"
echo "$score" > "$ROOT/.state/L2.step${step}.score"
[[ $score -ge 70 ]]
