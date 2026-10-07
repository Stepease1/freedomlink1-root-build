# ✦ Unified Layer Institutional Codex
Freedomlink1 • Institutional Layer Codex

The Unified Layer Institutional Codex is a consolidated reference to the declared architecture, governance expectations, and verification boundaries of the Freedomlink1 Institution. It connects governance, lineage, identity, hardware trust, economic continuity, verification, continuity, automation, stewardship, registries, and temporal governance.

This codex is an index and interpretive overview, not a substitute for governing instruments, signed decisions, authoritative lineage records, or action-specific evidence. Where descriptions differ, applicable law, approved governance instruments, and authoritative records control. Inclusion in this document does not establish that a system is deployed, operational, or independently verified.

---

## ✦ Institutional Overview

**Institution:** Freedomlink1  
**Configured Epoch:** 6 — Continuity Epoch  
**Institutional Layers:** Governance, lineage, identity, hardware trust, economic continuity, Unified Layer, verification, continuity, automation, stewardship, registries, and temporal governance

Institutional configuration is represented by declared metadata, steward-maintained documentation, and authoritative records. Each source must be read within its stated verification scope.

---

# ✦ 1. Sovereign Principles

The following principles summarize expectations across the institutional documentation:

### **1. Steward Primacy**

Authority requires action-specific approval evidence under applicable governance instruments.

### **2. Lineage Continuity**

Required institutional events are recorded through the applicable authoritative lineage process.

### **3. Identity Provenance**

Identity claims require appropriate evidence; metadata declarations alone do not attest an actor.

### **4. Hardware Trust**

Rootstone-I is the declared hardware identity reference. Metadata does not establish physical device identity or runtime attestation.

### **5. Economic Continuity**

Economic actions follow applicable PPTF policy and approval records. Declared configuration does not prove treasury execution.

### **6. Verification Boundaries**

Verification claims are limited to the artifacts and checks actually examined.

### **7. Continuity Preservation**

Epoch transitions follow the governing protocol and preserve required records and approvals.

### **8. Documentation Integrity**

Documentation distinguishes declared configuration from verified evidence and unresolved questions.

### **9. Automation Constraints**

Automation may assist with preparation and scoped checks but is not itself governance authority.

### **10. Audit Boundaries**

No local report implies runtime enforcement, deployment correctness, or chain-state validation unless supported by separate evidence.

---

# ✦ 2. Governance Layer

Governance actions are subject to applicable instruments and action-specific approval records.

### **Governance Authority**

Bindings name GovernanceRouter and AccessControl, but those declarations do not establish an individual's authority or verify a particular approval.

### **Governance Ceremony**

The [FL1-C Governance Ceremony](../unified/docs/fl1c_governance_ceremony.md) provides a structured review record. It does not itself grant authority, approve an action, or execute it.

### **Governance Constraints**

- ceremonies do not grant authority
- drift checks do not grant authority
- documentation does not grant authority
- approval status must be supported by authoritative evidence

---

# ✦ 3. Lineage Layer

Lineage artifacts support institutional continuity and temporal records.

### **Lineage References**

The FL1-C binding declares `lineage/FL1C_anchor.json`; the resolved workspace artifact is [`freedomlink1-root/lineage/FL1C_anchor.json`](../freedomlink1-root/lineage/FL1C_anchor.json). Declared and resolved paths should not be conflated.

### **Lineage Duties**

Stewards review lineage evidence and record events through the applicable authoritative process. An existing anchor does not prove later actions have been recorded.

### **Lineage Constraints**

Local metadata comparisons do not verify runtime behavior or replace protocol-required lineage and Merkle-root checks.

---

# ✦ 4. Identity Layer

Identity metadata describes declared identity relationships and provenance references.

### **Identity Duties**

Stewards cite appropriate identity evidence for relevant actors and actions. The FL1-C creator-binding declaration does not attest each later steward, minter, or recipient.

### **Identity Constraints**

Metadata presence does not perform identity attestation or establish governance authority.

---

# ✦ 5. Hardware Trust Layer

Rootstone-I is the institution's declared hardware identity reference.

### **Hardware Metadata**

The workspace contains [`artifacts/rootstone-identity.json`](../artifacts/rootstone-identity.json), FL1-C binding fields, and a Rootstone marker in the local lineage artifact. Their presence does not establish a physical device's identity or condition.

### **Hardware Review**

Stewards record the specific metadata or separately collected attestation evidence reviewed. Ceremonial acknowledgment does not invoke hardware or perform attestation.

### **Hardware Constraints**

- no runtime hardware attestation is performed by the local drift detector
- metadata does not enforce contract execution
- a hardware reference does not prove an action was device-backed

See the [Rootstone-I Hardware Trust Charter](../unified/docs/rootstone_hardware_trust_charter.md).

---

# ✦ 6. Economic Continuity Layer

Economic policy and treasury action are governed by the applicable PPTF instruments and action-specific evidence.

### **Economic Duties**

Stewards maintain treasury alignment documentation and review relevant approvals, execution records, and continuity evidence.

