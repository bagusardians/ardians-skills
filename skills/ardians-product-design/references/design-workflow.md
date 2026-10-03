# Design Workflow Reference

Detail for `ardians-product-design`. Keep the SKILL.md as the guide and this
file as the checklist.

## Extraction path

Use when the user supplies a reference site and `extract-design-system` is
active.

1. Confirm the URL is public and reachable.
2. Run the skill's workflow to produce `.extract-design-system/raw.json`,
   `.extract-design-system/normalized.json`, `design-system/tokens.json`, and
   `design-system/tokens.css`.
3. Summarize primary, secondary, and accent colors, detected fonts, and spacing,
   radius, and shadow scales.
4. Mark single-page or dynamic-site results as provisional.

## Fallback path

Use when `extract-design-system` is not available or the user has no reference
site.

1. Invoke `frontend-design` to choose and document a visual direction.
2. Invoke `theme-factory` to produce tokens and a theme.
3. Record in the spec that tokens are designer-authored.

## Component and page spec checklist

- Inventory: every component, with its variants.
- States: default, hover, focus, active, disabled, error, empty, loading.
- Responsive: breakpoints and how layout changes at each.
- Content: labels, empty states, error copy, and microcopy rules.
- Accessibility: contrast ratios, focus order, target sizes, motion reduction,
  and semantic structure.

## Exit criteria

- `design-system/tokens.json` and `design-system/tokens.css` exist.
- The component and page spec covers every screen in the PRD's MVP scope.
- Accessibility requirements are named, not implied.
- Token provenance is stated as extracted or designer-authored.
