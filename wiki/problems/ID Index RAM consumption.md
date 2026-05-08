---
type: problem
---

# ID Index RAM Consumption

The [[ID Index]] in [[Core DB]], stored in PostgreSQL alongside map datasets, consumed approximately 30–40% of available RAM on snapshot hosts, competing with dataset queries for cache and causing resource pressure.

## Root cause

- IDs are queried randomly (no spatial or temporal locality), making OS page-cache caching ineffective
- The index was ~2 TB in PostgreSQL, requiring substantial memory to serve efficiently
- Index and dataset queries shared the same PostgreSQL buffer pool

## Resolution

Addressed by the [[ID Index Improvement]] project: a dedicated [[ID Index Service]] implemented in Go with a sorted flat-file design and binary search. This reduced the index size to ~330 GB and eliminated RAM contention with dataset queries.

## Status

Resolved (POC validated; production rollout in progress as of 2026-05-07).

## Related

- [[ID Index]] — the component with the problem
- [[Core DB]] — host system
- [[ID Index Service]] — the solution
- [[ID Index Improvement]] — project

*Source: `raw/transcripts/converted/2026-05-07 tech-design-review-IDIndex-improvement.md`*
