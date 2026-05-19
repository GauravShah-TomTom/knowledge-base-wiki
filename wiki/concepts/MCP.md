---
type: concept
---

# MCP (Model Context Protocol)

An open protocol that allows AI coding assistants (such as [[Claude Code]]) to call tools exposed by a server over a standardised interface. In the [[Team Wiki]] architecture, the MCP server runs inside the same Next.js app as the Chat UI and exposes wiki search and ingestion tools to team members' AI assistants.

## Usage in Team Wiki

- The [[Team Wiki]] Next.js app runs an MCP server endpoint.
- Team members connect [[Claude Code]] (or GitHub Copilot) to this server via Git / MCP connectors to query and ingest wiki content without leaving their IDE.

## Related concepts

- [[Vector Index]] — underlying retrieval mechanism called by MCP tools

*Source: raw/scans/ChatGPT Image May 19_ 2026_ 10_18_11 AM.png*
