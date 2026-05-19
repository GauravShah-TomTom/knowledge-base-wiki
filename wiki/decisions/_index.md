---
type: index
date: 2026-05-19 06:29:03
---
# Decisions - index
[[wiki/index|← Index]]

Why decisions were taken, on what basis, by whom, and when.

- [[wiki/decisions/Auto-merge PRs in Team Wiki Ingest Flow|Auto-merge PRs in Team Wiki Ingest Flow]] — The [[Team Wiki]] GitHub Action ingest flow creates pull requests that auto-merge by default, without requiring manual review approval for every ingest run.
- [[wiki/decisions/Create Spike for Rule 51068 Before Implementing|Decision: Create Spike for Rule 51068 Before Implementing]] — Rule 51068 (invalid lane connectivity) involves many conflicting scenarios where [[Genesis]] and [[Orbis]] provide different lane data.
- [[wiki/decisions/Default Lane Connectivity at 3-Valent T-Junctions|Default Lane Connectivity at 3-Valent Junctions]] — For any 3-valid junction (not limited to T-type / FOW 3 / DC Taper): apply whatever lane connectivity [[systems/HD Basemap|HD]] / [[systems/Cross Link|Crosslink]] provides.
- [[wiki/decisions/Focus on Top-5 Rule Fixes First|Decision: Focus on Top-5 Rule Fixes First]] — The [[Lanes]] backlog contains many rule errors, but most have very low occurrence rates.
- [[wiki/decisions/No Action for Lane Divider Rules 51083 and 51149|No Action for Lane Divider Rules 51083 and 51149]] — No corrective action is to be taken for rules [[problems/Rule 51083 Incorrect Lane Divider Type|51083]] and [[problems/Rule 51149 Incorrect Lane Divider Type|51149]].
- [[wiki/decisions/Serve MCP from Team Wiki Next.js App|Serve MCP from Team Wiki Next.js App]] — The [[MCP]] server for the [[Team Wiki]] platform runs inside the same Next.js application as the Chat UI, rather than as a separate service.
- [[wiki/decisions/Skip Rule 52261 from Lanes Project Scope|Skip Rule 52261 from Lanes Project Scope]] — Rule 52261 ("Carriageways too close based upon number of lanes") is a candidate for removal from the [[projects/Lanes|Lanes project]] scope — no pipeline action is required.
- [[wiki/decisions/Use Airflow for End-to-End H3 Tile Processing|Decision: Use Airflow for End-to-End H3 Tile Processing]] — The [[Lanes]] pipeline currently runs one zone at a time via a GitHub Actions trigger.
- [[wiki/decisions/Use Azure AI Search for Team Wiki Indexing|Use Azure AI Search for Team Wiki Indexing]] — The [[Team Wiki]] platform uses [[Azure AI Search]] as its search and vector index backend, with automatic reindexing triggered on every push to `main` via the `wiki-aoai-index` GitHub Action.
- [[wiki/decisions/Use Azure OpenAI as Team Wiki Reasoning Gateway|Use Azure OpenAI as Team Wiki Reasoning Gateway]] — The [[Team Wiki]] Chat UI and [[MCP]] server use [[Azure OpenAI]] as the language model backend for answer generation and embedding production.
- [[wiki/decisions/Use Iris Priority Field for Rule-Specific Transactions|Decision: Use Iris Priority Field to Tag Rule-Specific Transactions]] — After fixing the top DTFR rule issues in [[Lanes]], the team needs editors in [[Iris]] to verify the generated transactions — specifically the ones affected by the rule changes — to calculate precision and recall.
