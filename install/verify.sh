#!/bin/bash
set -e

echo "[Verification] Canonicalizing artifacts..."
python3 "$(dirname "$0")/../scripts/canonicalize_json.py" artifacts/ canonical/

echo "[Verification] Computing hashes..."
python3 "$(dirname "$0")/../scripts/compute_hashes.py" canonical/ hash_manifest.json

echo "[Verification] Building Merkle root..."
python3 "$(dirname "$0")/../scripts/build_merkle_tree.py" hash_manifest.json merkle_root.txt

echo "[Verification] Comparing Merkle root to omni proof master..."
python3 "$(dirname "$0")/../scripts/compare_root.py" merkle_root.txt artifacts/omni-proof-master.json

echo "[Verification] Sovereign signature check..."
python3 "$(dirname "$0")/../scripts/verify_signature.py" merkle_root.txt artifacts/omni-proof-master.json

echo "[Verification] Root Build integrity confirmed."
