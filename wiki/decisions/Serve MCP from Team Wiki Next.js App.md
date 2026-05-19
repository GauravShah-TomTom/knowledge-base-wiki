---
type: decision
---

# Serve MCP from Team Wiki Next.js App

The [[MCP]] server for the [[Team Wiki]] platform runs inside the same Next.js application as the Chat UI, rather than as a separate service.

## Rationale

Co-locating the MCP server with the Chat UI reduces deployment complexity — a single Next.js app serves both browser users (Chat UI) and AI coding assistants ([[Claude Code]], GitHub Copilot) over the [[MCP]] protocol. Both paths share the same retrieval layer ([[Azure AI Search]] + [[Azure OpenAI]]).

*Source: raw/scans/ChatGPT Image May 19_ 2026_ 10_18_11 AM.png*
