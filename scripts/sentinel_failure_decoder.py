#!/usr/bin/env python3
"""Print failed events from the governance logbook."""

import json
from pathlib import Path


log_path = Path("lineage/governance_logbook.json")
with log_path.open(encoding="utf-8") as log_file:
    logbook = json.load(log_file)

for event in logbook.get("events", []):
    status = str(event.get("status", ""))
    if "failed" in status.lower():
        print(f"[Decoder] Failure: {event.get('event', 'Unknown event')}")
        print(f"Reason: {event.get('details', 'No details provided')}")
