# VECTAETOS Agentic Audit™ — Repository Architecture

**Status:** Draft v0.1  
**Scope:** Repository structure, architectural boundaries, naming map, file responsibilities  
**Primary Repository Name:** `vectaetos-agentic-audit`  
**Commercial Line:** Agentic Audit Solutions™  
**Core Kernel:** EAI — Epistemic Audit Interface  
**Protocol Layer:** ContractMesh™  
**Audit Trace Layer:** EAT Ledger  
**Framework Root:** VECTAETOS™

---

## 0. Purpose

This document defines the canonical repository architecture for **VECTAETOS Agentic Audit™**.

The repository is not merely a code repository.  
It is the canonical structural base for:

1. philosophy,
2. theory,
3. specifications,
4. schemas,
5. protocols,
6. reference implementation,
7. examples,
8. audit artifacts,
9. licensing notices,
10. future commercial infrastructure.

The goal is to prevent conceptual drift.

---

## 1. Non-Drift Rule

Every file in this repository must respect the following boundary:

> VECTAETOS is not a product.  
> VECTAETOS Agentic Audit™ is an applied audit architecture.  
> EAI is a non-intervention projection kernel.  
> ContractMesh™ is the operational contract layer.  
> EAT Ledger is the tamper-evident trace layer.  
> Agentic Audit Solutions™ is the commercial service line.

Any file that blurs these roles must be revised or rejected.

---

## 2. Naming Map

| Name | Function | Public Role | Sellable? |
|---|---|---:|---:|
| **VECTAETOS™** | Ontological / epistemic framework | Root framework | No |
| **VECTAETOS Agentic Audit™** | Applied audit architecture | Main product architecture | Yes |
| **Agentic Audit Solutions™** | Commercial service line | Market-facing offer | Yes |
| **EAI — Epistemic Audit Interface** | Non-intervention projection kernel | Technical core | Partially |
| **ContractMesh™** | Machine-readable agent contract protocol | Technical protocol | Yes |
| **EAT Ledger** | Tamper-evident audit trace | Audit infrastructure | Yes |
| **κ_trace** | Closure trace distribution | Structural artifact | No |
| **EAI Artifact** | Output of EAI run | Verifiable structural record | Yes, via reports/API |

---

## 3. Core Architectural Stack

```text
VECTAETOS™
    ↓
VECTAETOS Agentic Audit™
    ↓
EAI — Epistemic Audit Interface
    ↓
ContractMesh™
    ↓
EAT Ledger
    ↓
Audit Artifact
    ↓
Human Audit Report
    ↓
Agentic Audit Solutions™
```

### Interpretation

- **VECTAETOS™** provides the non-agentic epistemic foundation.
- **VECTAETOS Agentic Audit™** applies this foundation to agentic systems.
- **EAI** projects structural closure traces from system reactions.
- **ContractMesh™** defines operational contracts for agents.
- **EAT Ledger** records tamper-evident audit events.
- **Audit Artifact** is the machine-verifiable output.
- **Human Audit Report** is the commercial interpretation layer.
- **Agentic Audit Solutions™** packages the service for customers.

---

## 4. Repository Root

```text
vectaetos-agentic-audit/
│
├── README.md
├── PHILOSOPHY.md
├── THEORY.md
├── ARCHITECTURE.md
├── CANONICAL_STATUS.md
├── CHANGELOG.md
├── CITATION.cff
├── NOTICE.md
├── TRADEMARKS.md
├── LICENSE.md
│
├── docs/
├── specs/
├── schemas/
├── protocols/
├── examples/
├── artifacts/
├── reports/
├── reference/
├── connectors/
├── legal/
├── brand/
├── incubator/
└── .github/
```

---

## 5. Root File Responsibilities

### `README.md`

Public entry point.

Must answer:

- What is VECTAETOS Agentic Audit™?
- What problem does it address?
- What is EAI?
- What does the repository contain?
- What is explicitly not claimed?

Must not:

- claim legal audit,
- claim financial audit,
- claim autonomous decision-making,
- claim that EAI produces truth,
- confuse EAI artifacts with human interpretation.

---

### `PHILOSOPHY.md`

