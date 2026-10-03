---
name: ardians-product-growth
description: Prepares go-to-market positioning, launch communications, and growth plans. Use when the user asks to plan our go-to-market, write a GTM plan, prepare launch comms, define positioning, or build a growth plan.
triggers:
- go-to-market
- gtm plan
- launch comms
- positioning
- growth plan
---

# Ardians Product Growth

Optional stage 7 of the Ardians product pipeline. Turn a shipped or release-ready
product into positioning, launch assets, and a plan the team can run.

## Entry and exit

- **Entry:** a release candidate or shipped product, plus the PRD.
- **Exit:** a GTM plan plus launch assets.

Read `../ardians-product-orchestrator/references/pipeline.md` for stage order.
Run this stage when the request includes positioning, launch communications, or
go-to-market, or when the user asks for it.

## Steps

1. **Ground the market claims.** Invoke `research-brief` for market, competitor,
   and audience research, and `evidence-based-citations` so every external claim
   carries an exact quote and an official source. Distinguish evidence from
   hypothesis.
2. **Choose positioning.** State the target segment, the alternative the user
   has today, the differentiator, and the proof. Reject positioning that the
   evidence does not support.
3. **Write the launch copy.** Invoke `technical-writing` for developer and
   technical audiences and `plain-english-content` for general audiences. Use
   active voice and front-load the value.
4. **Build the plan.** Assemble channels, sequencing, owners, and success
   metrics. On request, publish it in `notion` and create launch tasks in
   `linear`.
5. **Define the measurement.** Reuse the stage 5 metrics where possible. Name
   what a good and a bad launch look like in numbers.

## Gate

Stop after the GTM plan and launch assets. Present positioning, the evidence
behind it, the plan, and the metrics, then ask the user to approve.

## Boundaries

- Do not state unverified market claims as fact.
- Do not publish launch content to an external channel without explicit
  confirmation.
