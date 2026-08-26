#!/usr/bin/env python3
import json
import sys
from datetime import datetime
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: update_logbook.py <event>")
    sys.exit(2)

event = sys.argv[1]

log_path = Path("lineage/governance_logbook.json")
log_path.parent.mkdir(parents=True, exist_ok=True)

if log_path.exists():
    try:
        with log_path.open("r", encoding="utf-8") as f:
            log = json.load(f)
    except Exception:
        # Repair corrupted file by resetting
        log = {"project": "Freedomlink1", "version": "1.0.0", "events": []}
else:
    log = {"project": "Freedomlink1", "version": "1.0.0", "events": []}

log.setdefault("events", []).append({
    "event": event,
    "timestamp": datetime.utcnow().isoformat() + "Z"
})

with log_path.open("w", encoding="utf-8") as f:
    json.dump(log, f, indent=2)

print(f"[Logbook] Recorded event: {event}")
#!/usr/bin/env python3
import json
import sys
from datetime import datetime
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: update_logbook.py <event>", file=sys.stderr)
    sys.exit(2)

event = sys.argv[1]
logbook_path = Path("lineage/governance_logbook.json")
logbook_path.parent.mkdir(parents=True, exist_ok=True)

if logbook_path.exists():
    with logbook_path.open("r", encoding="utf-8") as f:
        log = json.load(f)
else:
    log = {"project": "Freedomlink1", "version": "1.0.0", "events": []}

log.setdefault("events", []).append({
    "event": event,
    "timestamp": datetime.utcnow().isoformat() + "Z"
})

with logbook_path.open("w", encoding="utf-8") as f:
    json.dump(log, f, indent=2)

print(f"[Logbook] Recorded event: {event}")
#!/usr/bin/env python3
import json
import sys
from datetime import datetime
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: update_logbook.py \"event description\"")
    sys.exit(2)

event = sys.argv[1]

log_path = Path("lineage/governance_logbook.json")
if not log_path.exists():
    log = {"project": "Freedomlink1", "version": "1.0.0", "events": []}
else:
    with log_path.open() as f:
        log = json.load(f)

log.setdefault("events", []).append({
    "event": event,
    "timestamp": datetime.utcnow().isoformat() + "Z"
})

with log_path.open("w") as f:
    json.dump(log, f, indent=2)

print(f"[Logbook] Recorded event: {event}")
#!/usr/bin/env python3
import json
import sys
from datetime import datetime
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: update_logbook.py <event>", file=sys.stderr)
    sys.exit(2)

event = sys.argv[1]
log_path = Path("lineage/governance_logbook.json")
if not log_path.exists():
    log = {"project": "Freedomlink1", "version": "1.0.0", "events": []}
else:
    with log_path.open() as f:
        log = json.load(f)

log.setdefault("events", []).append({
    "event": event,
    "timestamp": datetime.utcnow().isoformat() + "Z"
})

with log_path.open("w") as f:
    json.dump(log, f, indent=2)

print(f"[Logbook] Recorded event: {event}")
