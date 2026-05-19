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

- Adapt folder structure to organise output JSON per H3 tile per zone (required for parallel multi-tile runs).
- Make the node pool auto-scalable based on the number of H3 tiles per zone.
- Orchestration to be moved to [[Airflow]] so multiple tiles can run in parallel (replacing [[GitHub Actions]] single-zone trigger).

## Output

Generates JSON files (one per H3 tile) with lane connectivity/count decisions and rule metadata. Each JSON is linked to one or more transactions created by [[Transaction Manager]]. Rule metadata in the JSON identifies which [[DTFR]] rules were applied, enabling downstream Iris priority tagging.

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
