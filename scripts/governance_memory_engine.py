#!/usr/bin/env python3
"""Persist unique governance event names as institutional memory."""

import json
from pathlib import Path


log_path = Path("lineage/governance_logbook.json")
memory_path = Path("lineage/consciousness_memory.json")
with log_path.open(encoding="utf-8") as log_file:
    events = json.load(log_file).get("events", [])
with memory_path.open(encoding="utf-8") as memory_file:
    memory = json.load(memory_file)

recorded = memory.setdefault("events", [])
for event in events:
    name = event.get("event") if isinstance(event, dict) else str(event)
    if name and name not in recorded:
        recorded.append(name)

memory_path.write_text(json.dumps(memory, indent=2) + "\n", encoding="utf-8")
print("[Consciousness] Governance memory updated.")
