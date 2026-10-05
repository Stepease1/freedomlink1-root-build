# ✦ Unified Layer Operational Handbook
Freedomlink1 Unified Layer • Steward Operations Guide

The Unified Layer Operational Handbook describes how stewards maintain, review, and extend the Freedomlink1 Unified Layer's local metadata and documentation. It covers sovereign asset records, institutional modules, continuity surfaces, verification tools, and temporal governance.

This handbook distinguishes documented configuration from operationally verified behavior. It does not grant authority, verify deployed systems, or replace applicable governance protocols.

---

## ✦ Operational Overview

**Institution:** Freedomlink1  
**Configured Epoch:** 6 — Continuity Epoch  
**Operational Authority:** Applicable governance instruments and authorized stewards  
**Verification Surfaces:** [Integrity Report](unified_layer_integrity.md), [Drift Dashboard](unified_layer_drift_dashboard.md)  
**Continuity Surfaces:** [Continuity Report](unified_layer_continuity.md), [Epoch Advancement Document](unified_layer_epoch_advancement.md)  
**Registry Surfaces:** [Asset Registry](asset_registry.md), [Module Registry](module_registry.md)

Stewards maintain coherence across governance, lineage, identity, hardware, economic, and Unified Layer metadata while preserving the verification limits recorded by each artifact.

---

# ✦ Steward Responsibilities

Stewards are responsible for:

1. Maintaining Unified Layer documentation and navigation.
2. Running and reviewing the local drift detector when appropriate.
3. Keeping integrity surfaces aligned with available evidence.
4. Recording continuity events in their authoritative records.
5. Preparing epoch transitions under the applicable governance protocol.
6. Documenting new sovereign assets and their supporting artifacts.
7. Registering institutional modules with accurate verification scope.
8. Reviewing metadata coherence and resolving discrepancies.
9. Preserving audit boundaries and unrelated workspace changes.

These are documentation and review responsibilities; they do not by themselves authorize institutional actions.

---

# ✦ Operating the Drift Detector

The FL1-C drift detector compares local binding metadata with available lineage artifacts and selected declared consistency fields. It does not verify runtime behavior, deployments, external governance, treasury execution, identity registries, or hardware attestation.

### **Run the detector**

From the repository root:

```powershell
python unified/scripts/drift_detector.py
```

The script writes `unified/reports/fl1c_drift_report.json` and updates `unified_layer.drift_detection.last_check` in `unified/bindings/fl1c_binding.json`. Review both outputs and inspect the working-tree diff before committing; running the detector changes files.

### **Interpret the result**

- Exit code `0`: no drift was found within the checked local metadata and artifacts.
- Exit code `1`: one or more local checks failed; review `failed_checks` and investigate before representing the result as clear.
- Exit code `2`: checks could not be fully assessed or the detector encountered an error; do not claim a clean result.

The [Drift Dashboard](unified_layer_drift_dashboard.md) is a human-readable document, not a live view. Refresh its displayed values manually when publishing a new report; the detector does not synchronize the dashboard or integrity report.

---

# ✦ Updating the Integrity Report

The local report is [unified_layer_integrity.md](unified_layer_integrity.md). Update it when its recorded evidence, verification scope, or referenced artifacts change. Keep declared configuration separate from checks actually performed, and state what remains unverified.

The report is not automatically updated by the drift detector. Do not describe its status as a runtime, deployment, legal, treasury, identity-attestation, or hardware-attestation audit unless the corresponding evidence was separately collected.

---

# ✦ Maintaining the Asset Registry

The [Asset Registry](asset_registry.md) indexes assets represented by local Unified Layer documentation and metadata. For a proposed new asset:

1. Record the asset's binding and identify its source and scope.
2. Add an integration document describing its declared relationships.
3. Link relevant lineage artifacts and distinguish declared paths from resolved files.
4. Document identity and hardware metadata only where applicable, with verification limits.
5. Record economic or treasury rules as declarations unless their operation is independently verified.
6. Add the asset to the registry and update relevant explorer documentation.
7. Confirm that available verification tooling covers the asset before reporting its status as checked.
8. Update integrity and drift documentation to reflect only the checks actually performed.

The current drift detector is specific to FL1-C; adding an asset to the registry does not automatically add detector coverage.

---

# ✦ Maintaining the Module Registry

The [Module Registry](module_registry.md) indexes modules represented in local metadata or documentation. To add a module:

1. Describe its layer, role, and declared configuration.
2. Identify the evidence available for local verification.
3. State runtime, deployment, and enforcement limits.
4. Add the entry to the registry and link supporting artifacts where available.
5. Update continuity references when the documented continuity model changes.

Do not mark a module operational or verified solely because it appears in a binding or document.

---

# ✦ Preparing Epoch Advancement

Epoch transitions are governed by the [Epoch Advancement Protocol](../../governance/epoch_advancement_protocol.md) and summarized for cross-layer review in the [Epoch Advancement Document](unified_layer_epoch_advancement.md). Follow the governing protocol for required checks, authorization, the authoritative lineage record, signatures, and Merkle-root requirements.

The drift detector provides local metadata evidence only. It does not authorize, block, or execute an epoch transition. Supporting reports and dashboards do not replace the authoritative lineage ledger or signed governance record.

After an authorized transition is recorded, review and update applicable Unified Layer references, including binding metadata, integrity and continuity documents, dashboards, and registries. Update each surface only with evidence appropriate to its scope.

---

# ✦ Maintaining Continuity Surfaces

Continuity references include:

- [Unified Layer Continuity Report](unified_layer_continuity.md)
- [Epoch Advancement Document](unified_layer_epoch_advancement.md)
- [Drift Dashboard](unified_layer_drift_dashboard.md)
- [Integrity Report](unified_layer_integrity.md)
- [Asset Registry](asset_registry.md)
- [Module Registry](module_registry.md)

Review these documents when relevant metadata, assets, modules, or authorized epoch records change. A detector run updates the binding timestamp and drift report only; other documents require a separate review and edit when their content is affected.

---

# ✦ Adding Documentation

When adding a Unified Layer document:

1. Place it in the appropriate documentation directory.
2. Add it to `mkdocs.yml` navigation when it belongs in the published site.
3. Check relative links and referenced artifacts.
4. Preserve evidence scope and avoid unsupported operational claims.
5. Review the exact files to be committed and leave unrelated or untracked work untouched.

MkDocs does not need to be installed to edit documentation or perform manual link checks. A full site build does require MkDocs; if it is unavailable, record that the build was not run rather than treating manual checks as a build result.

---

# ✦ Steward Conduct

Stewards should:

- preserve institutional records accurately
- distinguish declared configuration from verified behavior
- maintain explicit audit boundaries
- keep metadata and documentation consistent with available evidence
- follow the governing continuity and epoch protocols
- protect unrelated and untracked workspace files
- commit only reviewed, intended changes

Stewardship requires both continuity and accurate representation of evidence.

---

# ✦ Closing

The Unified Layer Operational Handbook provides practical guidance for maintaining Freedomlink1's local integration metadata and documentation across governance, lineage, identity, hardware, economic, and Unified Layer concerns. It supports institutional coherence while preserving the distinction between documented claims and independently verified operation.

Freedomlink1 Unified Layer  
Operational Handbook — Epoch 6