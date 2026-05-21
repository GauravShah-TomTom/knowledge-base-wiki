---
type: system
---

# Camunda

Camunda is the BPMN workflow engine used to manage restriction-change tasks in the Uber ACI pipeline. Each incoming lead from [[systems/Uber ACI Service]] becomes a Camunda task that must be explicitly closed after processing.

## Components used

- **BPMN process** — defines the end-to-end workflow for restriction verification and routing
- **DMN** — decision tables that route tasks based on [[Veritas]] status (e.g., overlapping vs. non-overlapping, QA-allowed vs. QA-violation)
- **Scripts** — auto-close scripts that set task status/sub-status and close the task when a QA violation is detected

## Integration

- [[Veritas]] consumes leads from a Camunda/Kafka topic and sets a status on each task; every task must receive a status so it can be closed
- [[BFrost]] upstream process feeds non-overlapping leads into the workflow
- The dry-run BPMN environment (used for dev/testing) uses the same topology as production but with "dry run" prefixes on topic and flow names; these must be stripped for production deployment

## Environments

| Environment | Notes |
|---|---|
| Dev (dry run) | Manually triggered; subset of production BPMN; topic names prefixed with "dry run" |
| Production | Scheduled (Mondays, after BFrost Thursday run); requires coordination with BFrost/Swapnil team |

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
