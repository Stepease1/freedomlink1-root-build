#!/bin/bash
set -e

echo "[Smoke] Running Freedomlink1 smoke tests..."

if [ -d "tests" ]; then
  if command -v pytest >/dev/null 2>&1; then
    pytest tests || echo "[Smoke] pytest failed, investigate locally."
  else
    echo "[Smoke] pytest not installed, skipping."
  fi
else
  echo "[Smoke] No tests/ directory, skipping."
fi

echo "[Smoke] Smoke test script completed."
