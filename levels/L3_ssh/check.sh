#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
mkdir -p "$ROOT/.state"
score=0
SSH_DIR="$ROOT/submissions/L3/.ssh"

[[ -f "$SSH_DIR/id_ed25519" ]] && [[ -f "$SSH_DIR/id_ed25519.pub" ]] && score=$((score+30))

if [[ -f "$SSH_DIR/config" ]] \
  && grep -qi '^Host train-node' "$SSH_DIR/config" \
  && grep -qi '^HostName 127.0.0.1' "$SSH_DIR/config" \
  && grep -qi '^User trainee' "$SSH_DIR/config" \
  && grep -qi '^Port 2222' "$SSH_DIR/config"; then
  score=$((score+30))
fi

if [[ -f "$ROOT/submissions/L3/ssh_effective.txt" ]] \
  && grep -q '^hostname 127.0.0.1$' "$ROOT/submissions/L3/ssh_effective.txt" \
  && grep -q '^user trainee$' "$ROOT/submissions/L3/ssh_effective.txt" \
  && grep -q '^port 2222$' "$ROOT/submissions/L3/ssh_effective.txt"; then
  score=$((score+25))
fi

if [[ -f "$ROOT/submissions/L3/ssh_summary.txt" ]] && [[ $(wc -l < "$ROOT/submissions/L3/ssh_summary.txt") -ge 3 ]]; then
  score=$((score+15))
fi

echo "$score" > "$ROOT/.state/L3.score"
echo "L3 得分: $score/100"
