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

## FMO Quality Run — Zone DEU-01 (Schleswig-Holstein)

An [[concepts/FMO|FMO]] (Feature Model Output) quality run was performed on zone DEU-01 (Schleswig-Holstein). Results:
- **Total transactions with QA violations**: 14,055
- **Top violation by transaction count**: Rule 51684 (Missing Lane Connectivity at 3-valent junctions) — 7,440 unique transactions (52.94%)

Top rules and proposed resolution paths:

| Rule | Problem | Resolution |
|---|---|---|
| 51684 / 51147 | Missing connectivity at T-junctions | Default all connections (see [[decisions/Default Lane Connectivity at 3-Valent T-Junctions]]) |
| 50329 | Intermediate road elements without lanes | Default lane count or Orbis improvement |
| 51059 | DTFR for Lane and Road not in line | Fix per scenario (bidirectional lanes / restrict DTFR) |
| 51068 | Invalid Lane Connectivity (restrictions not respected) | Orbis improvement |
| 52261 | Carriageways too close | Skip (see [[decisions/Skip Rule 52261 from Lanes Project Scope]]) |
| 51083 / 51149 | Lane Divider type | No action (see [[decisions/No Action for Lane Divider Rules 51083 and 51149]]) |

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/confluence/Lanes FMO-- violation review.md`*
