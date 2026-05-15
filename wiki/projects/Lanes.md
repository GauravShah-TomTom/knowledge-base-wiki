---
type: project
---

# Lanes

The Lanes project automates the derivation and correction of lane data (lane count and [[Lane Connectivity|lane connectivity]]) in the organisation's map pipeline. It processes road network data using rule-based logic ([[DTFR]]) and produces map change transactions for human editor verification.

## Pipeline overview

```
[Databricks]
  Data Preparator + Cross Link  (parallel, by H3 tile)
        ↓
  Lanes Automator  (per H3 tile → JSON output)
        ↓
  Transaction Manager  (JSON → map change transactions)
        ↓
  MCR  (Map Change Repository)
        ↓
  Iris  (editor task management / QA)
```

Systems: [[Databricks]], [[Data Preparator]], [[Cross Link]], [[Lanes Automator]], [[Transaction Manager]], [[MCR]], [[Iris]], [[Airflow]] (planned orchestrator).

## Active sprint (2026-05-15)

Stories being groomed:

| Story / Rule ID | Description | Owner |
|---|---|---|
| Route 5832 | Post-processing to add lanes at intersections | [[Gaurav Shah]] |
| 51059 | Detect/filter lanes on non-payload roads | Speaker 3 |
| 50329 | DTFR — missing link connectivity at 3-valid junctions | — |
| 51068 | Invalid lane connectivity (Genesis vs Orbis conflict) — **spike** | Niranjan |
| New story | End-to-end H3 tile parallel processing via Airflow | [[Gaurav Shah]] |
| New story | Rule-to-transaction tracing / Iris priority tagging | — |

## Key decisions

- [[decisions/Use Iris Priority Field for Rule-Specific Transactions]]
- [[decisions/Create Spike for Rule 51068 Before Implementing]]
- [[decisions/Use Airflow for End-to-End H3 Tile Processing]]
- [[decisions/Focus on Top-5 Rule Fixes First]]

## Open problems

- [[problems/Missing Country Driving Direction in Derivation]]
- [[problems/Rule 51059 Lanes on Non-Payload Roads]]
- [[problems/Rule 51068 Invalid Lane Connectivity]]
- [[problems/No Scalable Parallel H3 Tile Processing]]
- [[problems/No Rule-to-Transaction Tracing in Iris]]

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
