# ✦ Unified Layer Module Registry
Freedomlink1 Unified Layer • Institutional Module Index

The Unified Layer Module Registry is the index of institutional modules represented in the Freedomlink1 Unified Layer. Modules cover governance, lineage, identity, hardware, economic, and Unified Layer concerns that contribute to Epoch 6 continuity.

This registry provides a reference surface for stewards, architects, auditors, and system maintainers. A module's inclusion documents its declared role; it does not establish deployment, operation, or legal status.

---

## ✦ Registry Overview

**Registry Type:** Institutional Module Index  
**Institution:** Freedomlink1  
**Current Epoch:** 6 — Continuity Epoch  
**Registry State:** Active  
**Verification Surface:** [Unified Layer Integrity Report](unified_layer_integrity.md)  
**Continuity Surface:** [Unified Layer Continuity Report](unified_layer_continuity.md)

Local verification statements below are limited to the checks described in the [Unified Layer Drift Dashboard](unified_layer_drift_dashboard.md). Runtime, deployment, external registry, and attestation checks have not been performed.

---

# ✦ Registered Institutional Modules

The following modules and documentation surfaces are currently represented in local Unified Layer metadata or documentation.

## **1. GovernanceRouter**

**Layer:** Governance  
**Role:** Sovereign authorization and governance flow control  
**Declared:** Yes  
**Verified (Local):** Binding metadata only  
**Notes:** The binding declares the router and authorization rule; contract-level enforcement is not assessed.

GovernanceRouter is declared as part of the governance configuration for sovereign actions.

---

## **2. EpochManager**

**Layer:** Governance  
**Role:** Epoch advancement and temporal governance  
**Declared:** Yes  
**Verified (Local):** Epoch metadata comparison only  
**Notes:** The detector compares the declared epoch with the local lineage anchor; runtime enforcement is outside scope.

EpochManager is declared as part of epoch-aware governance configuration.

---

## **3. AccessControl**

**Layer:** Governance  
**Role:** Sovereign permissions and authority rules  
**Declared:** Yes  
**Verified (Local):** Binding metadata only  
**Notes:** Permission fields are declared; authorization enforcement is not tested.

AccessControl is named in the binding as part of the declared permissions model.

---

## **4. LineageRegistry**

**Layer:** Lineage  
**Role:** Lineage anchoring and continuity tracking  
**Declared:** Yes  
**Verified (Local):** Event and epoch metadata comparison  
**Notes:** The local lineage artifact resolves and its event and epoch match the binding; registry operation is not assessed.

LineageRegistry is declared as part of the governance and lineage configuration.

---

## **5. CreatorIdentityRegistry**

**Layer:** Identity  
**Role:** Creator provenance and sovereign identity binding  
**Declared:** Yes  
**Verified (Local):** Binding fields and anchor marker only  
**Notes:** Required metadata and a creator-bound anchor marker are checked; registry state and identity attestation are not assessed.

CreatorIdentityRegistry is declared as the identity provenance reference for FL1-C.

---

## **6. RootstoneBinding**

**Layer:** Hardware  
**Role:** Hardware identity binding and Rootstone-I trust anchor  
**Declared:** Yes  
**Verified (Local):** Binding fields and anchor marker only  
**Notes:** Required metadata and the local bound marker are checked; hardware attestation is not assessed.

RootstoneBinding is declared as the hardware identity reference for FL1-C.

---

## **7. PPTF Treasury Governance**

**Layer:** Economic  
**Role:** Treasury governance and economic continuity  
**Declared:** Yes  
**Verified (Local):** Consistency flag only  
**Notes:** Treasury alignment is declared; treasury execution and economic policy enforcement are not tested.

PPTF Treasury Governance is the declared economic governance reference for FL1-C.

---

## **8. Unified Layer Binding System**

**Layer:** Unified  
**Role:** Binding JSONs, integration documents, and cross-layer metadata  
**Declared:** Yes  
**Verified (Local):** Binding metadata and consistency flags  
**Notes:** The binding records version 1.0.0 and `last_check`; the detector updates `last_check` when run.

The binding system records the institution's declared cross-layer configuration.

---

## **9. Unified Layer Explorer**

**Layer:** Unified  
**Role:** Human-readable visibility surface for sovereign assets and bindings  
**Declared:** Yes  
**Verified (Local):** Documentation present  
**Notes:** The local Explorer page describes the declared asset and cross-layer bindings; it is not a live system view.

See the [Unified Layer Explorer](unified_layer_explorer.md).

---

## **10. Unified Layer Integrity Surface**

**Layer:** Unified  
**Role:** Static audit surface for declared and locally checked configuration  
**Declared:** Yes  
**Verified (Local):** Documentation present  
**Notes:** The report records verification scope and limitations; it is not an independent runtime audit.

See the [Unified Layer Integrity Report](unified_layer_integrity.md).

---

## **11. Unified Layer Drift Detector**

**Layer:** Unified  
**Role:** Local-artifact drift detection  
**Declared:** Yes  
**Verified (Local):** Detector and latest report present  
**Notes:** The detector compares local metadata and writes a machine-readable report; it does not verify deployed behavior.

See [`drift_detector.py`](../scripts/drift_detector.py) and the latest [FL1-C drift report](../reports/fl1c_drift_report.json).

---

## **12. Unified Layer Drift Dashboard**

**Layer:** Unified  
**Role:** Human-readable drift and consistency view  
**Declared:** Yes  
**Verified (Local):** Documentation present; values reference the latest checked-in report  
**Notes:** The page summarizes local drift results and their verification limits; it does not perform checks itself.

See the [Unified Layer Drift Dashboard](unified_layer_drift_dashboard.md).

---

## **13. Unified Layer Continuity Surface**

**Layer:** Unified  
**Role:** Epoch continuity documentation  
**Declared:** Yes  
**Verified (Local):** Documentation present  
**Notes:** The page documents the declared continuity model; inclusion does not independently validate its claims.

See the [Unified Layer Continuity Report](unified_layer_continuity.md).

---

# ✦ Registry Structure

Each module entry includes:

- module metadata
- layer classification
- declared configuration
- local verification status
- continuity role
- notes on enforcement and verification scope

This structure keeps declared integration distinct from independently verified operational behavior.

---

# ✦ Registry Expansion

Future entries may include:

- additional governance systems
- hardware attestation modules
- identity registries
- treasury instruments
- continuity frameworks
- sovereign automation modules
- integration orchestrators

Before listing a new module, record its declared configuration and supporting documentation, describe its local verification evidence and limitations, and link relevant integrity and continuity artifacts where available.

---

# ✦ Closing

The Unified Layer Module Registry indexes modules represented in local Freedomlink1 metadata and documentation. It supports visibility and review across governance, lineage, identity, hardware, economic, and Unified Layer concerns without implying that listed systems are deployed or operational.

Freedomlink1 Unified Layer  
Module Registry — Epoch 6