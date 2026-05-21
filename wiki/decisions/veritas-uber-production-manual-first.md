---
type: decision
date: 2026-05-12
participants: [Aditya Krishna, Sunil Jaiswal, Tushar Shirbhate]
---

# Decision: Run Veritas Uber ACI in Production Manually Before Scheduling

## Context

The [[projects/Uber ACI Flow]] production deployment (story 6011) will introduce [[Veritas]] processing of Uber restriction leads into the live environment. [[Airflow]] needs to be configured to schedule the flow after [[BFrost]] (which runs on Thursdays).

## Decision

- **Initial production runs will be triggered manually** rather than on a schedule
- After 1–2 manual runs confirming the pipeline is working and BFrost timing is understood, the Airflow DAG will be scheduled for **Mondays**

## Rationale

- Timing relative to BFrost Thursday runs needs to be validated before committing to a fixed schedule
- Manual runs allow the team to observe end-to-end behaviour and check how long Veritas takes to process all leads before tasks are locked

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
