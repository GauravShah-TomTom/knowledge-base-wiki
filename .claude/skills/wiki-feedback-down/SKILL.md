---
name: wiki-feedback-down
description: Use when the user gives negative feedback on a wiki answer — clicks 👎, says "this answer is wrong", "this is outdated", "this contradicts what I know", or invokes /wiki-feedback-down. Triggers the team-wiki MCP server to flag the cited wiki pages with frontmatter (`feedback_count_negative`) and open a tracking GitHub issue.
---

# Knowledge Base — Flag stale or wrong answer (👎)

This skill marks the cited wiki pages as having received negative feedback. The page text is **not** edited; only frontmatter signals are added. A GitHub issue is opened for human triage. The periodic staleness sweep (Task 7) prioritises pages with `feedback_count_negative > 0`.

## Procedure

1. Identify the **immediately preceding** assistant answer the user is giving 👎 on, plus the user question that produced it.
2. Identify the wiki pages the answer cited — these are the targets that get flagged.
3. **Required:** there must be at least one cited page. If the answer cited none, the feedback can't be filed at the page-level; tell the user the answer wasn't grounded in the wiki and there's nothing to flag.
4. Call `mcp__team-wiki__wiki_feedback_down` with:
   - `question`: the user's prior question, verbatim
   - `answer`: the assistant answer (saved into the issue body for context)
   - `citations`: the cited wiki page paths as an array, with `.md` extension
   - `conversation_url` (optional): only if this session has a stable URL
5. Report the resulting PR URL + issue URL back to the user.

## Fallback if the MCP server is not registered

If `mcp__team-wiki__wiki_feedback_down` isn't available, fall back to a manual flow:
- For each cited page, use `Edit` to add to its frontmatter:
  ```yaml
  feedback_count_negative: 1
  last_feedback_negative: "<today YYYY-MM-DD>"
  last_feedback_negative_conv: "(local — no URL)"
  ```
- Tell the user to commit + push, and to manually open a GitHub issue tagged `wiki-feedback`.

## Notes

- Polarity-only in v1: don't ask the user for a free-text reason. Reviewers infer the issue from the conversation context.
- Don't combine this with `wiki-feedback-up` in one turn — they're mutually exclusive signals.
