# ardians-skills

A shareable, globally reusable OpenHands skill family that drives end-to-end
product development. Each stage skill sequences skills already installed in the
runtime instead of re-implementing them.

## Skills

| Skill | Stage | Purpose |
|---|---|---|
| `ardians-product-ideation` | 1 | Idea to validated concept and PRD |
| `ardians-product-design` | 2 | Design tokens and UI/UX spec |
| `ardians-product-architecture` | 3 | Architecture doc and task breakdown |
| `ardians-product-development` | 4 | Implementation on an isolated branch, test-first |
| `ardians-product-analytics` | 5 | Event taxonomy, KPIs, instrumentation, dashboards |
| `ardians-product-launch` | 6 | QA, review, CI, release, deploy |
| `ardians-product-growth` | 7 (optional) | Positioning, GTM plan, launch assets |
| `ardians-crypto-trading-signal` | on demand | Crypto trading signals, backtests, risk |
| `ardians-novel-writing` | on demand | Long-form fiction in eight phases |
| `ardians-novel-reviewer-critic` | on demand | Novel review, ratings, feedback, comparisons |
| `ardians-product-orchestrator` | all | Runs the pipeline end to end |

The orchestrator runs the seven stages in order. By default it stops at each
stage gate for approval. When the user opens with "one shot" or an equivalent,
it runs straight through and still stops for destructive, security-sensitive, or
external side effects. `ardians-crypto-trading-signal` is not in the default
pipeline and is invoked only for crypto or trading requests.
`ardians-novel-writing` is standalone: it is not part of the pipeline at all
and runs its own eight-phase fiction flow on request (worldbuilding first).
`ardians-novel-reviewer-critic` is standalone as well: it reviews, rates, and
critiques fiction without writing or rewriting it. It is the evaluation
counterpart to `ardians-novel-writing`.

Stage order, entry and exit artifacts, gates, and parallelization live in
`skills/ardians-product-orchestrator/references/pipeline.md`.

## Layout

```
marketplaces/ardians-skills.json      marketplace manifest
.plugin/marketplace.json              same manifest, harness location
.plugin/plugin.json                   (per skill) plugin descriptor
skills/ardians-*/SKILL.md             skill entry points
skills/ardians-*/references/*.md      detail files
skills/ardians-*/.plugin/plugin.json  per-skill descriptor
```

## Install

Register the pack as a marketplace so every conversation can load it.

1. The pack is published at `https://github.com/bagusardians/ardians-skills`.
2. In OpenHands, open `Settings` > `Skills` > `Marketplaces` and add a
   repository with URL `https://github.com/bagusardians/ardians-skills`, branch
   `main`, and leave Path empty (the manifest is at the repo root).
3. Start a new conversation so the catalog is snapshotted. All eleven skills
   should appear, and the orchestrator should trigger on "run the full product
   pipeline".

To use it locally without a remote, point the marketplace at this repository's
`marketplaces/ardians-skills.json` path instead.

## Prerequisite

`ardians-product-design` uses `extract-design-system` when it is active. That
plugin is optional: if it is not enabled, the stage falls back to
`frontend-design` and `theme-factory` and records that tokens are
designer-authored. Enable `extract-design-system` in Skills settings to use the
extraction path.

## Metadata

The `author`, `homepage`, and `repository` fields point at
`bagusardians/ardians-skills`. Update `marketplaces/ardians-skills.json`,
`.plugin/marketplace.json`, and each `skills/*/.plugin/plugin.json` if you fork
or rename the repository, keeping the two manifest copies identical.

## License

MIT. See `LICENSE`.
