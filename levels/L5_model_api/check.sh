#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
mkdir -p "$ROOT/.state"
score=0
log="$ROOT/submissions/L5/requests_log.jsonl"
summary="$ROOT/submissions/L5/summary.md"

if [[ -f "$log" ]] && [[ $(wc -l < "$log") -ge 4 ]]; then
  score=$((score+20))
fi

if [[ -f "$log" ]] \
  && grep -q '"endpoint"[[:space:]]*:[[:space:]]*"official"' "$log" \
  && grep -q '"endpoint"[[:space:]]*:[[:space:]]*"selfhost"' "$log"; then
  score=$((score+25))
fi

if [[ -f "$log" ]] \
  && grep -q '"status"[[:space:]]*:[[:space:]]*200' "$log" \
  && grep -Eq '"attempt"[[:space:]]*:[[:space:]]*[2-9]' "$log"; then
  score=$((score+30))
fi

if [[ -f "$summary" ]] \
  && grep -qi 'official' "$summary" \
  && grep -qi 'selfhost' "$summary" \
  && [[ $(wc -l < "$summary") -ge 2 ]]; then
  score=$((score+25))
fi

echo "$score" > "$ROOT/.state/L5.score"
echo "L5 得分: $score/100"
