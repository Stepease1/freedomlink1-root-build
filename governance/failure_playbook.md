# Governance Failure Playbook
## Freedomlink1 — Genesis Epoch

This playbook defines the required actions when any governance pipeline, verification step, or lineage check fails.

---

## I. Failure Categories

### 1. CI/CD Failure
Triggered when:
- Smoke tests fail  
- Governance tests fail  
- Merkle root mismatch  
- Sovereign signature invalid  
- Lineage corruption detected  

### 2. Artifact Failure
Triggered when:
- Hash mismatch  
- Missing artifact  
- Malformed JSON  
- Canonicalization failure  

### 3. Module/POC Failure
Triggered when:
- Module verification fails  
- POC verification fails  
- Registry inconsistency  

---

## II. Immediate Actions

1. Freeze merges into `main`.  
2. Notify custodians via Slack + Email.  
3. Run local governance checks:
  Ctrl+Shift+B → Run Governance Checks
4. Inspect:
- `ci_summary.md`  
- `lineage/governance_logbook.json`  
- GitHub Actions logs  

---

## III. Recovery Actions

1. Re-run verification scripts locally:
```
python3 scripts/verify_lineage.py lineage/
python3 tools/module_verify_all.py
python3 tools/poc_verify_all.py
```
2. Regenerate Merkle root if needed:
```
python3 scripts/build_merkle_tree.py hash_manifest.json merkle_root.txt
```
3. Re-sign sovereign signature if required.  
4. Update logbook:
```
python3 scripts/update_logbook.py "Governance Failure Recovered"
```
---

## IV. Closing

> “Governance failures are lineage events. Recovery is a sovereign act.”
