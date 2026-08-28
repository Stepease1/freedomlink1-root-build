# Ceremony Checklist Template
Purpose: Standard checklist to record procedures, artifacts, and verification for governance ceremonies (activation, promotion, retirement, succession, epoch advancement).

Audience: Steward, Custodians, Sentinel operators, Recorders.

Checklist
1. Preparation
   - Confirm ceremony type and justification
   - Notify custodians and sentinels (Slack + Email)
   - Schedule time and designate recorder
   - Ensure required artifacts exist (merkle_root.txt, hash_manifest.json, relevant artifacts)

2. Pre-Verification
   - Run: `python3 scripts/validate_epoch_ledger.py` (if epoch-related)
   - Run: `python3 scripts/integrity_monitor.py`
   - Run: `python3 scripts/lineage_diff.py` to detect drift
   - Confirm signatures and hashes are present and valid

3. Ceremony Execution
   - Read invocation and present the subject (e.g., Sentinel ID, Module ID, Steward identity)
   - Perform required script actions:
     - Activation/Promotion/Retirement: update registry via `scripts/update_sentinel_registry.py` or `scripts/retire_module.py`
     - Succession: `python3 scripts/update_steward_registry.py "Name" "<pubkey>" "<fingerprint>"`
     - Epoch advancement: `python3 scripts/advance_epoch.py`
   - Steward signs artifacts (manual step): `merkle_root.txt`, `hash_manifest.json`, `epoch_ledger.json`

4. Post-Ceremony (Recorder)
   - Update `lineage/*` registries as required
   - Run: `python3 scripts/build_merkle_tree.py hash_manifest.json merkle_root.txt`
   - Update `artifacts/omni_proof_master.json` with new signature (manual)
   - Run: `python3 scripts/update_logbook.py "<Ceremony> Completed: details..."`
   - Run integrity monitor once more: `python3 scripts/integrity_monitor.py`

5. Artifacts to attach
   - Ceremony minutes (text/markdown)
   - Signed artifacts (paths)
   - Commit/PR URL and run logs
   - Updated registries and snapshots (`lineage/last_integrity_snapshot.json`)

6. Approvals
   - Steward signature (required)
   - Custodian confirmations (list names)
   - Sentinel validation (if automated)

7. Publication
   - Commit changes and push to `main` via PR with the ceremony checklist attached
   - Publish governance_logbook entry and link to PR

Example commands
```
python3 scripts/lineage_diff.py
python3 scripts/update_logbook.py "Sentinel GS-03 Activated by Steward"
git add lineage/* artifacts/* && git commit -m "Ceremony: Activate GS-03" && git push
```

Notes
- Preserve manual signature steps as human actions — they must remain auditable.
- Keep this checklist inside the PR so auditors can verify ceremony compliance.
