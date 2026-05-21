---
type: system
---

# Veritas

Veritas is the internal verification pipeline for maneuver (turn) restriction leads. It consumes leads from a Kafka topic, verifies them against [[CoreDB]] (road IDs, maneuver IDs), and emits a Veritas output record with a `verification_result` / Veritas status field for each lead.

## Veritas status values

| Status | Meaning |
|---|---|
| Verified | Lead passed all checks |
| Not Verified | Lead failed verification (exception during processing) |
| Fallout – Missing Feature | Lead skipped because a required road/maneuver ID was not found in CoreDB |
| SC Conflict | Status conflict detected |

A generic "fallout missing feature" status covers any CoreDB lookup failure (missing road ID or maneuver ID). Individual per-exception statuses were discussed but decided against in favour of the generic status — see [[decisions/veritas-fallout-status-generic]].

## Output format

Veritas produces XML output that includes transition metadata fields. Empty fields must not be emitted as empty XML tags — they cause invalid XML. If a metadata field has no value it must be omitted entirely (see [[decisions/veritas-xml-omit-empty-fields]]).

## Integration with Camunda

Veritas is a worker in the [[Camunda]] BPMN workflow. Each lead corresponds to a Camunda task. Veritas must set a status for **every** consumed lead, including those it previously skipped silently, so that the [[Camunda]] task can be closed. Before this quality improvement (story 5950), leads with missing CoreDB IDs were silently skipped and their Camunda tasks were never closed.

## Key facts

- Configured via YAML (environment-specific topic names, variables)
- Integrated with [[BFrost]] as the upstream source of non-overlapping leads
- Integrated with [[Airflow]] for orchestration
- Part of the [[projects/Uber ACI Flow]]
- Story IDs in sprint: 5950 (handle silently skipped leads), 5952 (external ID / task ID), 5947 (end-to-end testing), 6011 (production deployment)

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