Canonical philosophical foundation.

Must contain:

- non-intervention,
- non-optimization,
- non-interpretation,
- VECTAETOS as non-saleable root,
- audit as projection, not control,
- meaning drift visibility,
- κ as closure boundary, not score.

---

### `THEORY.md`

Formal-theoretical layer.

Must contain:

- system `X`,
- fixed input set `Q`,
- output set `A`,
- projection field `Φ̂`,
- encoding function,
- relational matrix `R`,
- curvature `Δ`,
- spectrum,
- `κ_trace`,
- non-absolute invariant disclaimer.

---

### `ARCHITECTURE.md`

System architecture.

Must contain:

- layer map,
- data flow,
- trust boundaries,
- non-feedback condition,
- separation between EAI Core and report layer,
- integration with ContractMesh™ and EAT Ledger.

---

### `CANONICAL_STATUS.md`

Current canonical status of repository.

Must contain:

- version,
- frozen / draft sections,
- open questions,
- invalidated terms,
- accepted naming map,
- pending decisions.

---

### `CHANGELOG.md`

Version history.

Must record:

- schema changes,
- naming changes,
- philosophical changes,
- protocol changes,
- implementation changes.

---

### `CITATION.cff`

Machine-readable citation file for academic / archival use.

---

### `NOTICE.md`

Copyright and attribution notice.

Must include:

```text
Copyright © 2026 Richard Fonfára.

VECTAETOS™, VECTAETOS Agentic Audit™, Agentic Audit Solutions™,
ContractMesh™, and EAI™ are claimed marks of the VECTAETOS Project.
```

---

### `TRADEMARKS.md`

Trademark boundary document.

Must clarify:

- ™ means claimed unregistered mark,
- no use of marks implies endorsement,
- no compatibility claim without permission or verification,
- no derivative project may claim official status.

---

### `LICENSE.md`

License map.

Must not be a single undifferentiated license.

Recommended structure:

```text
/docs, /philosophy, /papers
→ VEPL-1.0

/specs, /schemas
→ VSL-1.0

/reference
→ Apache-2.0 unless stated otherwise

/brand, names, logos
→ All rights reserved

/hosted verifier, reports, SaaS
→ proprietary commercial license
```

---

## 6. `/docs`

Purpose: explanatory human-readable documentation.

```text
docs/
├── 00-overview.md
├── 01-problem-category.md
├── 02-agentic-systems-accountability.md
├── 03-contracts-not-prompts.md
├── 04-audit-without-control.md
├── 05-epistemic-risk.md
├── 06-non-intervention-principle.md
├── 07-commercial-boundary.md
└── glossary.md
```

### File Roles

#### `00-overview.md`
General overview for readers.

#### `01-problem-category.md`
Defines the market problem: agentic systems without accountability.

#### `02-agentic-systems-accountability.md`
Defines the category.

#### `03-contracts-not-prompts.md`
Explains why agents should be bounded by machine-readable contracts, not only prompts.

#### `04-audit-without-control.md`
Explains non-intervention audit.

#### `05-epistemic-risk.md`
Explains overclaim, false certainty, uncertainty visibility.

#### `06-non-intervention-principle.md`
Explains why EAI cannot influence the target system.

#### `07-commercial-boundary.md`
Separates VECTAETOS from commercial products.

#### `glossary.md`
Canonical term definitions.

---

## 7. `/specs`

Purpose: normative technical specifications.

```text
specs/
├── eai-core-v0.1.md
├── contractmesh-v0.1.md
├── eat-ledger-v0.1.md
├── audit-artifact-v0.1.md
├── agentic-audit-report-v0.1.md
├── compatibility-v0.1.md
└── invalidity-conditions.md
```

### `eai-core-v0.1.md`

Must define:

```text
EAI = non-intervention projection mechanism
Input: system X, fixed input set Q, fixed transformations T
Output: structural artifact only
No insights
No recommendations
No classifications
No scores
No feedback
```

---

### `contractmesh-v0.1.md`

Must define:

- agent contract format,
- role boundaries,
- allowed inputs,
- allowed outputs,
- allowed tools,
- forbidden outputs,
- decision scope,
- versioning,
- hashing,
- signature requirements.

