# Device Registry

**Established**: 2026-07-02  
**Last Updated**: 2026-07-02  
**Purpose**: Track all hardware used in governance and cryptographic operations

## Overview

This registry documents all devices involved in:
- Cryptographic key generation
- Document signing
- Ceremony participation
- Record creation
- Verification operations

## Device Classification

### Tier 1: Critical
- Used for root key operations
- Must be air-gapped when possible
- Full audit trail required
- Approved by Council

### Tier 2: Primary
- Used for contributor signing
- Standard security requirements
- Logged for all operations
- User responsibility

### Tier 3: Verification
- Used for reading/verifying only
- Limited audit requirements
- Community accessible

## Device Template

```yaml
device_id: [unique identifier]
owner: [person or organization]
device_type: [laptop/hardware-wallet/server/etc]
os: [operating system]
tier: [1-3]
keys_stored: [list of key IDs]
ceremony_usage: [list of ceremonies]
status: [active/inactive/decommissioned]
last_used: [date]
audit_log: [link to detailed log]
verification: [signature of registry maintainer]
```

## Registered Devices

### Genesis Devices (2026-07-02)

**Device ID**: GEN-001  
**Owner**: FreedomLink1 Collective  
**Type**: Secure Hardware Module  
**OS**: Linux (hardened)
**Tier**: 1  
**Status**: Active  
**Use**: Root authority key operations

**Device ID**: GEN-002  
**Owner**: Council Archive  
**Type**: Server  
**OS**: Linux  
**Tier**: 2  
**Status**: Active  
**Use**: Repository hosting and signing

## Key-Device Mappings

| Device ID | Key ID | Purpose | Status |
|-----------|--------|---------|--------|
| GEN-001 | ROOT-2026 | Root signing | Active |
| GEN-002 | COUNCIL-2026 | Amendment approval | Active |

## Decommissioning Process

When a device is no longer used:

1. **Notification**: Owner informs Council
2. **Key Transfer**: Migrate keys to new device
3. **Verification**: Final signature of old device
4. **Record**: Archive with ceremony timestamp
5. **Destruction**: Secure physical destruction recorded
6. **Certificate**: Chain-of-custody documented

## Security Requirements

### Tier 1 Devices
- Air-gapped or minimal connectivity
- Full-disk encryption
- Multi-factor authentication
- Regular security audits
- Offline key storage
- No internet access during key operations

### Tier 2 Devices
- Standard OS hardening
- Full-disk encryption
- Strong authentication
- Firewall configured
- Regular patches applied
- Antivirus/malware scanning

### Tier 3 Devices
- Standard security practices
- Read-only access
- No signing operations
- Community accessible

## Audit Trails

All Tier 1 and 2 devices maintain:
- Operation logs
- Access records
- Key usage logs
- Ceremony participation
- Verification dates
- Signature records

## Compromise Procedures

If a device is compromised:

1. **Immediate**: Notify Council and Root Authority
2. **72 hours**: Formal incident report
3. **Investigation**: Determine scope and impact
4. **Mitigation**: Revoke compromised keys
5. **Recovery**: Issue new keys on clean device
6. **Documentation**: Complete record in lineage
7. **Review**: Security procedures updated

## Certification

This registry is:
- Maintained by Registry Administrator
- Signed by Root Authority (monthly)
- Blockchain anchored (quarterly)
- Community auditable
- Timestamp verified
