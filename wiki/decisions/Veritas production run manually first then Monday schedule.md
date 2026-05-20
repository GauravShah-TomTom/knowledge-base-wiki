---
type: decision
date: 2026-05-12
deciders: [Aditya Krishna, Sunil Jaiswal]
---

# Veritas production run manually first then Monday schedule

**Decision:** After production deployment, trigger the [[Veritas]] [[Airflow]] workflow manually for the first 1–2 runs to validate the flow, then schedule it to run automatically on Mondays.

## Context

During sprint grooming on 2026-05-12, [[Aditya Krishna]] and [[Sunil Jaiswal]] discussed the operational schedule for [[Veritas]] after production deployment. [[Tushar Shirbhate]] also asked about the manual trigger plan.

## Rationale

- [[BFrost]] runs on Thursdays. Running [[Veritas]] on Mondays gives the team a full understanding of how long BFrost takes to complete before the Veritas run starts.
- Running manually first allows validation of the end-to-end flow and task locking behaviour before committing to a fully automated schedule.
- This was discussed earlier with Ravi and confirmed in the sprint grooming.

## Schedule

| Phase | Trigger | Day |
|---|---|---|
| Initial validation | Manual | After deployment |
| Steady state | Scheduled | Mondays |

## Related

- [[Veritas]]
- [[BFrost]]
- [[Airflow]]
- [[Veritas Uber ACI Flow Integration]]
