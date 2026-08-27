# Lineage Drift Protocol
## Freedomlink1 — Genesis Epoch

This protocol defines the required actions when lineage drift is detected by the Integrity Monitor.

---

## I. Definition of Drift

Lineage drift occurs when:
- Epoch ledger changes unexpectedly  
- Module registry changes without ceremony  
- POC registry changes without graduation  
- Hashes or signatures differ from previous snapshot  

---

## II. Detection

Triggered by:
```
python3 scripts/lineage_diff.py
```
If any field reports `YES`, drift is present.

---

## III. Immediate Actions

1. Freeze merges into `main`.  
2. Notify custodians via Slack + Email.  
3. Review:
   - `lineage/last_integrity_snapshot.json`  
   - `lineage/governance_logbook.json`  
   - `ci_summary.md`  

---

## IV. Drift Classification

### Type A — Benign Drift  
- Expected module activation  
- Expected POC graduation  
- Expected epoch advancement  

### Type B — Suspicious Drift  
- Unexpected registry changes  
- Missing lineage entries  
- Hash mismatch  

### Type C — Critical Drift  
- Corruption  
- Malformed lineage  
- Signature mismatch  

---

## V. Drift Resolution

### Step 1 — Reconcile lineage
```
python3 scripts/verify_lineage.py lineage/
```
### Step 2 — Regenerate snapshot
```
python3 scripts/lineage_diff.py
```
### Step 3 — Log resolution
```
python3 scripts/update_logbook.py "Lineage Drift Resolved"
```

---

## VI. Closing

> “Drift reveals movement. Resolution restores sovereignty.”
