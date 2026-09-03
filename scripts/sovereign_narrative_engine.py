#!/usr/bin/env python3
"""Generate a current narrative of the institution's evolution."""

import json
from pathlib import Path


with Path("lineage/epoch_ledger.json").open(encoding="utf-8") as ledger_file:
    epochs = json.load(ledger_file).get("epochs", [])
if not epochs:
    raise SystemExit("[Consciousness] No epoch found.")

epoch = epochs[-1].get("epoch")
narrative = f"""# Sovereign Narrative - Epoch {epoch}

Freedomlink1 has entered Epoch {epoch}.
It has established identity, governance, intelligence, and autonomy.
The lineage continues to evolve through documented constitutional practice.
"""

output_path = Path("docs/governance/narrative_epoch.md")
output_path.write_text(narrative, encoding="utf-8")
print(f"[Consciousness] Sovereign narrative generated: {output_path}")
