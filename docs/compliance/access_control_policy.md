# FreedomLink1 Access Control Policy

| Document field | Value |
|---|---|
| Version | 1.0 |
| Status | Draft for approval |
| Policy owner | Access Control Owner (to be assigned) |
| Approver | Executive management and designated governance authority (approval required) |
| Effective date | Upon documented approval |
| Review frequency | At least annually and after material role, system, governance, or threat change |
| Related policy | [Information Security Policy](information_security_policy.md) |

This policy is a proposed institutional control. It does not establish implemented controls, operational effectiveness, certification, or independent assurance. The designated approver must approve this policy and retain evidence of implementation, review, and remediation before it is represented as an operating control.

## 1. Purpose

This policy defines requirements for authorizing, provisioning, using, reviewing, and revoking access to FreedomLink1 systems, information, governance records, cryptographic operations, repositories, cloud services, and institutional evidence.

Access controls must protect confidentiality, integrity, availability, accountable stewardship, and the lineage integrity of FreedomLink1 records. This policy implements the access-control principles established in the [Information Security Policy](information_security_policy.md) and supports future SOC 2 readiness.

## 2. Scope

This policy applies to:

- Stewards, custodians, sentinels, maintainers, contributors, contractors, auditors, administrators, and other authorized persons.
- Human and service identities that can access, modify, approve, publish, deploy, or review in-scope information or systems.
- Source repositories, organization settings, branch protections, CI/CD workflows, deployment environments, cloud services, identity providers, endpoints, secret stores, governance ledgers, and lineage records.
- Privileged, remote, emergency, service, shared, and cryptographic signing access.
- Third parties that store, process, transmit, administer, or materially support in-scope services or records.

Public information may remain publicly accessible only when its publication has been authorized. Access to restricted information must be limited to the persons and purposes documented in an approved role or access decision.

## 3. Governing Principles

Access decisions must follow these principles:

- **Constitutional authority:** Grant access only where the applicable governance instrument and designated authority permit the action.
- **Least privilege:** Grant only the permissions required for the assigned responsibility.
- **Need to know:** Restrict confidential, personal, security-sensitive, and governance evidence beyond operational need.
- **Role based:** Define duties and permissions by documented role, not by informal or permanent individual status.
- **Separation of duties:** Separate request, approval, implementation, and, where risk requires, review of security-sensitive activity.
- **Individual accountability:** Use attributable identities and prevent unidentified or unreviewable actions.
- **Temporary authorization:** Grant elevated or exceptional access for a defined purpose and time.
- **Lineage preservation:** Protect governance records, signatures, ledgers, and historical decisions from unauthorized alteration or deletion.
- **Evidence-based operation:** Record material access decisions and retain sufficient evidence to support review and audit.

## 4. Roles and Institutional Authority

FreedomLink1 roles must be maintained in a current permissions matrix and connected to the applicable constitutional or governance authority. The matrix must identify:

- The duties and permissions assigned to each role.
- The person or body authorized to approve, grant, change, and revoke access.
- The systems, records, environments, and actions within each role's scope.
- The required separation between requesters, approvers, administrators, and reviewers.
- Restrictions that apply to governed lineage, cryptographic signing, amendment, ceremonial, treasury, and institutional records.

The existing permissions matrix remains a role reference only. A role in the matrix does not itself authorize access to a system unless the system owner has approved the applicable account or permission change.

## 5. Identity Standards

- Assign each person an individually attributable account for in-scope systems.
- Prohibit identity sharing unless specifically approved, attributable to an accountable owner, technically controlled, and reviewed at least as frequently as other privileged access.
- Use unique identities across production, administrative, repository, cloud, and governance systems.
- Authenticate identities using methods proportionate to risk and supported by the system owner.
- Require multi-factor authentication for privileged, administrative, signing, remote, and sensitive-data access.
- Require current device, session, password, recovery, and account-recovery protections established through applicable standards.
- Disable or suspend identities that are orphaned, dormant, suspicious, or no longer associated with an active access need.
- Preserve attribution by preventing credentials or tokens from being disclosed or used under another person's identity.

