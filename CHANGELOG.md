# CHANGELOG

**Project:** VECTAETOS Agentic Audit  
**Repository:** `vectaetos-agentic-audit`  
**Status:** Draft v0.1  
**Document Type:** Project change history and decision log  

All notable changes, canonical decisions, architectural boundaries, and anti-drift updates should be recorded in this file.

This changelog follows the spirit of semantic versioning, but the project is still pre-MVP.

---

## Versioning Notes

Version classes:

```text
PATCH
- wording
- typo
- formatting
- clarification without conceptual change

MINOR
- new schema fields
- new examples
- new protocols
- compatible extensions
- new non-breaking documents

MAJOR
- change to non-intervention principle
- change to EAI output type
- change to kappa_trace meaning
- change to VECTAETOS identity
- change to artifact/report boundary
- change that grants authority to a formerly descriptive layer
```

Pre-v1.0 status:

```text
0.x = draft architecture
0.1 = canonical foundation
0.2 = schemas and artifact model
0.3 = verifier and sample artifacts
0.4 = report templates
0.5 = connectors / integration prototypes
1.0 = stable public specification
```

---

# [Unreleased]

## Changed

### Root cleanup phases 1-5

Recorded the initial root cleanup sequence.

Completed structural cleanup steps:

```text
Phase 1: prepared target directories
Phase 2: moved review documents into reviews/
Phase 3: moved upstream EAI markdown material into docs/upstream-vectaetos/eai/
Phase 4: moved EAI Python reference candidate files into reference/python/eai/
Phase 5: moved architecture map documents into docs/architecture/
```

Updated repository structure map:

```text
REPOSITORY_SCHEMA.md
```

Non-goals preserved:

```text
No EAI semantic change.
No spec freeze.
No schema freeze.
No verifier implementation.
No production-service claim.
No commercial/legal claim change.
```

## Planned

```text
EAI_IMPORT_REVIEW.md
specs/eai-core-v0.1.md
schemas/eai-artifact.schema.json
schemas/agent-contract.schema.json
schemas/transformation-set.schema.json
examples/sample-eai-artifact.json
examples/sample-agent-contract.json
protocols/artifact-verification.md
CITATION.cff
.github/PULL_REQUEST_TEMPLATE.md
```

## Open Questions

```text
Final VEPL-1.0 license text
Final VSL-1.0 license text
Reference code license headers
Artifact signing method
Compatibility claim process
Transformation set v0.1
Report interpretation boundary
Public/private split for future hosted verifier
```

---

# [0.1-draft] - 2026-05-18

## Added

### Repository foundation

Created the initial canonical foundation for the `vectaetos-agentic-audit` repository.

Added or prepared the following root documents:

```text
README.md
PHILOSOPHY.md
THEORY.md
ARCHITECTURE.md
CANONICAL_STATUS.md
NOTICE.md
TRADEMARKS.md
SECURITY_POLICY.md
LICENSE.md
CALIBRATION_ANCHOR_REVIEW.md
CHANGELOG.md
```

### README.md

Added public entry document defining:

```text
VECTAETOS Agentic Audit
EAI - Epistemic Audit Interface
ContractMesh
EAT Ledger
EAI Artifact
Human Audit Report
Agentic Audit Solutions
```

Key boundary added:

```text
VECTAETOS Agentic Audit does not produce truth.
It preserves visibility of structural change.
```

ASCII-safe variant produced to avoid rendering problems with special symbols.

### PHILOSOPHY.md

Added canonical philosophy document.

Core principles:

```text
VECTAETOS is not a product.
EAI is not an agent.
EAI does not interpret.
EAI does not optimize.
EAI does not decide.
Artifacts are not verdicts.
Reports are not EAI.
Audit is not control.
Visibility is not authority.
Humility is not weakness.
```

### THEORY.md

Added formal EAI theory draft.

Defined formal objects:

```text
X = target system
Q = fixed input set
T = fixed transformation set
A = output set
C = canonicalization function
E = encoding function
d = distance function
R = relational structure
Delta = curvature structure
S = spectral structure
kappa_trace = closure trace distribution
Omega = EAI artifact
```

