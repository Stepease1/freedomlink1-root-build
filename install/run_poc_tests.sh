#!/bin/bash
set -e

echo "[POC] Running POC verification suite..."

if [ ! -f lineage/poc_registry.json ]; then
    echo "[POC] lineage/poc_registry.json not found; nothing to run."
    exit 0
fi

for POC in $(jq -r '.pocs[].id' lineage/poc_registry.json); do
    echo "[POC] Testing $POC..."
    python3 "$(dirname "$0")/../tools/poc_verify.py" "$POC"
done

echo "[POC] All POCs tested."
