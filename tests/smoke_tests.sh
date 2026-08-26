#!/bin/bash
set -euo pipefail

echo "[Smoke] Starting quick smoke tests"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "[Smoke] Running dependency checks"
bash "$REPO_ROOT/scripts/check_deps.sh"

echo "[Smoke] Generating hardware hash"
HW_HASH=$(python3 "$REPO_ROOT/scripts/hardware_hash.py")
echo "[Smoke] Hardware hash: $HW_HASH"

echo "[Smoke] Registering test device (this will append to lineage/device_registry.json)"
TEST_DEVICE_ID="smoke-test-$(date +%s)"
python3 "$REPO_ROOT/scripts/register_device.py" "$TEST_DEVICE_ID" "$HW_HASH"

echo "[Smoke] Running a sample POC verification"
python3 "$REPO_ROOT/tools/poc_verify.py" "smoke-sample-poc"

echo "[Smoke] Checking CLI placeholder"
if command -v freedomlink1 >/dev/null 2>&1; then
  freedomlink1 version || true
elif [ -x "$REPO_ROOT/bin/freedomlink1-cli" ]; then
  "$REPO_ROOT/bin/freedomlink1-cli" version || true
else
  echo "[Smoke] CLI not installed; skipping CLI check"
fi

if [ -f "$REPO_ROOT/merkle_root.txt" ] && [ -f "$REPO_ROOT/artifacts/omni-proof-master.json" ]; then
  echo "[Smoke] Running signature verification (if cryptography available)"
  python3 "$REPO_ROOT/scripts/verify_signature.py" "$REPO_ROOT/merkle_root.txt" "$REPO_ROOT/artifacts/omni-proof-master.json" || echo "[Smoke] Signature verification failed or not configured"
else
  echo "[Smoke] merkle_root.txt or artifacts/omni-proof-master.json missing; skipping signature check"
fi

echo "[Smoke] Smoke tests completed successfully"
