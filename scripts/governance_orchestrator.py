#!/usr/bin/env python3
"""Run the intelligence and autonomous governance cycle in sequence."""

import subprocess
import sys
import json
from datetime import datetime, timezone
from pathlib import Path


steps = [
    [sys.executable, "scripts/sentinel_analytics.py"],
    [sys.executable, "scripts/drift_forecaster.py"],
    [sys.executable, "scripts/integrity_anomaly_detector.py"],
    [sys.executable, "scripts/epoch_health.py"],
    [sys.executable, "scripts/decision_support.py"],
    [sys.executable, "scripts/autonomous_sentinel_activation.py"],
    [sys.executable, "scripts/autonomous_epoch_advancement.py"],
    [sys.executable, "scripts/autonomous_module_activation.py"],
    [sys.executable, "scripts/autonomous_signature_renewal.py"],
    [sys.executable, "scripts/autonomous_lineage_rollback.py"],
]

for step in steps:
    print(f"[Orchestrator] Running: {' '.join(step)}")
    # Anomaly detection reports findings with a non-zero status; autonomy must inspect them.
    subprocess.run(step, check=step[1] != "scripts/integrity_anomaly_detector.py")

ledger_path = Path("lineage/autonomy_ledger.json")
ledger = json.loads(ledger_path.read_text(encoding="utf-8")) if ledger_path.exists() else {"autonomy_events": []}
ledger.setdefault("autonomy_events", []).append({
    "event": "Autonomous governance cycle",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "status": "complete",
})
ledger_path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")

print("[Orchestrator] Autonomous governance cycle complete.")
