# ✦ Unified Layer Auditor's Handbook
Freedomlink1 Unified Layer • External Verification Guide

The Unified Layer Auditor's Handbook describes how to interpret the institution's local configuration, steward-maintained documentation, and verification artifacts. It identifies what those materials establish and what remains outside their scope.

This handbook does not grant an auditor access or authority, restrict independent audit procedures, or replace the terms of an engagement or applicable law. Independent runtime, deployment, contract, or chain-state work requires separate scope, access, and evidence; it is not performed by the local-documentation checks described here.

---

## ✦ Auditor Overview

**Institution:** Freedomlink1  
**Configured Epoch:** 6 — Continuity Epoch  
**Guide Scope:** Local artifacts and steward-maintained documentation  
**Primary Authority Evidence:** Applicable governance instrument and action-specific approval record  
**Institutional Surfaces:** Governance, continuity, verification, lineage, identity, hardware trust, economic continuity, and registries

Auditors should distinguish declared configuration, supporting documentation, authoritative records, and independently verified operational evidence.

---

# ✦ 1. Auditor Mandate and Scope

Within an agreed audit scope, an auditor may examine the relevant artifacts and records, including:

- declared configuration and steward-maintained documentation
- continuity and verification surfaces
- lineage anchors and authoritative event records
- identity and hardware metadata, with appropriate safeguards
- economic policy declarations and treasury records made available
- governance ceremonies and approval evidence
- automation constraints and registries

This handbook is an interpretation guide, not an authorization to access systems or modify institutional records. Auditor access, testing methods, confidentiality, and evidence handling are set by the engagement and applicable law. Preserve originals and record any separately collected evidence without representing it as part of the local checks.

---

# ✦ 2. Verification Boundaries

The current Unified Layer verification artifacts describe local metadata and on-disk checks. They do not, by themselves, verify:

- contract runtime behavior or deployed bytecode
- deployment correctness or live chain state
- external governance decisions or legal status
- treasury execution, custody, or solvency
- external identity systems or identity attestations
- physical hardware identity or live hardware attestation

These are limits of the artifacts described here, not a prohibition on separate procedures an auditor may be authorized to perform. Report independent procedures and results separately, with their own scope and evidence.

---

# ✦ 3. Authority Evidence Requirements

Treat authority as evidence-based, not ceremonial.

### **Primary Evidence**

Review the applicable governance instrument, action-specific approval record, required signatories, and authoritative decision record. The exact evidence depends on the action and governing process.

### **Corroborating Context**

Steward identity records, lineage references, hardware metadata, and continuity documents may provide context. None of these alone establishes governance approval or authority to act.

### **Insufficient on Its Own**

- a ceremony or affirmation
- a drift-detector result
- documentation or registry presence
- automation output or recommendation
- a declared GovernanceRouter or AccessControl field

The [FL1-C Governance Ceremony](../unified/docs/fl1c_governance_ceremony.md) is a review record; it does not grant authority.

---

# ✦ 4. Interpreting Continuity Surfaces

Auditors may review the [Continuity Report](../unified/docs/unified_layer_continuity.md), [Epoch Advancement Document](../unified/docs/unified_layer_epoch_advancement.md), [Drift Dashboard](../unified/docs/unified_layer_drift_dashboard.md), and [Integrity Report](../unified/docs/unified_layer_integrity.md).

Interpret these as steward-maintained descriptions of declared state, references, and scoped checks. They are not, by themselves:

- proof of runtime or chain-state correctness
- proof of economic execution
- proof of hardware attestation
- substitutes for authoritative approvals, signed lineage records, or transaction evidence

Check dates, source artifacts, status fields, and verification limitations before relying on a statement.

---

# ✦ 5. Interpreting Verification Surfaces

Relevant surfaces include the [drift detector source](../unified/scripts/drift_detector.py), its [machine-readable report](../unified/reports/fl1c_drift_report.json), binding metadata, and the Integrity Report.

The detector checks selected FL1-C binding fields against a resolved local lineage artifact and evaluates declared consistency flags. It does not independently validate every layer's operational state.

When run, the detector writes `last_check` into the FL1-C binding and writes the drift report. Treat this as a governed file mutation: inspect the version and diff, and distinguish the timestamp from proof that every domain was verified.

---

# ✦ 6. Interpreting Lineage Anchors

