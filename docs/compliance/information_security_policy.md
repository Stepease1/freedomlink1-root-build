# FreedomLink1 Information Security Policy

| Document field | Value |
|---|---|
| Version | 1.0 |
| Status | Draft for approval |
| Policy owner | Information Security Owner (to be assigned) |
| Approver | Executive management (approval required) |
| Effective date | Upon documented approval |
| Review frequency | At least annually and after material change |

This policy is a proposed organizational policy. It is not evidence that the controls described below have been implemented, independently audited, or certified. Assign an owner, approve the policy, communicate it to the people in scope, and retain evidence of operation before representing it as an operating control.

## 1. Purpose

This policy establishes minimum expectations for protecting FreedomLink1 information and the systems used to create, review, build, publish, and maintain it. It supports the confidentiality, integrity, and availability of information, reduces security risk, and provides a basis for related standards and procedures.

## 2. Scope

This policy applies, once approved, to:

- Workforce members, maintainers, contractors, and other authorized contributors whose work can affect FreedomLink1 information or systems.
- FreedomLink1-controlled source repositories, source-control settings, CI/CD workflows, build artifacts, documentation sites, and related administrative accounts.
- Cloud services, endpoints, software, records, and data used to operate an in-scope service or perform in-scope work.
- Information handled on behalf of the organization, including confidential or personal information, if such information is in scope.

Publicly accessible repository contents are not necessarily approved for confidential information. Secrets, credentials, personal information, and non-public operational data must not be added to public source, issues, logs, or artifacts.

## 3. Security Principles

In-scope systems and processes must follow these principles:

- **Risk-based protection:** Select safeguards appropriate to the information, threats, and service commitments.
- **Least privilege:** Grant only the access needed for an assigned responsibility, for only as long as needed.
- **Defense in depth:** Do not rely on a single control to protect important systems or records.
- **Secure by design:** Consider security and privacy during design, implementation, review, and operation.
- **Accountability:** Assign owners and retain appropriate evidence for security decisions and control activities.
- **Continuous improvement:** Review incidents, findings, changes, and risk assessments to improve safeguards.

## 4. Asset Management

- Maintain an inventory of in-scope repositories, services, accounts, environments, data stores, and critical dependencies.
- Assign an owner to each material information asset and system.
- Classify information according to its sensitivity and handling requirements; document the classification scheme.
- Use only approved systems and services for organizational information.
- Protect organizational devices and promptly report loss, theft, or suspected compromise.
- Remove, return, or securely erase organizational information and access when an asset or service is retired, subject to retention requirements.

## 5. Access Control

- Use individually attributable accounts; shared accounts are prohibited unless approved, controlled, and attributable to an accountable owner.
- Require multi-factor authentication for privileged and remote access, and enable it for other supported in-scope services.
- Approve access based on role and business need; use least privilege and separate privileged activity where practical.
- Review access periodically and after material role or system changes.
- Promptly modify or revoke access when a person changes role, leaves, or no longer has a business need.
- Protect administrative credentials and never place credentials in source code, public documentation, tickets, logs, or build artifacts.
- Restrict repository settings, branch rules, workflow permissions, deployment environments, and production access to authorized administrators.

## 6. Cryptographic Security

- Use organization-approved cryptographic mechanisms to protect sensitive information in transit and at rest when supported by the system and risk assessment.
- Store private keys, tokens, and other secrets in approved secret-management facilities, separate from source and build outputs.
- Restrict key access, document key ownership, and define issuance, rotation, revocation, backup, and destruction procedures.
- Replace exposed or suspected-compromised credentials promptly and investigate the exposure.
- Use cryptographic verification for integrity or identity only where the verification method, key provenance, and limitations are documented.

## 7. Secure Cloud and Service Security

- Identify the security responsibilities of the organization and each cloud or service provider.
- Use supported configurations and restrict administrative interfaces to authorized users.
- Separate production from development and test environments when production services or sensitive data are in scope.
- Protect deployment workflows with review, restricted permissions, and approval gates appropriate to risk.
- Review third-party workflow actions and dependencies before use, pin them to immutable versions where practical, and update them through controlled changes.
- Do not treat public hosting or a successful build as evidence that access, availability, confidentiality, or other controls are effective.

## 8. Change Management

- Record and assess changes to in-scope code, infrastructure, access, workflows, and security settings.
- Require review and authorization appropriate to the risk; security-sensitive changes must receive independent review where practicable.
- Test changes and relevant security controls before release.
- Restrict production deployment to approved changes and authorized personnel.
- Maintain a rollback or recovery approach for material changes and document failed deployments and corrective actions.
- Record emergency changes and obtain a retrospective review as soon as practicable.

## 9. Documentation Integrity

