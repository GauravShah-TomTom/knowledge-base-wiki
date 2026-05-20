---
type: project
status: in-progress
deadline: 2026-05-31
---

# Veritas Uber ACI Flow Integration

End-to-end integration of [[Veritas]] with the [[Uber ACI Service]] restriction flow via [[Camunda]] and [[Airflow]]. The goal is to route Uber PC restriction leads through Veritas for verification and automatically close the corresponding Camunda tasks based on the verification result.

## Status (as of 2026-05-12)

- Dry-run BPMN and Airflow workflow deployed to dev environment.
- End-to-end dev testing in progress (story 5947).
- Production deployment planned before end of May 2026 (story 6011).
- Two blocking quality improvements in flight (stories 5950, 5952).

## Active Stories

| Story | Title | Status |
|---|---|---|
| 5950 | Handle silently skipped Veritas leads (set fallout status) | In progress — **mandatory before prod** |
| 5952 | Add external ID field in Veritas model | Pending verification — may be dropped if task ID works as restriction ID |
| 5947 | End-to-end testing of Veritas for Uber ACI flow | In progress |
| 6011 | Production deployment of Veritas Uber ACI flow | Planned |

## Architecture

```
Uber ACI Service
    → Camunda (Uber restriction rate project)
        → BFrost (Thursday run — marks non-overlapping leads)
            → Veritas (Airflow-triggered — consumes from Camunda topic)
                → Camunda DMN routing (based on Veritas status)
                    → auto-close script (for committed/QA-allowed)
                    → manual review queue
```

## End-to-End Testing Plan (Story 5947)

Test scenarios to validate:
1. All maneuver-type leads (can-left, no-left) route to Veritas after BFrost.
2. Veritas consumes all leads without silent skips (post-5950 fix).
3. Each Veritas status (VERIFIED, NOT_VERIFIED, FALLOUT_MISSING_FEATURE) is routed correctly by DMN.
4. Auto-close script closes tasks for the appropriate statuses.
5. All consumed tasks end up closed at the end of the flow.

For dev testing: [[Sunil Jaiswal]] mocked the BFrost output in a separate test project; sample data pushed to [[Camunda]] / [[Uber ACI Service]] via Swagger.

## Production Deployment Plan (Story 6011)

1. Review DMN and BPMN placement with BFrost team (Swapnil / Amog).
2. Copy dry-run BPMN/DMN changes to production BFrost BPMN; remove "dry-run" prefixes from topic/workflow names.
3. Replicate Airflow variables and HTTP connections from dev to production environment.
4. Use existing Uber restriction rate [[Camunda]] project in production (no new project needed — confirmed by [[Souvik Mudi]]).
5. Agree on deployment window with Swapnil (may require downtime).
6. Trigger manually for first 1–2 runs; then schedule Mondays. See [[Veritas production run manually first then Monday schedule]].

## Key Decisions

- [[Use generic CoreDB exception status for Veritas fallouts]]
- [[Defer detailed Veritas fallout reason field]]
- [[Guard Veritas XML against empty transition metadata fields]]
- [[Use task ID as restriction ID instead of external ID in Veritas]]
- [[Veritas production run manually first then Monday schedule]]

## Team

- [[Sunil Jaiswal]] — developer, lead implementer
- [[Aditya Krishna]] — tech lead
- [[Souvik Mudi]] — developer
- [[Tushar Shirbhate]] — developer

## Related Systems

- [[Veritas]]
- [[Camunda]]
- [[BFrost]]
- [[Airflow]]
- [[Uber ACI Service]]
- [[CoreDB]]
