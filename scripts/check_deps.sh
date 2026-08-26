#!/bin/bash
set -e

echo "[Deps] Checking required system commands..."
required_cmds=(curl jq python3)
missing=()
for c in "${required_cmds[@]}"; do
  if ! command -v "$c" >/dev/null 2>&1; then
    missing+=("$c")
  fi
done

if [ ${#missing[@]} -ne 0 ]; then
  echo "[Deps] Missing commands: ${missing[*]}"
  echo "Please install the missing packages (e.g. apt, yum, choco) and re-run."
  exit 2
fi

echo "[Deps] Checking Python package: cryptography..."
if ! python3 -c "import cryptography" >/dev/null 2>&1; then
  echo "[Deps] Python package 'cryptography' not found. Install with: pip3 install cryptography"
  exit 2
fi

echo "[Deps] All dependencies present."
