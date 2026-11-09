# SOC 2 Readiness Checklist

Use this checklist to assess the controls and evidence needed for a SOC 2 examination involving the FreedomLink1 Root Build repository and any services it supports. It is a readiness aid, not a certification, audit opinion, or legal interpretation. A qualified SOC 2 practitioner should confirm the system boundary, applicable Trust Services Criteria, and examination scope.

## How to use this checklist

- Keep every item unchecked until the control is implemented and evidence is available.
- For each applicable item, record an accountable owner, implementation status, evidence location, and last-reviewed date in your control register.
- Mark non-applicable items with a documented rationale approved by the control owner; do not silently omit them.
- Redact credentials, personal information, and other sensitive data from evidence shared outside the organization.
- Reassess controls periodically and after material changes to systems, providers, personnel, or risks.

## 1. Scope and system description

- [ ] Name the service, product, or process for which assurance is sought; distinguish repository controls from production-service controls.
- [ ] Define the system boundary, components, environments, locations, and teams included in the examination.
- [ ] Identify the service commitments and system requirements made to customers or other users.
- [ ] Select the applicable Trust Services Categories with the auditor: Security is foundational; Availability, Confidentiality, Processing Integrity, and Privacy apply when relevant to the commitments and system.
- [ ] Identify and document in-scope repositories, GitHub organizations, Actions workflows, Pages sites, cloud services, identity providers, and other dependencies.
- [ ] Identify subservice organizations and document whether the inclusive or carve-out method is used for each.
- [ ] Maintain a current system description, architecture/data-flow diagram, inventory, and list of control owners.
- [ ] Define the examination period and evidence-retention approach with the auditor. A Type II examination requires evidence over a defined period; a point-in-time review alone is not sufficient.

## 2. Governance and risk management

- [ ] Assign an executive sponsor and named owners for each control and system component.
- [ ] Approve and periodically review security, acceptable-use, access-control, change-management, incident-response, continuity, and data-handling policies.
- [ ] Maintain a risk register covering threats to the repository, build/deployment pipeline, hosted service, and user data, where applicable.
- [ ] Assess risks at least annually and after material system or threat changes; document decisions and remediation.
- [ ] Define security objectives, accountability, escalation paths, and consequences for policy violations.
- [ ] Communicate applicable policies to workforce members and retain acknowledgment records.
- [ ] Provide role-appropriate security and privacy training at onboarding and periodically; record completion.
- [ ] Establish a process to report, track, accept, mitigate, and verify remediation of exceptions and control deficiencies.

## 3. Identity and logical access

- [ ] Require unique identities and strong authentication for source control, cloud, production, and administrative systems.
- [ ] Require multi-factor authentication for privileged and remote access, and enforce organization-wide where supported.
- [ ] Define role-based access and least privilege for repository membership, branch settings, Actions, deployment environments, and secrets.
- [ ] Restrict production deployment and security-sensitive settings to authorized personnel with documented approval.
- [ ] Protect the `main` branch with required pull requests, appropriate approvals, status checks, and restrictions on direct pushes and force pushes.
- [ ] Periodically review repository, organization, cloud, and production access; retain reviewer, date, decisions, and remediation evidence.
- [ ] Promptly revoke or change access on termination, role change, or suspected compromise; retain completion evidence.
- [ ] Use separate administrative accounts or roles where appropriate and monitor privileged activity.
- [ ] Store credentials in approved secret stores; do not commit secrets to source, issues, logs, artifacts, or documentation.
- [ ] Rotate credentials on a defined schedule and after exposure or personnel changes; test revocation and replacement procedures.
- [ ] Review GitHub Actions permissions and grant each workflow only the minimum required token permissions.
- [ ] Pin third-party Actions to reviewed immutable references where practical, and periodically review Actions and dependency risk.

## 4. Change management and secure development

- [ ] Document a change-management process covering requests, risk/impact review, approval, testing, release, and rollback.
- [ ] Require independent review for changes to application code, workflow permissions, deployment configuration, access controls, and security-sensitive settings.
- [ ] Require relevant automated checks to pass before merge and prevent bypass without documented, authorized exception.
- [ ] Maintain separate development/test and production environments when a production service is in scope.
- [ ] Protect production deployments with environment approvals and restricted deployment branches where supported.
- [ ] Record releases and deployment events, including actor, time, change reference, result, and rollback when applicable.
- [ ] Test rollback and recovery procedures for material changes.
- [ ] Maintain an inventory of direct and transitive software dependencies and a process for timely security updates.
- [ ] Run appropriate secret, dependency, and code security checks; document alert triage, remediation deadlines, and approved exceptions.
- [ ] Verify build and release artifacts originate from the approved source and build process; restrict artifact publication permissions.

## 5. Risk monitoring and security operations

- [ ] Define monitoring for relevant identity, repository, CI/CD, cloud, endpoint, and production activity.
- [ ] Centralize security-relevant logs where appropriate, restrict access, protect log integrity, and define retention.
- [ ] Alert on suspicious sign-ins, privilege changes, branch-protection changes, secret exposure, failed deployments, and other material events.
- [ ] Define a vulnerability intake and remediation process with severity-based response targets and documented closure.
- [ ] Run and document periodic vulnerability scans and independent penetration tests appropriate to the in-scope system.
- [ ] Track findings through remediation, verification, risk acceptance, or other documented disposition.
- [ ] Review security alerts and failed control checks on a defined schedule and preserve review evidence.
- [ ] Confirm automated integrity or verification jobs have named owners, alert routing, and documented follow-up for failures.