### **Economic Constraints**

The FL1-C binding declares PPTF alignment and minting policy. The [FL1-C Treasury Integration Rules](governance/FL1C-treasury-integration.md) describe the boundary between those declarations and contract behavior. The drift detector does not verify treasury execution or supply policy.

See the [Root Build Economic Continuity Charter](root_build_economic_continuity_charter.md).

---

# ✦ 7. Unified Layer

The Unified Layer organizes declared integration metadata and steward-maintained reference surfaces.

### **Unified Layer Components**

- asset and module registries
- continuity and integrity documents
- drift reports and dashboards
- governance and integration references
- automation and stewardship policies

The [Unified Layer Explorer](unified/explorer.md) describes the integration model. These surfaces provide documentation and visibility; they do not independently establish operational synchronization.

---

# ✦ 8. Verification Layer

Verification is scoped to the tool and evidence used.

### **Drift Detector**

The [local FL1-C drift detector](../unified/scripts/drift_detector.py) compares selected binding metadata with an available lineage artifact, checks declared governance and identity/hardware fields, and checks whether consistency flags are enabled. It does not test every domain's operation or validate runtime, deployment, chain, treasury, identity-attestation, or hardware-attestation state.

### **Binding Mutation**

When run, the detector updates `last_check` in the FL1-C binding and writes a machine-readable report. Review the generated diff; the timestamp is not proof of economic, hardware, or end-to-end verification.

### **Integrity Report**

The [Unified Layer Integrity Report](../unified/docs/unified_layer_integrity.md) is a scoped static review of declared and locally checked configuration.

---

# ✦ 9. Continuity Layer

Continuity documents provide supporting descriptions of institutional evolution.

### **Continuity Surfaces**

- [Continuity Report](../unified/docs/unified_layer_continuity.md)
- [Epoch Advancement Document](../unified/docs/unified_layer_epoch_advancement.md)
- [Drift Dashboard](../unified/docs/unified_layer_drift_dashboard.md)
- [Integrity Report](../unified/docs/unified_layer_integrity.md)

Update supporting surfaces when relevant evidence or records change. They are not substitutes for authoritative governance, treasury, or lineage records and are not automatically synchronized by the detector.

---

# ✦ 10. Automation Layer

Automation may prepare documents, registry drafts, continuity metadata, and scoped verification reports for steward review.

### **Automation Constraints**

- recommendations and metadata do not grant authority
- local tools cannot claim runtime or chain-state verification
- registry and continuity edits require review
- automation must not be treated as approval to advance an epoch

**Known implementation gap:** `scripts/autonomous_epoch_advancement.py` can call `scripts/advance_epoch.py` based on a recommendation. The target script mutates the epoch ledger without performing the governing protocol's authorization and verification sequence. The [Sovereign Automation Specification](../unified/docs/unified_layer_automation_spec.md) documents this gap; do not treat the wrapper as compliant or as evidence of approved advancement.

---

# ✦ 11. Stewardship Layer

Stewards maintain institutional records within responsibilities established by applicable governance instruments.

### **Steward Duties**

- maintain accurate documentation and navigation
- review local verification results and side effects
- preserve lineage and continuity records
- use governance ceremonies when required by process
- maintain registries when approved and evidence is available
- keep hardware, identity, and economic claims within their evidence scope

The [Stewardship Charter](../unified/docs/unified_layer_stewardship_charter.md) describes these responsibilities. This codex does not appoint stewards or confer authority.

---

# ✦ 12. Registry Layer

Registries index declared institutional assets and modules.

### **Asset Registry**

The [Unified Layer Asset Registry](../unified/docs/asset_registry.md) records assets represented in local metadata and documentation. Inclusion is not proof of legal recognition or deployed operation.

### **Module Registry**

The [Unified Layer Module Registry](../unified/docs/module_registry.md) records modules and their declared roles, with local verification limits.

Registry edits should identify supporting evidence and distinguish metadata declarations from operational status.

---

# ✦ 13. Temporal Governance Layer

Epochs define the institution's declared temporal structure.

### **Epoch Advancement**

Advancement is governed by the [Epoch Advancement Protocol](../governance/epoch_advancement_protocol.md), including its required checks, authoritative records, signatures, and Merkle-root requirements. The Unified Layer [Epoch Advancement Document](../unified/docs/unified_layer_epoch_advancement.md) summarizes cross-layer review expectations and does not replace that protocol.

### **Epoch Constraints**

- recommendations alone do not authorize advancement
- local drift checks do not establish complete continuity verification
- hardware metadata or invocation alone is not hardware attestation
- epoch-ledger changes require the applicable governance process and records

---

# ✦ Closing

The Unified Layer Institutional Codex brings together the declared architecture and governance references of Freedomlink1. It supports review across governance, lineage, identity, hardware trust, economic continuity, verification, continuity, automation, stewardship, registries, and temporal governance while preserving the authority of underlying instruments and the limits of available evidence.

Freedomlink1 Unified Layer  
Institutional Codex — Epoch 6