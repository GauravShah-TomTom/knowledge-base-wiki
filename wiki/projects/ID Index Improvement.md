---
type: project
feedback_count_negative: 1
last_feedback_negative: "2026-05-08"
last_feedback_negative_conv: ""
stale_flagged_at: "2026-05-11"
---

> ⚠️ **STALE** — The opening sentence reads "Key cost-driven initiative for Q (2026)" — the quarter number is missing, suggesting an incomplete template substitution during ingestion. Per [[decisions/ID Index dedicated Go service]], the decision and POC were dated "~2026 Q1–Q2 (POC results presented 2026-05-07)". Human feedback flagged this page on 2026-05-08 (feedback_count_negative: 1); the quarter designation should be confirmed and filled in.

# ID Index Improvement

Key cost-driven initiative for Q (2026) to replace the in-PostgreSQL [[ID Index]] in [[Core DB]] with a dedicated [[ID Index Service]] implemented in Go — reducing RAM usage and infrastructure cost.

## Objective

- Eliminate [[ID Index RAM consumption]] (~30–40% of snapshot host RAM)
- Reduce ID index storage from ~2 TB (PostgreSQL) to ~330 GB (sorted flat file)
- Match or improve query latency while running on half the resources

## Approach

1. Split ID index structure into `ID → code` + `code → dataset`
2. Store in sorted flat file; query via binary search on pages
3. Implement in Go for performance and controlled memory usage

## POC results

- Traffic forked to compare Postgres vs new service
- Latency comparable to or better
- Service ran on ~half the resources of the PostgreSQL setup
- Memory concerns addressed early; no structural risks identified

## Status (2026-05-07)

POC complete; production rollout underway. Presented at tech design review by [[Piotr Patyra]].

## Related

- [[Core DB]] — host system
- [[ID Index]] — concept
- [[ID Index Service]] — new implementation
- [[ID Index RAM consumption]] — problem being solved
- [[Piotr Patyra]] — presenter/owner

*Source: `raw/transcripts/converted/2026-05-07 tech-design-review-IDIndex-improvement.md`*
