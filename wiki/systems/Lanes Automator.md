---
type: system
---

# Lanes Automator

Lanes Automator is the core processing service in the [[Lanes]] pipeline. It applies lane derivation rules to map data and produces output JSON files, one per [[H3 Tiles|H3 tile]], which are consumed by [[Transaction Manager]].

## Current state (as of 2026-05-15)

- Processes a single zone at a time; the node pool scales to one node per run.
- Does not yet support parallel processing of multiple H3 tiles for a single zone — see [[problems/No Scalable Parallel H3 Tile Processing]].
- Triggered via GitHub Actions (single-zone).

## Planned changes

- Make the node pool auto-scalable based on the number of H3 tiles.
- Orchestration to be moved to [[Airflow]] so multiple tiles can run in parallel.

## Output

Generates JSON files (one per H3 tile) with lane connectivity/count decisions and rule metadata. Each JSON is linked to one or more transactions created by [[Transaction Manager]].

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
