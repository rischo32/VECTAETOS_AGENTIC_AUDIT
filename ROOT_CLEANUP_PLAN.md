# ROOT_CLEANUP_PLAN

**Project:** VECTAETOS Agentic Audit  
**Status:** Draft v0.1  
**Document Type:** Repository cleanup plan / non-executive refactor map  
**Purpose:** Define safe movement from temporary root staging toward v0.1 repository structure.  

---

## 0. Purpose

This file maps current tracked repository files to their intended structural layer before `v0.1-freeze`.

It does not move files.

It does not redefine architecture.

It does not introduce new product names.

It exists to prevent root staging from becoming canonical architecture.

---

## 1. Cleanup Rule

```text
Temporary staging is allowed.
Root convenience must not become architecture.
No implementation may outrun ontology.
No anchor may outrun mapping.
No guard may become authority.
```

Root cleanup must preserve:

```text
EAI is not an agent.
EAI does not optimize.
EAI does not interpret.
EAI produces artifacts, not verdicts.
kappa_trace is not a score.
Reports are not EAI.
Artifacts are not recommendations.
Visibility is not authority.
VECTAETOS is not sold.
```

---

## 2. Target Root Policy

Before `v0.1-freeze`, repository root should contain only high-level canonical and administrative files.

Recommended root:

```text
README.md
PHILOSOPHY.md
THEORY.md
REPOSITORY_ARCHITECTURE.md
CANONICAL_STATUS.md
CHANGELOG.md
NOTICE.md
TRADEMARKS.md
LICENSE.md
SECURITY.md
CITATION.cff
REPOSITORY_SCHEMA.md
VECTAETOS_AGENTIC_AUDIT_HANDOFF_ANCHOR.md
REFACTORING_NOTE.md
ROOT_CLEANUP_PLAN.md
```

Optional root files:

```text
CONTRIBUTING.md
CODE_OF_CONDUCT.md
```

---

## 3. Current File Map

