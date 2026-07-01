# Contributing to Freedomlink

Thank you for your interest in contributing to Freedomlink! This document outlines our contribution process, governance requirements, and technical standards.

## Getting Started

1. **Read the Welcome**: Start with [onboarding/WELCOME.md](onboarding/WELCOME.md)
2. **Review the Charter**: Understand our principles in [governance/charter.md](governance/charter.md)
3. **Join the Registry**: Add yourself to [lineage/contributor-registry.md](lineage/contributor-registry.md)
4. **Review Tech Stack**: See [onboarding/tech-stack.md](onboarding/tech-stack.md)

## Contribution Types

### Documentation
- Governance documents and policy updates
- Technical specifications and design docs
- Ceremony records and milestone documentation
- Process improvements and best practices

### Code & Scripts
- Cryptographic verification tools
- Hash and merkle tree implementations
- Integration scripts and automation
- Testing and validation utilities

### Governance Participation
- Amendment proposals
- Appeals and dispute resolution
- Permissions and authorization reviews
- Charter and policy discussions

## Contribution Process

### 1. Preparation
- Create a branch with a descriptive name
- Document your changes clearly
- Ensure compliance with our governance standards
- Update relevant registries if applicable

### 2. Development
- Follow TypeScript conventions (see `tsconfig.json`)
- Write cryptographically sound code
- Include verification capabilities
- Document your work thoroughly

### 3. Verification
- Run all verification scripts (see [VERIFY.md](VERIFY.md))
- Ensure hash consistency
- Validate digital signatures
- Check governance compliance

### 4. Review & Consensus
- Submit your contribution for community review
- Participate in the governance approval process
- Address feedback and concerns
- Obtain required approvals per [governance/permissions-matrix.md](governance/permissions-matrix.md)

### 5. Merge & Recording
- Merge approved changes
- Update ceremony records in [lineage/ceremonies.md](lineage/ceremonies.md)
- Record contributor roles in [lineage/contributor-registry.md](lineage/contributor-registry.md)
- Compute new canonical hashes and blockchain anchors

## Governance Requirements

All contributions must:

1. **Comply with Charter**: Align with principles in [governance/charter.md](governance/charter.md)
2. **Follow Amendment Protocol**: Major changes require approval per [governance/amendment-protocol.md](governance/amendment-protocol.md)
3. **Respect Permissions**: Check [governance/permissions-matrix.md](governance/permissions-matrix.md) for your authorization level
4. **Maintain IP Clarity**: Review [governance/licensing-ip.md](governance/licensing-ip.md)
5. **Support Verification**: Enable independent verification of all changes

## Technical Standards

### Code Style
- TypeScript with strict mode enabled
- Clear, documented functions
- Cryptographic best practices
- No hardcoded secrets or keys

### Verification
```bash
# Verify your changes
npm run build
python scripts/hashing.py --file <your-changes>
python scripts/signature-verification.py
python scripts/merkle-tree.py --verify
```

### Documentation
- Clear markdown formatting
- Links to related documents
- Examples where helpful
- Attribution for external references

## Commit Message Standards

Format commit messages as:
```
[Type] Brief description

Detailed explanation of changes. Reference relevant governance documents
and verification procedures used.

Contributor: Your Name
Ceremony: [Ceremony ID if applicable]
Verification: Hash <hash-value>
```

Types: `docs`, `feat`, `fix`, `refactor`, `test`, `chore`

## Dispute Resolution

If there are concerns about a contribution:

1. Raise the issue transparently
2. Consult [governance/oversight-appeals-sanctions.md](governance/oversight-appeals-sanctions.md)
3. Follow the formal appeals process if needed
4. Document all discussions

## Contributor Recognition

All contributors are recognized in:
- [lineage/contributor-registry.md](lineage/contributor-registry.md)
- Commit histories and signatures
- Ceremony records in [lineage/ceremonies.md](lineage/ceremonies.md)
- Appropriate documentation acknowledgments

Your contribution becomes part of the permanent, immutable record.

## Resources

- **Contributor Guide**: [onboarding/contributor-guide.md](onboarding/contributor-guide.md)
- **Tech Stack**: [onboarding/tech-stack.md](onboarding/tech-stack.md)
- **Verification**: [VERIFY.md](VERIFY.md)
- **External Standards**: [anchors/external-references.md](anchors/external-references.md)
- **Full Index**: [docs/index.md](docs/index.md)

## Questions?

Consult:
- [onboarding/governance-primer.md](onboarding/governance-primer.md)
- [governance/charter.md](governance/charter.md)
- Contributor registry contacts in [lineage/contributor-registry.md](lineage/contributor-registry.md)

Welcome to Freedomlink! 🔗
