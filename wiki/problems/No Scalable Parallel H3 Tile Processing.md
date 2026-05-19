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

Subtasks confirmed in 2026-05-19 sprint planning:

1. **Infra** — make the [[Lanes Automator]] node pool auto-scalable based on the number of H3 tiles for a zone.
2. **Airflow orchestration** — [[Airflow]] triggers the [[Databricks]] job ([[Data Preparator]] + [[Cross Link]]); on completion, launches Lanes Automator for each H3 tile in parallel; Lanes Automator generates JSON files per tile in their respective folders.
3. **Transaction Manager** — [[Transaction Manager]] (web service) stays unchanged; it will be called via REST API once per H3 tile. For N tiles in a zone, N parallel REST API calls generate N sets of transactions.

A new story will be created for this work; existing story 5900 may be reused or deleted. See [[decisions/Use Airflow for End-to-End H3 Tile Processing]].

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
