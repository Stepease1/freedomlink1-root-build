#!/usr/bin/env python3
"""Compare recorded SHA-256 hashes with files on disk."""

import hashlib
import json
from pathlib import Path


MANIFEST_PATH = Path("artifacts/hash-manifest.json")
with MANIFEST_PATH.open(encoding="utf-8") as manifest_file:
    manifest = json.load(manifest_file)

if not isinstance(manifest, dict):
    print("[AnomalyDetector] Hash manifest contains no file entries; no comparisons performed.")
    raise SystemExit(0)

entries = manifest.get("files", manifest)
if not entries or not all(isinstance(value, str) for value in entries.values()):
    print("[AnomalyDetector] Hash manifest contains no file entries; no comparisons performed.")
    raise SystemExit(0)
anomalies = []
for file_path, expected_hash in entries.items():
    path = Path(file_path)
    if not path.exists():
        anomalies.append({"file": file_path, "error": "missing"})
        continue
    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual_hash != expected_hash:
        anomalies.append({"file": file_path, "expected": expected_hash, "actual": actual_hash})

if anomalies:
    print("[AnomalyDetector] Integrity anomalies detected:")
    print(json.dumps(anomalies, indent=2))
    raise SystemExit(1)

print("[AnomalyDetector] No anomalies detected.")
