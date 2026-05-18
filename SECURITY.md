# SECURITY_POLICY

**Project:** VECTAETOS Agentic Audit  
**Repository:** `vectaetos-agentic-audit`  
**Status:** Draft v0.1  
**Document Type:** Repository security and anti-drift security policy  

---

## 0. Purpose

This file defines the security policy for the VECTAETOS Agentic Audit repository.

Security in this repository has two dimensions:

```text
1. Technical security
2. Conceptual security
```

Technical security protects code, artifacts, keys, dependencies, and repository integrity.

Conceptual security protects the non-agentic, non-intervention, non-optimization, and non-interpretation boundaries of the project.

Both are required.

---

## 1. Security Scope

This policy applies to:

```text
README.md
PHILOSOPHY.md
THEORY.md
ARCHITECTURE.md
CANONICAL_STATUS.md
NOTICE.md
TRADEMARKS.md
LICENSE.md
docs/
specs/
schemas/
protocols/
examples/
artifacts/
reports/
reference/
connectors/
legal/
brand/
.github/
```

Future hosted services, APIs, dashboards, and commercial infrastructure will require a separate production security policy.

---

## 2. Supported Versions

Current supported status:

| Version | Status | Security Support |
|---|---|---|
| v0.1-draft | Active draft | Yes |
| pre-v0.1 informal materials | Historical | Limited |
| forks | Unofficial | No official support |

Only canonical repository materials are covered by this policy.

Unofficial forks are not covered unless explicitly stated.

---

## 3. Reporting Security Issues

Do not report sensitive security vulnerabilities in public issues if they expose:

```text
secrets
private keys
signing keys
tokens
credentials
exploit paths
artifact forgery methods
supply-chain weaknesses
repository takeover paths
```

Preferred reporting route:

```text
Use GitHub private vulnerability reporting if enabled.
Otherwise request a private contact channel through a minimal public issue.
```

Do not include secrets, tokens, or exploit details in public issues.

---

## 4. Technical Security Priorities

The repository should protect:

```text
main branch integrity
release integrity
artifact integrity
schema integrity
license and notice integrity
trademark boundary integrity
GitHub Actions integrity
dependency integrity
secret hygiene
signing key separation
```

---

## 5. Branch Protection Policy

The `main` branch should be protected.

Minimum rules:

```text
no direct push to main
no force push to main
no deletion of main
pull request required before merge
conversation resolution required
status checks required once tests exist
linear history preferred
```

Recommended rule:

```text
canonical files require owner review
```

Canonical files include:

```text
PHILOSOPHY.md
THEORY.md
ARCHITECTURE.md
CANONICAL_STATUS.md
NOTICE.md
TRADEMARKS.md
LICENSE.md
specs/
schemas/
protocols/
legal/
brand/
```

---

## 6. CODEOWNERS Policy

A future `.github/CODEOWNERS` file should assign required review for critical areas.

Recommended ownership boundaries:

```text
/PHILOSOPHY.md
/THEORY.md
/ARCHITECTURE.md
/CANONICAL_STATUS.md
/NOTICE.md
/TRADEMARKS.md
/LICENSE.md
/specs/
/schemas/
/protocols/
/legal/
/brand/
```

Changes to these areas should require review before merge.

---

## 7. Secret Policy

No secrets may be committed to the repository.

Forbidden materials:

```text
API keys
private keys
signing keys
GitHub tokens
OpenAI keys
Stripe secrets
database credentials
cloud credentials
production config files
session tokens
webhook secrets
KMS credentials
```

Allowed materials:

```text
public keys
test keys clearly marked as test-only
example placeholders
sample configuration without secrets
```

Example placeholder format:

```text
YOUR_API_KEY_HERE
example_public_key_only
test_private_key_do_not_use_in_production
```

---

## 8. Signing Key Policy

Production signing keys must not be stored in the repository.

This includes:

```text
artifact signing keys
release signing keys
certificate signing keys
commercial audit signing keys
private verifier keys
```

The repository may contain:

```text
public verification keys
test keys
key format examples
signing protocol documentation
```

Production signing should occur in a controlled external environment.

---

## 9. GitHub Actions Policy

GitHub Actions must be minimal and reviewable.

Actions should be pinned where practical.

Workflows must not expose secrets to untrusted pull requests.

Initial allowed workflows:

```text
schema validation
markdown linting
unit tests
license header checks
artifact schema checks
```

Forbidden workflow behavior:

```text
publishing secrets
printing secrets
uploading private keys
deploying production services from unreviewed PRs
running untrusted scripts with write tokens
granting broad repository permissions without need
```

Default token permissions should be minimal.

---

## 10. Dependency Security

When implementation code is added, enable dependency monitoring.

Recommended future setup:

```text
Dependabot alerts
Dependabot security updates
lockfiles committed
minimal dependencies
regular dependency review
```

Dependency additions should be reviewed for:

```text
license compatibility
maintenance status
supply-chain risk
transitive dependency size
security history
```

---

## 11. Code Scanning

When reference implementation code exists, enable code scanning.

Recommended checks:

```text
CodeQL or equivalent
static analysis
schema validation tests
artifact verification tests
hash-chain tests
signature verification tests
invalidity-condition tests
```

Security tests should specifically cover:

```text
artifact mutation detection
broken hash chain detection
schema bypass attempts
signature mismatch detection
malformed input handling
path traversal in file inputs
unsafe deserialization
```

---

## 12. Artifact Integrity Policy

Artifacts must be treated as immutable after creation.

