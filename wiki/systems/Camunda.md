---
type: system
---

# Camunda

Camunda is the workflow orchestration platform used for managing PC restriction leads end-to-end. It hosts BPMN process definitions and DMN decision tables that route leads through verification, auto-close, and manual-review steps.

## Role in the Uber ACI Flow

In the [[Veritas Uber ACI Flow Integration]], Camunda:

1. Receives restriction leads from the [[Uber ACI Service]] (via the Uber restriction rate project in production).
2. Routes leads to [[Veritas]] for verification (after [[BFrost]] marks them as non-overlapping).
3. Applies DMN routing rules based on the Veritas output status (e.g. committed, QA-violation, fallout).
4. Runs auto-close scripts for leads marked with specific statuses (e.g. QA-allowed → auto-close as valid/committed).
5. Closes completed [[Veritas]] tasks after processing.

## BPMN / DMN

- A dry-run BPMN was created for dev/testing environment.
- Production deployment requires copying the DMN and BPMN changes into the existing production BFrost BPMN, removing the "dry-run" prefix from topic and workflow names.
- DMN placement within the production BPMN must be reviewed with the BFrost team (Swapnil / Amog). See [[Veritas Uber ACI Flow Integration]].

## Task Management

- Each Veritas-processed lead must result in its Camunda task being closed (not silently dropped).
- Task ID can be used as restriction ID for closing tasks (see [[Use task ID as restriction ID instead of external ID]]).

## Production Project

An existing Uber-restriction-rate project in Camunda production is used for Uber leads — a separate project is not needed.

## Related

- [[Veritas]]
- [[BFrost]]
- [[Veritas Uber ACI Flow Integration]]
- [[BPMN]]
- [[DMN]]
