# Root Build Recovery Protocol
## Freedomlink1 — Genesis Epoch

This protocol defines the steps required to restore the Root Build after corruption, signature failure, or artifact inconsistency.

---

## I. Detection

Recovery is triggered when:
- Merkle root mismatch  
- Sovereign signature invalid  
- Hash manifest corrupted  
- Canonicalization fails  
- Lineage registry malformed  

---

## II. Recovery Steps

### Step 1 — Canonicalize
```
python3 scripts/canonicalize_json.py artifacts/ canonical/
```

### Step 2 — Rebuild Hash Manifest
```
python3 scripts/compute_hashes.py canonical/ hash_manifest.json
```

### Step 3 — Regenerate Merkle Root
```
python3 scripts/build_merkle_tree.py hash_manifest.json merkle_root.txt
```

### Step 4 — Sovereign Re-Signing
Steward signs:
- `merkle_root.txt`  
- `hash_manifest.json`  

Signature stored in:
- `omni_proof_master.json`

### Step 5 — Lineage Reconciliation
Run:
```
python3 scripts/verify_lineage.py lineage/
```

### Step 6 — Log Recovery Event
```
python3 scripts/update_logbook.py "Root Build Recovery Completed"
```

---

## III. Closing

> “Recovery is the renewal of sovereignty. The chain remembers.”
