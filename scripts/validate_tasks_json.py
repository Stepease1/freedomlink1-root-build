#!/usr/bin/env python3
import json
from pathlib import Path
import sys

path = Path(".vscode/tasks.json")

if not path.exists():
    print("[tasks.json] NOT FOUND: .vscode/tasks.json")
    sys.exit(2)

try:
    raw = path.read_text(encoding="utf-8")
    json.loads(raw)
    print("[tasks.json] VALID JSON")
except Exception as e:
    print("[tasks.json] INVALID JSON")
    print(e)
    sys.exit(1)

# Check for hidden Unicode control characters (allow newline, tab, carriage return)
bad = [c for c in raw if ord(c) < 32 and c not in ("\n", "\t", "\r")]
if bad:
    print("[tasks.json] Hidden control characters detected.")
    sys.exit(3)
else:
    print("[tasks.json] No hidden Unicode characters.")
