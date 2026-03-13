#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
step="${1:-1}"
score=0
mkdir -p "$ROOT/.state"
case "$step" in
  1)
    for f in "$ROOT/player/current/out/vim_version.txt" "$ROOT/submissions/L0/vim_version.txt"; do
      [[ -f "$f" ]] && grep -qi 'vim' "$f" && score=100 && break
    done
    ;;
  2)
    for f in "$ROOT/player/current/out/hello_vim.txt" "$ROOT/submissions/L0/hello_vim.txt"; do
      if [[ -f "$f" ]] && [[ $(wc -l < "$f") -ge 2 ]] && grep -qi 'vim' "$f"; then score=100; break; fi
    done
    ;;
esac
echo "$score" > "$ROOT/.state/L0.step${step}.score"
[[ $score -ge 70 ]]
