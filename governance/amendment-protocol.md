# Amendment Protocol

**Established**: 2026-07-02  
**Last Revised**: 2026-07-02

## Purpose

This protocol governs how the FreedomLink1 system may be modified, updated, or amended.

## Types of Amendments

### Level 1: Minor Clarifications
**Supermajority**: 50% + 1 contributor  
**Timeline**: 7 days review, 3 days vote  
**Requirements**: 
- Documentation of current state
- Rationale for change
- No impact on governance rules
- Backward compatible

### Level 2: Operational Changes
**Supermajority**: 66% of Council  
**Timeline**: 14 days review, 7 days vote  
**Requirements**:
- Detailed impact analysis
- Community notification
- Verification procedures
- Ceremony documentation

### Level 3: Governance Changes
**Supermajority**: 80% of Council + Root Authority  
**Timeline**: 30 days review, 14 days vote  
**Requirements**:
- Full impact assessment
- Public comment period
- Alternative proposals considered
- Blockchain anchor required

## Amendment Process

### Phase 1: Proposal (Days 0-2)
1. Submitter creates amendment proposal
2. Proposal includes:
   - Current text
   - Proposed text
   - Rationale and justification
   - Impact assessment
   - Signed by proposer
3. Proposal published to all contributors
4. Recorded in `lineage/ceremonies.md`

### Phase 2: Discussion (Days 2-14)
1. Contributors submit comments
2. Concerns are documented
3. Amendments to the proposal allowed
4. Community can request clarification
5. All feedback recorded in ceremony log

### Phase 3: Voting (Days 14-21)
1. Formal vote by eligible parties
2. Voting recorded with signatures
3. Results documented
4. All votes preserved cryptographically

### Phase 4: Implementation (After Approval)
1. Amendment text finalized
2. Approval signatures collected
3. Change committed to repository
4. Blockchain anchor created
5. Hash computed and verified
6. New epoch marker created

## Veto Authority

The Root Authority may veto Level 1-2 amendments with documented justification. Level 3 amendments cannot be vetoed but can trigger dispute resolution.

## Withdrawal and Reversal

- Proposed amendments can be withdrawn until voting begins
- Approved amendments can be reversed following the same process
- Reversals require same supermajority as original approval

## Emergency Amendments

For critical security issues:
1. Root Authority may implement emergency amendment
2. Must be documented within 24 hours
3. Community vote held within 30 days
4. If vote fails, amendment is reversed

## Documentation

All amendments are:
- Recorded in git commit history
- Documented in ceremony records
- Blockchain anchored
- Timestamp verified
- Cryptographically signed

## Amendment History

See `lineage/ceremonies.md` for complete amendment history.

## Appeals

Amendment decisions may be appealed per `governance/oversight-appeals-sanctions.md`.
