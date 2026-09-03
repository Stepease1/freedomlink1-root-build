#!/usr/bin/env python3
"""Map each registered sentinel to its governance intent."""

import json
from pathlib import Path


with Path("lineage/sentinel_registry.json").open(encoding="utf-8") as sentinels_file:
    sentinels = json.load(sentinels_file).get("sentinels", [])

intent_by_id = {
    "GS-01": "Protects smoke test integrity.",
    "GS-02": "Ensures governance test validity.",
    "GS-03": "Monitors lineage and corruption.",
}
intent = {}
for sentinel in sentinels:
    sentinel_id = sentinel.get("id", "unknown") if isinstance(sentinel, dict) else str(sentinel)
    intent[sentinel_id] = intent_by_id.get(sentinel_id, "Unknown sentinel intent.")

print("[Consciousness] Sentinel Intent Mapping:")
print(json.dumps(intent, indent=2))
