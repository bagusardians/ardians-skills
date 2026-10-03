---
name: ardians-product-ideation
description: Turns a raw product idea into a validated concept and a PRD. Use when the user asks to ideate a product, validate a product idea, define an MVP, scope a new product, run product discovery, or write a PRD.
triggers:
- ideate a product
- validate a product idea
- define an mvp
- product discovery
- write a prd
---

# Ardians Product Ideation

Stage 1 of the Ardians product pipeline. Turn a one-line idea into a validated
concept with a PRD the later stages can build from.

## Entry and exit

- **Entry:** a one-line idea, a problem statement, or a request to explore a product.
- **Exit:** a PRD containing the problem, target users, MVP scope, acceptance
  criteria, success metrics, and explicit non-goals.

Read `../ardians-product-orchestrator/references/pipeline.md` for stage order,
the gate rule, and where this stage hands off.

## Steps

1. **Clarify intent and scope.** Invoke `brainstorming`. Ask about the problem,
   the users, the constraint that makes this worth doing now, and what is out of
   scope. Do not write the PRD until the problem and the MVP boundary are agreed.
2. **Ground the claims in evidence.** If the idea relies on market claims, user
   research, competitor behavior, or sizing, invoke `research-brief` for the
   research and `evidence-based-citations` so every factual claim carries an
   exact quote and an official source. Mark anything unverified as an assumption.
3. **Define the MVP.** State the smallest release that proves the core value.
   List what ships in the MVP and what is deliberately deferred. Every deferred
   item is a non-goal, not a silent gap.
4. **Write the PRD.** Invoke `prd`. Produce the problem statement, personas,
   user stories, acceptance criteria, success metrics, and non-goals. Acceptance
   criteria must be testable; metrics must name a baseline and a target.
5. **Publish if asked.** On request, record the PRD in `notion` or create
   follow-up issues in `linear`. Use `technical-writing` for any prose section
   that will be read outside the team.

## Gate

Stop after the PRD. Present the problem, MVP scope, acceptance criteria, and
metrics, then ask the user to approve or revise before stage 2 (design) begins.
Do not start design or architecture on the same turn.

## Handoff

The PRD is the entry artifact for `ardians-product-design` and
`ardians-product-architecture`. Keep it in a stable location and reference it by
path in the handoff.
