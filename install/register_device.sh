#!/bin/bash
set -e

echo "[Device Sovereignty] Generating hardware identity hash..."
HW_HASH=$(python3 "$(dirname "$0")/../scripts/hardware_hash.py")

DEVICE_ID="device-$(date +%s)"

echo "[Device Sovereignty] Registering device: $DEVICE_ID"

python3 "$(dirname "$0")/../scripts/register_device.py" "$DEVICE_ID" "$HW_HASH"

echo "[Device Sovereignty] Device registered in lineage/device_registry.json"
