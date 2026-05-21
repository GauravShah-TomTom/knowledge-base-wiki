---
type: concept
---

# BPMN (Business Process Model and Notation)

BPMN is an industry-standard notation for modeling business processes as flow diagrams. It defines tasks, gateways, events, and sequence flows.

In the organisation's [[projects/Uber ACI Flow]], [[Camunda]] executes a BPMN process that governs how restriction leads flow from intake through [[Veritas]] verification to task closure. A separate dry-run BPMN is used in the dev environment; its topology mirrors the production BPMN but with environment-specific topic name prefixes.

Related: [[DMN]]

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
