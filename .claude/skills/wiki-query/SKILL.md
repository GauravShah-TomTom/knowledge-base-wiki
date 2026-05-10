---
name: wiki-query
description: Use when the user asks any question, requests research, or wants information from the knowledge base. This is the default action in this repository — when in doubt, search the Wiki. Use for "find me...", "what do we know about...", "tell me about...", "who is...", "what is...", or any general research question.
---

# Knowledge Base - Query

When the user asks any question:

- **Prefer `mcp__team-wiki__wiki_query` when the team-wiki MCP server is registered** (team-mode setup). It runs hybrid BM25 + vector retrieval against the Azure AI Search index and returns top-k pages directly — same engine the team chat UI uses, no local SQLite needed. Use `mcp__team-wiki__wiki_get_page` to fetch a single page by path when you have a citation. Fall back to qmd only when the team-wiki MCP isn't registered.
- Otherwise, use `mcp__plugin_qmd_qmd__query` to search across Wiki collections: `concepts`, `decisions`, `people`, `systems`, `competition`. For broad questions, also search `notes`. Use `mcp__plugin_qmd_qmd__get` or `mcp__plugin_qmd_qmd__multi_get` to retrieve identified documents.
- If neither returns results, fall back to reading `wiki/<type>/_index.md` directly, or `wiki/index.md` for top-level navigation.
- Synthesize an answer with citations: `[[wiki/decisions/title]]`, `[[wiki/systems/name]]`, etc.
- **Stale-feedback awareness:** when citing a page, check its frontmatter. If `feedback_count_negative` is set and > 0, append an inline note next to that citation: `⚠️ This page has been flagged N× as potentially stale (last on <date>); treat its claims with caution and cross-reference other sources.` Don't drop the citation — readers still benefit from following it — just warn them.

Follow-up:
- If the answer seems to be a valuable artifact (analysis, full recap, comparison, non-obvious connection between pieces of information), propose filing it as a new page in `wiki/conversations/` and updating the index. In that case, the title of the new page should be descriptive and include the date, e.g. `wiki/conversations/YYYY-MM-DD Descriptive Page Title For Discussion.md`.
- Include the page in the index, with a one-liner summary of the content.
- **To save: prefer `mcp__team-wiki__wiki_feedback_up` if the team-wiki MCP server is registered in this session.** It opens a PR via the dedicated GitHub App and auto-merges — no local commit needed. Fall back to writing the file locally (and asking the user to commit + push) only when the MCP tool isn't available.
