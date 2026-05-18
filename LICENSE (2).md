# LICENSE

**Project:** VECTAETOS Agentic Audit  
**Repository:** `vectaetos-agentic-audit`  
**Status:** Draft v0.1  
**Document Type:** License map and usage boundary  
**Legal Status:** Draft, not legal advice  

---

## 0. Purpose

This file defines the initial license structure for the VECTAETOS Agentic Audit repository.

This repository is intentionally multi-layered.

It contains:

```text
philosophy
theory
specifications
schemas
protocols
examples
reports
reference implementation code
brand and trademark materials
future commercial infrastructure
```

These layers should not all use the same license.

The goal is:

```text
Open specification.
Protected identity.
Paid verification.
```

---

## 1. Important Notice

This file is a draft license map.

It is not legal advice.

Until a full custom license text is finalized, any file without an explicit license header remains protected by copyright.

No rights are granted beyond those explicitly stated in this file or in a file-specific license header.

---

## 2. Default Copyright

Copyright (c) 2026 Richard Fonfara.

All rights reserved unless a specific license is explicitly applied.

This includes but is not limited to:

```text
conceptual documents
philosophy
theory
specifications
schemas
protocols
reports
examples
brand materials
diagrams
architectural descriptions
terminology maps
```

---

## 3. Repository License Model

The repository uses a layered licensing model.

```text
/docs, /philosophy, /papers
    -> VEPL-1.0 draft

/specs, /schemas, /protocols
    -> VSL-1.0 draft

/reference, /cli
    -> Apache-2.0 planned unless stated otherwise

/examples
    -> Example Use License / VSL-compatible draft

/reports
    -> Template Use License, no legal/financial audit claim

/brand, marks, names, logos
    -> All rights reserved

/hosted services, APIs, dashboards, commercial reports
    -> Proprietary commercial terms
```

---

## 4. VEPL-1.0 Draft

**Name:** VECTAETOS Epistemic Public License 1.0  
**Short Name:** VEPL-1.0  
**Status:** Draft  
**Applies To:** Philosophy, theory, papers, conceptual materials, explanatory documentation  

### 4.1 Intended Permission

The following uses are intended to be allowed:

```text
read
study
quote with attribution
cite
link
share unchanged copies
use for non-commercial research and discussion
```

### 4.2 Intended Restrictions

The following uses are not allowed without explicit permission:

```text
commercial resale of the materials as a standalone product
removal of attribution
representation of modified materials as canonical
representation of derivative work as official VECTAETOS
use of VECTAETOS marks to imply endorsement
use of the materials to claim official certification
use that converts EAI into an agent
use that converts kappa_trace into a score
```

### 4.3 Canonical Boundary

VEPL-protected materials must preserve the following boundary:

```text
VECTAETOS is not a product.
EAI is not an agent.
kappa_trace is not a score.
Artifacts are not verdicts.
Reports are not EAI.
Audit is not control.
Visibility is not authority.
```

---

## 5. VSL-1.0 Draft

**Name:** VECTAETOS Specification License 1.0  
**Short Name:** VSL-1.0  
**Status:** Draft  
**Applies To:** Technical specifications, schemas, protocols, compatibility definitions  

### 5.1 Intended Permission

The following uses are intended to be allowed:

```text
read
study
implement
test
validate
reference
create experimental implementations
create internal implementations
use public schemas for interoperability experiments
```

### 5.2 Intended Restrictions

The following uses are not allowed without explicit permission:

```text
claim official compatibility
claim certification
claim endorsement
claim official implementation status
remove attribution
rename derivative specifications in a confusing way
alter schemas and present them as canonical
use marks in product names without permission
```

### 5.3 Compatibility Claims

Implementation of a public schema does not create official compatibility.

Do not claim:

```text
VECTAETOS-compliant
EAI-certified
ContractMesh-certified
official VECTAETOS implementation
official EAI verifier
official ContractMesh verifier
```

unless a published compatibility process exists and is satisfied.

Allowed descriptive wording:

```text
implements selected public schemas
unofficial implementation
experimental implementation
research prototype
inspired by the public specification
```

---

## 6. Reference Implementation Code

Reference implementation code is planned to use:

```text
Apache License 2.0
```

unless a file-specific license header states otherwise.

This applies to future code under:

```text
/reference
/reference/python
/reference/cli
```

