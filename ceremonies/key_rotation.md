# Sovereign Key Rotation Ceremony
## Freedomlink1 — Genesis Epoch

This ceremony governs the rotation of the steward’s sovereign signing key.

---

## I. Opening Invocation

> “We gather to rotate the sovereign key that protects the lineage of Freedomlink1.”

---

## II. Presentation of the New Key

Custodian presents:
- New public key  
- Key fingerprint  
- Key lineage entry  

---

## III. Revocation of Old Key

Steward declares:
> “The previous sovereign key is hereby retired and shall no longer sign lineage artifacts.”

Old key is moved to:
`lineage/retired_keys/`

---

## IV. Activation of New Key

Steward signs:
- `merkle_root.txt`  
- `hash_manifest.json`  
- `epoch_ledger.json`

New key stored in:
`artifacts/omni_proof_master.json`

---

## V. Publication

Custodians publish:
- Updated proof master  
- Updated lineage  
- Updated governance logbook  

---

## VI. Closing Seal

> “Let this key guard continuity, justice, and sovereignty. The chain remembers.”
