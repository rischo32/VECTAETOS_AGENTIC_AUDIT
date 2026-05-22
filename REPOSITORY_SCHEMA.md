# REPOSITORY_SCHEMA

**Project:** VECTAETOS Agentic Audit  
**Status:** Draft v0.1  
**Document Type:** Repository structure map  
**Scope:** Current tracked layout after root cleanup phases 1-5  

---

## 0. Purpose

This file maps the current repository structure after the initial root cleanup.

It is descriptive.

It does not define runtime behavior.

It does not freeze EAI v0.1.

It does not convert placeholders into specifications.

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

Root files are canonical, administrative, commercial-positioning, or cleanup-control files.

Temporary upstream EAI source files and EAI reference Python files have been moved out of root.

---

## 2. Reviews

```text
reviews/
├── CALIBRATION_ANCHOR_REVIEW.md
├── EAI_CORPUS_INVENTORY.md
└── EAI_IMPORT_REVIEW.md
```

Review files record import and compatibility decisions.

They do not define runtime behavior.

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

`docs/upstream-vectaetos/eai/` contains upstream EAI source material.

It is accepted for controlled import, but it is not automatically the final v0.1 specification.

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
├── eai-core-v0.1.md
├── eai-artifact.schema.json
├── agent-contract.schema.json
├── agent-event.schema.json
├── audit-report.schema.json
└── transformation-set.schema.json
```

Current status:

```text
specs/ files exist as placeholders
specs/ files are not yet canonical technical specifications
```

Important note:

```text
Schema file placement is still under review.
Future cleanup may move JSON schemas from specs/ to schemas/.
```

---

## 6. Examples

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
```

---

## 7. Reference

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

## 8. Legal

```text
legal/
└── VECTAETOS_AGENTIC_AUDIT_REPOSITORY_EU_AI_ACT_SCOPE_STATEMENT_v1.1.md
```

The legal scope statement is repository-specific and does not create legal advice, certification, compliance guarantee, or official authority.

---

## 9. Research

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

## 10. Papers

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

## 11. Incubator

```text
incubator/
├── candidate-001/.gitkeep
├── candidate-002/.gitkeep
└── candidate-003/.gitkeep
```

Incubator content is non-canonical until reviewed and promoted.

---

## 12. GitHub Metadata

```text
.github/
└── CODEOWNERS
```

Future expected files:

```text
.github/PULL_REQUEST_TEMPLATE.md
```

---

## 13. Cleanup Status

Completed cleanup phases:

```text
Phase 1: target directories prepared
Phase 2: review documents moved to reviews/
Phase 3: upstream EAI documents moved to docs/upstream-vectaetos/eai/
Phase 4: EAI Python reference files moved to reference/python/eai/
Phase 5: architecture map documents moved to docs/architecture/
```

Remaining structural questions:

```text
1. Whether JSON schemas stay in specs/ or move to schemas/.
2. Whether protocols placeholders should be filled or pruned before v0.1.
3. Whether research files remain as-is or get classified further.
4. Whether KOMERCIALIZACIA.md moves under docs/commercial/ or brand/.
5. Whether the handoff anchor remains root or moves under docs/handoff/.
```

---

## 14. Non-Drift Reminder

```text
Repository structure is not ontology.
Placeholder is not specification.
Research is not authority.
Review is not runtime.
Reference code is not production service code.
No implementation may outrun ontology.
```

END
