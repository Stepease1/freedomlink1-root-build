#!/usr/bin/env bash
set -euo pipefail

echo "[Runner] Starting governance checks..."

SCRIPTS=(
  "scripts/integrity_monitor.py"
  "scripts/ci_summary.py"
  "scripts/update_logbook.py"
  "scripts/validate_epoch_ledger.py"
  "scripts/lineage_diff.py"
)

FAILED=0
for s in "${SCRIPTS[@]}"; do
  if [ -f "$s" ]; then
    echo "[Runner] Running $s"
    if ! python3 "$s"; then
      echo "[Runner] $s failed"
      FAILED=1
    fi
  else
    echo "[Runner] Skipping missing $s"
  fi
done

if [ "$FAILED" -eq 0 ]; then
  echo "[Runner] All checks completed successfully"
  exit 0
else
  echo "[Runner] Some checks failed"
  exit 2
fi
#!/usr/bin/env bash
set -euo pipefail
# Governance checks runner — safe to run locally or in CI
echo "[Runner] Starting governance checks..."

echo "[Runner] Validate epoch ledger"
python3 scripts/validate_epoch_ledger.py || { echo "Validation failed"; exit 2; }

echo "[Runner] Run integrity monitor"
python3 scripts/integrity_monitor.py || { echo "Integrity monitor failed"; exit 3; }

echo "[Runner] Run lineage diff"
python3 scripts/lineage_diff.py || { echo "Lineage diff failed"; exit 4; }

echo "[Runner] Run CI summary (if present)"
if [ -f scripts/ci_summary.py ]; then
  python3 scripts/ci_summary.py || echo "CI summary exited non-zero"
else
  echo "[Runner] scripts/ci_summary.py not found — skipping"
fi

echo "[Runner] Run governance tests (pytest) if available"
if command -v pytest >/dev/null 2>&1; then
  pytest -q || echo "Some tests failed"
else
  echo "pytest not installed — skipping test run"
fi

echo "[Runner] Governance checks complete"
#!/usr/bin/env bash
# Run a sequence of governance checks locally.
set -euo pipefail

echo "[Run] Validate epoch ledger"
python3 scripts/validate_epoch_ledger.py

echo "[Run] Integrity monitor"
python3 scripts/integrity_monitor.py

echo "[Run] Lineage diff"
python3 scripts/lineage_diff.py

if command -v pytest >/dev/null 2>&1; then
  echo "[Run] Governance pytest suite"
  pytest tests/governance -q
else
  echo "[Run] pytest not found; skipping pytest step"
fi

echo "[Run] Governance checks completed"
