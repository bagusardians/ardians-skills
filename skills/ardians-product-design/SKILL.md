---
name: ardians-product-design
description: Produces UI and UX specifications grounded in a real design system. Use when the user asks to design the UI with a real design system, create design tokens, produce a UX spec, design the interface, or extract a design system from a reference site.
triggers:
- design system
- design the ui
- ux spec
- design tokens
- extract a design system
---

# Ardians Product Design

Stage 2 of the Ardians product pipeline. Produce design tokens and a UI/UX spec
that stage 3 (architecture) and stage 4 (development) can implement without
guessing.

## Entry and exit

- **Entry:** an approved PRD (or an equivalent written scope).
- **Exit:** `design-system/tokens.json` and `design-system/tokens.css` plus a
  component and page spec with states, responsive behavior, and accessibility
  notes.

Read `../ardians-product-orchestrator/references/pipeline.md` for stage order
and handoff. Detail lives in `references/design-workflow.md`.

## Steps

1. **Establish the design system.** If the user points at a reference site,
   invoke `extract-design-system` to produce starter token files. If that skill
   is not active in the runtime, do not invent tokens: fall back to
   `frontend-design` and `theme-factory` and say the extraction path was
   unavailable. Never overwrite an existing design system without confirmation.
2. **Design the interface.** Invoke `frontend-design` to produce the page and
   component structure, interaction states, and responsive behavior. Commit to
   one clear visual direction rather than a generic default.
3. **Apply and extend theming.** Invoke `theme-factory` to bind tokens to a
   theme, or to generate one when none fits. Keep semantic tokens separate from
   raw scale values.
4. **Write the spec.** Record component inventory, states (default, hover,
   focus, active, disabled, error, empty, loading), breakpoints, and content
   rules. State accessibility requirements: contrast, focus order, target size,
   motion, and semantics.
5. **State the limits.** Mark tokens that came from a single page or a dynamic
   site as provisional. Do not treat extracted output as authoritative without
   review.

## Gate

Stop after the design system and spec. Present the tokens, the interface
direction, and the accessibility notes, then ask the user to approve before
stage 3 (architecture) or stage 4 (development). Do not implement UI code here.

## Fallback rule

`extract-design-system` is optional. When it is unavailable, the stage still
completes using `frontend-design` and `theme-factory`, and the spec records that
tokens are designer-authored rather than extracted.
