# SCHEMA_PLACEMENT_REVIEW

**Project:** VECTAETOS Agentic Audit  
**Status:** Review v0.1  
**Document Type:** Repository structure review / schema placement decision record  
**Scope:** JSON schema file location before v0.1 freeze  

---

## 0. Purpose

This file reviews where JSON schema files should live in the repository.

It does not move files.

It does not define schema contents.

It does not freeze EAI v0.1.

It exists to prevent repository structure from silently becoming ontology.

---

## 1. Current Situation

Current placeholder schema files live under:

```text
specs/eai-artifact.schema.json
specs/agent-contract.schema.json
specs/agent-event.schema.json
specs/audit-report.schema.json
specs/transformation-set.schema.json
```

`REPOSITORY_SCHEMA.md` records that schema file placement remains under review.

`CANONICAL_STATUS.md` also records that JSON schema placement remains open.

`.github/CODEOWNERS` already includes a future `/schemas/` path.

---

## 2. Options Considered

### Option A — Keep JSON schemas under `specs/`

Pros:

```text
single technical directory
fewer top-level directories
simple for early draft
```

Cons:

```text
mixes prose specifications with machine-readable schemas
makes it harder to distinguish spec authority from schema validation
conflicts with existing CODEOWNERS expectation for /schemas/
may confuse future tooling
```

---

### Option B — Move JSON schemas to `schemas/`

Pros:

```text
separates prose specs from machine-readable schemas
matches common repository convention
matches existing CODEOWNERS expectation
makes later validator tooling simpler
keeps specs/ for normative prose documents
keeps schemas/ for JSON Schema artifacts
```

Cons:

```text
requires structural move
requires updating references in README, CANONICAL_STATUS, REPOSITORY_SCHEMA, ROOT_CLEANUP_PLAN, and future specs
```

---

### Option C — Keep both with generated copies

Pros:

```text
could support docs and tooling at the same time
```

Cons:

```text
creates duplicate sources of truth
increases drift risk
requires generation rules before they exist
not appropriate before v0.1
```

---

## 3. Decision

Recommended decision:

```text
MOVE JSON schema files to schemas/ in a later structural PR.
```

Repository convention:

```text
specs/   = prose technical specifications
schemas/ = machine-readable JSON schemas
```

This decision does not make current schema placeholders authoritative.

The future move is structural only.

---

## 4. Target Layout

Recommended target layout:

```text
specs/
    eai-core-v0.1.md
    contractmesh-v0.1.md
    eat-ledger-v0.1.md
    audit-artifact-v0.1.md
    agentic-audit-report-v0.1.md
    compatibility-v0.1.md
    invalidity-conditions.md

schemas/
    eai-artifact.schema.json
    agent-contract.schema.json
    agent-event.schema.json
    transformation-set.schema.json
    audit-report.schema.json
```

Future schemas may include:

```text
eai-run.schema.json
audit-ledger-event.schema.json
signed-envelope.schema.json
```

---

## 5. Non-Authority Rule

Schema placement does not define ontology.

A JSON schema is not automatically canonical because it lives under `schemas/`.

A schema becomes authoritative only when:

```text
1. its content is reviewed
2. its status is recorded
3. related EAI precision questions are resolved where relevant
4. sample artifacts validate against it
5. verifier behavior is specified
```

---

## 6. Anti-Drift Constraints

The schema move must not:

```text
change EAI semantics
resolve kappa_trace by accident
resolve Delta by accident
resolve R representation by accident
promote placeholder schemas into authority
create validator behavior
claim MVP readiness
claim commercial readiness
```

---

## 7. Next PR Recommendation

Next structural PR:

```text
Move JSON schema placeholders from specs/ to schemas/.
```

Files to move:

```text
specs/eai-artifact.schema.json -> schemas/eai-artifact.schema.json
specs/agent-contract.schema.json -> schemas/agent-contract.schema.json
specs/agent-event.schema.json -> schemas/agent-event.schema.json
specs/audit-report.schema.json -> schemas/audit-report.schema.json
specs/transformation-set.schema.json -> schemas/transformation-set.schema.json
```

Do not change file contents in that PR.

After the move, update:

```text
REPOSITORY_SCHEMA.md
CANONICAL_STATUS.md
ROOT_CLEANUP_PLAN.md
CHANGELOG.md
```

---

## 8. Final Decision Statement

```text
JSON schemas belong in schemas/.
Prose specifications belong in specs/.
Moving schema placeholders does not make them canonical.
Schema authority requires separate review and validation.
```

END
