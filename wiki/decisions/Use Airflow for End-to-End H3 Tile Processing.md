---
type: decision
date: 2026-05-15
---

# Decision: Use Airflow for End-to-End H3 Tile Processing

## Context

The [[Lanes]] pipeline currently runs one zone at a time via a GitHub Actions trigger. As zones grow larger, the data is split into multiple [[H3 Tiles]], and [[Lanes Automator]] needs to process each tile in parallel. GitHub Actions cannot natively orchestrate this fan-out pattern at the required scale.

## Decision

Move end-to-end pipeline orchestration to [[Airflow]]. Airflow will:
1. Trigger the [[Databricks]] job ([[Data Preparator]] + [[Cross Link]]).
2. On completion, launch [[Lanes Automator]] for each H3 tile in parallel.
3. After Lanes Automator finishes, call [[Transaction Manager]] REST API once per tile.

A new story will be created to implement this (the existing story 5900 may be reused or replaced).

## Rationale

Airflow supports DAG-based fan-out orchestration and is already used in the organisation's data platform. Migrating away from GitHub Actions enables the parallel tile processing required for larger zones.

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
