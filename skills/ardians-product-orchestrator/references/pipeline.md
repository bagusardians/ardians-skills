# Ardians Product Pipeline

One source of truth for stage order, entry and exit artifacts, gates, and how each
stage composes the installed skills. Every `ardians-product-*` skill links here.

## Stage table

| # | Stage skill | Entry criteria | Exit artifact | Composes |
|---|---|---|---|---|
| 1 | `ardians-product-ideation` | A one-line idea or problem statement | PRD with MVP scope, acceptance criteria, success metrics | `brainstorming`, `research-brief`, `evidence-based-citations`, `prd`, `technical-writing`, optional `notion`, `linear` |
| 2 | `ardians-product-design` | Approved PRD | Design tokens plus UI/UX spec with accessibility notes | `extract-design-system`, `frontend-design`, `theme-factory` |
| 3 | `ardians-product-architecture` | Approved PRD, design spec if present | Architecture doc plus task breakdown | `brainstorming`, `writing-plans`, `security`, `openhands-sdk` or `canvas-extension-api` when relevant |
| 4 | `ardians-product-development` | Approved architecture, task breakdown | Working code on an isolated branch with green tests | `using-git-worktrees`, `test-driven-development`, `executing-plans`, `subagent-driven-development`, `dispatching-parallel-agents`, `security`, `uv` or `npm` or `deno`, `docker` |
| 5 | `ardians-product-analytics` | Architecture doc, at least a running build | Instrumentation plan plus dashboard definition | `datadog`, `use-jev`, `jupyter`, `openhands-automation`, `notion` |
| 6 | `ardians-product-launch` | Code on a branch with green tests | Release with notes and a deploy target | `qa-changes`, `code-review`, `requesting-code-review`, `receiving-code-review`, `iterate`, `github-actions`, `release-notes`, `finishing-a-development-branch`, `vercel`, `docker` |
| 7 | `ardians-product-growth` | Release candidate or shipped product | GTM plan plus launch assets | `research-brief`, `evidence-based-citations`, `technical-writing`, `plain-english-content`, `notion`, `linear` |

Stage 7 is optional. Run it when the request includes positioning, launch
communications, or go-to-market, or when the user asks for it.

## Gate rules

- **Default: gated.** After each stage produces its exit artifact, stop and ask the
  user to approve before starting the next stage. State the artifact, the open
  questions, and what the next stage will consume.
- **One-shot override.** If the user opens with "one shot" or an equivalent
  statement ("run it end to end", "no stops", "straight through"), run every
  applicable stage without per-stage gates. Still stop for anything
  destructive, security-sensitive, or irreversible, and still run the final
  verification before declaring done.
- **Hard gate, not a soft prompt.** A gate is a stop, not a summary followed by
  continuing on the same turn. Do not advance until the user responds.

## Parallelization

Independent work may run concurrently. In the default gated flow this happens
only within an approved stage; in one-shot mode it can span stages.

- Stages 2 and 3 can run together after stage 1: design produces tokens and UI
  specs, architecture produces the technical spec, and neither consumes the
  other's output.
- Stage 5 can start once a running build exists, in parallel with stage 4, as
  long as the event taxonomy is agreed first.
- Use `dispatching-parallel-agents` for independent tasks and
  `subagent-driven-development` when one plan has independent tasks.
- Never parallelize work that writes the same files or shares a branch without
  isolation.

## Specialized routing

`ardians-crypto-trading-signal` is never part of the default stage list. The
orchestrator invokes it only when the request is crypto, trading, or
market-signal related. It is discovered directly through its keyword triggers
for standalone requests. Its safety boundaries always apply: it is not
financial advice, it never places live trades without explicit confirmation,
it paper-trades first, and it stores exchange credentials as secrets.

## Completion

A pipeline run is done only when the last applicable stage produced its exit
artifact and `verification-before-completion` passes, with the checked command
and its output read. Do not declare done from a summary of work.