## 6. Incident response

- [ ] Maintain an approved incident-response plan with severity definitions, roles, contact paths, and decision authority.
- [ ] Define procedures for suspected credential compromise, unauthorized repository changes, malicious dependencies, data exposure, and service compromise.
- [ ] Document containment, investigation, evidence preservation, eradication, recovery, and post-incident review steps.
- [ ] Define customer, regulator, law-enforcement, and other notification decision processes and applicable deadlines with counsel.
- [ ] Exercise the plan periodically using scenarios relevant to the in-scope system; retain participants, results, and corrective actions.
- [ ] Track incidents and near misses in a restricted, auditable record and verify remediation.
- [ ] Maintain and test credential revocation, key rotation, and compromised workflow/deployment recovery procedures.

## 7. Availability and continuity (if applicable)

- [ ] Define availability commitments, recovery time objectives (RTO), and recovery point objectives (RPO).
- [ ] Maintain documented backup, restoration, disaster-recovery, and business-continuity procedures for in-scope services and records.
- [ ] Protect backups from unauthorized access and deletion; define retention and geographic requirements.
- [ ] Test backup restoration and continuity procedures periodically and track corrective actions.
- [ ] Monitor service health and capacity and document outage escalation and communication procedures.
- [ ] Assess critical provider outages and dependencies; document contingency plans.

## 8. Data protection, confidentiality, and privacy (as applicable)

- [ ] Inventory and classify data collected, created, processed, stored, or transmitted by the in-scope system.
- [ ] Document data flows, purposes, owners, locations, access, subprocessors, and retention periods.
- [ ] Minimize collection and restrict access to confidential, personal, or customer data.
- [ ] Define approved encryption requirements for data in transit and at rest and verify implementation.
- [ ] Define secure deletion and retention procedures for production data, logs, backups, and exports.
- [ ] Maintain a process for data-subject requests, privacy complaints, and required notices if personal data is in scope.
- [ ] Review vendor and subprocessor agreements for confidentiality, security, privacy, breach notice, and deletion obligations.
- [ ] Avoid putting personal data, secrets, or confidential operational details in this public repository and its public CI logs or artifacts.

## 9. Vendor and subservice organization oversight

- [ ] Maintain an inventory of vendors and subprocessors that can access, host, process, or materially support the in-scope system.
- [ ] Perform and document risk-based due diligence before onboarding and periodically thereafter.
- [ ] Review available independent assurance reports, scope, examination period, exceptions, and complementary user-entity controls.
- [ ] Document contractual security, privacy, availability, incident-notification, and data-return/deletion requirements.
- [ ] Track vendor incidents, service changes, assurance gaps, and remediation.

## 10. Repository-specific evidence to collect

The repository currently contains automated verification and integrity workflows. Their existence is not by itself evidence that the broader SOC 2 controls above are operating effectively.

- [ ] Preserve successful and failed CI runs for the examination period, including associated commit or pull request and timestamps.
- [ ] Preserve review and approval records for sampled changes, including evidence of reviewer independence where required by policy.
- [ ] Export and periodically review repository membership, organization roles, branch-protection settings, and deployment-environment access.
- [ ] Preserve workflow configuration history and evidence that workflow permissions and third-party Actions were reviewed.
- [ ] Preserve integrity-monitor alerts, investigation notes, approvals, and remediation evidence.
- [ ] Preserve vulnerability/dependency scan results, triage decisions, remediation records, and approved exceptions.
- [ ] Preserve deployment approvals, artifact provenance, deployment logs, and rollback records for in-scope releases.
- [ ] Confirm whether published Pages content is only public documentation or is part of an in-scope service; document the decision.
- [ ] Set and verify evidence retention for each source. Do not rely on a repository workflow's artifact-retention setting as the sole audit-evidence retention policy.
- [ ] Keep evidence exports read-only or access-controlled, dated, attributable, and linked to the applicable control and sample.

## 11. Examination readiness

- [ ] Map each applicable control to the agreed SOC 2 criteria and an accountable owner.
- [ ] Maintain a control register with control description, frequency, evidence source, owner, last performance date, exceptions, and remediation.
- [ ] Collect operating evidence throughout the examination period rather than reconstructing it at the end.
- [ ] Prepare a population of changes, access reviews, incidents, releases, vendor reviews, and other recurring control events for auditor sampling.
- [ ] Confirm policies, system description, diagrams, inventories, risk assessment, and evidence are current and consistent.
- [ ] Track auditor requests and responses through an authorized, access-controlled process.
- [ ] Resolve or formally document control gaps and exceptions; do not state that the organization is SOC 2 compliant or certified before an independent examination supports the relevant claim.

## Control register

Use or copy this table into the organization's controlled evidence register. Do not record credentials or sensitive evidence directly in this public repository.

| Control / checklist item | Owner | Status | Evidence location | Last performed | Exception / remediation |
|---|---|---|---|---|---|
|  |  | Not started / In progress / Operating / Not applicable |  |  |  |

## References

- [AICPA SOC Suite of Services](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
- [AICPA Trust Services Criteria resources](https://www.aicpa-cima.com/resources/download/trust-services-criteria)
- [Root Build verification workflow](https://github.com/Stepease1/freedomlink1-root-build/blob/main/.github/workflows/verify-root-build.yml)
- [Root Build integrity monitor workflow](https://github.com/Stepease1/freedomlink1-root-build/blob/main/.github/workflows/integrity-monitor.yml)
