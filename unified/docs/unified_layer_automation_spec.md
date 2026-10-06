# ✦ Unified Layer Sovereign Automation Specification
Freedomlink1 Unified Layer • Automation Governance Charter

The Unified Layer Sovereign Automation Specification defines the governance boundaries for automation operating within the Freedomlink1 Institution. Automation may assist stewards only within approved scope, with reviewable changes and explicit verification limits.

This specification states policy expectations; it does not itself enforce them. Repository tools must be assessed individually before being treated as compliant.

---

## ✦ Automation Overview

**Institution:** Freedomlink1  
**Configured Epoch:** 6 — Continuity Epoch  
**Automation Authority:** Steward-initiated work under applicable governance instruments  
**Verification Surfaces:** [Drift Detector](../scripts/drift_detector.py), [Integrity Report](unified_layer_integrity.md)  
**Continuity Surfaces:** [Continuity Report](unified_layer_continuity.md), [Epoch Advancement Document](unified_layer_epoch_advancement.md)  
**Registry Surfaces:** [Asset Registry](asset_registry.md), [Module Registry](module_registry.md)

The local binding names GovernanceRouter and other governance components, but this metadata does not establish which human actors are authorized or prove that an automation tool checks their authority. Authorization must come from the applicable governance process.

---

# ✦ 1. Sovereign Automation Principles

Automation operating under this specification must follow these principles:

### **1. Steward Primacy**

Automation acts only on a steward's explicit request and cannot replace required human approval.

### **2. Governance Alignment**

Automation must not interpret a recommendation, metadata flag, or successful local check as governance authorization.

### **3. Continuity Preservation**

Automation must preserve authoritative lineage and institutional records unless a specifically authorized, reviewed procedure requires a change.

### **4. Audit Boundaries**

Automation must state what local artifacts it examines and must not imply that local checks verify external or runtime state.

### **5. Transparency**

Actions and affected files must be reviewable. Changes to authoritative or governance-sensitive files require explicit review before commit.

### **6. Non-Enforcement**

Automation may prepare or check evidence, but must not claim to enforce runtime, deployment, identity, hardware, or treasury guarantees unless a separate verified control provides that enforcement.

---

# ✦ 2. Automation Scope

When explicitly requested by a steward, automation may assist with:

### **Documentation Preparation**

- drafting integration and continuity documents
- preparing registry-entry drafts
- checking local links and references
- proposing updates to steward-facing artifacts

### **Local Verification**

- running approved local metadata checks
- producing scoped, machine-readable reports
- summarizing results without overstating what was checked

### **Continuity and Registry Support**

- preparing epoch-transition materials for review
- drafting asset and module entries
- identifying related documentation that may need review

Automation must not autonomously publish or commit these changes. A steward reviews the proposed diff and decides whether it is accepted.

Automation must not perform or claim to perform:

- contract deployment or execution
- runtime or chain-state verification
- treasury execution
- identity or hardware attestation
- governance authorization
- autonomous epoch advancement
- autonomous drift resolution

---

# ✦ 3. Automation Constraints

### **1. Explicit Initiation**

Automation is run only in response to an explicit steward request. A recommendation or scheduled trigger alone is not authorization for a sovereign action.

### **2. Local-Artifact Verification**

Local tools may report only what their on-disk inputs support. They must disclose missing, failed, and unassessed checks.

### **3. No Runtime Claims**

Metadata checks do not establish contract behavior, deployment correctness, chain state, treasury execution, identity status, or hardware attestation.

### **4. No Autonomous Epoch Advancement**

Automation may prepare evidence but must not advance an epoch without the approvals and signed records required by the [Epoch Advancement Protocol](../../governance/epoch_advancement_protocol.md).

**Known implementation gap:** `scripts/autonomous_epoch_advancement.py` can invoke `scripts/advance_epoch.py` when the intelligence ledger contains a matching recommendation. The target script increments `lineage/epoch_ledger.json` and writes a new epoch with `sovereign_signature` set to `pending`; it does not perform the protocol's required verification or authorization checks. This existing capability does not satisfy this specification. Do not treat a recommendation as approval or use the autonomous wrapper for an authoritative transition without a separately approved, governed control process.

