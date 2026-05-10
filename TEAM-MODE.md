# Team-mode for `knowledge-base-wiki`

A two-page operator's guide. What it is, what's in each repo, how the pieces glue together, what's running where.

---

## What it is

A team-shared knowledge base that ingests raw stuff (transcripts, emails, clips, screenshots, pasted notes) and turns it into structured Markdown wiki pages with citations. Two surfaces: a web chat for non-engineers, and a Claude Code MCP path for engineers. Karpathy's "wiki of yourself" — but for a team, with the ingest pipeline, retrieval index, and feedback loop in shared infrastructure.

## Repos

| Repo | What it holds |
|---|---|
| `GauravShah-TomTom/knowledge-base-wiki` | The wiki content (`wiki/<topic>/*.md`), ingest scripts, ingest-cron + index workflows, qmd plugin install, `/.claude/skills/` for engineers' CLI flows. Forked from upstream personal-mode wiki. |
| `tomtom-internal/team-wiki-app` | The Next.js app: web upload UI, chat UI, MCP server, feedback endpoints, Terraform for all Azure infra. |

## Architecture

```
              ┌─────────────────────────────────────────┐
  uploads     │         team-wiki-app  (Container App)  │
  (web)──────▶│  /upload   /chat   /api/mcp   /settings │
              │  /api/chat/feedback                     │
              └────────────┬────────────────────────────┘
                           │ writes raw/, queries Azure AI Search
                           ▼
                  ┌───────────────────────┐
                  │  Azure Blob (raw/)    │ ←──┐
                  └───────────┬───────────┘    │
                              │ cron 15 min    │  PRs (feedback,
                              ▼                │   ingest)
                  ┌───────────────────────┐    │
                  │  GitHub Actions:      │    │
                  │  ingest-cron + claude │────┘
                  │  -code-action wires   │
                  │  in wiki-ingest skill │
                  └───────────┬───────────┘
                              │ commits Markdown to wiki/
                              ▼
                  ┌───────────────────────┐
                  │  knowledge-base-wiki  │
                  │  (main)               │
                  └───────────┬───────────┘
                              │ on push to wiki/**
                              ▼
                ┌────────────────────────────────────┐
                │  Azure AI Search (BM25 + vector)   │
                │  Single index serving:             │
                │   • chat UI (server-side)          │
                │   • engineer CLI via team-wiki MCP │
                └────────────────────────────────────┘
```

## Functionality

- **Ingest.** Drop files into the upload UI (drag-drop, URL paste, Confluence via stored Atlassian PAT) or use the MCP `wiki_add_*` tools from Claude Code. Lands in Azure Blob `raw/`. A 15-min cron Action picks up new blobs, dispatches `claude-code-action` running the `wiki-ingest` skill, opens a PR with raw + generated Markdown. Auto-merge unless the LLM flags `⚠️ CONFLICT`.
- **Indexing.** A single Azure AI Search index, rebuilt by `wiki-aoai-index.yml` on push to `wiki/**` — BM25 + vector via `text-embedding-3-small`, hybrid retrieval. Used by both surfaces.
- **Chat (web).** `/chat` runs `useChat` from the AI SDK. The route handler embeds the question, runs hybrid retrieval over Azure AI Search, stuffs top-8 pages as context, streams a GPT-5-mini answer through Vercel AI Elements components (Conversation / Message / Sources / PromptInput).
- **Engineer (CLI).** Same wiki repo. Engineers register the team-wiki MCP server with their `twk_…` token; `mcp__team-wiki__wiki_query` and `mcp__team-wiki__wiki_get_page` hit the same Azure AI Search index the chat UI uses. Saves and feedback go through `mcp__team-wiki__wiki_feedback_up|down`.
- **Feedback.** 👍 saves the conversation as `wiki/conversations/YYYY-MM-DD <slug>.md` via a PR opened by the `team-wiki-feedback-bot` GitHub App; auto-merges. 👎 increments `feedback_count_negative` on each cited page's frontmatter and opens a `wiki-feedback`-labeled issue. Same code path serves both the chat-UI buttons and the CLI `/wiki-feedback-up|down` skills.
- **Staleness sweep.** Weekly Action runs Claude Code over the wiki, prioritises pages with negative feedback, opens one PR with `⚠️ STALE` markers for human review.

## Tools & technology

- **Frontend:** Next.js 16 (App Router) + TypeScript, Tailwind v4, shadcn/ui, Vercel AI SDK + AI Elements (`Conversation`, `Message`, `Sources`, `PromptInput`).
- **Auth:** Auth.js v5 with Microsoft Entra ID provider (single-tenant — any TomTom employee can sign in). Per-user Atlassian access via stored PAT. Microsoft Graph integration (Teams, Outlook) is on the v2 list, not built today.
- **LLM (chat backend):** Azure OpenAI via TomTom's gateway (`api.chatgpt.tomtom-global.com`), deployment `dep-gpt-5-mini`, embedding `dep-text-embedding-3-small`.
- **Retrieval:** Azure AI Search Free tier (50 MB, 3 indexes, hybrid BM25 + vector, no semantic re-ranker).
- **Storage:** Azure Blob (raw/) + Tables (oauth_grants, apitokens, auditlog) on a dedicated storage account, managed-identity-only.
- **Secrets:** Azure Key Vault (`kv-team-wiki-ulkrw5`) — all 10 secrets mounted into the Container App via `secretRef:` with managed-identity auth.
- **Hosting:** Azure Container Apps (`ca-team-wiki`), `minReplicas: 1` to avoid jsdom cold-start. ACR pulls via managed identity.
- **Ingest LLM:** `anthropics/claude-code-action@v1` with the user's Claude Pro `CLAUDE_CODE_OAUTH_TOKEN`, model pinned to `claude-sonnet-4-6`.
- **Engineer-side:** team-wiki MCP server registration in Claude Code (per-user `twk_…` bearer); `wiki-ingest`, `wiki-query`, `wiki-feedback-up|down` skills in the wiki repo. Optional fallback: upstream's `qmd` plugin still works for personal-mode use.
- **Bot:** dedicated GitHub App `team-wiki-feedback-bot` (Contents R/W, PRs R/W, Issues R/W). Authenticates per request via `@octokit/auth-app` using App ID + Installation ID + private key from Key Vault.

