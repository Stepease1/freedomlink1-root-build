#!/usr/bin/env python3
"""Explain the purpose of each registered module."""

import json
from pathlib import Path


with Path("lineage/module_registry.json").open(encoding="utf-8") as modules_file:
    modules = json.load(modules_file).get("modules", [])

reasoning = {}
for module in modules:
    module_id = module.get("id", "unknown") if isinstance(module, dict) else str(module)
    if module_id == "GIM-01":
        reasoning[module_id] = "Provides sovereign intelligence and analytical capability."
    else:
        reasoning[module_id] = "Purpose not yet defined."

print("[Consciousness] Module Purpose Reasoning:")
print(json.dumps(reasoning, indent=2))