Defined minimal EAI form:

```text
EAI(X; Q,T,C,E,d) = Omega
```

Established that EAI produces a structural artifact, not a recommendation, classification, or decision.

### ARCHITECTURE.md

Added repository and system architecture draft.

Defined high-level stack:

```text
VECTAETOS
    |
    v
VECTAETOS Agentic Audit
    |
    v
EAI - Epistemic Audit Interface
    |
    v
ContractMesh
    |
    v
EAT Ledger
    |
    v
EAI Artifact
    |
    v
Human Audit Report
    |
    v
Agentic Audit Solutions
```

### CANONICAL_STATUS.md

Added anti-drift control document.

Recorded:

```text
accepted names
reserved names
rejected/suspended names
canonical principles
current document status
technical component status
MVP gate
commercial gate
invalid claims
accepted public phrases
forbidden public phrases
open questions
freeze conditions
```

### NOTICE.md

Added copyright, attribution, and claimed marks notice.

Defined:

```text
copyright notice
claimed marks
no implied official status
attribution requirements
non-endorsement
no legal/financial/statutory audit claim
no warranty
canonical reminder
```

### TRADEMARKS.md

Added trademark and brand-boundary policy.

Defined rules for:

```text
claimed marks
allowed descriptive use
forbidden official/certified/compliant claims
forks and derivative projects
compatibility claims
commercial use
certification boundaries
conceptual integrity of marks
```

### SECURITY_POLICY.md

Added repository security and conceptual-security policy.

Defined:

```text
technical security
conceptual security
branch protection guidance
secret policy
signing key policy
GitHub Actions policy
dependency security
code scanning guidance
artifact integrity
schema integrity
anti-drift pull request checklist
incident response
release security
connector boundaries
hosted service boundary
```

### LICENSE.md

Added layered license map.

Defined draft licensing structure:

```text
docs / philosophy / papers
    -> VEPL-1.0 draft

specs / schemas / protocols
    -> VSL-1.0 draft

reference / cli
    -> Apache-2.0 planned unless stated otherwise

examples
    -> example use / VSL-compatible draft

reports
    -> template use license boundary

brand / marks / names / logos
    -> all rights reserved

hosted services / APIs / dashboards / commercial reports
    -> proprietary commercial terms
```

Canonical license principle:

```text
Open specification.
Protected identity.
Paid verification.
```

### CALIBRATION_ANCHOR_REVIEW.md

Added review of `CALIBRATION_AND_TRAJECTORY_MAPPING_ANCHOR.md`.

Accepted as:

```text
non-executive methodological discipline
```

Not accepted as:

```text
runtime mechanism
agent module
optimizer
validator
decision system
truth engine
deployment gate
scoring layer
control layer
```

Core accepted memory:

```text
No implementation may outrun ontology.
No anchor may outrun mapping.
No guard may become authority.
```

---

## Changed

### Naming hierarchy stabilized

Accepted naming map:

```text
VECTAETOS
    -> framework root

VECTAETOS Agentic Audit
    -> applied audit architecture

Agentic Audit Solutions
    -> commercial service line

EAI
    -> Epistemic Audit Interface

ContractMesh
    -> operational contract protocol

EAT Ledger
    -> tamper-evident audit trace layer

EAI Artifact
    -> machine-verifiable structural artifact

kappa_trace
    -> closure trace distribution
```

### Commercial framing refined

Clarified that:

```text
VECTAETOS itself is not sold.
Commercial services may be sold around verification, hosting, reports, connectors, and integration.
Money is treated as infrastructure metabolism, not project authority.
```

### DOI timing clarified

Decision:

```text
No Zenodo DOI yet.
```

Rationale:

```text
The repository does not yet contain enough real technical content for archival release.
A DOI should follow a v0.1 tag containing at least one core spec, one schema, one sample artifact, and one sample report.
```

### EAI import strategy clarified

Decision:

