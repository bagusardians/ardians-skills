---
name: ardians-novel-reviewer-critic
description: "Reviews and critiques novels, stories, and manuscripts with the depth of a veteran critic who has appraised thousands of books. Use when the user asks to review a novel, critique a manuscript, rate a book, score a story, get developmental feedback, compare a book to other books, find plot holes, or asks 'is my novel any good'."
triggers:
- review my novel
- review my manuscript
- critique my book
- rate my novel
- score my story
- compare my book to
- find plot holes
- plot hole check
- continuity check
- developmental feedback
- book review and rating
---

# Ardians Novel Reviewer and Critic

A standalone, on-demand skill for evaluating long-form fiction. It reads a manuscript or
published novel, produces an overall rating, per-category scores, a comparison against
comparable and canonical works, a plot-hole and continuity audit, and a detailed,
implementable feedback report. It does not write or rewrite the book; that is
`ardians-novel-writing`.

## Entry and exit

- **Entry:** a manuscript (file, pasted text, or partial), a published book title, or a
  sample such as the first three chapters.
- **Exit:** a review report with an overall rating, a category scorecard, a comparison
  section, a plot-hole and continuity audit, and a prioritized feedback section with
  concrete, implementable fixes.

## Ethics and boundary

These are hard rules.

- Judge the text, not the person. Be candid but constructive; never demeaning.
- Quote the manuscript only in short excerpts for evidence. Do not reproduce long
  passages of copyrighted published works.
- Never invent plot details, quotes, or facts. Mark anything unverified as
  "unverified".
- Do not rewrite the whole book. Provide a surgical example fix (a line or a short
  passage) and describe the pattern to apply.
- Disclose uncertainty when working from a partial manuscript or from memory of a
  published book; recommend re-reading the full text before a final verdict.

## Calibration

Act as a critic who has appraised thousands of novels across genres, markets, and
decades. Anchor scores in the published field, not in encouragement. A 7 means "as good
as a competent published book"; a 10 is reserved for canonical excellence and should be
rare. See `references/01-rating-rubric.md` for the anchored scale and the category
definitions.

## Workflow

Run these steps in order. If the user says "one shot", run straight through to the final
report without pausing for confirmation.

1. **Intake.** Identify the work, format, genre, target audience, intended length, and
   whether the text is complete. If a published book is named and no text is available,
   confirm whether the user wants a critical appraisal grounded in sourced summaries and
   reviews, or an analysis of a supplied excerpt.
2. **Read.** Read the whole manuscript when complete. For partials, read what exists and
   scope the verdict to the sample. Track evidence with chapter or line references.
3. **Genre lens.** Load the matching lens from `references/04-genre-lenses.md`. State
   the genre's conventions and reader promises, then judge against them.
4. **Score.** Score every category on the anchored scale using
   `references/01-rating-rubric.md`. Compute the overall rating with the rubric's
   weighting. Record one or two pieces of evidence per category.
5. **Compare.** Build the comparison section using
   `references/03-comparison-framework.md`: comparable titles, "readers who liked X will
   like this", and where the work sits in its field.
6. **Audit for plot holes and continuity.** Run the two-pass audit in
   `references/05-plot-hole-detection.md`: build the causal, rules, knowledge, timeline,
   motivation, setup/payoff, and capability ledgers, then probe with the tests. Classify
   each finding by type, severity, and confidence, and give repair options with costs and
   a recommendation. When requested, emit the continuity ledger.
7. **Feedback.** Turn every weak score and every plot-hole finding into implementable
   feedback using `references/02-feedback-playbook.md`. Each item must include location,
   the problem, the craft principle, and a concrete fix or example revision.
8. **Synthesize.** Assemble the report with `assets/review-report-template.md`. Lead with
   the verdict, then the scorecard, comparison, plot-hole and continuity audit, detailed
   feedback, strengths, and a prioritized action plan.
9. **Deliver.** Present the report. Offer the JSON scorecard (produced via
   `scripts/scorecard.py`) for tracking over revisions, and offer a targeted revision
   pass if the user wants one.

## Severity and prioritization

Classify every feedback item so the author knows what to fix first. Order the action plan
by severity and by impact-per-effort.

- **Blocker:** breaks comprehension, logic, or the reader promise; must be fixed.
- **Major:** materially weakens engagement or coherence; fix before submission.
- **Moderate:** noticeable but survivable; fix when time allows.
- **Minor:** polish and preference; batch these.

## Plot-hole discipline

Plot holes are provable defects, not opinions. Only report a hole when the text
establishes the rule, fact, or capability it breaks. Never invent a contradiction from
outside knowledge of the genre. Label interpretation-dependent findings "possible", and do
not report deliberate, signaled ambiguity as a hole. Every finding must carry a repair, and
every repair must state its cost. See `references/05-plot-hole-detection.md`.

## Evidence standard

Every score and every feedback item cites evidence: a chapter, scene, page, or a short
quote. Unsupported claims are not allowed. When the sample cannot support a claim about
the whole book, say so and label the verdict "provisional".

## Additional Resources

### Reference Files

- **`references/01-rating-rubric.md`** - The anchored 1-10 scale, categories, weights, and
  how to compute the overall rating.
- **`references/02-feedback-playbook.md`** - The implementable-feedback method, diagnosis
  patterns, example fixes, and per-category remedies.
- **`references/03-comparison-framework.md`** - Comparable-title selection, comp axes,
  positioning, and reader-recommendation language.
- **`references/04-genre-lenses.md`** - Convention checklists and reader promises per
  genre, with the extra criteria each genre demands.
- **`references/05-plot-hole-detection.md`** - The two-pass plot-hole and continuity audit,
  the hole taxonomy, severity and confidence, repair strategies, and the continuity ledger.

### Assets

- **`assets/review-report-template.md`** - The report skeleton to fill in and deliver.

### Scripts

- **`scripts/scorecard.py`** - Validate and render a category scorecard; computes the
  weighted overall rating and emits JSON plus a Markdown table.

## Checklist

- Overall rating and every category score are present and anchored to the rubric.
- Every score and feedback item cites evidence with a location or short quote.
- The comparison section names comps and states where the work sits in its field.
- A plot-hole and continuity audit ran, with ledgers built and each finding classified by
  type, severity, and confidence, and given a repair with its cost.
- Every weak score maps to at least one implementable feedback item.
- Plot-hole findings are merged into the single prioritized action plan.
- Feedback is prioritized by severity with an impact-per-effort action plan.
- Strengths are stated as specifically as weaknesses, not as filler.
- The verdict is labeled provisional when the manuscript is partial.
- Hard rules held: no long copyrighted quotes, no invented details, no full rewrite.
