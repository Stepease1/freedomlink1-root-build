# ✦ Unified Layer Verification Codex
Freedomlink1 Unified Layer • Verification Doctrine

The Unified Layer Verification Codex describes the principles, responsibilities, constraints, and interpretation rules for verification across the Freedomlink1 Institution. It distinguishes local metadata checks from independent evidence and operational testing.

Verification can support institutional truth by stating what was checked and what was not. A local result does not validate runtime behavior, chain-state correctness, deployment, or economic execution, and it does not grant governance authority.

---

## ✦ Verification Overview

**Institution:** Freedomlink1  
**Configured Epoch:** 6 — Continuity Epoch  
**Verification Surfaces:** [Drift Detector](../unified/scripts/drift_detector.py), [Integrity Report](../unified/docs/unified_layer_integrity.md), FL1-C binding metadata  
**Continuity Surfaces:** [Continuity Report](../unified/docs/unified_layer_continuity.md), [Epoch Advancement Document](../unified/docs/unified_layer_epoch_advancement.md)  
**Authority Evidence:** Applicable governance instrument and action-specific approval records  
**Local Detector Scope:** Selected metadata and on-disk lineage artifact checks

Verification should be intentional, steward-reviewed, and limited to the evidence and method actually used. Other audit or technical procedures may have broader scopes when separately authorized and documented.

---

# ✦ 1. Verification Principles

Verification under this local Unified Layer doctrine follows eight principles:

### **1. Evidence-Specific Claims**

Describe the artifacts, versions, and checks examined. Do not generalize a narrow result to untested systems.

### **2. No Unsupported Runtime Claims**

Local documentation and metadata checks do not validate contract behavior, deployment correctness, or chain state.

### **3. No Authority Claims**

Verification does not grant governance authority or establish action approval.

### **4. Steward Review**

Local checks are initiated and reviewed under the applicable process. Automation may execute a bounded check when explicitly requested; it must not operate as autonomous authority.

### **5. Continuity Support**

Verification may inform continuity review but does not perform or authorize a transition.

### **6. Hardware Trust Boundaries**

Hardware metadata is a declaration, not physical or runtime attestation.

### **7. Economic Boundaries**

Economic metadata describes declared policy; it does not establish treasury execution or economic correctness.

### **8. Transparent Limitations**

Report failed, unknown, and untested conditions alongside passing local checks.

---

# ✦ 2. Verification Surfaces

### **Drift Detector**

The local FL1-C detector compares selected binding and lineage fields, checks required governance, identity, and hardware metadata, and tests whether declared cross-layer consistency flags are enabled.

When run, it updates `last_check` in `unified/bindings/fl1c_binding.json` and writes `unified/reports/fl1c_drift_report.json`. This is a file mutation; review the command result and diff. The detector does not inspect deployed systems, validate hardware identity artifacts, or execute economic policy.

### **Integrity Report**

The [Integrity Report](../unified/docs/unified_layer_integrity.md) documents declared configuration, local checks, and their limitations. It is steward-maintained documentation, not an enforcement mechanism.

### **Binding Metadata**

Binding metadata records declared configuration and the detector's `last_check` timestamp. That timestamp records when the detector ran; it does not establish that every field or institutional layer was independently verified.

These surfaces preserve an auditable account of local declarations and checks, not runtime correctness.

---

# ✦ 3. Verification Responsibilities

Stewards should:

- run the local detector intentionally when appropriate
- review its result and generated binding mutation
- update integrity documentation only when supported by evidence
- describe the actual verification scope
- preserve audit boundaries and source references
- avoid autonomous or scheduled checks being treated as governance approval
- report unknown and untested areas without implying they passed

Verification is a steward-reviewed activity; the tools themselves do not provide steward authority.

---

# ✦ 4. Verification Constraints

The local detector and the surfaces described here have these limits:

### **1. Local-Artifact Scope**

They inspect selected repository artifacts and metadata, not every institutional artifact or external source.

### **2. No Runtime Verification**

They do not inspect deployed system behavior.

### **3. No Chain-State Verification**

They do not query or validate blockchain state.

### **4. No Hardware Attestation**

They do not attest physical hardware or live device state.

### **5. No Economic Execution Claims**

They do not verify treasury approval or execution, supply behavior, or runtime economics.

### **6. No Autonomous Authority**

