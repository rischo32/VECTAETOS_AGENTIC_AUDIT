# REPOSITORY_SCHEMA

**Project:** VECTAETOS Agentic Audit  
**Status:** Draft v0.1  
**Document Type:** Repository structure map  
**Scope:** Current tracked layout after root cleanup and schema placement review  

---

## 0. Purpose

This file maps the current repository structure after the initial root cleanup and schema placeholder move.

It is descriptive.

It does not define runtime behavior.

It does not freeze EAI v0.1.

It does not convert placeholders into specifications.

Repository structure is not ontology.

---

## 1. Root

```text
vectaetos-agentic-audit/
├── README.md
├── PHILOSOPHY.md
├── THEORY.md
├── REPOSITORY_ARCHITECTURE.md
├── CANONICAL_STATUS.md
├── CHANGELOG.md
├── NOTICE.md
├── TRADEMARKS.md
├── LICENSE.md
├── SECURITY.md
├── REPOSITORY_SCHEMA.md
├── ROOT_CLEANUP_PLAN.md
├── REFACTORING_NOTE.md
├── KOMERCIALIZACIA.md
└── VECTAETOS_AGENTIC_AUDIT_HANDOFF_ANCHOR.md
```

Root files are canonical, administrative, commercial-positioning, handoff, or cleanup-control files.

Temporary upstream EAI source files, EAI reference Python files, review documents, architecture maps, and JSON schema placeholders have been moved out of root.

---

## 2. Reviews

```text
reviews/
├── CALIBRATION_ANCHOR_REVIEW.md
├── EAI_CORPUS_INVENTORY.md
├── EAI_IMPORT_REVIEW.md
└── SCHEMA_PLACEMENT_REVIEW.md
```

Review files record import, compatibility, and repository-structure decisions.

They do not define runtime behavior by themselves.

---

## 3. Documentation

```text
docs/
├── architecture/
│   ├── DATA_FLOW.md
│   └── TRUST_BOUNDARY_MAP.md
│
└── upstream-vectaetos/
    └── eai/
        ├── CONSTRAINTS.md
        ├── DO_NOT_OPTIMIZE.md
        ├── philosophy.md
        ├── theory.md
        └── mathematics.md
```

`docs/architecture/` contains architecture maps.

`docs/upstream-vectaetos/eai/` contains upstream EAI source material.

Upstream EAI material is accepted for controlled import, but it is not automatically the final v0.1 specification.

---

## 4. Protocols

```text
protocols/
├── README.md
├── FAIL_LOWER_DRIFT.md
├── CALIBRATION_AND_TRAJECTORY_MAPPING_ANCHOR.md
├── non-intervention.md
├── fixed-transformations.md
├── encoding-canonicalization.md
├── relational-matrix.md
├── curvature-delta.md
├── kappa-trace.md
└── artifact-verification.md
```

Current status:

```text
FAIL_LOWER_DRIFT.md = drafted protocol
CALIBRATION_AND_TRAJECTORY_MAPPING_ANCHOR.md = upstream methodological anchor
other protocol files = placeholders unless filled later
```

---

## 5. Specs

```text
specs/
└── eai-core-v0.1.md
```

Current status:

```text
specs/ contains prose technical specifications
specs/eai-core-v0.1.md exists as a placeholder
specs/ files are not yet canonical technical specifications
```

Future expected prose specs may include:

```text
specs/contractmesh-v0.1.md
specs/eat-ledger-v0.1.md
specs/audit-artifact-v0.1.md
specs/agentic-audit-report-v0.1.md
specs/compatibility-v0.1.md
specs/invalidity-conditions.md
```

---

## 6. Schemas

```text
schemas/
├── eai-artifact.schema.json
├── agent-contract.schema.json
├── agent-event.schema.json
├── audit-report.schema.json
└── transformation-set.schema.json
```

Current status:

```text
schemas/ contains machine-readable JSON schema placeholders
schema files are not yet authoritative
schema files must not outrun EAI import review or related specs
```

Placement decision:

```text
specs/   = prose technical specifications
schemas/ = machine-readable JSON schemas
```

This decision is recorded in:

```text
reviews/SCHEMA_PLACEMENT_REVIEW.md
```

---

## 7. Examples

```text
examples/
├── sample-agent-contract.json
├── sample-agentic-audit-report.md
├── sample-eai-artifact.json
└── sample-transformation-set.json
```

Current status:

```text
examples/ files exist as placeholders
examples/ files must not outrun schemas
examples/ files are not authoritative until validated against reviewed schemas
```

---

## 8. Reference

```text
reference/
├── non_agentic_system.py
├── cli/
│   └── .gitkeep
└── python/
    ├── .gitkeep
    └── eai/
        ├── __init__.py
        ├── implementation.py
        ├── encode_v2.py
        ├── encode_v3.py
        ├── delta.py
        ├── spectral.py
        └── kappa.py
```

Current status:

```text
reference/python/eai/ contains EAI reference candidates
reference/non_agentic_system.py is a broader non-agentic prototype
reference code is not yet production-ready service code
```

---

## 9. Legal

```text
legal/
└── VECTAETOS_AGENTIC_AUDIT_REPOSITORY_EU_AI_ACT_SCOPE_STATEMENT_v1.1.md
```

The legal scope statement is repository-specific and does not create legal advice, certification, compliance guarantee, or official authority.

---

## 10. Research

```text
research/
├── MVP_core.md
├── agent_contract.json
├── repo_schema.md
├── signed_envelopes.json
└── workflow.md
```

Research files are non-canonical candidates.

They may guide later product/service work, but they do not override canonical files, review decisions, security boundaries, or EAI constraints.

---

## 11. Papers

```text
papers/
└── vectaetos_non_intervention_framework.pdf
```

Current status:

```text
paper file exists as placeholder / release candidate location
paper content must be reviewed before release or DOI use
```

---

## 12. Incubator

```text
incubator/
├── candidate-001/.gitkeep
├── candidate-002/.gitkeep
└── candidate-003/.gitkeep
```

Incubator content is non-canonical until reviewed and promoted.

---

## 13. GitHub Metadata

```text
.github/
├── CODEOWNERS
└── PULL_REQUEST_TEMPLATE.md
```

Current status:

```text
CODEOWNERS defines protected review ownership.
PULL_REQUEST_TEMPLATE.md defines anti-drift review checklist.
```

---

## 14. Cleanup Status

Completed cleanup phases:

```text
Phase 1: target directories prepared
Phase 2: review documents moved to reviews/
Phase 3: upstream EAI documents moved to docs/upstream-vectaetos/eai/
Phase 4: EAI Python reference files moved to reference/python/eai/
Phase 5: architecture map documents moved to docs/architecture/
Phase 6: schema placement reviewed
Phase 7: JSON schema placeholders moved to schemas/
```

Remaining structural questions:

```text
1. Whether protocol placeholders should be filled or pruned before v0.1.
2. Whether research files remain as-is or get classified further.
3. Whether KOMERCIALIZACIA.md moves under docs/commercial/ or brand/.
4. Whether the handoff anchor remains root or moves under docs/handoff/.
5. Whether REFACTORING_NOTE.md remains root after cleanup is fully complete.
```

---

## 15. Non-Drift Reminder

```text
Repository structure is not ontology.
Placeholder is not specification.
Schema placement is not schema authority.
Research is not authority.
Review is not runtime.
Reference code is not production service code.
No implementation may outrun ontology.
```

END
