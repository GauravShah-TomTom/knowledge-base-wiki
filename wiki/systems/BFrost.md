---
type: system
---

# BFrost

BFrost (also referred to as "VFrost" in transcripts) is the pre-processing pipeline that runs on Thursdays to mark restriction leads as "non-overlapping". Only leads that BFrost marks as non-overlapping are subsequently routed to [[Veritas]] for verification.

## Schedule

- BFrost runs on **Thursdays**.
- [[Veritas]] is planned to run on **Mondays** (after BFrost output is ready). Initially triggered manually; eventually scheduled.

## Role in Uber ACI Flow

1. BFrost consumes restriction leads and evaluates overlaps.
2. Non-overlapping leads are published to a Camunda/Kafka topic consumed by [[Veritas]].
3. For dev/testing, [[Sunil Jaiswal]] mocked the BFrost output in a separate test project so the full BFrost run is not required to test Veritas.

## Production Deployment Dependency

Production deployment of the [[Veritas Uber ACI Flow Integration]] requires:
- Reviewing the DMN and BPMN changes with the BFrost team (Swapnil / Amog).
- Agreeing on a deployment window (possibly requiring downtime).
- Copying dry-run BPMN/DMN changes into the production BFrost BPMN.

## Related

- [[Veritas]]
- [[Camunda]]
- [[Veritas Uber ACI Flow Integration]]
- [[Airflow]]
