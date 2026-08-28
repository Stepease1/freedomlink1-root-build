#!/usr/bin/env python3
import os
from pathlib import Path
import sys

# 1. Remove Git lock
lock = Path(".git/index.lock")
if lock.exists():
    try:
        lock.unlink()
        print("[Recover] Removed .git/index.lock")
    except Exception as e:
        print(f"[Recover] Failed to remove .git/index.lock: {e}")
        # continue

# 2. Ensure tasks.json is writable by rewriting it
tasks = Path(".vscode/tasks.json")
if tasks.exists():
    try:
        data = tasks.read_text(encoding="utf-8")
        tasks.write_text(data, encoding="utf-8")
        print("[Recover] Rewrote .vscode/tasks.json to break Windows lock")
    except Exception as e:
        print(f"[Recover] Failed to rewrite .vscode/tasks.json: {e}")

print("[Recover] Now run:")
print("  git add .")
print("  git commit -m \"governance: recovery push\"")
print("  git push")
