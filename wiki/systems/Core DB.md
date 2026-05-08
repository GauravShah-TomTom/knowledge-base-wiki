---
type: system
---

# Core DB

Internal map database service that stores the world map as a sequence of changes (deltas) and periodic snapshots.

## Overview

Core DB serves map data by storing deltas (incremental changes) and snapshots (point-in-time states). The map is divided into datasets, typically around 400 datasets spread across ~7 database hosts.

## Query types

- **Geometric queries** — hit datasets based on geographic area
- **ID-based queries** — require the [[ID Index]] to resolve which host/dataset to query

## Storage

Originally used PostgreSQL to store both datasets and the [[ID Index]]. The ID Index competed with dataset queries for RAM and cache, consuming ~30–40% of RAM on snapshot hosts.

## Related

- [[ID Index]] — component that maps feature IDs to datasets
- [[ID Index Service]] — dedicated replacement for the in-PostgreSQL ID Index
- [[ID Index Improvement]] — project to extract ID Index into a dedicated service

*Source: `raw/transcripts/converted/2026-05-07 tech-design-review-IDIndex-improvement.md`*
