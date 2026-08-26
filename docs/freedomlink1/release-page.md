---
title: Freedomlink1 Release Page
layout: default
permalink: /freedomlink1/release-page
---

# Freedomlink1 Release Page
## Root Build Launch — Early Access for Reviewers

### Release summary
Freedomlink1 Root Build `freedomlink1-root-2026.03.08` is now available for early review.

This release includes:
- health endpoint  
- dev-only admin seed routes  
- audit logging  
- steward flow simulation  
- Decade Seal execution  
- CI integration tests

### Access
Request access by emailing **legal@freedomlink1.com** with subject “Freedomlink1 root build access request.”  
Access is granted only after signing the Freedomlink1 NDA.

### Artifacts
- `agent.log`  
- `agent.pid`  
- `.github/workflows/integration-test.yml`

### Verification
Run the local integration script:
```bash
./run_local_integration.sh --test-key "your_test_api_key_here"
```

Trigger CI:
```bash
gh workflow run integration-test.yml --ref feature/admin-health-seed
```

### Notes
This is an early access release. Do not share artifacts or logs publicly.  
Use the NDA for all confidential access and review.

### Contacts
- Joshua — joshua@freedomlink1.com  
- Legal / NDA — legal@freedomlink1.com
