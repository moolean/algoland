#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
step="${1:-1}"
score=0
case "$step" in
  1)
    if [[ -f "$ROOT/submissions/L3/pdb_session.txt" ]] \
      && grep -q '(Pdb)' "$ROOT/submissions/L3/pdb_session.txt" \
      && grep -Eq 'b[[:space:]]*build_score|bb[[:space:]]*bbuuiilldd__ssccoorree' "$ROOT/submissions/L3/pdb_session.txt" \
      && grep -Eq 'selected|sseelleecctteedd' "$ROOT/submissions/L3/pdb_session.txt" \
      && grep -Eq 'len\([[:space:]]*selected[[:space:]]*\)|len\([[:space:]]*sseelleecctteedd[[:space:]]*\)|lleenn\([[:space:]]*sseelleecctteedd[[:space:]]*\)' "$ROOT/submissions/L3/pdb_session.txt"; then
      score=100
    fi
    ;;
  2)
    [[ -f "$ROOT/submissions/L3/pdb_bug_fixed.py" ]] && [[ -f "$ROOT/submissions/L3/run_output.txt" ]] && grep -q 'result=4.0' "$ROOT/submissions/L3/run_output.txt" && score=100
    ;;
  3)
    [[ -f "$ROOT/submissions/L3/batch_report_fixed.py" ]] \
      && [[ -f "$ROOT/submissions/L3/final_report.txt" ]] \
      && grep -q 'best=run_a' "$ROOT/submissions/L3/final_report.txt" \
      && grep -q 'val_score=0.873' "$ROOT/submissions/L3/final_report.txt" \
      && score=100
    ;;
esac
mkdir -p "$ROOT/.state"
echo "$score" > "$ROOT/.state/L3.step${step}.score"
[[ $score -ge 70 ]]
