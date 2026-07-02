# Permissions Matrix

**Effective Date**: 2026-07-02  
**Last Updated**: 2026-07-02

## Overview

This document defines who may perform which actions within the FreedomLink1 system.

## Role Definitions

### Root Authority
- Full access to all systems
- Can create/modify governance documents
- Can authorize new roles
- Can modify permissions matrix
- Can approve amendments
- **Count**: 1 (Founding Authority)

### Council Members
- Can propose amendments
- Can participate in consensus votes
- Can create ceremonies
- Can sign critical documents
- Can modify lineage records
- **Count**: 3-7 active members

### Contributors
- Can propose changes
- Can participate in votes
- Can create and document work
- Can add to contributor registry
- Can create sub-ceremonies
- **Count**: Unlimited

### Auditors
- Can verify signatures
- Can run verification scripts
- Can access all records
- Can report findings
- Cannot modify documents
- **Count**: 2-5

### Community
- Can view all public records
- Can comment on proposals
- Can request verification
- Cannot modify any records
- **Count**: Unlimited

## Action Matrix

| Action | Root | Council | Contributor | Auditor | Community |
|--------|------|---------|-------------|---------|----------|
| Create amendment | ✓ | ✓ | ✓ | ✗ | ✗ |
| Approve amendment | ✓ | ✓ | ✗ | ✗ | ✗ |
| Sign document | ✓ | ✓ | ✓ | ✗ | ✗ |
| Create ceremony | ✓ | ✓ | ✓ | ✗ | ✗ |
| Add to registry | ✓ | ✓ | ✓ | ✗ | ✗ |
| Modify existing record | ✓ | ✓ | ✗ | ✗ | ✗ |
| Verify signatures | ✓ | ✓ | ✓ | ✓ | ✓ |
| Audit records | ✓ | ✓ | ✓ | ✓ | ✓ |
| Modify permissions | ✓ | ✗ | ✗ | ✗ | ✗ |
| Propose sanctions | ✓ | ✓ | ✓ | ✓ | ✗ |

## Escalation Procedures

Actions requiring higher permission levels must follow escalation:
1. Request from lower-permission role
2. Approval from higher-permission role
3. Documentation in ceremony records
4. Entry in permissions audit log

## Special Permissions

### Cryptographic Signing
- Requires registered key in contributor registry
- Must be accompanied by documented ceremony
- Requires timestamp authority verification

### Amendment Approval
- Requires supermajority of Council
- Must be voted and documented
- Cannot be delegated

### Sanction Authority
- Root authority with Council approval
- Requires documented evidence
- Must be appealable per oversight framework

## Permission Revocation

Permissions may be revoked when:
1. Member resigns or withdraws
2. Sanctions are imposed
3. System compromise is detected
4. Member requests revocation

Revocation procedures are documented in `governance/oversight-appeals-sanctions.md`.

## Review Schedule

This matrix is reviewed quarterly by the Council and amended as needed per the amendment protocol.