## Sequence (chat path)

1. User signs in to `/chat` via Entra SSO.
2. Types a question; `useChat` POSTs to `/api/chat`.
3. Server `auth()`-gates, embeds the question (`dep-text-embedding-3-small`), POSTs `search` + `vectorQueries` to Azure AI Search → top-8 hits.
4. Server stuffs hits as context, streams GPT-5-mini reply through `createUIMessageStream`. A pass-through buffer strips inline `[[wiki/...]]` markers and stray empty bullets the LLM sometimes emits.
5. After streaming ends, server emits `data-citations` with the cited page paths.
6. UI renders streamed text via Streamdown (markdown), shows citations as a collapsible Sources panel.
7. User clicks 👍 → POST `/api/chat/feedback` → `saveConversation()` → GitHub App opens a PR → auto-merge → next index workflow run picks up the new `wiki/conversations/...` page.

Engineer CLI path follows the same retrieval but skips steps 4–6 — `mcp__team-wiki__wiki_query` returns top-k hits as raw context for Claude Code to synthesise locally.

## Setup (one-time, Azure side)

```sh
# 1. Clone, configure
cd team-wiki-app/infra && terraform init && terraform plan && terraform apply

# 2. Populate Key Vault with the 9 manually-managed secrets
#    (auth-secret, auth-entra-client-secret, atlassian-client-id/-secret,
#     github-pat, github-app-id/-installation-id/-private-key,
#     azure-openai-api-key) — azure-search-api-key is set by Terraform.

# 3. CI secrets on knowledge-base-wiki repo
#    AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_SUBSCRIPTION_ID  (OIDC federation)
#    AZURE_OPENAI_API_KEY, AZURE_SEARCH_API_KEY                (index workflow)
#    CLAUDE_CODE_OAUTH_TOKEN                                   (ingest action)

# 4. Initial deploy: GitHub Actions builds the Docker image, pushes to ACR,
#    `az containerapp update`s the revision. URL: https://ca-team-wiki.<env>.azurecontainerapps.io
```

## Setup (local dev for chat work)

```sh
cd team-wiki-app
./scripts/pull-env.sh          # writes .env.local from Key Vault
echo "AUTH_DEV_BYPASS=1" >> .env.local
npm run dev                    # http://localhost:3300/chat
# OR exercise just retrieval+LLM without UI:
node --env-file=.env.local scripts/smoke-chat.mjs "your question"
```

## Setup (engineer's local Claude Code)

```sh
# 1. Clone the wiki for local browsing (Obsidian, file edits, skills)
git clone GauravShah-TomTom/knowledge-base-wiki && cd knowledge-base-wiki

# 2. Issue yourself a team-wiki bearer token at
#    https://ca-team-wiki.<env>.azurecontainerapps.io/settings/tokens

# 3. Register the team-wiki MCP server in your Claude Code config
#    (~/.claude.json or via `claude mcp add`):
{
  "mcpServers": {
    "team-wiki": {
      "url": "https://ca-team-wiki.<env>.azurecontainerapps.io/api/mcp/mcp",
      "headers": { "Authorization": "Bearer twk_..." }
    }
  }
}

# 4. Try it: /wiki-query "who is leading id index improvement"
#    Behind the scenes Claude calls mcp__team-wiki__wiki_query → Azure AI Search.
```

No local SQLite, no `az login`, no post-merge hook — the MCP server fronts the same index the chat UI uses.

## Syncing from upstream

This repo is a fork of `tomtom-forks/knowledge-base-wiki`, which moves quickly. The team-mode delta is mostly net-new files (zero conflict surface), so syncing is usually clean.

```sh
git fetch upstream
git merge upstream/main
# resolve any conflicts (see below), then:
git push origin main
```

**Known recurring conflict surface (3 files):**

| File | Reason | Resolution |
|---|---|---|
| `.gitignore` | We removed upstream's `wiki/` line because we track `wiki/` as team content. (Negation `!wiki/` can't reverse a directory-level ignore.) | Always keep our version (no `wiki/` line). |
| `.claude/skills/wiki-ingest-per-note/SKILL.md` | We added a `[team-mode]` QMD-driven conflict-detection bullet *after* upstream's existing one. Pure addition — usually merges cleanly. | Keep both upstream's bullet and our `[team-mode]` block. |
| `.claude/skills/wiki-query/SKILL.md` | We appended two bullets at the end (stale-feedback awareness; prefer MCP for save). Pure addition at end of list. | Keep both upstream's bullets and our two appended ones. |

Everything else (new workflows, new scripts, new skills, all `wiki/**` content) is additive and conflict-free.

**Long term:** the team-mode bundle is meant to be contributed back upstream (per the original spec). Once that lands, this whole section goes away.

## Out of scope (v2)

Event-driven ingest (Event Grid → Function App). Manager / cloud persona (remote MCP for ChatGPT/Claude.ai). Sensitive-content classifier on uploads. Per-blob PRs (currently per-cron-run). Conversation history persistence in chat. Mobile responsive pass.
