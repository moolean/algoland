#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
step="${1:-1}"
score=0
case "$step" in
  1)
    [[ -f "$ROOT/submissions/L4/.ssh/id_ed25519" ]] && [[ -f "$ROOT/submissions/L4/.ssh/id_ed25519.pub" ]] && score=100
    ;;
  2)
    cfg="$ROOT/submissions/L4/.ssh/config"
    [[ -f "$cfg" ]] \
      && grep -Eqi '^Host[[:space:]]+train-node$' "$cfg" \
      && grep -Eqi '^[[:space:]]*HostName[[:space:]]+127\.0\.0\.1$' "$cfg" \
      && grep -Eqi '^[[:space:]]*User[[:space:]]+trainee$' "$cfg" \
      && grep -Eqi '^[[:space:]]*Port[[:space:]]+2222$' "$cfg" \
      && score=100
    ;;
  3)
    [[ -f "$ROOT/submissions/L4/login_result.txt" ]] \
      && grep -q 'login ok' "$ROOT/submissions/L4/login_result.txt" \
      && grep -q 'alias=train-node' "$ROOT/submissions/L4/login_result.txt" \
      && score=100
    ;;
esac
mkdir -p "$ROOT/.state"
echo "$score" > "$ROOT/.state/L4.step${step}.score"
[[ $score -ge 70 ]]
