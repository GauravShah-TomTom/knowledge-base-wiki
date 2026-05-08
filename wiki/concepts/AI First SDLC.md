---
type: concept
---

# AI First SDLC

An approach to software development lifecycle (SDLC) where AI tools are systematically integrated at each phase — from strategy and requirements through planning, execution, and review — to augment or automate developer workflows.

## SDLC phases and AI integration

```
Strategy → Product Requirements → Goal Setting → Planning & RoadMap
→ Execution & Monitoring → Review → Closure & Repeat
```

| Phase | AI role | Primary tools |
|---|---|---|
| Strategy / Requirements | Augment | [[Atlassian Rovo]], Microsoft Copilot, Minute Mate |
| Planning (OKR → Epics) | Automate | [[Atlassian Rovo]] |
| Backlog / Grooming | Augment + Automate | Rovo, Copilot |
| Sprint Planning | Augment | Rovo |
| Implementation & Testing | Augment + Conditionally Automate | Agentic IDE, Claude Code, Copilot CLI |
| Debug & Fix | Augment + Automate | Azure MCP, Airflow skills |
| Monitor & Support | Augment + Automate | same as Debug & Fix |

## Key principles

- Use [[HITL]] (Human-in-the-Loop) at high-stakes steps (story creation, grooming)
- Standardise on English-only meeting conversations for better transcript quality
- No assignees at story creation time
- Uniform [[Agentic Coding]] guidelines across all developers

## Related

- [[AI First SDLC]] project — the initiative implementing this approach
- [[Atlassian Rovo]] — primary automation tool
- [[Agentic Coding]] — concept
- [[HITL]] — concept

*Source: `raw/confluence/AI First SDLC Plan.md`*
