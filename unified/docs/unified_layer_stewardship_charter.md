# ✦ Unified Layer Stewardship Charter
Freedomlink1 Unified Layer • Stewardship Charter

The Unified Layer Stewardship Charter describes the steward role, responsibilities, constraints, and authority boundaries within the Freedomlink1 Institution. Stewards support institutional continuity, verification, governance records, lineage integrity, hardware trust references, economic alignment, and Unified Layer coherence.

This charter states governance expectations. It does not itself appoint a steward, grant authority, or prove that a person is recognized by an on-chain or institutional system.

---

## ✦ Stewardship Overview

**Institution:** Freedomlink1  
**Configured Epoch:** 6 — Continuity Epoch  
**Authority Basis:** Applicable governance instruments and action-specific approval records  
**Verification Surfaces:** [Drift Dashboard](unified_layer_drift_dashboard.md), [Integrity Report](unified_layer_integrity.md)  
**Continuity Surfaces:** [Continuity Report](unified_layer_continuity.md), [Epoch Advancement Document](unified_layer_epoch_advancement.md)  
**Governance Ceremony:** [FL1-C Governance Ceremony](fl1c_governance_ceremony.md)  
**Economic Policy Reference:** [Root Build Economic Continuity Charter](../../docs/root_build_economic_continuity_charter.md)

Stewards are responsible for maintaining accurate institutional records across layers and for distinguishing documented declarations from independently verified behavior.

---

# ✦ 1. Definition of a Steward

A steward is a person assigned responsibilities under applicable institutional governance instruments. Within the scope of those responsibilities, a steward may:

- maintain continuity documentation
- preserve verification boundaries
- prepare or participate in governance ceremonies
- record institutional actions in their authoritative records
- review lineage, identity, and hardware-trust evidence
- maintain economic-alignment documentation
- support Unified Layer coherence

The binding's GovernanceRouter and AccessControl fields are declarations; they do not independently establish a person's appointment, identity, or authority.

---

# ✦ 2. Steward Authority

Within applicable governance instruments and recorded approvals, stewards may have responsibilities to:

### **Governance**

- prepare governance records and initiate reviews
- declare proposed actions and document approval status
- prepare epoch-transition materials

### **Verification**

- run approved local drift checks
- review integrity documentation and generated binding changes
- report verification results within their actual scope

### **Continuity**

- prepare updates to continuity surfaces
- record lineage-aligned events in the designated authoritative records
- maintain documented epoch metadata

### **Documentation**

- prepare institutional documents
- update registries when supported by evidence and approval
- maintain Unified Layer navigation and references

### **Economic**

- maintain treasury-alignment documentation
- review economic-continuity evidence and limitations

This charter does not confer autonomous authority. Each action remains subject to its governing process, required approvals, and applicable controls.

---

# ✦ 3. Steward Responsibilities

Stewards should:

### **1. Preserve Institutional Truth**

Maintain accurate documentation and distinguish declarations from verified facts.

### **2. Maintain Verification**

Run local drift detection when appropriate and review its outputs and side effects. Update integrity documents only when supported by evidence.

### **3. Maintain Continuity**

Record continuity events in authoritative records and update supporting surfaces when their contents change.

### **4. Perform Governance Reviews**

Use the [FL1-C Governance Ceremony](fl1c_governance_ceremony.md) when required by the applicable process. A ceremony documents review; it does not itself authorize or execute an action.

### **5. Maintain Registries**

Update the [Asset Registry](asset_registry.md) and [Module Registry](module_registry.md) when entries are approved and their evidence is documented.

### **6. Maintain Economic Alignment**

Keep treasury documentation aligned with applicable PPTF governance, and avoid presenting declared rules as executed or enforced policy.

### **7. Maintain Hardware Trust References**

Preserve Rootstone-I metadata and record separately any required hardware evidence. A metadata reference is not runtime attestation.

### **8. Maintain Identity Provenance References**

Keep identity metadata accurate and cite the evidence reviewed. Creator-binding metadata alone does not establish each actor's identity or authority.

### **9. Maintain Lineage Integrity**

Review lineage artifacts and preserve authoritative records under the applicable lineage protocol.

### **10. Maintain Unified Layer Coherence**

Keep cross-layer documents consistent while preserving the verification scope of each surface.

---

# ✦ 4. Steward Constraints

Stewards are constrained by the following requirements:

### **1. Governance Authorization**

Authority must be established through applicable governance instruments and action-specific approval evidence. A binding reference to GovernanceRouter does not prove the steward is recognized or authorized.

### **2. Verification Boundaries**

Local checks support claims only about the artifacts and checks they actually cover.