| Current path | Current role | Target path | Action | Risk |
|---|---|---|---|---|
| `README.md` | public entry | `README.md` | keep | low |
| `PHILOSOPHY.md` | canonical philosophy | `PHILOSOPHY.md` | keep | low |
| `THEORY.md` | canonical theory | `THEORY.md` | keep | low |
| `REPOSITORY_ARCHITECTURE.md` | repository architecture | `REPOSITORY_ARCHITECTURE.md` | keep | low |
| `CANONICAL_STATUS.md` | anti-drift status | `CANONICAL_STATUS.md` | keep | low |
| `CHANGELOG.md` | decision log | `CHANGELOG.md` | keep | low |
| `NOTICE.md` | copyright / marks notice | `NOTICE.md` | keep | low |
| `TRADEMARKS.md` | brand boundary | `TRADEMARKS.md` | keep | low |
| `LICENSE.md` | license map | `LICENSE.md` | keep | low |
| `SECURITY.md` | security policy | `SECURITY.md` | keep | low |
| `REPOSITORY_SCHEMA.md` | intended repo structure | `REPOSITORY_SCHEMA.md` | keep and update after moves | medium |
| `VECTAETOS_AGENTIC_AUDIT_HANDOFF_ANCHOR.md` | handoff anchor | root or `docs/handoff/` | keep for now | low |
| `REFACTORING_NOTE.md` | staging note | `REFACTORING_NOTE.md` or `_REFACTORING_NOTE.md` | keep until cleanup complete | low |
| `ROOT_CLEANUP_PLAN.md` | cleanup plan | `ROOT_CLEANUP_PLAN.md` | keep until cleanup complete | low |
| `DATA_FLOW.md` | extracted architecture diagram | `docs/architecture/DATA_FLOW.md` or keep temporarily | move later | low |
| `TRUST_BOUNDARY_MAP.md` | extracted trust-boundary diagram | `docs/architecture/TRUST_BOUNDARY_MAP.md` or keep temporarily | move later | low |
| `KOMERCIALIZACIA.md` | commercial boundary note | `docs/commercial/KOMERCIALIZACIA.md` or `brand/public-positioning.md` | move later | medium |
| `CALIBRATION_ANCHOR_REVIEW.md` | review document | `reviews/CALIBRATION_ANCHOR_REVIEW.md` | move | low |
| `EAI_CORPUS_INVENTORY.md` | EAI inventory | `reviews/EAI_CORPUS_INVENTORY.md` | move | low |
| `EAI_IMPORT_REVIEW.md` | EAI import review | `reviews/EAI_IMPORT_REVIEW.md` | move | low |
| `CONSTRAINTS.md` | upstream EAI constraints | `docs/upstream-vectaetos/eai/CONSTRAINTS.md` | move | low |
| `DO_NOT_OPTIMIZE.md` | upstream EAI constraint anchor | `docs/upstream-vectaetos/eai/DO_NOT_OPTIMIZE.md` | move | low |
| `philosophy.md` | upstream EAI philosophy | `docs/upstream-vectaetos/eai/philosophy.md` | move | low |
| `theory.md` | upstream EAI theory | `docs/upstream-vectaetos/eai/theory.md` | move | low |
| `mathematics.md` | upstream EAI math sketch | `docs/upstream-vectaetos/eai/mathematics.md` | move | medium |
| `__init__.py` | root Python staging | `reference/python/eai/__init__.py` | move | medium |
| `implementation.py` | EAI reference candidate | `reference/python/eai/implementation.py` | move | medium |
| `encode_v2.py` | EAI encoder candidate | `reference/python/eai/encode_v2.py` | move | medium |
| `encode_v3.py` | EAI encoder candidate | `reference/python/eai/encode_v3.py` | move | medium |
| `delta.py` | EAI delta candidate | `reference/python/eai/delta.py` | move | medium |
| `spectral.py` | EAI spectral candidate | `reference/python/eai/spectral.py` | move | medium |
| `kappa.py` | EAI kappa candidate | `reference/python/eai/kappa.py` | move | medium |
| `reference/non_agentic_system.py` | broader non-agentic prototype | `reference/non_agentic_system.py` or `reference/python/vectaetos/non_agentic_system.py` | keep for now | medium |
| `protocols/README.md` | protocol index | `protocols/README.md` | keep | low |
| `protocols/FAIL_LOWER_DRIFT.md` | anti-drift protocol | `protocols/FAIL_LOWER_DRIFT.md` | keep | low |
| `protocols/CALIBRATION_AND_TRAJECTORY_MAPPING_ANCHOR.md` | upstream methodological anchor | `docs/upstream-vectaetos/CALIBRATION_AND_TRAJECTORY_MAPPING_ANCHOR.md` or keep in protocols | review later | medium |
| `protocols/non-intervention.md` | placeholder | `protocols/non-intervention.md` | fill later | medium |
| `protocols/fixed-transformations.md` | placeholder | `protocols/fixed-transformations.md` | fill later | medium |
| `protocols/encoding-canonicalization.md` | placeholder | `protocols/encoding-canonicalization.md` | fill later | medium |
| `protocols/relational-matrix.md` | placeholder | `protocols/relational-matrix.md` | fill later | medium |
| `protocols/curvature-delta.md` | placeholder | `protocols/curvature-delta.md` | fill later | medium |
| `protocols/kappa-trace.md` | placeholder | `protocols/kappa-trace.md` | fill later | medium |
| `protocols/artifact-verification.md` | placeholder | `protocols/artifact-verification.md` | fill later | medium |
| `specs/eai-core-v0.1.md` | placeholder | `specs/eai-core-v0.1.md` | fill only after EAI precision questions | high |
| `specs/eai-artifact.schema.json` | placeholder schema | `schemas/eai-artifact.schema.json` or keep after repo decision | review location | high |
| `specs/agent-contract.schema.json` | placeholder schema | `schemas/agent-contract.schema.json` or keep after repo decision | review location | high |
| `specs/agent-event.schema.json` | placeholder schema | `schemas/agent-event.schema.json` or keep after repo decision | review location | high |
| `specs/audit-report.schema.json` | placeholder schema | `schemas/audit-report.schema.json` or keep after repo decision | review location | high |
| `specs/transformation-set.schema.json` | placeholder schema | `schemas/transformation-set.schema.json` or keep after repo decision | review location | high |
| `examples/sample-agent-contract.json` | placeholder | `examples/sample-agent-contract.json` | fill after schema | medium |
| `examples/sample-transformation-set.json` | placeholder | `examples/sample-transformation-set.json` | fill after schema | medium |
| `examples/sample-eai-artifact.json` | placeholder | `examples/sample-eai-artifact.json` | fill after schema | medium |
| `examples/sample-agentic-audit-report.md` | placeholder | `examples/sample-agentic-audit-report.md` | fill after artifact boundary | medium |
| `research/MVP_core.md` | research candidate | `research/MVP_core.md` | keep non-canonical | medium |
| `research/agent_contract.json` | research candidate | `research/agent_contract.json` | keep non-canonical | medium |
| `research/signed_envelopes.json` | research candidate | `research/signed_envelopes.json` | keep non-canonical | medium |
| `research/repo_schema.md` | older schema candidate | `research/repo_schema.md` | keep non-canonical | medium |
| `research/workflow.md` | commercial/workflow candidate | `research/workflow.md` | keep non-canonical | high |
| `legal/VECTAETOS_AGENTIC_AUDIT_REPOSITORY_EU_AI_ACT_SCOPE_STATEMENT_v1.1.md` | legal scope statement | `legal/REPOSITORY_EU_AI_ACT_SCOPE_STATEMENT.md` or keep versioned | review later | low |
| `papers/vectaetos_non_intervention_framework.pdf` | empty placeholder | `papers/vectaetos_non_intervention_framework.pdf` | fill or remove before release | medium |
| `.github/CODEOWNERS` | ownership rules | `.github/CODEOWNERS` | keep | low |
| `incubator/candidate-001/.gitkeep` | placeholder | keep | none | low |
| `incubator/candidate-002/.gitkeep` | placeholder | keep | none | low |
| `incubator/candidate-003/.gitkeep` | placeholder | keep | none | low |
| `reference/cli/.gitkeep` | placeholder | keep | none | low |
| `reference/python/.gitkeep` | placeholder | keep until populated | maybe remove after `reference/python/eai/` exists | low |

