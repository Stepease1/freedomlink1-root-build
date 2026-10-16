# Rootstone-I Hardware Governance — Continuity Index
**Freedomlink1 Unified Layer — Constitutional Continuity Registry**  
**Epoch:** 6
**Subsystem:** Rootstone-I Hardware Governance
**Seal Commit:** `9a91859`  
**Explorer Commit:** `22edba9`  
**Signature:** GPG commit signatures verified (RSA-4096 key)
**Fingerprint:** `9C607FCB9EB4901C3F8A074B2C5599A6E7720198`

## **1. Purpose**
This index binds the Rootstone-I Seal and Explorer Entry into a recorded Epoch 6 lineage chain. It prepares an epoch transition, aligns continuity surfaces, records continuity events, and acknowledges lineage anchors.

## **2. Lineage Chain**

| Artifact | Commit | Commit Signature | Status |
| --- | --- | --- | --- |
| Rootstone-I Hardware Governance Seal | `9a91859` | Good signature from the listed key | Applied |
| Rootstone-I Explorer Entry | `22edba9` | Good signature from the listed key | Applied |

## **3. Continuity Rules**
The Rootstone-I Seal requires continuity and references Editorial, Treasury, Agency, and SCL. This index preserves those declared dependencies and the Seal-to-Explorer lineage; it does not establish that the dependent subsystem records are complete.

For this entry, **Epoch 6** means the governance period declared by the Epoch 6 Seal. Hardware trust invocation records declared hardware identity and physical sovereignty binding; Rootstone-I identity is declared, not attested.

## **4. Sovereign Verification**
Both commits pass local GPG signature verification with:

- **Primary Key:** RSA-4096
- **Fingerprint:** `9C607FCB9EB4901C3F8A074B2C5599A6E7720198`
- **Capabilities:** `[SC]`

```sh
git show --show-signature 9a91859
git show --show-signature 22edba9
```

Verification is limited to the cryptographic validity of commit signatures. Local GPG does not certify that the key belongs to the named signer; confirm the fingerprint through a trusted channel when signer identity must be established. Commit-signature verification is not physical hardware attestation.

## **5. Scope and Authority Boundaries**

- **Deferred authority:** This index records declared hardware-governance lineage; it does not grant authority or establish physical attestation.
- **Runtime boundary:** This document does not establish hardware runtime behavior.
- **Autonomous-action boundary:** This document does not perform actions on behalf of governance.

> Freedomlink1 Unified Layer
> Rootstone-I Hardware Governance Continuity Index — Epoch 6