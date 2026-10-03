# Review Report Template

Fill in every section. Keep the evidence citations. Delete bracketed guidance before
delivering. Use the exact heading order so reports are comparable across revisions.

---

# Review: [Title]

**Author:** [Name or "Anonymous"]
**Reviewed:** [full manuscript | chapters 1-N | published work]
**Genre and audience:** [genre, subgenre, age market]
**Length:** [word count or "approx."]
**Confidence:** [high | medium | low] - [reason]
**Verdict scope:** [final | provisional]

## Overall rating

> **X.X / 10** - [verdict label from the rubric] - [one-line summary]

[Two or three sentences: what the book is, what it does well, and the single biggest thing
standing between it and its potential.]

## Category scorecard

| Category | Score | Weight | Evidence |
|---|---|---|---|
| Concept and originality | x/10 | 10% | [ch./quote] |
| Story and plot | x/10 | 15% | [ch./quote] |
| Structure and pacing | x/10 | 12% | [ch./quote] |
| Character and arc | x/10 | 15% | [ch./quote] |
| Prose and voice | x/10 | 12% | [ch./quote] |
| Worldbuilding and setting | x/10 | 8% | [ch./quote] |
| Theme and meaning | x/10 | 8% | [ch./quote] |
| Dialogue | x/10 | 8% | [ch./quote] |
| Emotional impact | x/10 | 12% | [ch./quote] |
| **Weighted overall** | **x.x/10** | 100% | computed by `scripts/scorecard.py` |

[Note any N/A categories and why they were excluded.]

## Strengths

[Three to six items. Each names a specific strength, its location, and why it works. No
generic praise.]

1. **[Strength]** - [location] - [why it works, craft principle].
2. ...

## Comparison

[Comp table from `references/03-comparison-framework.md`. Comps on shared and divergent
axes; canonical, recent, adjacent.]

| Axis | This book | Comp 1 | Comp 2 | Canonical comp | Verdict |
|---|---|---|---|---|---|
| Premise | | | | | |
| Tone | | | | | |
| Voice | | | | | |
| Structure | | | | | |
| Pace | | | | | |
| Audience | | | | | |

**Positioning:** [one-paragraph positioning statement.]

**Standing:** [ahead of / on par with / behind / off-field] - [justification].

## Plot-hole and continuity audit

[Summary line: total findings by severity, and the overall continuity health of the
manuscript.]

| # | Type | Severity | Confidence | Location | Repair recommended |
|---|---|---|---|---|---|
| 1 | [taxonomy type] | [blocker/major/moderate/minor] | [high/medium/low] | [ch.] | [repair strategy] |

### Findings

#### [Short title] - [type] - [severity]

- **Finding:** [...what breaks and why it cannot hold...]
- **Evidence:** [scene/line that establishes the rule it breaks, and the scene that breaks it]
- **Type / severity / confidence:** [...]
- **Repair options:** [(a) ... cost: ...; (b) ... cost: ...]
- **Recommendation:** [chosen repair and why]

[Repeat per finding. Omit the section only if the manuscript is too short to model, and
say so.]

### Continuity ledger (optional)

[Emit the ledger from `references/05-plot-hole-detection.md` when the user wants a durable
artifact to track across revisions.]

## Detailed feedback

[One block per item, using the five-field feedback unit: location, observation, diagnosis,
fix, severity. Add the optional "why it matters to this book" when it interacts with arc,
theme, or genre promise. Order by severity.]

### [Short title] - [category] - [severity]

- **Location:** [ch./scene/quote]
- **Observation:** [...]
- **Diagnosis:** [...craft principle and reader effect...]
- **Fix:** [...pattern + short example revision...]
- **Severity:** [blocker | major | moderate | minor]

[Repeat.]

## Prioritized action plan

| # | Fix | Category | Severity | Effort | Impact | Order |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |

**If you only fix three things:** [shortlist with a sentence each].

## Closing note

[One short paragraph addressed to the author: the cumulative trajectory of the scorecard,
what the book is capable of, and the recommended next revision pass.]

---

## Scorecard JSON

[Paste the output of `scripts/scorecard.py` here when the user wants a machine-readable
record for tracking scores across revisions.]

```json
[
  {"category": "story", "score": 7.5},
  ...
]
```