## 6. Authentication

- Enforce strong, risk-based authentication for in-scope systems.
- Require multi-factor authentication wherever supported for privileged and remote access.
- Configure organization, repository, cloud, and identity-provider security settings to prevent unauthorized bypass.
- Use managed password, passkey, hardware-token, or other approved authentication mechanisms when available.
- Protect recovery codes and account-recovery processes with the same or higher controls as the protected account.
- Require re-authentication or additional approval for security-sensitive actions where the system supports it.
- Investigate unexpected authentication failures, recovery requests, sign-ins from unknown locations or devices, and other suspicious events.

## 7. Authorization and Role Assignment

Access requests must specify:

- The requester.
- The requested system, role, permission, environment, or record.
- The business, institutional, or governance purpose.
- The requesting manager, system owner, or institutional authority.
- The requested start date and expiration or review date.
- Required compensating controls or restrictions.

Access may be granted only after documented approval by an authorized approver. System owners must verify that the approved role matches the implemented permission set. No person may approve their own access unless an authorized governance instrument explicitly provides a separation-safe exception.

## 8. Provisioning

Provisioning personnel must:

- Implement only approved, attributable access.
- Apply least privilege and, where applicable, separate administrative and standard roles.
- Configure branch rules, repository roles, workflow permissions, deployment environments, secret access, and cloud permissions to the approved scope.
- Verify that access is effective and attributable before completing the request.
- Record the approver, implementer, date, system, permissions, purpose, and expiration or review date.
- Notify the requester and relevant system owner when provisioning is complete.
- Remove incomplete or duplicate access created as part of provisioning.

Automated provisioning may be used when it is configured, reviewed, logged, and attributable. Automation does not replace the required approval or ownership decision.

## 9. Privileged and Administrative Access

Privileged access is controlled more strictly and includes:

- Identity-provider and cloud administration.
- Repository organization or settings administration.
- Branch-protection and environment-approval administration.
- CI/CD, deployment, signing, key-management, secret-management, backup, and security-tool administration.
- Governance ledger, permissions-matrix, and institutional-record administration.

Controls must include:

- Separate privileged and non-privileged roles where supported.
- Individually attributable privileged identities or authenticated elevation.
- Multi-factor authentication and re-authentication for elevated operations.
- Approval by an authorized system or governance owner.
- Time-limited or just-in-time access where supported.
- Monitoring of privileged sign-in and administrative changes.
- Periodic review of privileged role membership and elevation activity.
- Restrictions on modifying logs, records, access controls, or evidence by the same person who generated it.

## 10. Repository and Governance Access

Repository access must be limited according to the person's responsibility and institutional role.

- Protect the primary branch through pull requests and required independent review for security-sensitive changes.
- Restrict direct pushes, force pushes, organization settings, repository deletion, workflow changes, signing configurations, and environment access to authorized maintainers.
- Limit workflow token permissions and deployment credentials to the minimum required scope.
- Review third-party workflow actions, dependencies, and other executable integrations before approval and use.
- Protect governance documents, lineage records, ledgers, seals, signatures, and approval evidence from unauthorized modification or deletion.
- Access to cryptographic signing capability must be based on registered identity, documented authority, and the applicable ceremony or control procedure.
- Integrity checks, automated tests, signatures, and seals are evidence within documented limits; they do not replace approval or operational access controls.

## 11. Cryptographic and Signing Access

Access to signing keys, hardware trust material, backup credentials, and recovery methods must be:

- Limited to approved custodians and documented institutional roles.
- Bound to a specific, attributable purpose.
- Protected by approved storage, authentication, and recovery procedures.
- Logged or otherwise attributable to an accountable custodian.
- Subject to use restrictions, rotation, revocation, and destruction requirements.
- Segregated from public source, CI logs, build artifacts, and public documentation.

