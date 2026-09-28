#!/usr/bin/env python3
"""Check FL1-C binding metadata against available local lineage artifacts."""

import json
import time
from pathlib import Path


UNIFIED_ROOT = Path(__file__).resolve().parent.parent
REPOSITORY_ROOT = UNIFIED_ROOT.parent
BINDING_FILE = UNIFIED_ROOT / "bindings" / "fl1c_binding.json"
DRIFT_REPORT = UNIFIED_ROOT / "reports" / "fl1c_drift_report.json"


def load_json(path):
    if not path.is_file():
        return None
    with path.open("r", encoding="utf-8") as source:
        value = json.load(source)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def resolve_lineage_file(binding):
    lineage = binding.get("lineage", {})
    anchor_file = lineage.get("anchor_file") if isinstance(lineage, dict) else None
    if not isinstance(anchor_file, str) or not anchor_file:
        return None

    relative_path = Path(anchor_file)
    if relative_path.is_absolute() or ".." in relative_path.parts:
        return None

    candidates = (
        UNIFIED_ROOT / relative_path,
        REPOSITORY_ROOT / relative_path,
        REPOSITORY_ROOT / "freedomlink1-root" / relative_path,
    )
    return next((path for path in candidates if path.is_file()), None)


def has_values(mapping, keys):
    return isinstance(mapping, dict) and all(mapping.get(key) not in (None, "") for key in keys)


def run_drift_checks(binding, lineage, lineage_path):
    governance = binding.get("governance", {}) if binding else {}
    governance_rules = governance.get("governance_rules", {}) if isinstance(governance, dict) else {}
    identity = binding.get("identity", {}) if binding else {}
    hardware = binding.get("hardware", {}) if binding else {}
    unified_layer = binding.get("unified_layer", {}) if binding else {}
    consistency = unified_layer.get("cross_layer_consistency", {}) if isinstance(unified_layer, dict) else {}

    lineage_metadata = binding.get("lineage", {}) if binding else {}
    anchor_identity = lineage.get("identity") if lineage else None
    anchor_rootstone = lineage.get("rootstone") if lineage else None

    checks = {
        "binding_present": binding is not None,
        "lineage_present": lineage is not None,
        "lineage_event_match": (
            lineage_metadata.get("event") == lineage.get("event")
            if lineage and isinstance(lineage_metadata, dict)
            else None
        ),
        "epoch_alignment": (
            lineage_metadata.get("epoch") == lineage.get("epoch")
            if lineage and isinstance(lineage_metadata, dict)
            else None
        ),
        "governance_bindings_declared": (
            has_values(governance, ("router", "epoch_manager", "lineage_registry", "access_control"))
            and has_values(governance_rules, ("mint_authority", "lineage_event"))
            and governance_rules.get("epoch_awareness") is True
        ),
        "governance_lineage_event_match": (
            governance_rules.get("lineage_event") == lineage_metadata.get("event")
            if isinstance(governance_rules, dict) and isinstance(lineage_metadata, dict)
            else False
        ),
        "identity_binding_match": (
            has_values(identity, ("creator_registry", "creator_binding", "provenance"))
            and isinstance(anchor_identity, str)
            and "creator" in anchor_identity.lower()
            and "bound" in anchor_identity.lower()
            if lineage
            else None
        ),
        "hardware_binding_match": (
            has_values(hardware, ("rootstone_binding", "hardware_identity", "trust_anchor"))
            and isinstance(anchor_rootstone, str)
            and anchor_rootstone.lower() == "bound"
            if lineage
            else None
        ),
        "consistency_flags_enabled": (
            has_values(consistency, ("identity", "lineage", "governance", "hardware", "economic"))
            and all(consistency.get(key) is True for key in ("identity", "lineage", "governance", "hardware", "economic"))
        ),
    }

    failed_checks = [name for name, passed in checks.items() if passed is False]
    unknown_checks = [name for name, passed in checks.items() if passed is None]
    if failed_checks:
        drift_status = "detected"
    elif unknown_checks:
        drift_status = "not_assessed"
    else:
        drift_status = "none_detected"

    return {
        "timestamp": int(time.time()),
        "verification_scope": "local metadata and on-disk artifacts only",
        "resolved_lineage_file": lineage_path.relative_to(REPOSITORY_ROOT).as_posix() if lineage_path else None,
        "checks": checks,
        "failed_checks": failed_checks,
        "unknown_checks": unknown_checks,
        "drift_status": drift_status,
        "drift_detected": True if failed_checks else False if not unknown_checks else None,
    }


def update_binding_last_check(binding, timestamp):
    unified_layer = binding.get("unified_layer")
    if not isinstance(unified_layer, dict):
        raise ValueError("Binding is missing the unified_layer object")
    drift_detection = unified_layer.get("drift_detection")
    if not isinstance(drift_detection, dict):
        raise ValueError("Binding is missing the unified_layer.drift_detection object")

    drift_detection["last_check"] = timestamp
    with BINDING_FILE.open("w", encoding="utf-8", newline="\n") as destination:
        json.dump(binding, destination, indent=2)
        destination.write("\n")


def write_drift_report(results):
    DRIFT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    with DRIFT_REPORT.open("w", encoding="utf-8", newline="\n") as destination:
        json.dump(results, destination, indent=2)
        destination.write("\n")


def main():
    print("Running Unified Layer Drift Detector for FL1-C...")
    try:
        binding = load_json(BINDING_FILE)
        lineage_path = resolve_lineage_file(binding) if binding else None
        lineage = load_json(lineage_path) if lineage_path else None
        results = run_drift_checks(binding, lineage, lineage_path)

        if binding:
            update_binding_last_check(binding, results["timestamp"])
        write_drift_report(results)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"ERROR: {error}")
        return 2

    print("\nDrift Detection Results:")
    for name, passed in results["checks"].items():
        print(f"  {name}: {passed}")
    print(f"  drift_status: {results['drift_status']}")
    print(f"  report: {DRIFT_REPORT.relative_to(REPOSITORY_ROOT).as_posix()}")

    if results["drift_status"] == "detected":
        print("\nDrift detected; see the machine-readable report for failed checks.")
        return 1
    if results["drift_status"] == "not_assessed":
        print("\nSome checks could not be assessed; no clean result is claimed.")
        return 2
    print("\nNo drift detected within the checked local metadata and artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())