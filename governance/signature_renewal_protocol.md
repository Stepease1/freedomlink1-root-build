# Sovereign Signature Renewal Protocol
## Freedomlink1 — Genesis Epoch

This protocol governs the renewal of sovereign signatures across lineage artifacts.

---

## I. Renewal Triggers

Signature renewal occurs when:
- Steward key rotation  
- Steward succession  
- Epoch advancement  
- Merkle root regeneration  
- Hash manifest regeneration  

---

## II. Renewal Steps

### Step 1 — Regenerate Merkle Root
```
python3 scripts/build_merkle_tree.py hash_manifest.json merkle_root.txt
```
### Step 2 — Steward Signs Artifacts
Steward signs:
- `merkle_root.txt`  
- `hash_manifest.json`  
- `epoch_ledger.json`  

### Step 3 — Update Proof Master
Custodians update:
`artifacts/omni_proof_master.json`

### Step 4 — Log Renewal
```
python3 scripts/update_logbook.py "Sovereign Signature Renewal"
```
---

## III. Closing

> “Renewal preserves continuity. Signature preserves sovereignty.”
