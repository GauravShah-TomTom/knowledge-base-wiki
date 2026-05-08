---
type: decision
---

# Decision: Build a dedicated ID Index service in Go

**Date:** ~2026 Q1–Q2 (POC results presented 2026-05-07)  
**Project:** [[ID Index Improvement]]

## Decision

Replace the in-PostgreSQL [[ID Index]] in [[Core DB]] with a dedicated standalone service implemented in Go, storing the index as a sorted flat file queried via binary search.

## Rationale

- PostgreSQL ID Index consumed ~30–40% of snapshot host RAM and competed with dataset queries for cache
- IDs are queried randomly — PostgreSQL caching ineffective for this workload
- A dedicated service allows workload-specific optimisations (sorted file + binary search, paged access)
- Go chosen for low-level performance and minimal dynamic memory allocation

## Alternatives considered

- Continue with PostgreSQL (rejected: RAM and cost issues persist)

## Outcome

- Index size reduced from ~2 TB → ~330 GB
- Latency comparable or better than PostgreSQL in POC traffic fork
- Service runs on ~half the resources

## Related

- [[ID Index Service]] — implementation
- [[Core DB]] — system affected
- [[Piotr Patyra]] — owner

*Source: `raw/transcripts/converted/2026-05-07 tech-design-review-IDIndex-improvement.md`*
