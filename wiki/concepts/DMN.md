---
type: concept
---

# DMN (Decision Model and Notation)

DMN is a standard for modeling and executing decision logic as decision tables. It is used alongside [[BPMN]] in [[Camunda]] to route tasks based on evaluated conditions.

In the [[projects/Uber ACI Flow]], DMN tables route [[Veritas]]-processed leads based on their verification status (e.g., overlapping vs. non-overlapping, QA-allowed vs. QA-violation). The DMN placement within the [[Camunda]] BPMN was discussed with the [[BFrost]] team (Swapnil) and must be reviewed again before production deployment (story 6011).

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
