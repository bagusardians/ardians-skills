# Phase 3: Voice Emulation

Build an original style fingerprint from a named author's stylistic features.
This phase composes `research-brief`, `evidence-based-citations`, and `use-jev`.

## Copyright and ethics boundary

- Extract features only: syntax, pacing, diction, rhythm, structure, and tone.
- Never reproduce copyrighted passages or text, and do not store long excerpts.
- Do not present the result as the work of a living author.
- If the user asks for verbatim reproduction, decline and offer feature-level emulation
  instead.

## Features to measure

- Sentence length distribution and variance.
- Punctuation habits: dashes, semicolons, fragments, run-ons.
- Default point of view and tense.
- Ratio of scene to summary, and dialogue to narration.
- Chapter length and structure.
- Imagery and metaphor density.
- Recurring structural devices, such as epigraphs or interleaved timelines.

## Steps

1. Use the user's own samples or public-domain works as the study set.
2. Measure the features above. Use `use-jev` to classify or score features where a
   typed judgment helps.
3. Record each feature as a rule the writer can apply, not as a quotation.
4. Cite the source of every factual claim about the author with
   `evidence-based-citations`.
5. Fill `../assets/style-fingerprint-template.md`.

## Deliverable

A completed style fingerprint: features, rules, provenance, and an ethics note.

## Gate

Present the fingerprint and confirm it captures the intended features before phase 4.

## Checklist

- No verbatim text from the source is stored.
- Every feature maps to an applicable rule.
- Provenance and an ethics note are present.
