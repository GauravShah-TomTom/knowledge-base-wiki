---
type: system
stale_flagged_at: "2026-05-11"
---

> ⚠️ **STALE** — This page's Status section says "Production rollout **planned** as a key cost-driven initiative," but [[projects/ID Index Improvement]] states "POC complete; production rollout **underway**" and [[problems/ID Index RAM consumption]] states "production rollout **in progress**" — both as of 2026-05-07, the same source date. The word "planned" is inconsistent with the other two pages and likely reflects an ingestion-time wording difference from the same transcript. The actual status should be confirmed and harmonised across these three pages.

# ID Index Service

Dedicated Go service that replaces the in-PostgreSQL [[ID Index]] in [[Core DB]], providing faster and more memory-efficient feature-ID-to-dataset lookups.

## Design

- Stores IDs in a sorted flat file; queries use binary search within pages
- Splits the index structure into: `ID → code` and `code → dataset` combinations, reducing total size from ~2 TB (PostgreSQL) to ~330 GB
- Implemented in Go for low-level performance and controlled memory allocation (minimal dynamic allocation)

## Performance

- Latency comparable to or better than the PostgreSQL-backed index in POC traffic mirroring
- Ran on roughly half the resources of the original PostgreSQL setup
- Eliminates the RAM contention (previously ~30–40% of snapshot host RAM)

## Status

POC completed (traffic forked to compare Postgres vs the new service). No structural risks identified. Production rollout planned as a key cost-driven initiative.

## Related

- [[Core DB]] — host system
- [[ID Index]] — concept being implemented
- [[ID Index Improvement]] — project

*Source: `raw/transcripts/converted/2026-05-07 tech-design-review-IDIndex-improvement.md`*
