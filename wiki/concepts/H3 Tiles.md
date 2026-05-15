---
type: concept
---

# H3 Tiles

H3 is a hexagonal hierarchical spatial indexing system (developed by Uber) used to subdivide geographic zones into discrete tiles for parallel processing.

In the [[Lanes]] pipeline, large map zones are split into multiple H3 tiles so that [[Lanes Automator]] can process them in parallel rather than handling an entire zone sequentially. Each H3 tile corresponds to one derivation run; for a single zone there may be 4–5 tiles.

## Usage in the pipeline

- [[Data Preparator]] and [[Cross Link]] already process tiles in parallel on [[Databricks]].
- [[Lanes Automator]] currently handles only a single zone at a time; scaling to multiple H3 tiles per zone is a planned [[problems/No Scalable Parallel H3 Tile Processing|open problem]].
- [[Transaction Manager]] is called once per tile (REST API) to create transactions for each tile's output JSON.

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
