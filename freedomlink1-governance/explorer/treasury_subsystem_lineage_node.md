# Treasury Subsystem — Lineage Node
**Freedomlink1 Unified Layer — Constitutional Lineage Graph**  
**Epoch:** 6
**Subsystem:** Treasury
**Graph Identity:** `freedomlink1/subsystem/treasury/epoch/6`
**Seal Commit:** `0bcc2b0`  
**Explorer Commit:** `aa8bd6a`  
**Continuity Index Commit:** `7c14e27`  
**Signature:** GPG commit signatures verified (RSA-4096 key)
**Fingerprint:** `9C607FCB9EB4901C3F8A074B2C5599A6E7720198`

## **1. Node Purpose**
This node records the Treasury Subsystem's Epoch 6 presence in the Freedomlink1 lineage graph. It prepares an epoch transition, aligns continuity surfaces, records continuity events, and acknowledges lineage anchors.

For this entry, **Epoch 6** means the governance period declared by the Epoch 6 Seal. The graph identity names the Treasury Subsystem node within that period.

## **2. Lineage Chain**

| Artifact | Commit | Commit Signature | Status |
| --- | --- | --- | --- |
| Treasury Subsystem Seal | `0bcc2b0` | Good signature from the listed key | Applied |
| Treasury Explorer Entry | `aa8bd6a` | Good signature from the listed key | Applied |
| Treasury Continuity Index | `7c14e27` | Good signature from the listed key | Applied |

## **3. Sovereign Verification**
All listed commits pass local GPG verification with:

- **Primary Key:** RSA-4096
- **Fingerprint:** `9C607FCB9EB4901C3F8A074B2C5599A6E7720198`
- **Capabilities:** `[SC]`

```sh
git show --show-signature 0bcc2b0
git show --show-signature aa8bd6a
git show --show-signature 7c14e27
```

Verification is limited to the cryptographic validity of commit signatures. Local GPG does not certify that the key belongs to the named signer; confirm the fingerprint through a trusted channel when signer identity must be established.

## **4. Treasury Identity and Scope**
The node records declared custody, multisignature, funding, reporting, audit, and epoch-continuity policy. It does not record transaction execution, wallet balances, or completed multisignature approvals.
Economic continuity alignment records the declared economic configuration under treasury governance policy; it does not establish transaction execution or holdings.

## **5. Scope and Authority Boundaries**

- **Deferred authority:** This node records Treasury policy lineage; it does not confer transaction authority or replace required multisignature approval.
- **Runtime boundary:** This document does not establish treasury runtime execution or balances.
- **Autonomous-action boundary:** This document does not perform transactions or other actions on behalf of governance.

> Freedomlink1 Unified Layer
> Treasury Subsystem Lineage Node — Epoch 6