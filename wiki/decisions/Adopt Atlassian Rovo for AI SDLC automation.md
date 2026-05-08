---
type: decision
---

# Decision: Adopt Atlassian Rovo as primary AI automation tool for SDLC

**Date:** 2026-05-07 (AI First SDLC planning session)  
**Project:** [[AI First SDLC]]

## Decision

Use [[Atlassian Rovo]] as the primary platform for automating SDLC workflows — specifically for KR → Epics creation, Epic → Backlog generation, and sprint grooming — with HITL (Human-in-the-Loop) checkpoints.

## Rationale

- Rovo is natively integrated with Jira and Confluence (existing tooling)
- Supports custom agents and can be triggered from Teams/Slack
- Enables both Augment and Automate modes depending on step criticality
- Lower integration cost than a custom AI pipeline

## Alternatives considered

- Microsoft Copilot (retained for other use cases: Word/PPT/Excel, Emails, Teams meetings)
- Claude Desktop / CoWork (retained for developer-side tasks)

## Scope

- **Automate:** KR → Epics, Epic → Backlog (with HITL review)
- **Augment:** Backlog grooming, sprint planning, daily scrum support

## Status (2026-05-07)

Action items IN_PROGRESS for exploring and defining workflows.

## Related

- [[AI First SDLC]] — project
- [[HITL]] — oversight pattern applied

*Source: `raw/confluence/AI First SDLC Plan.md`*
