---
type: concept
---

# BPMN

Business Process Model and Notation (BPMN) is an industry-standard graphical notation for specifying business processes in a workflow. The organisation uses BPMN definitions hosted in [[Camunda]] to model the end-to-end flow of restriction lead processing.

## Usage

- [[Camunda]] executes BPMN process definitions for PC restriction workflows.
- The [[Veritas Uber ACI Flow Integration]] involved creating a dry-run BPMN in the dev environment; production deployment requires merging those changes into the existing production BFrost BPMN.
- BPMN files include embedded [[DMN]] decision tables for routing leads to different paths.

## Related

- [[DMN]]
- [[Camunda]]
- [[BFrost]]
