---
name: ardians-product-architecture
description: Produces the system architecture and technical spec for a product. Use when the user asks to plan the architecture, write a technical spec, do system design, produce an architecture doc, or break a product into build tasks.
triggers:
- product architecture
- technical spec
- system design
- architecture doc
- break into tasks
---

# Ardians Product Architecture

Stage 3 of the Ardians product pipeline. Turn an approved scope and design into
an architecture and a task breakdown the development stage can execute.

## Entry and exit

- **Entry:** approved PRD. The design spec is used when it exists.
- **Exit:** an architecture document plus an ordered, independently testable task
  breakdown.

Read `../ardians-product-orchestrator/references/pipeline.md` for stage order,
handoff, and parallelization points.

## Steps

1. **Weigh approaches.** Invoke `brainstorming` to compare at least two credible
   architectures against the PRD's constraints: cost, latency, scale, team
   skills, and time to first release. Record why the chosen one wins and what
   would change the decision.
2. **Specify the system.** Define components, boundaries, data models, APIs,
   storage, and the request and event flows. Name the failure modes and the
   recovery path for each critical flow.
3. **Cover security and data handling.** Invoke `security` for the threat model,
   authentication and authorization, secrets handling, input validation, and
   data retention. Security is a design input, not a later review.
4. **Match the product type.** For agent or app products, invoke `openhands-sdk`
   or `canvas-extension-api` so the design follows the platform's contracts
   rather than an invented one.
5. **Break the work down.** Invoke `writing-plans` to produce ordered tasks with
   entry and exit criteria, dependencies, and the tests that prove each one.
   Mark tasks that are safe to run in parallel.
6. **State non-functional targets.** Record performance, availability, and
   observability targets with the measurement for each.

## Gate

Stop after the architecture doc and task breakdown. Present the chosen
architecture, the top risks, and the task list, then ask the user to approve
before stage 4 (development).

## Handoff

The task breakdown is the entry artifact for `ardians-product-development`. Each
task must be small enough for test-driven development and independent enough to
parallelize when marked so.
