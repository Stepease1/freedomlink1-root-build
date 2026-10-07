# ✦ Rootstone-I Hardware Trust Charter
Freedomlink1 Unified Layer • Hardware Trust Charter

The Rootstone-I Hardware Trust Charter describes the declared role of hardware identity within the Freedomlink1 Institution. It sets policy expectations for hardware-related metadata, stewardship, and evidence across governance, lineage, identity, economic, and Unified Layer concerns.

The presence of Rootstone-I metadata does not establish the identity or condition of a physical device, perform attestation, or prove runtime enforcement.

---

## ✦ Hardware Trust Overview

**Institution:** Freedomlink1  
**Configured Epoch:** 6 — Continuity Epoch  
**Declared Hardware Reference:** Rootstone-I  
**Verification Surfaces:** [Drift Dashboard](unified_layer_drift_dashboard.md), [Integrity Report](unified_layer_integrity.md)  
**Continuity Surfaces:** [Continuity Report](unified_layer_continuity.md), [Epoch Advancement Document](unified_layer_epoch_advancement.md)  
**Governance Ceremony:** [FL1-C Governance Ceremony](fl1c_governance_ceremony.md)  
**Stewardship Reference:** [Unified Layer Stewardship Charter](unified_layer_stewardship_charter.md)

Hardware trust is an institutional policy concept supported by declared metadata and, where separately collected, hardware evidence. The local artifacts described here do not themselves prove physical sovereignty.

---

# ✦ 1. Definition of Rootstone-I

Rootstone-I is the institution's declared hardware identity reference. The workspace includes a Rootstone identity artifact at [`artifacts/rootstone-identity.json`](../../artifacts/rootstone-identity.json), which contains a public key, signature field, manifest, and hardware flags. The FL1-C binding names `RootstoneBinding`, `rootstone.bind(msg.sender)`, and Rootstone-I; the local FL1-C lineage anchor records `rootstone: "bound"`.

These artifacts describe the intended hardware relationship. This charter does not validate the artifact signature, establish that a physical device possesses the corresponding key, or prove that a hardware binding occurred for a particular governance or economic action.

---

# ✦ 2. Hardware Trust Principles

The following are policy requirements for hardware-related claims:

### **1. Physical Identity**

Claims about a specific physical device require evidence that links the device to the declared Rootstone-I identity. A metadata label alone is insufficient.

### **2. Steward Review**

Stewards review and record relevant hardware metadata and any separately collected evidence. A ceremony statement does not invoke hardware or perform attestation.

### **3. Continuity Anchoring**

Where required by policy, hardware-related events should be recorded in the appropriate authoritative lineage process. A genesis anchor marker does not establish later action records.

### **4. Identity Provenance**

Hardware evidence and actor identity are separate concerns. A hardware reference does not establish the identity or authority of a steward.

### **5. Economic Alignment**

Hardware requirements for economic actions must come from applicable governance and treasury policy. A Rootstone-I reference does not demonstrate treasury approval or execution.

### **6. Scoped Verification**

Verification reports must state exactly which local fields and artifacts were examined and must not imply hardware attestation where none occurred.

---

# ✦ 3. Hardware Trust Components

### **Hardware Identity Artifact**

The local Rootstone identity artifact contains declared identity material and flags. Its contents should be reviewed under the applicable cryptographic verification procedure before making integrity claims.

### **FL1-C Binding Metadata**

[`fl1c_binding.json`](../bindings/fl1c_binding.json) declares the RootstoneBinding reference, hardware identity expression, and trust-anchor name. These are configuration fields, not proof of a successful runtime binding.

### **Lineage Marker**

The resolved local [FL1-C lineage anchor](../../freedomlink1-root/lineage/FL1C_anchor.json) includes a Rootstone `bound` marker. This is a local record value, not a device attestation or proof of later hardware use.

### **Steward Review**

Stewards record which metadata or separately collected hardware evidence they reviewed, along with its scope and limitations.

### **Continuity Documentation**

Continuity and integrity documents may reference hardware metadata and review status. They do not automatically create or synchronize hardware evidence.

---

# ✦ 4. Hardware Trust Invocation

When required by a governance process, a steward may record the following acknowledgment with its evidence reference:

