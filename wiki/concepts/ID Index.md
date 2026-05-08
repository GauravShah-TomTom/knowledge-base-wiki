---
type: concept
---

# ID Index

An internal lookup table in [[Core DB]] that maps feature IDs to the specific dataset (and therefore database host) where those features are stored. Required for all ID-based map queries.

## Structure

The index was originally stored in PostgreSQL alongside the map datasets. A new design separates it into two structures:
- `ID → code` mapping
- `code → dataset` mapping

This decomposition significantly reduces the index size (from ~2 TB in PostgreSQL to ~330 GB in the new flat-file design).

## Query pattern

IDs are queried randomly (no locality), which makes OS-level caching inefficient. The new implementation stores the data in a sorted flat file and uses binary search within paged segments.

## Performance issue

In the original PostgreSQL design, the ID Index competed with dataset queries for RAM, consuming ~30–40% of RAM on snapshot hosts. See [[ID Index RAM consumption]].

## Related

- [[Core DB]] — system it lives within
- [[ID Index Service]] — dedicated service replacing the PostgreSQL implementation
- [[ID Index Improvement]] — project
- [[ID Index RAM consumption]] — problem

*Source: `raw/transcripts/converted/2026-05-07 tech-design-review-IDIndex-improvement.md`*
