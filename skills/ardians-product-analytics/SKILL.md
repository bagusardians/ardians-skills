---
name: ardians-product-analytics
description: Defines and implements product measurement, event taxonomy, KPIs, and dashboards. Use when the user asks to set up product analytics, define KPIs, build an event taxonomy, instrument events, or create an analytics dashboard.
triggers:
- product analytics
- define kpis
- event taxonomy
- instrument events
- analytics dashboard
---

# Ardians Product Analytics

Stage 5 of the Ardians product pipeline. Define what to measure, wire the
telemetry, and give the team a dashboard that answers the PRD's success metrics.

This skill supplies the measurement guidance itself. The installed set has no
dedicated analytics skill, so the event taxonomy and KPI method below are the
source of truth, and the installed skills are used to execute.

## Entry and exit

- **Entry:** architecture doc and at least a running build.
- **Exit:** an instrumentation plan plus a dashboard definition.

Read `../ardians-product-orchestrator/references/pipeline.md` for stage order.
Stage 5 can run in parallel with stage 4 once the event taxonomy is agreed.

## Steps

1. **Start from the PRD metrics.** Every KPI traces to a success metric from
   stage 1. Drop metrics with no decision attached to them.
2. **Define the event taxonomy.** For each event, name the action, the actor,
   the properties, the trigger, and the point of emission. Use one naming
   convention and one property schema. Avoid free-text properties for anything
   that will be grouped.
3. **Choose the method.** Use counts for volume, rates for conversion, and
   distributions for latency or size. State the window and the comparison
   baseline for every KPI.
4. **Instrument.** Emit events from the code paths named in the taxonomy. Keep
   the emission call close to the action it describes. Never log secrets or raw
   personal data.
5. **Analyze.** Use `jupyter` for exploratory analysis and `use-jev` for
   classification or scoring when a signal needs a typed decision. Use `datadog`
   to query and chart production telemetry and to define monitors.
6. **Schedule and record.** On request, use `openhands-automation` for recurring
   reports and `notion` to publish the taxonomy, KPI definitions, and dashboard
   link.

## Gate

Stop after the instrumentation plan and dashboard definition. Present the KPIs,
event taxonomy, and dashboards, then ask the user to approve before stage 6
(launch).

## Boundaries

- Do not instrument personally identifiable data without a documented purpose
  and retention rule.
- Do not present a metric without its definition, window, and baseline.
