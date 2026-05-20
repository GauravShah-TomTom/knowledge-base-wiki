---
type: concept
---

# DMN

Decision Model and Notation (DMN) is an industry standard for modelling business decisions as decision tables. In the organisation's PC restriction workflow, DMN tables are embedded within [[BPMN]] process definitions in [[Camunda]] and control how [[Veritas]] output statuses are routed.

## Usage

- DMN tables map [[Veritas]] verification result statuses to workflow paths (e.g. commit → auto-close, QA-violation → manual review).
- [[Sunil Jaiswal]] updated the Camunda DMN for the [[Veritas Uber ACI Flow Integration]] to add Veritas-specific status routing.
- Placement of the DMN within the production BFrost BPMN must be reviewed with the BFrost team before production deployment.

## Related

- [[BPMN]]
- [[Camunda]]
- [[Veritas]]
