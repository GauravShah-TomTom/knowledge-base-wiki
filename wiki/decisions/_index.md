---
type: index
date: 2026-05-20 06:48:14
---
# Decisions - index
[[wiki/index|← Index]]

Why decisions were taken, on what basis, by whom, and when.

- [[wiki/decisions/Defer detailed Veritas fallout reason field|Defer detailed Veritas fallout reason field]] — **Decision:** Defer adding a dedicated "fallout reason" text field to [[Veritas]] output (to surface per-lead exception details to [[Camunda]]).
- [[wiki/decisions/Guard Veritas XML against empty transition metadata fields|Guard Veritas XML against empty transition metadata fields]] — **Decision:** Add a guard in the [[Veritas]] XML generator so that fields with no value are omitted from the transition metadata XML output rather than emitted as empty tags.
- [[wiki/decisions/Use generic CoreDB exception status for Veritas fallouts|Use generic CoreDB exception status for Veritas fallouts]] — **Decision:** Use a single generic fallout status (e.g.
- [[wiki/decisions/Use task ID as restriction ID instead of external ID in Veritas|Use task ID as restriction ID instead of external ID in Veritas]] — **Decision (pending verification):** Use the [[Camunda]] task ID as the restriction ID to close Camunda tasks, instead of adding a separate `externalId` field to the [[Veritas]] output model.
- [[wiki/decisions/Veritas production run manually first then Monday schedule|Veritas production run manually first then Monday schedule]] — **Decision:** After production deployment, trigger the [[Veritas]] [[Airflow]] workflow manually for the first 1–2 runs to validate the flow, then schedule it to run automatically on Mondays.