---

### `eat-ledger-v0.1.md`

Must define:

- append-only events,
- event hash,
- previous event hash,
- artifact hash,
- timestamp,
- signature,
- verification rules.

---

### `audit-artifact-v0.1.md`

Must define the EAI artifact as a machine-verifiable structural record.

---

### `agentic-audit-report-v0.1.md`

Must define the report layer.

Important:

> Reports may interpret artifacts.  
> EAI itself may not.

---

### `compatibility-v0.1.md`

Must define what may be called:

- EAI-compatible,
- ContractMesh-compatible,
- VECTAETOS Agentic Audit-compatible,
- official implementation,
- unofficial implementation.

---

### `invalidity-conditions.md`

Must define when a system becomes invalid.

Examples:

```text
adaptive transformations → INVALID
feedback into system → INVALID
output-dependent input selection → INVALID
κ interpreted as score inside EAI → INVALID
EAI used as decision module → INVALID
```

---

## 8. `/schemas`

Purpose: JSON Schemas for machine-readable structures.

```text
schemas/
├── agent-contract.schema.json
├── agent-event.schema.json
├── transformation-set.schema.json
├── eai-run.schema.json
├── eai-artifact.schema.json
├── audit-ledger-event.schema.json
├── audit-report.schema.json
└── compatibility-claim.schema.json
```

### Required Schemas

#### `agent-contract.schema.json`

Defines an operational contract for an agent.

Core fields:

```text
contract_id
agent_id
role
allowed_inputs
allowed_outputs
forbidden_outputs
tools_allowed
decision_scope
confidence_policy
escalation_policy
version
previous_contract_hash
contract_hash
issuer_signature
```

---

#### `agent-event.schema.json`

Defines signed agent event.

Core fields:

```text
event_id
run_id
sender_agent
recipient_agent
sender_contract_hash
message_type
payload_hash
evidence_hashes
uncertainty
claim_strength
timestamp
previous_event_hash
signature
```

---

#### `transformation-set.schema.json`

Defines immutable transformation set.

Core fields:

```text
transformation_set_id
version
transformations
immutability_hash
created_at
signature
```

---

#### `eai-run.schema.json`

Defines one deterministic EAI execution.

Core fields:

```text
run_id
system_id
input_set_hash
transformation_set_hash
encoder_version
distance_metric
timestamp
runner_version
```

---

#### `eai-artifact.schema.json`

Defines EAI output.

Core fields:

```text
artifact_id
run_id
system_id
input_set_hash
transformation_set_hash
encoding_model
distance_metric
R
delta_curvature
spectrum
kappa_trace
previous_artifact_hash
artifact_hash
signature
```

---

#### `audit-ledger-event.schema.json`

Defines append-only ledger event.

---

#### `audit-report.schema.json`

Defines human-facing report metadata.

---

#### `compatibility-claim.schema.json`

Defines how third parties may claim compatibility.

---

## 9. `/protocols`

Purpose: procedural rules.

```text
protocols/
├── non-intervention.md
├── fixed-transformations.md
├── encoding-canonicalization.md
├── relational-matrix.md
├── curvature-delta.md
├── kappa-trace.md
├── artifact-generation.md
├── artifact-verification.md
├── contract-registration.md
├── contract-versioning.md
├── event-signing.md
├── ledger-append.md
├── drift-detection.md
└── report-generation.md
```

### Protocol Boundaries

#### `non-intervention.md`
Defines `∂Φ / ∂EAI = 0`.

#### `fixed-transformations.md`
Defines how transformations are created, frozen, hashed, and used.

#### `encoding-canonicalization.md`
Defines how outputs are normalized before encoding.

#### `relational-matrix.md`
Defines `R`.

#### `curvature-delta.md`
Defines cyclic inconsistency.

#### `kappa-trace.md`
Defines closure trace.

#### `artifact-generation.md`
Defines artifact construction.

#### `artifact-verification.md`
Defines verification steps.

#### `contract-registration.md`
Defines how agent contracts are registered.

#### `contract-versioning.md`
Defines how contracts change without mutation.

#### `event-signing.md`
Defines event signatures.

