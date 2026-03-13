#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
step="${1:-1}"
state="$ROOT/lab/api_state.json"
score=0
case "$step" in
  1)
    [[ -f "$state" ]] \
      && grep -q '"openai_sync_ok": true' "$state" \
      && grep -q '"anthropic_sync_ok": true' "$state" \
      && score=100
    ;;
  2)
    [[ -f "$state" ]] \
      && grep -q '"multiturn_ok": true' "$state" \
      && grep -q '"image_ok": true' "$state" \
      && grep -q '"stream_ok": true' "$state" \
      && score=100
    ;;
esac
mkdir -p "$ROOT/.state"
echo "$score" > "$ROOT/.state/L5.step${step}.score"
[[ $score -ge 70 ]]
