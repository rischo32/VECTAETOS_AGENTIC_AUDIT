# CANONICAL_STATUS

**Project:** VECTAETOS Agentic Audit  
**Repository:** `vectaetos-agentic-audit`  
**Status:** Draft v0.1  
**Ontology:** Not frozen  
**Implementation:** Pre-MVP  
**Commercial Layer:** Defined, not production-active  
**Last Updated:** 2026-05-22  

---

## 0. Purpose

This file defines the current canonical status of the repository.

It is a control document.

Its purpose is to prevent conceptual drift.

If another file contradicts this file, the contradiction must be reviewed before the repository can advance.

Conversational statements, research notes, placeholders, and reference code are not automatically canonical.

---

## 1. Current Canonical Layer Map

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

Layer rule:

```text
artifact != report
report != EAI
ledger != truth proof
verifier != decision engine
connector != architecture
commercial layer != ontology
```

---

## 2. Accepted Names

| Name | Status | Role |
|---|---|---|
| VECTAETOS | Accepted | Non-saleable framework root |
| VECTAETOS Agentic Audit | Accepted | Applied audit architecture |
| Agentic Audit Solutions | Accepted | Commercial service bridge |
| EAI | Accepted | Epistemic Audit Interface |
| Epistemic Audit Interface | Accepted | Non-intervention projection kernel |
| ContractMesh | Accepted | Operational contract protocol |
| EAT Ledger | Accepted | Tamper-evident audit trace layer |
| EAI Artifact | Accepted | Machine-verifiable structural artifact |
| Human Audit Report | Accepted | Interpretive report layer |
| kappa_trace | Accepted | Structural trace, not score |

---

## 3. Reserved, Suspended, and Rejected Names

Reserved names:

```text
EAI Verifier
ContractMesh Verifier
Agentic Audit Report
VECTAETOS Compatibility Process
Agentic Audit Certificate
```

Suspended or rejected names:

```text
AgentLedger = suspended
Audit Agentic Systems = rejected as main name
AI Truth Audit = rejected
Autonomous Audit Agent = rejected
kappa Score = rejected
```

Reserved names may not be used as official product claims until specified.

---

## 4. Canonical Principles

```text
1. VECTAETOS is not a product.
2. VECTAETOS is not sold.
3. EAI is not an agent.
4. EAI does not interpret.
5. EAI does not optimize.
6. EAI does not decide.
7. EAI produces artifacts, not verdicts.
8. kappa_trace is not a score.
9. Reports are not EAI.
10. Artifacts are not recommendations.
11. ContractMesh contracts are operational contracts, not legal contracts by default.
12. EAT Ledger records traces; it does not interpret.
13. Audit is not control.
14. Visibility is not authority.
15. Hashes, signatures, and Merkle roots are integrity witnesses, not truth witnesses.
16. No implementation may outrun ontology.
17. No anchor may outrun mapping.
18. No guard may become authority.
```

---

## 5. Current Root Documents

| File | Status | Purpose |
|---|---|---|
| `README.md` | Draft v0.1 | Public entry point |
| `PHILOSOPHY.md` | Draft v0.1 | Canonical philosophical base |
| `THEORY.md` | Draft v0.1 | Formal EAI theory |
| `REPOSITORY_ARCHITECTURE.md` | Draft v0.1 | Repository and system architecture |
| `CANONICAL_STATUS.md` | Draft v0.1 | Status and anti-drift control |
| `CHANGELOG.md` | Draft v0.1 | Version and decision history |
| `NOTICE.md` | Draft v0.1 | Copyright and attribution notice |
| `TRADEMARKS.md` | Draft v0.1 | Mark usage boundary |
| `LICENSE.md` | Draft v0.1 | License map and usage boundary |
| `SECURITY.md` | Draft v0.1 | Technical and conceptual security policy |
| `REPOSITORY_SCHEMA.md` | Draft v0.1 | Current repository structure map |
| `ROOT_CLEANUP_PLAN.md` | Draft v0.1 | Non-executive cleanup/refactor map |
| `REFACTORING_NOTE.md` | Temporary staging note | Historical cleanup/control note |
| `KOMERCIALIZACIA.md` | Commercial boundary note | VECTAETOS non-saleable / VAA sellable boundary |
| `VECTAETOS_AGENTIC_AUDIT_HANDOFF_ANCHOR.md` | Handoff anchor v0.1 | Continuity anchor for future chats/models |

