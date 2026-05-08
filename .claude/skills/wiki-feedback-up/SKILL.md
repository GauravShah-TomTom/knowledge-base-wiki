---
name: wiki-feedback-up
description: Use when the user gives positive feedback on a wiki answer — clicks 👍, says "save this answer", "save this conversation", "this was helpful, file it", or invokes /wiki-feedback-up. Triggers the team-wiki MCP server to file the answer back to wiki/conversations/ as a permanent page.
---

# Knowledge Base — Save useful answer back (👍)

Per Karpathy's "good answers compound back into the wiki" loop, this skill files a useful chat answer as a `wiki/conversations/<date> <slug>.md` page. The synthesis is preserved as written; no re-ingestion through `raw/`.

## Procedure

1. Identify the **immediately preceding** assistant answer in this session and the user question that produced it. If the prior answer was multi-part, save the most synthesised / most useful framing — not the entire transcript.
2. Identify the wiki pages the answer cited (look for `[[wiki/...]]` WikiLinks or path-style references like `wiki/people/Foo Bar`).
3. Call `mcp__team-wiki__wiki_feedback_up` with:
   - `question`: the user's prior question, verbatim
   - `answer`: the assistant synthesis (you may lightly clean formatting but don't change content)
   - `citations`: the cited wiki page paths as an array, with `.md` extension (e.g. `["wiki/projects/Foo.md", "wiki/people/Bar Baz.md"]`)
   - `conversation_url` (optional): only if this session has a stable URL
4. Report the resulting blob path + PR URL back to the user.

## Fallback if the MCP server is not registered

If `mcp__team-wiki__wiki_feedback_up` isn't available in this session, fall back to the upstream-compatible local-write path:
- Use `Write` to create `wiki/conversations/YYYY-MM-DD <slug>.md` with the same content shape (frontmatter `type: conversation`, body with Question / Answer / Citations sections).
- Tell the user to `git add wiki/conversations/... && git commit && git push`.

## Notes

- The MCP server's `wiki_feedback_up` opens an auto-merging PR with the page; the wiki-rebuild-index workflow re-embeds it on merge.
- Don't call this for trivial answers (one-line factual lookups). The intent is "compound" — save analysis, comparisons, syntheses, or non-obvious connections.