Signing activity must distinguish:

- Technical identity verification.
- Governance authorization.
- Ceremonial participation.
- Human approval.
- Automated integrity checking.

A cryptographic signature or seal does not establish authority unless the authority and approval evidence are independently documented.

## 12. Third-Party and Service Access

Third-party identities and service accounts must:

- Have documented ownership, purpose, scope, and expiration or review date.
- Receive only the permissions required to support the approved service.
- Use secure authentication and approved secret-management mechanisms.
- Be restricted from unrelated repositories, environments, records, or administrative functions.
- Be inventoried and included in periodic access reviews.
- Be removed or disabled when a service is retired or no longer requires access.

Provider access must be included in the vendor risk and due-diligence process. Subservice access must not exceed the documented system boundary or contractual purpose.

## 13. Emergency and Break-Glass Access

Emergency access must be approved by an authorized owner unless delay would create an imminent, documented risk to availability or security.

Emergency access must:

- Use a separate controlled method where practical.
- Limit permissions and duration to the incident or recovery need.
- Require individual attribution or pre-approved accountable ownership.
- Generate or preserve available audit evidence.
- Notify the designated owner and incident-response authority promptly.
- End with access removal or return to normal scope.
- Receive retrospective review and documentation as soon as practicable.

Use of emergency access must not create or validate a new permanent role. Permanent access requires normal provisioning and approval.

## 14. Changes to Access

Access must be changed promptly after:

- Transfer to another role or responsibility.
- Increased or reduced institutional authority.
- Change in project, repository, system, or governance scope.
- Material system or security configuration change.
- Detection of suspicious activity or compromise.
- Failure to complete access reviews or required training.
- Suspension, leave, resignation, separation, contract termination, or loss of authority.

Role changes must remove obsolete access in addition to granting required access. The system owner or designated administrator must verify completion and retain review evidence.

## 15. Revocation and Offboarding

When access is no longer required:

- Revoke or disable accounts promptly through approved offboarding procedures.
- Revoke organization, repository, cloud, VPN, signing, deployment, secret, and governance permissions.
- Rotate shared credentials or exposed secrets where applicable.
- Recover or reassign institutional devices, keys, hardware trust material, and other controlled assets.
- Transfer necessary records and responsibilities to an authorized successor.
- Preserve required records and evidence while preventing unauthorized continuation or deletion.
- Record the reason, approving authority, completion date, responsible administrator, and residual access or exceptions.

Compromise or suspected misconduct may require immediate suspension. Revocation must not destroy required lineage evidence or interfere with legally or institutionally required retention.

## 16. Periodic Access Review

System owners must conduct documented access reviews at least annually and more frequently for privileged, signing, administrative, governance, and production access when risk warrants.

Each review must:

- Include the applicable population of users, roles, service accounts, and permissions.
- Identify the reviewer and the review date.
- Confirm the person's or service's current need and institutional authority.
- Identify over-provisioning, dormant accounts, shared identities, orphaned permissions, and conflicting duties.
- Record approved actions to retain, modify, suspend, or revoke access.
- Retain evidence of implementation and remediation.
- Escalate unresolved or high-risk findings.

The review must include repository organization membership, Actions permissions, branch protections, deployment environments, cloud and identity-provider roles, secret access, and governed lineage or signing access.

## 17. Monitoring and Logging

In-scope systems must record or preserve, where supported:

- Account creation, modification, elevation, and deletion.
- Authentication, failed authentication, and recovery activity.
- Role and permission changes.
- Repository membership and settings changes.
- Workflow and deployment permission changes.
- Signing, governance, ledger, and sensitive-record access.
- Emergency or break-glass access.
- Access-review decisions and revocation actions.

Logs must be protected from unauthorized modification or deletion, retained according to approved requirements, and reviewed at a defined schedule by an accountable owner. Security investigations must preserve relevant records and restrict access to authorized personnel.

