#!/usr/bin/env python3
"""Activate a sentinel through the canonical registry updater."""

import subprocess
import sys
from pathlib import Path


if len(sys.argv) != 2:
    print("Usage: activate_sentinel.py <sentinel-id>", file=sys.stderr)
    sys.exit(2)

if not Path("lineage/sentinel_registry.json").is_file():
    print("[Sentinel] registry not found", file=sys.stderr)
    sys.exit(3)

subprocess.run([
    sys.executable,
    "scripts/update_sentinel_registry.py",
    sys.argv[1],
    "active",
], check=True)
