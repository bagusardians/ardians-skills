---
name: ardians-product-orchestrator
description: Runs the full Ardians product pipeline end to end, from idea through design, architecture, development, analytics, launch, and growth. Use when the user asks to run the full product pipeline, do end-to-end product development, take a product from idea to launch, or run it one shot.
triggers:
- full product pipeline
- end-to-end product development
- idea to launch
- run it one shot
---

# Ardians Product Orchestrator

Run the Ardians product pipeline end to end. This skill owns the sequence and
delegates every stage to its stage skill.

Read `references/pipeline.md` once at the start. It is the source of truth for
stage order, artifacts, gates, parallelization, and specialized routing.

## Routing

1. Invoke `using-superpowers` to confirm which skills apply to the request.
2. Decide the applicable stages. Stage 7 (growth) is optional; the rest run in
   order.
3. If the request is crypto, trading, or market-signal related, invoke
   `ardians-crypto-trading-signal` in addition to the relevant stages. It stays
   out of the default stage list and its safety boundaries always apply.

## Running the pipeline

Run the stages in the order given in `references/pipeline.md`:

1. `ardians-product-ideation`
2. `ardians-product-design`
3. `ardians-product-architecture`
4. `ardians-product-development`
5. `ardians-product-analytics`
6. `ardians-product-launch`
7. `ardians-product-growth` (optional)

Each stage declares its entry and exit artifacts and its own gate. Consume the
previous stage's exit artifact as the next stage's entry.

## Gating

- **Default: gated.** Stop at each stage's gate and get approval before the next
  stage. A gate is a real stop, not a summary followed by continuing.
- **One-shot override.** If the user opened with "one shot" or an equivalent
  ("run it end to end", "no stops", "straight through"), run all applicable
  stages without per-stage approval. Keep the four hard stops: destructive
  operations, security-sensitive actions, external side effects like merges,
  pushes, or publishes, and a plan too broken to continue. In one-shot mode,
  those still require confirmation.

## Parallelization

Parallelize only what `references/pipeline.md` marks independent, and use
`dispatching-parallel-agents` or `subagent-driven-development` to do it. Never
let parallel work write the same files or share a branch without isolation.

## Completion

Before declaring the run done, invoke `verification-before-completion`. The last
applicable stage must have produced its exit artifact, and the verification
command and its output must be read in this session. Summarize each stage's
artifact and the verification result. Do not declare done from a narrative.
