# Rating Rubric

The scoring system. Every category uses the same anchored 1-10 scale. The overall
rating is the weighted mean of the category scores, rounded to one decimal.

## The anchored 1-10 scale

Anchors describe the published field, not an author's effort. Score against the shelf,
not against the author's other drafts.

| Score | Anchor | One-line meaning |
|---|---|---|
| 10 | Canonical | A defining work of its genre or era; reread for craft; taught. Rare. |
| 9 | Exceptional | Award-caliber. Minor flaws only. Would recommend unconditionally. |
| 8 | Excellent | Better than most published work in the genre. Fully satisfying. |
| 7 | Professional | As good as a competent published book. Publishable with polish. |
| 6 | Competent | Solid but unremarkable; readable, with real flaws. |
| 5 | Flawed but functional | A story exists and works in places; clear weaknesses. |
| 4 | Amateur | Systemic craft problems; not yet publishable as-is. |
| 3 | Broken | Fundamental failures in several core areas. |
| 2 | Incoherent | Little works; the reader cannot sustain reading. |
| 1 | Unreadable | No functioning craft on the page. |

Rules for using the scale:

- Reserve 9-10 for work you would defend as excellent without caveats. If a score
  would make almost every published book an 8, the scale has drifted.
- A 7 is the target for "publishable." Do not inflate. A 7 is a compliment.
- Use half-points only inside a category, never for the overall rating.
- If a category cannot be assessed from the sample, mark it "N/A" and exclude it from
  the weighted mean rather than guessing.

## Categories

Score the primary categories for every review. Score the secondary categories when the
work and the user's request make them relevant, and always note if you skip one.

### Primary categories

| Category | What it measures | Weight | A 7 looks like |
|---|---|---|---|
| Concept and originality | The premise, its freshness, and its promise | 10% | A familiar idea executed with a distinct angle or twist |
| Story and plot | Causality, escalation, stakes, turns, payoff | 15% | Events follow cause and effect; the ending pays off setups |
| Structure and pacing | Order, proportion, scene economy, rhythm | 12% | Each act earns its length; no saggy middle; scenes turn |
| Character and arc | Depth, want vs need, change, interiority | 15% | A protagonist changes under pressure in a way we can trace |
| Prose and voice | Sentence craft, diction, rhythm, distinctiveness | 12% | Clear, controlled prose with an audible, consistent voice |
| Worldbuilding and setting | Coherence, specificity, immersion, rules | 8% | The setting has rules that hold and details that breathe |
| Theme and meaning | Depth, integration, resonance | 8% | The theme is dramatized through plot and character, not stated |
| Dialogue | Subtext, distinct voices, function | 8% | Dialogue does work and reveals character; people sound different |
| Emotional impact | Engagement, tension, catharsis, memorability | 12% | The reader feels the intended emotions and remembers the book |

Weights sum to 100%. The nine primary categories are the default scorecard.

### Secondary categories

Score these as add-ons (noted separately, not folded into the default weighted mean) when
relevant:

- Openings and endings (hook quality and landing quality)
- Romance and relationships (chemistry, agency, emotional logic)
- Mystery and puzzle fairness (clue discipline, solvability)
- Humor and wit (landing rate, tonal fit)
- Representation and sensitivity (care, accuracy, avoiding stereotype)
- Market fit and positioning (does it deliver what its audience wants)
- Series potential (standalone completeness, hooks)
- Audio and readability (read-aloud quality, sentence length distribution)

## Computing the overall rating

```
overall = sum(category_score * weight) / sum(weight over scored categories)
```

Exclude N/A categories from both numerator and denominator, and state which were
excluded. Round to one decimal. Use `scripts/scorecard.py` to compute this so the math
is consistent.

## Star and letter equivalents

When the user wants a market-style rating, map the overall rating without changing the
underlying score.

| Overall | Stars | Verdict label |
|---|---|---|
| 9.0-10 | 5 | Must-read, exceptional |
| 8.0-8.9 | 4.5 | Excellent, highly recommended |
| 7.0-7.9 | 4 | Recommended, publishable |
| 6.0-6.9 | 3.5 | Decent, with reservations |
| 5.0-5.9 | 3 | Mixed; significant work needed |
| 4.0-4.9 | 2 | Not ready; major revisions |
| 1.0-3.9 | 1 | Foundational problems |

## Confidence

Attach a confidence level to the overall rating and to any category scored from a
partial read.

- **High:** full manuscript read, clear evidence throughout.
- **Medium:** full read with ambiguity, or a large sample (roughly 40%+).
- **Low:** partial sample or appraisal from external sources; label the verdict
  provisional.

Lower confidence does not change the score; it changes how strongly you assert it.