```text
Existing EAI from the wider VECTAETOS corpus should be imported only after review.
```

Required process:

```text
1. collect existing EAI material
2. create EAI_IMPORT_REVIEW.md
3. compare against PHILOSOPHY.md / THEORY.md / CANONICAL_STATUS.md
4. classify as compatible / needs adaptation / drift risk
5. promote into specs/eai-core-v0.1.md only after review
```

---

## Deprecated

No deprecated files yet.

---

## Removed

No removed files yet.

---

## Rejected

Rejected or suspended names and framings:

```text
AgentLedger
    -> suspended due to potential naming conflict / unclear availability

Audit Agentic Systems
    -> rejected as main name; weaker and less brandable

AI Truth Audit
    -> rejected because it implies truth production

Autonomous Audit Agent
    -> rejected because it violates non-agentic boundary

kappa Score
    -> rejected because it converts kappa_trace into score
```

Rejected conceptual transformations:

```text
EAI -> agent
Artifact -> verdict
Report -> EAI
kappa_trace -> score
Verifier -> decision engine
Connector -> architecture
Audit -> control
Visibility -> authority
```

---

## Security

Added security principles:

```text
No secrets in repo.
No silent mutation of artifacts.
No EAI feedback into target systems.
No kappa_trace scoring.
No artifact recommendations.
No report-as-artifact confusion.
No official-status claims without permission.
No concept drift through convenience.
```

Recommended GitHub security posture:

```text
public repository
protected main branch
pull requests required
secret scanning enabled
push protection enabled
direct push disabled
force push disabled
Wiki disabled
Actions restricted to reviewed workflows
```

---

## Documentation

Current documentation state:

```text
README.md                   draft public entry
PHILOSOPHY.md               draft philosophical base
THEORY.md                   draft formal theory
ARCHITECTURE.md             draft architecture
CANONICAL_STATUS.md         anti-drift anchor
NOTICE.md                   copyright and marks notice
TRADEMARKS.md               mark policy
SECURITY_POLICY.md          security and conceptual security
LICENSE.md                  layered license map
CALIBRATION_ANCHOR_REVIEW.md methodological import review
CHANGELOG.md                project history and decision log
```

---

## Known Gaps

The following are not yet complete:

```text
full VEPL-1.0 text
full VSL-1.0 text
CITATION.cff
EAI_IMPORT_REVIEW.md
specs/eai-core-v0.1.md
schemas/eai-artifact.schema.json
schemas/agent-contract.schema.json
schemas/transformation-set.schema.json
sample EAI artifact
sample agent contract
artifact verifier
sample audit report
pull request template
contributing guide
```

---

## Next Recommended Step

Next file:

```text
EAI_IMPORT_REVIEW.md
```

Reason:

```text
EAI already exists in the wider VECTAETOS corpus and should be imported with review rather than rewritten blindly.
```

Fallback next file:

```text
CITATION.cff
```

only if the repository needs citation metadata before technical import.

---

# [0.0-pre] - Before 2026-05-18

## Context

The project emerged from the broader VECTAETOS ecosystem, including prior work on:

```text
VECTAETOS
ZMYSEL
Epistemic Cryptography
TetraGlyph
EAI
non-agentic epistemic field architecture
structural audit
relational topology
entropic humility
intrinsic humility
```

## Strategic Shift

The applied commercial direction was clarified as:

```text
Agentic Audit Solutions
```

with the core product architecture:

```text
VECTAETOS Agentic Audit
powered by EAI + ContractMesh
```

## Core Business Insight

Agentic systems will become common.

The scarce layer is not agent creation.

The scarce layer is:

```text
verifiable structural auditability
contract integrity
trace continuity
epistemic risk visibility
non-intervention artifact generation
```

## Pre-Repository Principle

Before this changelog, the core principle was already emerging:

```text
AI agents can act.
VECTAETOS makes their action auditable.
```

Later refined to:

```text
Where agents act, contracts must be visible.
Where systems drift, traces must remain.
Where meaning changes, the change must not disappear.
```

END
