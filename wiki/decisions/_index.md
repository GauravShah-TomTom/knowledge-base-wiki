---
type: index
date: 2026-05-15 16:47:15
---
# Decisions - index
[[wiki/index|← Index]]

Why decisions were taken, on what basis, by whom, and when.

- [[wiki/decisions/Create Spike for Rule 51068 Before Implementing|Decision: Create Spike for Rule 51068 Before Implementing]] — Rule 51068 (invalid lane connectivity) involves many conflicting scenarios where [[Genesis]] and [[Orbis]] provide different lane data.
- [[wiki/decisions/Focus on Top-5 Rule Fixes First|Decision: Focus on Top-5 Rule Fixes First]] — The [[Lanes]] backlog contains many rule errors, but most have very low occurrence rates.
- [[wiki/decisions/Use Airflow for End-to-End H3 Tile Processing|Decision: Use Airflow for End-to-End H3 Tile Processing]] — The [[Lanes]] pipeline currently runs one zone at a time via a GitHub Actions trigger.
- [[wiki/decisions/Use Iris Priority Field for Rule-Specific Transactions|Decision: Use Iris Priority Field to Tag Rule-Specific Transactions]] — After fixing the top DTFR rule issues in [[Lanes]], the team needs editors in [[Iris]] to verify the generated transactions — specifically the ones affected by the rule changes — to calculate precision and recall.
