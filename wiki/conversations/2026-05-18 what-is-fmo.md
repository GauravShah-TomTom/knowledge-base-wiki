---
type: conversation
title: "What is FMO?"
posted_by: "72a9f352-c246-4124-8ba0-be189031ee5b"
posted_at: "2026-05-18T10:35:29.313Z"
posted_via: "wiki_feedback_up"
citations:
  - "wiki/concepts/FMO.md"
  - "wiki/problems/Rule 52721 Geometry Mismatch for Composing Part.md"
  - "wiki/problems/Rule 51068 Invalid Lane Connectivity.md"
  - "wiki/projects/Lanes.md"
  - "wiki/concepts/Lane Connectivity.md"
  - "wiki/problems/Rule 50263 Traffic Flow Conflicting with Driving Side.md"
  - "wiki/concepts/FOW.md"
  - "wiki/problems/Rule 51830 Incorrect Relationship to Lane Connectivity.md"
---
# What is FMO?

## Question

What is FMO?

## Answer

FMO stands for **Feature Model Output** (also referred to as a quality run). 

- **What it is** — a quality validation run performed on a geographic zone in the Lanes pipeline that executes a set of validation rules against derived lane data and reports violations per rule ID.  
- **Purpose** — to identify and prioritise quality issues before a zone’s output is published; results are analysed rule-by-rule to determine root causes and fixes.  
- **Where used** — in the Lanes project’s pipeline as a gate / QA step on derived lane and lane‑connectivity data.  
- **Example** — the DEU-01 FMO run (Schleswig‑Holstein) found 14,055 transactions with QA violations across the top rules.

## Citations

- [[wiki/concepts/FMO]]
- [[wiki/problems/Rule 52721 Geometry Mismatch for Composing Part]]
- [[wiki/problems/Rule 51068 Invalid Lane Connectivity]]
- [[wiki/projects/Lanes]]
- [[wiki/concepts/Lane Connectivity]]
- [[wiki/problems/Rule 50263 Traffic Flow Conflicting with Driving Side]]
- [[wiki/concepts/FOW]]
- [[wiki/problems/Rule 51830 Incorrect Relationship to Lane Connectivity]]
