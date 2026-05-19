---
type: system
---

# Team Wiki

An internal knowledge base platform that ingests raw files (notes, transcripts, emails, scans) into structured Markdown wiki pages, indexes them for semantic search, and serves answers via a chat UI and MCP server.

## Architecture

```
Team → [Next.js upload UI] → Azure Blob (files)
                                    ↓
                        [GitHub Action — wiki-ingest flow]
                         write / chunk / draft wiki pages
                                    ↓
                        [Auto-PR] → Wiki repo (Markdown pages)
                                    ↓
                        [Embed + Index — incremental on PR]
                         B2S + Vector index → Azure AI Search
```

### Serving layer (Next.js app)

- **Chat UI** — answers questions using retrieval-augmented generation
- **Azure OpenAI** — reasoning gateway for LLM inference
- **[[MCP]]** server — exposes wiki tools to AI coding assistants (same Next.js app)

### Developer integrations

Team members interact via **[[Claude Code]]** or GitHub Copilot through Git / MCP connectors. External integrations: Jira, Confluence, GitHub.

## Key design decisions

- [[Auto-merge PRs in Team Wiki Ingest Flow]] — PRs created by the ingest flow merge automatically by default
- [[Use Azure AI Search for Team Wiki Indexing]] — Azure AI Search reindexes automatically on push to `main`
- [[Use Azure OpenAI as Team Wiki Reasoning Gateway]]
- [[Serve MCP from Team Wiki Next.js App]]

## Related systems

- [[Azure Blob]] — raw file storage
- [[Azure AI Search]] — search and vector index
- [[Azure OpenAI]] — LLM inference

*Source: raw/scans/ChatGPT Image May 19_ 2026_ 10_18_11 AM.png*
