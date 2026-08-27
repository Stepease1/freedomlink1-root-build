# Epoch Advancement Protocol
## Freedomlink1 — Genesis Epoch

This protocol governs the advancement from one epoch to the next.

---

## I. Preconditions

Epoch advancement requires:
- All modules in current epoch verified  
- All POCs either graduated or retired  
- No lineage corruption  
- Sovereign signature valid  
- Merkle root stable  

---

## II. Advancement Steps

### Step 1 — Verify Lineage
```
python3 scripts/verify_lineage.py lineage/
```
### Step 2 — Verify Modules
```
python3 tools/module_verify_all.py
```
### Step 3 — Verify POCs
```
python3 tools/poc_verify_all.py
```
### Step 4 — Generate Epoch Summary
```
python3 scripts/ci_summary.py
```
### Step 5 — Advance Epoch

Update `lineage/epoch_ledger.json` by appending:
```
{
  "epoch": "N+1",
  "advanced_at": "<timestamp>",
  "reason": "<governance justification>"
}
```
### Step 6 — Sovereign Signature

Steward signs:
- new `epoch_ledger.json`  
- new Merkle root  

---

## III. Log Advancement

```
python3 scripts/update_logbook.py "Epoch Advanced to N+1"
```

---

## IV. Closing

> “Epochs mark the passage of sovereignty. Advancement is continuity.”