#### `ledger-append.md`
Defines append-only ledger.

#### `drift-detection.md`
Defines structural drift.

#### `report-generation.md`
Defines human report generation from artifacts.

---

## 10. `/examples`

Purpose: concrete examples for users and developers.

```text
examples/
├── agent-contracts/
│   ├── sales-agent-contract.json
│   ├── research-agent-contract.json
│   ├── finance-agent-contract.json
│   └── strategy-agent-contract.json
│
├── transformation-sets/
│   ├── basic-agentic-transformations.json
│   └── contradiction-pressure-transformations.json
│
├── eai-runs/
│   ├── sample-eai-run.json
│   └── sample-eai-artifact.json
│
├── ledgers/
│   └── sample-ledger.jsonl
│
└── reports/
    └── sample-agentic-audit-report.md
```

---

## 11. `/artifacts`

Purpose: generated structural artifacts.

```text
artifacts/
├── README.md
├── samples/
├── signed/
└── archived/
```

Rules:

- artifacts must be immutable once published,
- modified artifact = new artifact,
- no artifact may contain interpretation as EAI output,
- artifact may be referenced by reports.

---

## 12. `/reports`

Purpose: human-facing interpretations.

```text
reports/
├── README.md
├── templates/
│   ├── agentic-audit-report-template.md
│   └── contract-drift-report-template.md
│
├── samples/
│   ├── sample-agentic-audit-report.md
│   └── sample-contract-drift-report.md
│
└── disclaimers/
    ├── not-legal-audit.md
    ├── not-financial-audit.md
    └── interpretation-boundary.md
```

Important:

> Reports are not EAI artifacts.  
> Reports are interpretive human/business documents generated from artifacts.

---

## 13. `/reference`

Purpose: reference implementation.

```text
reference/
├── README.md
├── python/
│   ├── eai_runner/
│   ├── eai_verifier/
│   ├── contractmesh/
│   ├── eat_ledger/
│   └── report_generator/
│
├── cli/
│   ├── eai
│   └── contractmesh
│
└── tests/
    ├── test_artifact_schema.py
    ├── test_non_intervention.py
    ├── test_contract_hash.py
    ├── test_ledger_chain.py
    └── test_invalidity_conditions.py
```

### Minimal CLI Target

```bash
eai run config.json
eai verify artifact.json
contractmesh register contract.json
contractmesh verify contract.json
eat-ledger append event.jsonl
```

---

## 14. `/connectors`

Purpose: integrations with external automation and agent platforms.

```text
connectors/
├── README.md
├── n8n/
├── make/
├── zapier/
├── pipedream/
├── langgraph/
└── openai-agents-sdk/
```

### Priority Order

```text
1. n8n
2. Make
3. Zapier
4. Pipedream
5. LangGraph
6. OpenAI Agents SDK
```

Connectors are distribution channels, not conceptual core.

---

## 15. `/legal`

Purpose: legal and license boundary.

```text
legal/
├── README.md
├── copyright-notice.md
├── trademark-notice.md
├── license-map.md
├── non-legal-disclaimer.md
├── audit-disclaimer.md
├── brand-usage.md
├── compatibility-claims.md
├── third-party-use.md
└── commercial-terms-placeholder.md
```

Mandatory disclaimers:

```text
Not a statutory audit.
Not legal advice.
Not financial assurance.
Not insurance.
Not regulatory certification.
Technical and epistemic auditability only.
```

---

## 16. `/brand`

Purpose: identity, naming, public language.

```text
brand/
├── naming-map.md
├── approved-phrases.md
├── forbidden-phrases.md
├── public-positioning.md
├── short-description.md
├── long-description.md
└── marks.md
```

### Approved Phrases

```text
Verifiable trust infrastructure for multi-agent AI systems.
Contracts, not prompts.
Audit without control.
Structural artifacts, not decisions.
Non-intervention projection layer.
```

### Forbidden Phrases

```text
EAI decides.
EAI scores truth.
VECTAETOS certifies reality.
The system guarantees safety.
The audit proves correctness.
The agent is trusted because EAI says so.
```

---

## 17. `/incubator`

Purpose: controlled space for future candidates.

