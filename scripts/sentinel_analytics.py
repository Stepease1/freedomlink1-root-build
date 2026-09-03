#!/usr/bin/env python3
"""Summarize governance events by outcome and sentinel."""

import json
from pathlib import Path


LOG_PATH = Path("lineage/governance_logbook.json")

with LOG_PATH.open(encoding="utf-8") as log_file:
    logbook = json.load(log_file)

events = logbook.get("events", [])
stats = {
    "total_events": len(events),
    "failures": 0,
    "successes": 0,
    "sentinel_activity": {},
}

for event in events:
    sentinel = event.get("sentinel", "unknown")
    stats["sentinel_activity"][sentinel] = stats["sentinel_activity"].get(sentinel, 0) + 1
    status = str(event.get("status", "success"))
    if "failed" in status.lower():
        stats["failures"] += 1
    else:
        stats["successes"] += 1

print("[Analytics] Governance Event Summary")
print(json.dumps(stats, indent=2))