---

## 6. Current Repository Structure Status

Initial root cleanup phases 1-5 are complete.

```text
reviews/                         = review records
docs/architecture/               = architecture maps
docs/upstream-vectaetos/eai/      = upstream EAI source material
reference/python/eai/             = EAI reference candidate code
specs/                            = spec/schema placeholders, not frozen
examples/                         = sample placeholders, not authoritative
research/                         = non-canonical research candidates
legal/                            = repository-specific legal/regulatory scope material
```

Repository structure is descriptive.

Repository structure is not ontology.

Placeholder is not specification.

Reference code is not production service code.

---

## 7. Review Documents

| File | Status | Purpose |
|---|---|---|
| `reviews/CALIBRATION_ANCHOR_REVIEW.md` | Accepted as methodological review | Classifies calibration anchor as non-executive discipline |
| `reviews/EAI_CORPUS_INVENTORY.md` | Inventory v0.1 | Describes upstream EAI corpus without final decisions |
| `reviews/EAI_IMPORT_REVIEW.md` | Import Review v0.1 | Accepts EAI for controlled import; not frozen |

Review documents are project memory and import records.

They do not define runtime behavior by themselves.

---

## 8. EAI Import Status

EAI upstream material is accepted for controlled import.

Current source locations:

```text
docs/upstream-vectaetos/eai/CONSTRAINTS.md
docs/upstream-vectaetos/eai/DO_NOT_OPTIMIZE.md
docs/upstream-vectaetos/eai/philosophy.md
docs/upstream-vectaetos/eai/theory.md
docs/upstream-vectaetos/eai/mathematics.md

reference/python/eai/__init__.py
reference/python/eai/implementation.py
reference/python/eai/encode_v2.py
reference/python/eai/encode_v3.py
reference/python/eai/delta.py
reference/python/eai/spectral.py
reference/python/eai/kappa.py
```

Current verdict:

```text
ACCEPTED FOR IMPORT
NOT YET FROZEN
TECHNICAL ADAPTATION REQUIRED
NO PRODUCT NAMING CONCLUSIONS YET
```

Required precision questions before `specs/eai-core-v0.1.md` may become canonical:

```text
1. Transform mode
2. kappa_trace vs kappa_signature
3. Delta observable family
4. R_distance vs R_antisymmetric
5. Complex spectrum JSON serialization
6. Fingerprint h outside EAI v0.1 core unless explicitly justified
```

---

## 9. Current Technical Components

| Component | Status | Notes |
|---|---|---|
| EAI Core | Theoretical draft | Requires resolution of precision questions before freeze |
| EAI reference code | Reference candidate | Located in `reference/python/eai/` |
| ContractMesh | Conceptual draft | Needs agent contract schema and protocol specification |
| EAT Ledger | Conceptual draft | Needs ledger event schema and append protocol |
| EAI Artifact | Conceptual draft | Needs JSON schema and sample artifact |
| Artifact Verifier | Not started | Required for MVP |
| Report Template | Placeholder | Required for first commercial demo |
| Connectors | Not started | Later phase |
| Dashboard | Not started | Not part of first MVP |

---

## 10. Specs, Schemas, and Examples

Current placeholder files:

```text
specs/eai-core-v0.1.md
specs/eai-artifact.schema.json
specs/agent-contract.schema.json
specs/agent-event.schema.json
specs/audit-report.schema.json
specs/transformation-set.schema.json

examples/sample-agent-contract.json
examples/sample-transformation-set.json
examples/sample-eai-artifact.json
examples/sample-agentic-audit-report.md
```

Status:

