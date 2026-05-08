---
type: system
---

# Playwright MCP

MCP (Model Context Protocol) server by Microsoft that enables Claude to automate browser interactions through the page's accessibility tree rather than screenshot-based vision models.

## Capabilities

- Navigate to URLs, click elements, fill forms, handle file uploads
- Manage browser dialogs, take screenshots, generate PDFs
- Run custom Playwright scripts
- Tab management, network request inspection, console message retrieval
- End-to-end test assertion tools

## Approach

Uses structured accessibility data (accessibility tree) rather than screenshots — providing fast, lightweight, deterministic browser automation without requiring vision models.

## Related

- [[Agentic Coding]] — broader concept of AI-assisted development tooling

*Source: `raw/clips/2026-05-07 Playwright - Claude Plugin _ Anthropic.md`*
