---
type: system
---

# Airflow

Apache Airflow is the workflow orchestration platform planned for the end-to-end [[Lanes]] pipeline to replace the current single-zone GitHub Actions trigger.

## Planned role

- Trigger the [[Databricks]] job ([[Data Preparator]] + [[Cross Link]]).
- On successful completion, launch [[Lanes Automator]] for all H3 tiles in parallel.
- Each tile's Lanes Automator run produces JSON that [[Transaction Manager]] consumes via REST API calls.

This migration is needed to support parallel processing of multiple [[H3 Tiles]] per zone — see [[problems/No Scalable Parallel H3 Tile Processing]] and [[decisions/Use Airflow for End-to-End H3 Tile Processing]].

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
