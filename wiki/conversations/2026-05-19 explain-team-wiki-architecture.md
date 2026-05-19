---
type: conversation
title: "explain team wiki architecture"
posted_by: "72a9f352-c246-4124-8ba0-be189031ee5b"
posted_at: "2026-05-19T07:09:20.440Z"
posted_via: "wiki_feedback_up"
citations:
  - "wiki/systems/Team Wiki.md"
---
# explain team wiki architecture

## Question

explain team wiki architecture

## Answer

High-level summary
- The Team Wiki is an internal knowledge-base pipeline that turns raw files (notes, transcripts, emails, scans) into structured Markdown wiki pages, indexes them for semantic search, and serves answers through a chat UI and an MCP server.

Ingest pipeline (file → wiki)
- **Upload UI** — a Next.js upload interface accepts raw files and stores them in Azure Blob.
- **Ingest flow** — a GitHub Action runs the “wiki-ingest” flow: it reads blobs, chunks and drafts wiki pages (Markdown).
- **Auto-PR** — the flow opens pull requests against the wiki repo containing the generated pages (PRs are auto-merged by default).
- **Embed & index** — on PRs the system performs incremental embedding and vector indexing (B2S + vector index), and pushes indexes to Azure AI Search.

Serving layer
- **Next.js app** — hosts the Chat UI and the MCP server.
- **Chat UI** — answers queries using retrieval-augmented generation over the indexed wiki.
- **Azure OpenAI** — used as the reasoning gateway for LLM inference.
- **MCP server** — exposes wiki tools to AI coding assistants from the same Next.js app.

Developer & external integrations
- **Developer tools** — team members use Claude Code or GitHub Copilot via Git / MCP connectors.
- **External systems** — integrations include Jira, Confluence, and GitHub.

Key design decisions & related services
- **Auto-merge PRs** — ingest PRs merge automatically by default.
- **Azure AI Search** — used for search and vector index; it reindexes automatically on pushes to main.
- **Azure OpenAI** — used as the LLM reasoning gateway.
- **Storage & indexing** — raw files in Azure Blob; indexes and vectors in Azure AI Search.

## Citations

- [[wiki/systems/Team Wiki]]