The exact Apache-2.0 license text should be included when reference code is added.

Until then, code files without explicit license headers remain under default copyright.

---

## 7. Examples

Example files may be used for learning, testing, and validation.

Examples may include:

```text
sample-agent-contract.json
sample-transformation-set.json
sample-eai-artifact.json
sample-agentic-audit-report.md
```

Examples must not be represented as real audits, real contracts, legal documents, financial assurance, or production artifacts.

If examples contain keys, signatures, hashes, or identifiers, they are test-only unless explicitly stated otherwise.

---

## 8. Reports and Templates

Report templates may be used to understand the intended report structure.

Reports are interpretive documents.

Reports are not EAI artifacts.

Report templates must preserve the following disclaimers where applicable:

```text
Not a statutory audit.
Not legal advice.
Not financial assurance.
Not insurance.
Technical and epistemic auditability only.
```

Commercial use of official report templates may require separate permission or commercial terms.

---

## 9. Brand, Marks, and Identity

No license in this repository grants trademark rights.

The following names remain claimed marks of the VECTAETOS Project unless otherwise stated:

```text
VECTAETOS
VECTAETOS Agentic Audit
Agentic Audit Solutions
EAI
Epistemic Audit Interface
ContractMesh
EAT Ledger
kappa_trace
```

Use of public materials does not grant permission to use these names as a product brand, certification badge, compatibility badge, or official-status claim.

See:

```text
TRADEMARKS.md
NOTICE.md
```

---

## 10. Hosted Services and Commercial Infrastructure

The following are not licensed by this repository license map:

```text
hosted verifier
commercial API
signed audit certificates
enterprise dashboard
paid connectors
customer reports
white-label reports
commercial artifact signing
production key infrastructure
customer data infrastructure
```

These require separate commercial terms.

---

## 11. No Warranty

Unless required by applicable law or agreed in writing, materials are provided on an "as is" basis.

No warranty is provided regarding:

```text
correctness
security
fitness for a particular purpose
legal sufficiency
regulatory sufficiency
commercial suitability
non-infringement
absence of defects
```

---

## 12. No Legal, Financial, or Statutory Audit Service

Nothing in this repository provides:

```text
legal advice
financial assurance
statutory audit
insurance
regulatory certification
professional compliance certification
```

The term "audit" refers to technical and epistemic auditability of agentic systems.

---

## 13. No Patent Grant Unless Explicitly Stated

No patent rights are granted unless a specific license expressly grants them.

If Apache-2.0 is applied to reference code, the patent provisions of Apache-2.0 apply only to that code and only under the terms of that license.

---

## 14. Derivative Works

Derivative works must not imply official status.

Modified materials must not be presented as canonical VECTAETOS Agentic Audit materials.

Derivative specifications should use a clearly distinct name unless explicit permission is granted.

Recommended disclaimer:

```text
This is an unofficial derivative work based on public VECTAETOS Agentic Audit materials.
It is not endorsed by or affiliated with the VECTAETOS Project.
```

---

## 15. Contributions

Until a separate contributor license or developer certificate of origin process is adopted, contributions are accepted only under the assumption that the contributor has the right to submit them and agrees that they may be incorporated into the project under this repository's licensing model.

A future version may introduce:

```text
DCO
CLA
contributor terms
signed-off-by requirement
```

---

## 16. File-Specific License Headers

A file may override this general map by including an explicit license header.

Example:

```text
SPDX-License-Identifier: Apache-2.0
```

or:

```text
License: VSL-1.0 Draft
```

If no explicit file-specific license exists, this license map and default copyright apply.

---

## 17. License Evolution

The licensing model may evolve before v1.0.

Potential future changes:

```text
publish full VEPL-1.0 text
publish full VSL-1.0 text
apply Apache-2.0 to reference code
add DCO or CLA
add commercial API terms
add official compatibility terms
```

Breaking license changes must be recorded in `CHANGELOG.md`.

---

## 18. Final License Canon

```text
Public does not mean ownerless.
Open specification does not mean unprotected identity.
Implementation does not mean certification.
Forking does not mean endorsement.
Schemas do not grant trademark rights.
Artifacts do not create legal assurance.
Reports do not become EAI.
VECTAETOS is not sold.
```

This license map exists to preserve public usefulness without losing conceptual identity.
