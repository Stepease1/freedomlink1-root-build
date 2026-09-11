# Rootstone-I Identity Tile  
**Hardware Sovereignty Anchor — Freedomlink1**

Rootstone-I is the hardware root of trust for Freedomlink1.  
This identity tile provides a concise, public representation of its sovereign identity.

---

## Identity Summary

**Name:** Rootstone-I  
**Role:** Hardware Sovereignty Anchor  
**Epoch:** 3 — Expansion & Autonomy  
**Lineage:** Sovereign Genesis  
**Institution:** Freedomlink1  

---

## Hardware Identity Embed

**Artifact:**  
[artifacts/rootstone-identity.json](../artifacts/rootstone-identity.json)

Contains:

- RSA-4096 public key  
- 512-byte signature  
- Sovereign manifest  
- Hardware governance flags  
- Epoch and lineage metadata  

---

## Governance Flags

- **immutable:** true  
- **verify_on_boot:** true  
- **verify_on_epoch_advance:** true  
- **allow_external_replacement:** false  

These flags define Rootstone-I's behavior as a hardware governance anchor.

---

## Signature Integrity

- **Encoding:** Base64  
- **Length:** 684 characters  
- **Decoded:** 512 bytes  
- **Algorithm:** RSA-4096  
- **Verification:** Passed  

Rootstone-I's identity is cryptographically anchored and verified.

---

## Sovereign Context

Rootstone-I completes Freedomlink1's tri-root governance system:

1. **Creator Seal** — Identity Root  
2. **PPTF Identity Anchor** — Economic Root  
3. **Codex Genesis Node** — Lineage Root  
4. **Rootstone-I Identity Embed** — Hardware Root  

Together, these form the foundation of Epoch 3.

---

## Verification

Verification engine:  
[verifyCreatorSeal.ts](../artifacts/verifyCreatorSeal.ts)

All checks passed during the Epoch 3 Expansion Release.

---

## Closing

Rootstone-I is the physical anchor of Freedomlink1's sovereignty.  
Its publication in Epoch 3 marks the completion of the institution's hardware identity foundation.