## 18. Segregation of Duties

System owners must identify duties that create a material risk if held by the same person. Where practical, separate:

- Request and approval.
- Approval and provisioning.
- Change implementation and independent review.
- Deployment approval and production administration.
- Signing or key custody and governance approval.
- Access review and implementation of access changes.
- Evidence creation and evidence acceptance.

Compensating reviews, restricted logging, dual control, or independent monitoring may address systems that cannot technically separate duties. Any exception must be documented and risk accepted under the [Information Security Policy](information_security_policy.md).

## 19. Access Exceptions

Exceptions to this policy must:

- Be requested before implementation when practicable.
- Identify the affected requirement, user or service, and system.
- State the business or institutional rationale.
- Record the risk, affected data or activity, and compensating controls.
- Identify the approver, owner, implementation date, and expiration or review date.
- Be reviewed for renewal and closed when no longer required.

The authorized risk owner must approve exceptions. An exception cannot waive legal, contractual, regulatory, or constitutional obligations. Emergency exceptions must receive prompt retrospective review.

## 20. Training and Accountability

People with access to in-scope systems must receive role-appropriate guidance on:

- Individual accountability.
- Least privilege and need-to-know requirements.
- Credential, MFA, recovery, and secret handling.
- Approval and provisioning procedures.
- Incident and suspicious-access reporting.
- Changes, revocation, and offboarding duties.
- Governance and lineage integrity boundaries.

Training and acknowledgment must be recorded where required by role or risk. Violations must be referred through the applicable institutional and incident-response process.

## 21. Evidence and Records

Controlled evidence must be attributable and protectable. Records should include, where applicable:

- Approved role and permissions matrices.
- Access requests and approver decisions.
- Provisioning records and technical verification.
- Privileged and service-account inventories.
- Access-review records and remediation.
- Revocation and offboarding records.
- Emergency-access records.
- Exception approvals and renewals.
- Authentication and administrative settings exports.
- Repository membership and branch-protection reviews.
- Governance decisions and lineage references.

Evidence must be retained according to an approved schedule. Sensitive evidence must not be placed in public repositories, public issues, public CI logs, or public artifacts. Evidence supplied to auditors or assessors must use controlled disclosure and appropriate redaction.

## 22. Compliance and SOC 2 Readiness

FreedomLink1 must map material access controls to applicable SOC 2 Trust Services Criteria and a current control register. The control owner must retain implementation, population, review, exception, and remediation evidence.

This policy supports, but does not establish, SOC 2 compliance or certification. Claims of compliance or audit readiness require confirmation of the system boundary, implemented controls, evidence period, and an authorized independent examination.

The organization must:

- Identify contractual, legal, regulatory, and customer access requirements.
- Assess compliance with this policy at a defined frequency.
- Track deficiencies through remediation or formally approved risk acceptance.
- Cooperate with authorized independent assessments.
- Avoid overstating findings that are derived only from repository configuration or internal review.

## 23. Policy Review

The policy owner must review this policy at least annually and after material changes to:

- Institutional roles or governance authority.
- Systems, services, repositories, or environments.
- Identity or authentication architecture.
- Threats or security incidents.
- Constitutional or lineage requirements.
- SOC 2 scope or applicable requirements.

Proposed revisions require the designated governance and executive approval before taking effect. Approved changes must be communicated to people in scope and must be recorded in the controlled document and lineage surfaces as required.

## 24. Policy Statement

FreedomLink1 personnel and authorized contributors must use only the access assigned to their documented role and business or institutional purpose. Access must be approved, attributable, periodically reviewed, and promptly revoked when no longer required.

Governance records and lineage evidence must remain attributable to the authority that approved them. Cryptographic verification, repository automation, or institutional seals do not replace authorized approval or documented access control.

This policy becomes effective only after documented approval and institutional recording by the designated approver.