- Maintain authoritative, version-controlled policies, procedures, architecture records, and security-relevant decisions.
- Protect records from unauthorized modification and deletion, and retain them according to approved retention requirements.
- Record the owner, approval status, version, and review date for controlled policies.
- Keep evidence attributable and associated with the relevant system, control, and time period.
- Treat checksums, signatures, seals, and lineage records as integrity evidence only within their documented scope; they do not replace access controls, review, monitoring, or independent assurance.

## 10. Monitoring and Logging

- Identify important security events for in-scope identity, repository, build/deployment, cloud, and production systems.
- Enable and protect relevant logs where supported; restrict log access and define retention based on risk and applicable requirements.
- Monitor security alerts and failed control checks on a defined schedule, with an accountable owner and escalation path.
- Investigate suspicious access, unauthorized changes, exposed secrets, and unusual deployment activity.
- Preserve relevant records during investigations and protect them from unauthorized alteration.

## 11. Vulnerability Management

- Identify vulnerabilities through appropriate advisories, dependency and code analysis, service-provider notices, and testing.
- Triage findings according to severity, exploitability, exposure, and business impact.
- Assign owners and target remediation dates; document mitigation, retesting, and closure.
- Document and approve any risk acceptance, including rationale, compensating safeguards, owner, and expiration or review date.
- Conduct independent security testing at a frequency appropriate to the risks and commitments of in-scope services.

## 12. Incident Response

- Maintain an incident-response procedure with severity levels, roles, contacts, and decision authority.
- Provide a way to report suspected incidents and security weaknesses promptly.
- Triage, contain, investigate, preserve evidence, eradicate causes, and recover affected systems.
- Escalate incidents to appropriate organizational leadership and determine notification obligations with qualified legal and privacy advisers.
- Document material incidents, decisions, communications, lessons learned, and corrective actions.
- Exercise the response procedure periodically and track resulting improvements.

## 13. Business Continuity

- Identify critical services, records, dependencies, and recovery priorities.
- Define recovery objectives and continuity procedures for in-scope services where availability is a commitment.
- Protect backups from unauthorized access and deletion, and establish retention and restoration procedures.
- Test restoration and continuity plans periodically; document results and remediation.
- Communicate material service disruptions through authorized channels.

## 14. Vendor and Third-Party Services

- Maintain an inventory of providers that store, process, transmit, or materially support in-scope information or services.
- Assess provider security and privacy risk before onboarding and periodically according to risk.
- Review relevant independent assurance, service scope, exceptions, and complementary customer controls where available.
- Document appropriate security, confidentiality, privacy, incident-notification, continuity, and data-return or deletion obligations.
- Reassess providers after material changes, incidents, or assurance findings.

## 15. Cryptographic Controls

- Approve cryptographic algorithms, libraries, protocols, and minimum configuration through a maintained technical standard.
- Use cryptographic implementations from maintained, trusted sources and track relevant security updates.
- Protect signing and verification keys from unauthorized access; establish ownership and approved use.
- Define how signatures and hashes are validated, including trust anchors, revocation, and known limitations.
- Do not represent a hash or signature as proof of the truth, authorization, or completeness of the underlying content.

## 16. Governance Records

- Assign owners to security policies, controls, risks, exceptions, and remediation actions.
- Record approvals, control performance, access reviews, incidents, training, and risk decisions in approved systems.
- Restrict governance evidence to authorized personnel and protect it according to its sensitivity.
- Make records available to authorized auditors and assessors through controlled disclosure and appropriate redaction.
- Retain records for approved periods and dispose of them securely when retention ends.

## 17. Exceptions

- Submit policy exceptions to the policy owner before implementation whenever practicable.
- Document the affected requirement, business rationale, risk, compensating measures, approver, owner, and expiration date.
- Obtain approval from an authorized risk owner; exceptions must be time-limited and reviewed before renewal.
- Track exceptions to closure and promptly revoke them when the rationale no longer applies.
- An exception does not waive legal, contractual, or regulatory obligations.

## 18. Compliance

- Identify applicable contractual, legal, regulatory, and customer requirements with qualified advisers.
- Assess compliance with this policy and related standards at a defined frequency.
- Track deficiencies and corrective actions to closure or documented, approved risk acceptance.
- Cooperate with authorized independent assessments and provide accurate, appropriately scoped evidence.
- Do not claim SOC 2 compliance, certification, or an audit opinion based solely on this policy, repository checks, or internal attestations.

## 19. Policy Review

The policy owner must review this policy at least annually and after material changes to systems, services, threats, commitments, or applicable requirements. Proposed revisions require documented approval before taking effect. The owner must communicate approved changes to people in scope and retain prior versions and approval records according to the records-retention requirements.

## Policy Statement

FreedomLink1 personnel and authorized contributors are expected to protect in-scope information and systems, follow approved security procedures, promptly report suspected incidents, and cooperate with authorized reviews. Owners must implement and periodically evaluate the controls assigned to them. This policy becomes effective only after documented approval by the designated approver.