Auditors may compare declared lineage events, epochs, and metadata with the local artifact resolved by the detector. The binding declares `lineage/FL1C_anchor.json`; the workspace's resolved artifact is [`freedomlink1-root/lineage/FL1C_anchor.json`](../freedomlink1-root/lineage/FL1C_anchor.json).

A local anchor can document a declared genesis event or marker. It does not, without separate evidence, prove runtime lineage, chain-state history, external-system continuity, or that later actions were recorded. For epoch transitions, review the authoritative ledger, signatures, and Merkle-root evidence required by the [Epoch Advancement Protocol](../governance/epoch_advancement_protocol.md).

---

# ✦ 7. Interpreting Identity Metadata

Auditors may review declared creator and steward identity references within the agreed scope. Metadata can describe intended provenance, but does not by itself establish a person's identity, authority, external identity verification, or identity at the time of a later action.

Separate declared identity fields from independently obtained identity evidence, and handle personal or sensitive information according to the engagement and applicable law.

---

# ✦ 8. Interpreting Hardware Trust Metadata

Auditors may review the Rootstone-I identity artifact, FL1-C hardware binding fields, and lineage marker. The [Rootstone-I Hardware Trust Charter](../unified/docs/rootstone_hardware_trust_charter.md) describes their intended role and limits.

The local drift detector checks for required hardware binding fields and a `bound` marker in the lineage artifact. It does not inspect the Rootstone identity artifact, validate its signature, identify a physical device, or perform runtime attestation. Hardware metadata is not physical attestation.

---

# ✦ 9. Interpreting Economic Continuity Metadata

Auditors may review the binding's declared PPTF alignment and policy fields, the [Root Build Economic Continuity Charter](root_build_economic_continuity_charter.md), and the [FL1-C Treasury Integration Rules](governance/FL1C-treasury-integration.md).

The drift detector checks that the economic consistency flag is enabled; it does not verify the economic policy's values, treasury approval or execution, supply behavior, custody, or economic correctness. Review transaction, approval, and treasury records separately when included in audit scope.

---

# ✦ 10. Interpreting Governance Rituals

Governance ceremonies may show that a steward recorded a review and cited evidence. They do not, by themselves:

- grant authority or establish approval
- execute a governance or economic action
- prove lineage, identity, or hardware attestation
- verify runtime behavior

Compare ceremony statements with approval records and authoritative action records. Treat unsupported or pending affirmations as such.

---

# ✦ 11. Interpreting Automation Constraints

The [Sovereign Automation Specification](../unified/docs/unified_layer_automation_spec.md) states intended policy boundaries and identifies current implementation gaps. It is not itself an enforcement mechanism.

In particular, `scripts/autonomous_epoch_advancement.py` can invoke the epoch-ledger update script based on an intelligence-ledger recommendation; the target script does not perform the governing protocol's required authorization and verification sequence. The drift detector also writes `last_check` into the binding. Auditors should compare policy statements with tool behavior and resulting file changes rather than assume the tools enforce the policy.

---

# ✦ 12. Interpreting Registries

Auditors may review the [Asset Registry](../unified/docs/asset_registry.md) and [Module Registry](../unified/docs/module_registry.md) as indexes of declared assets and modules represented in local metadata and documentation.

Registry inclusion does not establish deployment, runtime state, legal recognition, chain-state correctness, or operational verification. Follow each entry's references and evidence limitations.

---

# ✦ 13. Auditor Conduct

Auditors should:

- respect the agreed scope, access controls, confidentiality, and applicable law
- distinguish primary authority evidence from contextual metadata
- preserve evidence provenance and record the source and date reviewed
- distinguish institutional local checks from independent audit procedures
- report limitations, gaps, and contradictory evidence plainly
- avoid changing artifacts under review unless explicitly authorized and documented
- preserve the distinction between policy intent and implemented behavior

Auditing is observational with respect to this handbook's institutional surfaces; independent procedures remain governed by the engagement and applicable law.

---

# ✦ Closing

The Unified Layer Auditor's Handbook explains how to interpret Freedomlink1's local institutional artifacts and their verification limits. It supports review across governance, lineage, identity, hardware trust, economic continuity, verification, continuity, automation, stewardship, and registries without treating declarations as proof of operational behavior.

Freedomlink1 Unified Layer  
Auditor's Handbook — Epoch 6