Rules:

```text
modified artifact = new artifact
artifact hash must change when content changes
artifact must not be edited after signing
artifact signature must be invalidated by mutation
artifact provenance must be preserved
```

An EAI artifact must not contain:

```text
recommendations
classifications
legal conclusions
financial assurance
moral verdicts
decision instructions
```

If such content is present, the artifact is invalid as an EAI artifact.

---

## 13. Schema Integrity Policy

Schemas define machine-readable boundaries.

Schema changes must be reviewed carefully.

Breaking schema changes require at least a minor or major version update depending on impact.

Schema files must not silently change field meaning.

Forbidden schema drift:

```text
kappa_trace becomes score
artifact gains recommendation field
EAI output gains decision field
report schema is treated as artifact schema
contract schema becomes legal contract by default
```

---

## 14. Conceptual Security

Conceptual security protects the project from drift.

The following transformations are considered conceptual security violations:

```text
EAI becomes an agent
EAI starts recommending actions
EAI starts scoring truth
kappa_trace becomes a quality score
artifact becomes a verdict
report is presented as raw EAI output
audit becomes control
VECTAETOS becomes a product
ContractMesh is claimed to create legal contracts by default
visibility is presented as authority
```

Such changes must be rejected unless the project intentionally creates a new major lineage.

---

## 15. Pull Request Anti-Drift Checklist

Every significant pull request should satisfy:

```text
[ ] This change does not make EAI an agent.
[ ] This change does not make EAI a decision engine.
[ ] This change does not make EAI an optimizer.
[ ] This change does not interpret kappa_trace as a score.
[ ] This change does not present artifacts as recommendations.
[ ] This change does not present reports as raw EAI output.
[ ] This change does not claim legal, financial, or statutory audit.
[ ] This change preserves the artifact/report boundary.
[ ] This change preserves VECTAETOS as non-saleable root.
[ ] This change preserves attribution and mark boundaries.
```

---

## 16. Issue Security Labels

Recommended issue labels:

```text
security
conceptual-security
schema-security
artifact-integrity
secret-leak
supply-chain
license-risk
trademark-risk
non-intervention-risk
invalidity-condition
```

---

## 17. Incident Response

If a security issue is discovered:

```text
1. Stop affected release or merge if possible.
2. Preserve evidence.
3. Do not rewrite public history unless absolutely necessary.
4. Revoke exposed secrets immediately.
5. Rotate keys if signing material was exposed.
6. Publish a corrective commit or advisory.
7. Add a regression test if applicable.
8. Update this policy if the incident reveals a missing rule.
```

For conceptual security incidents:

```text
1. Identify the drift.
2. Locate affected files.
3. Compare against CANONICAL_STATUS.md.
4. Revert or revise the drift.
5. Document the correction in CHANGELOG.md.
6. Add an invalidity rule if needed.
```

---

## 18. Release Security

Before any release:

```text
README.md must be consistent with CANONICAL_STATUS.md
PHILOSOPHY.md must be consistent with THEORY.md
schemas must validate
sample artifacts must validate
no secrets may be present
license notices must be present
trademark notices must be present
release notes must identify breaking changes
```

Future signed releases should include:

```text
release tag
release artifact hashes
public verification key
changelog
schema version
compatibility status
```

---

## 19. Security Boundary of Reports

Reports are human-facing interpretations.

They must not be confused with EAI artifacts.

Reports must include disclaimers when applicable:

```text
Not a statutory audit.
Not legal advice.
Not financial assurance.
Not insurance.
Technical and epistemic auditability only.
```

Security concern:

> A misleading report can become a trust exploit.

Therefore, report templates must preserve the interpretation boundary.

---

## 20. Security Boundary of Connectors

Connectors are integration surfaces.

They are not the architecture.

Future connectors must avoid:

```text
hardcoded secrets
overbroad permissions
silent data exfiltration
unlogged contract changes
unverified artifact uploads
automatic interpretation as decision
feedback into target system during EAI run
```

Connector outputs must preserve artifact/report separation.

---

## 21. Security Boundary of Hosted Services

Hosted verifier, API, dashboard, and commercial infrastructure are out of scope for this draft repository policy.

When hosted services exist, create a separate policy covering:

```text
authentication
authorization
tenant isolation
data retention
logging
key management
incident response
rate limiting
audit logs
backup and recovery
privacy
commercial artifact signing
```

---

## 22. Public vs Private Materials

Public repository may include:

```text
schemas
specifications
sample artifacts
test vectors
public keys
reference verifier
documentation
```

Private infrastructure must include:

```text
production signing keys
API secrets
customer data
billing secrets
commercial reports unless published
private audit evidence
internal infrastructure configuration
```

---

## 23. Minimal Security Configuration for GitHub

Recommended current configuration:

```text
Repository visibility: Public
Default branch: main
Direct push to main: Disabled
Force push: Disabled
Branch deletion: Disabled
Pull requests: Required
Secret scanning: Enabled
Push protection: Enabled
Issues: Enabled
Wiki: Disabled
Discussions: Optional / disabled at start
Projects: Optional / disabled at start
Actions: Restricted to reviewed workflows
```

---

## 24. Final Security Canon

```text
No secrets in repo.
No silent mutation of artifacts.
No unsigned official release once signing exists.
No EAI feedback into target systems.
No kappa_trace scoring.
No artifact recommendations.
No report-as-artifact confusion.
No official-status claims without permission.
No concept drift through convenience.
```

Security is not only protection from attackers.

For this project, security also means protection from false authority