---

## 4. Proposed Cleanup Phases

### Phase 1 — Safe structural preparation

No semantic edits.

```text
create reviews/
create docs/upstream-vectaetos/eai/
create docs/architecture/
create reference/python/eai/
```

### Phase 2 — Move review documents

```text
CALIBRATION_ANCHOR_REVIEW.md -> reviews/CALIBRATION_ANCHOR_REVIEW.md
EAI_CORPUS_INVENTORY.md -> reviews/EAI_CORPUS_INVENTORY.md
EAI_IMPORT_REVIEW.md -> reviews/EAI_IMPORT_REVIEW.md
```

### Phase 3 — Move upstream EAI source material

```text
CONSTRAINTS.md -> docs/upstream-vectaetos/eai/CONSTRAINTS.md
DO_NOT_OPTIMIZE.md -> docs/upstream-vectaetos/eai/DO_NOT_OPTIMIZE.md
philosophy.md -> docs/upstream-vectaetos/eai/philosophy.md
theory.md -> docs/upstream-vectaetos/eai/theory.md
mathematics.md -> docs/upstream-vectaetos/eai/mathematics.md
```

### Phase 4 — Move reference EAI code

```text
__init__.py -> reference/python/eai/__init__.py
implementation.py -> reference/python/eai/implementation.py
encode_v2.py -> reference/python/eai/encode_v2.py
encode_v3.py -> reference/python/eai/encode_v3.py
delta.py -> reference/python/eai/delta.py
spectral.py -> reference/python/eai/spectral.py
kappa.py -> reference/python/eai/kappa.py
```

### Phase 5 — Move extracted architecture diagrams

```text
DATA_FLOW.md -> docs/architecture/DATA_FLOW.md
TRUST_BOUNDARY_MAP.md -> docs/architecture/TRUST_BOUNDARY_MAP.md
```

### Phase 6 — Update references

After moves, update:

```text
README.md
CANONICAL_STATUS.md
REPOSITORY_ARCHITECTURE.md
REPOSITORY_SCHEMA.md
CHANGELOG.md
VECTAETOS_AGENTIC_AUDIT_HANDOFF_ANCHOR.md
```

This phase must not change EAI semantics.

---

## 5. Spec / Schema Boundary

Do not fill or freeze specs until the following EAI questions are resolved:

```text
1. Transform mode
2. kappa_trace vs kappa_signature
3. Delta observable family
4. R_distance vs R_antisymmetric
5. Complex spectrum JSON serialization
6. Fingerprint h outside EAI v0.1 core
```

Schemas may be drafted only after these are resolved enough to avoid semantic lock-in.

---

## 6. Research Boundary

Files under `research/` are not canonical.

They may contain useful commercial or implementation direction, but they must not override:

```text
PHILOSOPHY.md
THEORY.md
CANONICAL_STATUS.md
EAI_IMPORT_REVIEW.md
SECURITY.md
TRADEMARKS.md
LICENSE.md
```

Potential drift-risk terms in research material must be reviewed before promotion:

```text
score
scorer
compliance export
dashboard
webhook alert
drift detector
lead_score
claim_strength
uncertainty
```

These terms are not automatically invalid, but they must remain outside EAI Core authority.

---

## 7. Completion Criteria

Root cleanup is complete when:

```text
root contains only canonical/admin files
reviews/ contains review records
docs/upstream-vectaetos/eai/ contains upstream EAI source material
reference/python/eai/ contains EAI reference candidate code
protocol placeholders are either filled or clearly marked as placeholders
spec placeholders are either filled or clearly marked as placeholders
examples are either filled or clearly marked as placeholders
CHANGELOG.md records the refactor
REPOSITORY_SCHEMA.md matches actual tracked tree
```

---

## 8. Non-Goal

This cleanup plan does not:

```text
write EAI v0.1 spec
write schemas
write verifier
create commercial API
create dashboard
create connector implementation
create legal certification language
```

Those belong to later phases.

---

## 9. Final Reminder

```text
Cleanup is not architecture change.
Movement is not canonization.
Placeholder is not specification.
Research is not authority.
Artifact is not report.
Report is not EAI.
```

END
