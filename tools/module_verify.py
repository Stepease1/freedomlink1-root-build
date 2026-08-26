#!/usr/bin/env python3
"""Minimal module verifier stub.
Usage: module_verify.py <module_id>
This script is intentionally lightweight — replace with full verification logic.
"""
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: module_verify.py <module_id>")
    sys.exit(2)

mid = sys.argv[1]
print(f"[module_verify] Verifying module {mid}")

# Example check: look for a module artifact under artifacts/modules/<mid>.tar
artifact = Path(f"artifacts/modules/{mid}.tar")
if artifact.exists():
    print(f"[module_verify] Found artifact: {artifact}")
    print(f"[module_verify] {mid}: OK")
else:
    print(f"[module_verify] No artifact for {mid} — mark as SKIPPED")
