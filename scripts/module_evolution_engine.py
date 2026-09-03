#!/usr/bin/env python3
"""Apply capability evolution to registered modules."""

import json
from pathlib import Path


module_path = Path("lineage/module_registry.json")
with module_path.open(encoding="utf-8") as modules_file:
    registry = json.load(modules_file)

for module in registry.get("modules", []):
    if module.get("id") == "GIM-01":
        module["evolution"] = "Expanded analytical capabilities"

module_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
print("[Evolution] Module evolution applied.")
