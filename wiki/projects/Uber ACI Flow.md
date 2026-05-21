---
type: project
status: active
---

# Uber ACI Flow

Integration project to process maneuver restriction leads from the [[systems/Uber ACI Service]] through the organisation's verification and workflow platform.

## Overview

Uber sends restriction data (turn restrictions: "can left", "no left", maneuver-type leads) to the organisation's pipeline. These leads go through:

1. **[[BFrost]]** — identifies non-overlapping leads (runs Thursdays)
2. **[[Veritas]]** — verifies leads against [[CoreDB]] and sets a verification status
3. **[[Camunda]]** — routes leads via [[DMN]] decision tables, auto-closes qualifying tasks, manages task lifecycle
4. **[[Airflow]]** — orchestrates scheduling and execution (including [[Dumbo]] job runs)

## Active sprint stories (as of 2026-05-12)

| Story | Title | Priority |
|---|---|---|
| 5950 | Handle silently skipped leads in Veritas | Must-do before prod deployment |
| 5952 | External ID / task ID in Veritas model (reassess if needed) | Needs investigation |
| 5947 | End-to-end testing of Veritas Uber ACI flow (dev) | Active — [[Sunil Jaiswal]] |
| 6011 | Production deployment | Blocked on 5950, 5947 completion |

## Production deployment plan (story 6011)

- Copy BPMN/DMN changes from dry-run to production environment (remove "dry run" prefixes)
- Review DMN placement and flow with BFrost team (Swapnil / Amog)
- Add [[Airflow]] variables and connections for production environment
- Use existing Uber-specific production project in [[Camunda]]
- Initial trigger: manual; then schedule Mondays (see [[decisions/veritas-uber-production-manual-first]])
- Deployment timing: requires coordination with BFrost team for a maintenance window
- Target: before end of May 2026

## Team

- [[Sunil Jaiswal]] — Veritas pipeline, E2E testing, deployment coordination
- [[Aditya Krishna]] — tech lead / reviewer
- [[Souvik Mudi]] — contributor
- [[Tushar Shirbhate]] — contributor

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