> I reviewed the Rootstone-I hardware evidence identified in this record and noted its verification scope. This acknowledgment does not itself invoke hardware, attest a device, authorize the governance action, or prove runtime behavior.

Use the [FL1-C Governance Ceremony](fl1c_governance_ceremony.md) to document the broader action review. Do not use ceremonial language as a substitute for an actual hardware operation or attestation.

---

# ✦ 5. Hardware Trust Verification

### **Local Metadata Review**

Review the FL1-C binding and resolved lineage artifact. Record which files were checked and whether their metadata matches the intended configuration.

### **Drift Detection**

The local [drift detector](../scripts/drift_detector.py) checks that required hardware binding fields are present and that the resolved lineage anchor's Rootstone marker is `bound`. It does not inspect `artifacts/rootstone-identity.json`, validate its signature, communicate with a device, or perform physical or runtime attestation.

### **Integrity Reporting**

The [Unified Layer Integrity Report](unified_layer_integrity.md) is a scoped static review. State separately whether the identity artifact's signature or any hardware evidence was validated; do not infer those checks from the drift result.

### **Continuity Reporting**

The [Continuity Report](unified_layer_continuity.md) may document declared hardware continuity. It is not an authoritative record of each hardware-backed action unless the relevant event is actually recorded there under the governing process.

All verification claims are limited to the specific evidence reviewed. Local metadata checks do **not** perform hardware attestation or verify runtime and deployment behavior.

---

# ✦ 6. Hardware Trust Constraints

### **1. No Runtime Attestation Claim**

Do not describe Rootstone-I metadata as proof of live device state or runtime attestation.

### **2. No Implied Enforcement**

A hardware reference does not establish enforcement of contract execution or governance rules.

### **3. No Ceremonial Substitution**

Steward acknowledgment records a review; it does not perform a hardware operation or confer authority.

### **4. No Silent Mutations**

Hardware-related metadata changes require the applicable authorization, review, and recorded diff.

### **5. Lineage and Identity Separation**

Keep hardware, lineage, and actor-identity evidence distinct. One metadata marker does not prove the others.

### **6. Economic Evidence**

Economic actions require their applicable treasury and governance evidence; hardware metadata alone does not establish economic authorization or continuity.

---

# ✦ 7. Hardware Trust Interaction with Institutional Layers

### **Governance Layer**

Governance processes may require hardware evidence, but Rootstone-I metadata does not authorize a steward or action.

### **Lineage Layer**

Lineage artifacts may record declared hardware markers. Review the authoritative event record for the action in question.

### **Identity Layer**

Hardware identity and human identity are separate evidence domains and must not be conflated.

### **Economic Layer**

Hardware requirements for treasury actions are determined by applicable policy; this charter does not verify treasury operation.

### **Unified Layer**

Bindings, drift reports, integrity documents, and continuity documents provide scoped metadata and documentation references, not live hardware state.

---

# ✦ 8. Steward Hardware Duties

Stewards should:

- preserve Rootstone-I metadata and identify its source
- cite the specific artifact or evidence reviewed
- use the drift detector only for its documented local checks
- inspect and report signature-validation results separately
- update integrity and continuity documents only when supported by evidence
- record hardware evidence required for the applicable governance action
- keep actor identity, hardware identity, and lineage records distinct
- review and record authorized metadata changes

Hardware stewardship requires accurate scope statements, not merely the presence of a hardware reference.

---

# ✦ 9. Hardware Trust Across Epochs

For an epoch transition, applicable governance may require review of:

- governance approval and signatures
- authoritative lineage records
- actor identity evidence
- Rootstone-I metadata and any required device attestation
- treasury requirements where relevant
- local drift and integrity results within their stated scope
- continuity documentation

The Epoch Advancement Protocol remains authoritative. A passing local hardware-marker check does not satisfy an independent hardware-attestation requirement or authorize an epoch transition.

---

# ✦ Closing

The Rootstone-I Hardware Trust Charter defines the intended role of hardware identity references within Freedomlink1 and the evidence boundaries for claims made about them. It supports governance, lineage, identity, economic continuity, and Unified Layer review without equating local metadata with physical or runtime attestation.

Freedomlink1 Unified Layer  
Rootstone-I Hardware Trust Charter — Epoch 6