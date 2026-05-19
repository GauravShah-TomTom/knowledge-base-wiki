---
type: problem
status: open
---

# No Scalable Parallel H3 Tile Processing Per Zone

## Summary

The [[Lanes Automator]] node pool currently scales to a single node and processes one zone at a time. As larger zones are split into multiple [[H3 Tiles]], the pipeline must run each tile in parallel. There is no mechanism today to:
1. Auto-scale the Lanes Automator node pool based on the number of tiles.
2. Orchestrate a fan-out from zone → N tiles → aggregate statistics/transactions.

## Current workaround

Single-zone [[GitHub Actions]] trigger. The [[Data Preparator]] and [[Cross Link]] on [[Databricks]] already handle H3 tiles in parallel, but this parallelism is not propagated to Lanes Automator or [[Transaction Manager]].

## Planned solution

From the 2026-05-19 sprint planning, a new story will be created with these subtasks:

1. **Lanes Automator infra** — adapt folder structure; make the node pool auto-scalable based on number of H3 tiles per zone.
2. **Airflow DAG** — trigger [[Databricks]] job; on completion, launch [[Lanes Automator]] for all tiles in parallel; call [[Transaction Manager]] REST API N times (one per tile).
3. **Testing** — full zone run end-to-end.

[[Transaction Manager]] requires no code changes; it will be called via REST API once per tile by Airflow. The [[Lanes Automator]] folder structure change is needed to organise output per tile.

See [[decisions/Use Airflow for End-to-End H3 Tile Processing]] for the decision record.

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