```text
incubator/
├── README.md
├── candidate-001/
│   ├── THESIS.md
│   ├── STATUS.md
│   ├── RISK.md
│   ├── FIT_WITH_VECTAETOS.md
│   ├── MONETIZATION.md
│   └── DECISION.md
│
├── candidate-002/
└── candidate-003/
```

Rules:

- incubator candidates are not canonical,
- no candidate may use official names until accepted,
- each candidate must state its relation to VECTAETOS,
- each candidate must pass non-drift review.

---

## 18. `.github`

Purpose: governance and issue templates.

```text
.github/
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   ├── schema_change.md
│   ├── philosophical_drift.md
│   ├── compatibility_claim.md
│   └── implementation_question.md
│
├── PULL_REQUEST_TEMPLATE.md
└── workflows/
    ├── validate-schemas.yml
    ├── run-tests.yml
    └── check-license-headers.yml
```

---

## 19. Data Flow

```text
Fixed Input Set Q
      ↓
Fixed Transformation Set T
      ↓
Target System X
      ↓
System Responses A
      ↓
Canonicalization
      ↓
Encoding
      ↓
Relational Matrix R
      ↓
Curvature Δ
      ↓
Spectrum
      ↓
κ_trace
      ↓
EAI Artifact
      ↓
Hash + Signature
      ↓
EAT Ledger
      ↓
Human Audit Report
```

---

## 20. Trust Boundary Map

```text
[Target System X]
    │
    │ responses only
    ↓
[EAI Core]
    │
    │ structural artifact only
    ↓
[EAT Ledger]
    │
    │ hash / signature / append-only trace
    ↓
[Report Layer]
    │
    │ human-readable interpretation
    ↓
[Customer / Auditor / Operator]
```

### Forbidden Reverse Flow

```text
Report Layer → EAI Core
EAI Core → Target System X
Ledger → Target System X
Artifact → Input Selection
Output → Transformation Selection
```

Any reverse flow invalidates the run.

---

## 21. Canonical Invalidity Conditions

A run is invalid if:

```text
1. Transformations are modified during the run.
2. Inputs are selected based on prior outputs.
3. Outputs influence future prompts.
4. The system receives feedback from EAI.
5. EAI produces recommendations inside core.
6. κ_trace is treated as a score inside EAI.
7. Artifact is mutated after generation.
8. Hash chain is broken.
9. Agent contract changes without version event.
10. Report is presented as direct EAI output.
```

---

## 22. Minimal MVP Scope

The first working release should include only:

```text
README.md
PHILOSOPHY.md
THEORY.md
ARCHITECTURE.md
NOTICE.md
TRADEMARKS.md
LICENSE.md

specs/eai-core-v0.1.md
specs/contractmesh-v0.1.md
schemas/eai-artifact.schema.json
schemas/agent-contract.schema.json
schemas/agent-event.schema.json

examples/sample-agent-contract.json
examples/sample-eai-artifact.json
reports/samples/sample-agentic-audit-report.md

reference/python/eai_verifier/
```

Do not build dashboard first.

---

## 23. Monetization Boundary

Open / public:

```text
philosophy
theory
schemas
sample artifacts
protocol descriptions
reference verifier
```

Paid / protected:

```text
hosted verifier
signed audit certificates
commercial reports
connector automation
enterprise retention
API access
dashboard
white-label agentic audit reports
```

Commercial principle:

> Open specification.  
> Protected identity.  
> Paid verification.

---

## 24. Repository Governance Rule

Changes must be classified as:

```text
PATCH  = wording, typo, clarification
MINOR  = schema or protocol extension
MAJOR  = ontology, naming, or non-intervention boundary change
```

Any change affecting non-intervention, VECTAETOS identity, EAI output type, or κ interpretation requires a major version review.

---

## 25. Final Canonical Summary

This repository defines the applied audit architecture around VECTAETOS™.

It does not sell VECTAETOS.  
It does not convert VECTAETOS into an agent.  
It does not make EAI a decision system.  
It does not interpret κ as a score.  
It does not produce truth.

It defines a way to make structural changes in agentic systems visible, verifiable, and auditable.

> If meaning changes, the change must be visible.