### **3. No Unsupported Runtime Claims**

Do not assert contract behavior, deployment correctness, or chain-state correctness without separately verified evidence.

### **4. No Autonomous Sovereign Actions**

Automation must not be treated as authority. Known repository scripts can mutate the epoch ledger or binding metadata; use and review them according to the applicable governance process and the [Automation Specification](unified_layer_automation_spec.md).

### **5. No Silent Mutations**

Changes to bindings and other authoritative records must be intentional, authorized, reviewed, and recorded.

### **6. Lineage Alignment**

Record actions in lineage only when required and through the authoritative process; do not imply an action is anchored merely because an anchor exists.

### **7. Identity Evidence**

Establish identity and authority from appropriate evidence; do not infer them from a ceremony or metadata flag.

### **8. Hardware Evidence**

Record hardware metadata and attestation separately. A Rootstone-I reference alone does not establish hardware trust for a particular action.

---

# ✦ 5. Steward Interaction with Institutional Layers

### **Governance Layer**

Stewards prepare and review governance actions under the applicable process. Ceremonies document the process but do not replace approval.

### **Lineage Layer**

Stewards review lineage evidence and preserve authoritative event records. Local metadata checks are not a substitute for protocol-required lineage verification.

### **Identity Layer**

Stewards cite relevant identity evidence. This charter does not perform identity attestation.

### **Hardware Layer**

Stewards review Rootstone-I references and separately collected evidence where required. This charter does not perform hardware attestation.

### **Economic Layer**

Stewards review PPTF policy and action-specific approval or execution evidence. Binding consistency flags do not prove treasury operation.

### **Unified Layer**

Stewards maintain verification reports, continuity documents, registries, and navigation, clearly identifying which surfaces are descriptive and which contain authoritative records.

---

# ✦ 6. Steward Verification Duties

### **Run Drift Detection When Appropriate**

From the repository root, and only when approved for the task:

```powershell
python unified/scripts/drift_detector.py
```

The detector checks selected local metadata and lineage artifacts. It writes `unified/reports/fl1c_drift_report.json` and updates `unified_layer.drift_detection.last_check` in `unified/bindings/fl1c_binding.json`. Review the result and generated diff before committing. The detector does not update the dashboard or integrity report and does not verify runtime or deployment behavior.

### **Acknowledge Verification Scope**

Record what was checked and what remains unassessed. A `none_detected` result applies only to the detector's local checks.

### **Update Integrity Surfaces**

Reflect declared and verified configuration separately, and update the report only when supported by the evidence reviewed.

### **Review Policy Gaps**

Stewards should account for:

- the autonomous epoch wrapper's ability to trigger a ledger update from a recommendation
- the drift detector's `last_check` binding mutation

Verification remains subject to steward review and applicable governance approval.

---

# ✦ 7. Steward Continuity Duties

Stewards should:

- update continuity surfaces when relevant information changes
- record epoch transitions in the authoritative records required by governance
- preserve lineage continuity and evidence
- maintain hardware-trust and identity references without overstating attestation
- review economic-continuity evidence and treasury records
- keep supporting documentation aligned with the authoritative record

Continuity work must not convert descriptive documents into substitutes for authoritative records.

---

# ✦ 8. Steward Governance Duties

Use the FL1-C Governance Ceremony when required by the applicable process. The ceremony provides a structured record for:

- recording approval references
- reviewing lineage, identity, hardware, and economic evidence
- documenting local Unified Layer verification and its scope
- identifying action status and follow-up

It does not itself establish authorization, perform attestations, execute actions, or create multi-surface updates. Governance remains an approved human process, not a ritual alone.

---

# ✦ 9. Steward Documentation Duties

Stewards should:

- maintain MkDocs navigation for published documents
- preserve accurate links and evidence scope
- avoid modifying unrelated or untracked files
- review and commit only intended changes
- preserve institutional audit boundaries

Documentation records institutional claims; it does not independently prove them.

---

# ✦ 10. Steward Conduct

Stewards should:

- act intentionally and transparently
- remain within the authority and approval applicable to each action
- preserve continuity and verification boundaries
- distinguish evidence from assertion
- consider economic, lineage, hardware, and identity implications
- record pending matters as pending
- protect unrelated workspace data

Stewardship requires both care for institutional continuity and candor about what is known.

---

# ✦ Closing

The Unified Layer Stewardship Charter describes the steward role and its boundaries within the Freedomlink1 Institution. It supports governance, lineage, identity, hardware-trust, economic-continuity, and Unified Layer stewardship while distinguishing responsibility from authority and documentation from independently verified operation.

Freedomlink1 Unified Layer  
Stewardship Charter — Epoch 6