### **5. No Autonomous Registry Modification**

Automation may prepare registry drafts. A steward reviews and commits additions or edits; registry presence is not proof of operational status.

### **6. No Autonomous Drift Resolution**

Automation may identify discrepancies and propose a change. It must not silently alter the underlying declared configuration to make a check pass.

### **7. Binding Metadata Writes**

Bindings are governance-sensitive. The current `unified/scripts/drift_detector.py` has a documented side effect: when run, it writes `unified_layer.drift_detection.last_check` to `unified/bindings/fl1c_binding.json` and writes a drift report. Invoke it only as steward-requested work, inspect the resulting diff, and obtain review before committing. This timestamp write is not evidence that other binding fields may be autonomously changed.

---

# ✦ 4. Automation Interaction with Institutional Layers

### **Governance Layer**

Automation may prepare governance documents and ceremony drafts. It may not authorize actions or execute governance transitions.

### **Lineage Layer**

Automation may check local anchor presence and prepare metadata for review. It may not autonomously write lineage events or modify lineage anchors. Epoch-ledger changes must follow the governing protocol and approval process.

### **Identity Layer**

Automation may reference declared identity metadata. It may not attest identity or change identity provenance.

### **Hardware Layer**

Automation may reference declared Rootstone metadata. It may not perform or claim hardware attestation.

### **Economic Layer**

Automation may prepare treasury documentation. It may not execute treasury actions or claim that declared policy has been enforced.

### **Unified Layer**

Automation may prepare dashboard, integrity, registry, and continuity-document changes for review. It does not automatically synchronize these surfaces. All changes are subject to steward review, and the drift detector's documented `last_check` write is governed by the constraint above.

---

# ✦ 5. Automation Safety Rules

Automation must:

- operate only on steward request
- produce human-reviewable output
- avoid unrelated and untracked workspace files
- avoid runtime and deployment systems
- distinguish declared metadata from verified behavior
- disclose file writes and verification scope
- preserve authoritative records absent explicit approval
- never bypass governance, verification, or continuity requirements

Before accepting automated changes, stewards review the exact file list and diff. Do not stage unrelated or untracked files as part of an automation change.

---

# ✦ 6. Automation Logging Requirements

For material automation work, the steward's review record should identify:

- the initiating steward or request reference
- action timestamp
- affected files
- verification scope and result
- known limitations and unresolved checks
- reviewer and approval decision, where required

Commit messages and documentation updates may reference the work, but are not by themselves proof of authorization or a complete audit log. Use the applicable institutional logbook or governance record where required. Do not claim that automation logs these fields unless the tool actually does so.

---

# ✦ 7. Automation Example Workflow

### **Steward Request**

A steward requests a draft integration document and registry entry for a proposed asset.

### **Automation Output**

Automation prepares the requested drafts, identifies supporting references, and states which checks are available. It does not autonomously change authoritative bindings or lineage records.

### **Steward Review**

The steward reviews the content, evidence, links, verification limits, and exact file diff; missing evidence is recorded rather than inferred.

### **Steward Approval and Commit**

The steward approves the intended files and commits only those files under the applicable governance process.

### **Verification**

An approved local check may be run. Its generated writes are reviewed, and the result is reported within its actual scope. A report or registry entry does not itself authorize sovereign action.

Automation supports preparation and review; it does not replace steward decisions or required governance approvals.

---

# ✦ Closing

The Unified Layer Sovereign Automation Specification defines the intended boundaries for automation across governance, lineage, identity, hardware, economic, and Unified Layer work. It requires steward initiation, reviewable changes, and honest audit scope, while identifying existing tooling that does not yet satisfy these constraints.

Freedomlink1 Unified Layer  
Sovereign Automation Specification — Epoch 6