An automated check may run only within its approved invocation and scope; a result alone is not an institutional decision.

### **7. No Authority Inference**

Verification does not appoint a steward, establish authorization, or substitute for approval evidence.

---

# ✦ 5. Verification Interaction with Governance

Verification may support governance by providing scoped local observations and documentation for steward review.

It does not:

- grant authority or approve an action
- validate governance execution or contract behavior
- establish that a named actor is authorized
- validate chain-state governance

Governance authority depends on the applicable instrument and action-specific approval evidence. A successful local check is not approval.

---

# ✦ 6. Verification Interaction with Lineage

The detector compares selected declared lineage event and epoch fields with a resolved local anchor. This can identify specific metadata mismatches in the checked artifacts.

It does not:

- validate runtime or chain-state lineage
- establish continuity in external lineage systems
- prove that later events were recorded
- replace protocol-required lineage, signature, or Merkle-root checks

Lineage records define institutional history within their stated authority and evidence scope; a local anchor is not runtime history.

---

# ✦ 7. Verification Interaction with Identity

The detector checks required identity binding fields and a creator-bound marker in the local anchor.

It does not:

- perform identity attestation
- validate external identity systems
- establish each actor's identity or authority
- validate runtime identity behavior

Identity metadata describes declared provenance, not external identity verification.

---

# ✦ 8. Verification Interaction with Hardware Trust

The detector checks that hardware binding fields are present and that the resolved lineage anchor contains the expected `bound` marker.

It does not:

- inspect or validate the Rootstone-I identity artifact's signature
- identify or communicate with a physical device
- perform hardware attestation
- validate runtime hardware behavior

Hardware verification claims must distinguish local metadata review from physical or runtime attestation.

---

# ✦ 9. Verification Interaction with Economic Continuity

The detector checks that the declared economic consistency flag is enabled as part of the cross-layer flags.

It does not:

- validate the economic policy values
- verify treasury approval or execution
- verify supply behavior or chain-state economics
- prove economic continuity across epochs

Economic metadata describes declared configuration and policy, not runtime economics.

---

# ✦ 10. Verification Interaction with Automation

Automation may run a scoped local check when explicitly initiated and reviewed by a steward. It may produce reports and documented side effects; those outputs must be examined before they are relied upon.

Automation must not be treated as:

- autonomous governance approval
- authority to resolve drift by silently changing declarations
- permission to modify registries or authoritative records
- authorization to advance epochs

**Known implementation gap:** the repository's autonomous epoch wrapper can invoke an epoch-ledger update script based on a recommendation, without performing the governing protocol's authorization and verification sequence. The drift detector also writes `last_check` to the binding. These behaviors are documented policy gaps, not evidence that the automation constraints are technically enforced.

---

# ✦ 11. Verification Interaction with Registries

Verification can compare registry entries with the local references and evidence explicitly checked.

It does not:

- validate live or deployed registry state
- validate external registry systems
- establish legal recognition or operational status
- prove chain-state correctness

Registries index declared institutional structure; inclusion is not operational verification.

---

# ✦ 12. Verification Interaction with Epoch Transitions

Local results may inform preparation and review of an epoch transition, alongside the evidence required by the [Epoch Advancement Protocol](../governance/epoch_advancement_protocol.md).

Verification does not:

- perform or authorize epoch transitions
- establish completion of protocol preconditions by itself
- validate runtime epoch behavior
- substitute for approval, signatures, lineage records, or Merkle-root evidence

The local drift detector does not block a transition or enforce a freshness threshold for its timestamp.

---

# ✦ 13. Verification Conduct

Stewards and reviewers should:

- act intentionally and transparently
- state which artifacts and versions were examined
- preserve approval and authority evidence requirements
- maintain continuity and lineage boundaries
- distinguish hardware metadata from attestation
- distinguish identity declarations from identity evidence
- distinguish economic policy declarations from execution
- disclose automation side effects and limitations
- preserve source artifacts and report contradictory or unresolved results

Verification is disciplined evidence handling, not a claim broader than the work performed.

---

# ✦ Closing

The Unified Layer Verification Codex describes the local verification doctrine of the Freedomlink1 Institution. It supports review across governance, lineage, identity, hardware trust, economic continuity, automation, registries, and epoch transitions while preserving the distinction between local metadata checks and independently verified operational behavior.

Freedomlink1 Unified Layer  
Verification Codex — Epoch 6