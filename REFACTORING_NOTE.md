# _REFACTORING_NOTE

**Project:** VECTAETOS Agentic Audit  
**Repository:** `vectaetos-agentic-audit`  
**Status:** Temporary staging note  
**Document Type:** Repository refactoring note  

---

## 0. Purpose

This file records the current temporary repository state.

The repository is currently in an import and staging phase.

During this phase, some files may temporarily exist in the repository root even though they are not intended to remain there permanently.

This is allowed only until v0.1 structure cleanup.

---

## 1. Current Temporary State

The repository root may temporarily contain:

```text
upstream EAI documents
EAI Python files
review documents
working notes
staging artifacts
```

This is a working condition, not a final architecture.

---

## 2. Final Root Policy

Before v0.1 freeze, the repository root should contain only high-level canonical and administrative files:

```text
README.md
PHILOSOPHY.md
THEORY.md
ARCHITECTURE.md
CANONICAL_STATUS.md
CHANGELOG.md
NOTICE.md
TRADEMARKS.md
SECURITY_POLICY.md
LICENSE.md
CITATION.cff
REPOSITORY_SCHEMA.md
_REFACTORING_NOTE.md
```

Optional later root files:

```text
CONTRIBUTING.md
CODE_OF_CONDUCT.md
```

---

## 3. Planned Refactor Targets

### 3.1 Review files

Move:

```text
EAI_CORPUS_INVENTORY.md
EAI_IMPORT_REVIEW.md
CALIBRATION_ANCHOR_REVIEW.md
```

To:

```text
reviews/
```

---

### 3.2 Upstream EAI documents

Move:

```text
CONSTRAINTS.md
DO_NOT_OPTIMIZE.md
README.md          # upstream EAI README, not repo README
philosophy.md      # upstream EAI philosophy
theory.md          # upstream EAI theory
mathematics.md
```

To:

```text
docs/upstream-vectaetos/eai/
```

Important:

```text
Do not confuse upstream EAI README.md with repository root README.md.
```

If necessary, rename upstream files during import:

```text
README.md       -> EAI_README.md
philosophy.md   -> EAI_PHILOSOPHY.md
theory.md       -> EAI_THEORY.md
mathematics.md  -> EAI_MATHEMATICS.md
```

---

### 3.3 EAI reference implementation

Move:

```text
implementation.py
encode_v2.py
encode_v3.py
delta.py
spectral.py
kappa.py
```

To:

```text
reference/python/eai/
```

Target layout:

```text
reference/python/eai/
    __init__.py
    implementation.py
    encode_v2.py
    encode_v3.py
    delta.py
    spectral.py
    kappa.py
```

---

### 3.4 Future canonical specifications

Create later:

```text
specs/eai-core-v0.1.md
specs/eai-artifact-v0.1.md
```

Do not treat upstream EAI theory as final specification until reviewed.

---

### 3.5 Future schemas

Create later:

```text
schemas/eai-artifact.schema.json
schemas/eai-run.schema.json
schemas/transformation-set.schema.json
```

---

### 3.6 Future protocols

Create later:

```text
protocols/non-intervention.md
protocols/fixed-transformations.md
protocols/encoding-canonicalization.md
protocols/relational-matrix.md
protocols/curvature-delta.md
protocols/kappa-trace.md
protocols/artifact-verification.md
```

---

## 4. Temporary Root Staging Rule

Temporary root staging is allowed only if all of the following remain true:

```text
1. The staging state is documented.
2. No staged file is treated as final canonical placement.
3. Review files record what is accepted and what requires adaptation.
4. Root cleanup occurs before v0.1 freeze.
5. README.md remains the public repository entry point.
```

---

## 5. Refactoring Sequence

Recommended sequence:

```text
1. Create reviews/ directory.
2. Move EAI_CORPUS_INVENTORY.md into reviews/.
3. Move EAI_IMPORT_REVIEW.md into reviews/.
4. Move CALIBRATION_ANCHOR_REVIEW.md into reviews/.
5. Create docs/upstream-vectaetos/eai/.
6. Move upstream EAI markdown files there.
7. Create reference/python/eai/.
8. Move EAI Python implementation files there.
9. Create specs/, schemas/, protocols/ only as needed.
10. Clean root.
11. Update REPOSITORY_SCHEMA.md.
12. Update CHANGELOG.md.
```

---

## 6. Root Cleanup Gate

The root is considered clean when it contains no:

```text
implementation modules
upstream source fragments
temporary import notes
duplicate README files
unreviewed EAI files
unclassified markdown files
```

---

## 7. v0.1 Freeze Gate

Before v0.1 freeze:

```text
root must be clean
reviews/ must contain import records
upstream EAI files must be placed under docs/upstream-vectaetos/eai/
reference code must be under reference/python/eai/
at least one EAI artifact schema must exist
at least one sample artifact must exist
CHANGELOG.md must record the refactor
```

---

## 8. Canonical Reminder

```text
Temporary staging is not canonical structure.
Root convenience must not become architecture.
No implementation may outrun ontology.
No anchor may outrun mapping.
No guard may become authority.
```

END