```text
placeholders exist
not frozen
not authoritative
must not outrun EAI import review
```

Schema location remains under review:

```text
JSON schema files currently exist under specs/.
Future cleanup may move them to schemas/.
```

---

## 11. Minimum MVP Gate

The first MVP is not a dashboard.

The first MVP is:

```text
1. agent contract schema
2. transformation set schema
3. EAI artifact schema
4. sample agent contract
5. sample transformation set
6. sample EAI artifact
7. artifact verifier
8. sample human audit report
```

MVP success condition:

> A user can produce or inspect a structural artifact and verify that it is well-formed and tamper-evident.

---

## 12. Commercial Boundary

```text
VECTAETOS is not sold.
VECTAETOS Agentic Audit may become applied audit infrastructure.
Agentic Audit Solutions may sell reports, verification, hosting, connectors, and implementation support.
```

Commercial language must preserve:

```text
artifact != report
verification != certification by default
traceability != compliance guarantee
integrity witness != truth witness
```

---

## 13. Invalid Claims

The following claims are invalid and must not appear in repository materials.

```text
EAI proves truth.
EAI certifies safety.
EAI guarantees compliance.
EAI replaces human judgment.
EAI decides whether an agent is good.
kappa_trace is a quality score.
Reports are raw EAI output.
ContractMesh creates legal contracts by default.
VECTAETOS is a SaaS product.
VECTAETOS Agentic Audit is an autonomous audit agent.
```

---

## 14. Accepted Public Phrases

```text
Verifiable structural auditability for agentic systems.
Contracts, not prompts.
Audit without control.
Structural artifacts, not decisions.
Non-intervention projection layer.
Open specification. Protected identity. Paid verification.
Where meaning changes, the change must not disappear.
```

---

## 15. Open Questions

```text
1. Final license structure.
2. Final compatibility process.
3. Artifact signing and key management.
4. Transformation set freezing and naming.
5. Report layer boundaries and mandatory disclaimers.
6. Commercial boundary between open material and paid verification.
7. JSON schema placement: specs/ or schemas/.
8. Whether KOMERCIALIZACIA.md remains root or moves later.
9. Whether the handoff anchor remains root or moves later.
```

---

## 16. Versioning Rule

```text
PATCH:
- wording
- typo
- formatting
- clarification without conceptual change
- file movement without semantic change

MINOR:
- new schema fields
- new examples
- new protocols
- compatible extensions

MAJOR:
- change to non-intervention principle
- change to EAI output type
- change to kappa_trace meaning
- change to VECTAETOS identity
- change to artifact/report boundary
```

Any major change requires canonical review.

---

## 17. Freeze Conditions

The repository may enter `v0.1-freeze` only when:

```text
README.md exists
PHILOSOPHY.md exists
THEORY.md exists
REPOSITORY_ARCHITECTURE.md exists
CANONICAL_STATUS.md exists
NOTICE.md exists
TRADEMARKS.md exists
LICENSE.md exists
SECURITY.md exists
reviews/EAI_IMPORT_REVIEW.md exists
at least 3 core schemas exist and are non-placeholder
at least 1 sample artifact exists and is non-placeholder
at least 1 sample report exists and is non-placeholder
invalidity conditions are defined
artifact/report boundary is explicit
```

Current status:

```text
not ready for v0.1-freeze
```

---

## 18. Current Decision

Current strategic decision:

> Build the canonical foundation first.  
> Build the verifier second.  
> Build connectors third.  
> Build dashboard later.

Current cleanup decision:

> Root cleanup phases 1-5 are complete.  
> Further work should update status references before filling specs or schemas.

---

## 19. Final Canonical Reminder

```text
VECTAETOS is not sold.
EAI does not decide.
ContractMesh does not create legal personhood.
EAT Ledger does not interpret.
Reports are not artifacts.
Artifacts are not verdicts.
Visibility is not authority.
Placeholder is not specification.
Research is not authority.
Reference code is not production service code.
```

This file is the current anti-drift anchor of the repository.

END
