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

Single-zone GitHub Actions trigger. The [[Data Preparator]] and [[Cross Link]] on [[Databricks]] already handle H3 tiles in parallel, but this parallelism is not propagated to Lanes Automator or [[Transaction Manager]].

## Planned solution

- Make the Lanes Automator node pool auto-scalable (infra subtask).
- Move orchestration to [[Airflow]] (see [[decisions/Use Airflow for End-to-End H3 Tile Processing]]).
- A new story will be created for this work; existing story 5900 may be reused.

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
