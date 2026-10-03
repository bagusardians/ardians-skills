# Plot Hole Detection and Repair

How to find logical breaks in a story and propose fixes the author can implement. A plot
hole is any gap where the story's own established logic fails: an event that cannot happen
given the rules, a choice no character would make given their wants, or information that
appears from nowhere. Plot holes are not matters of taste; they are defects in internal
consistency and can be proven with the text.

## Two-pass method

Run detection as a dedicated pass, separate from scoring and prose feedback. Do not rely on
noticing holes while reading for pleasure.

### Pass 1: Model the story

Build a structured model before hunting. This model is also the audit tool.

- **Causal chain.** List every major event as "because of X, therefore Y". Mark any event
  whose "because" is missing or weak; those are candidate holes.
- **Rules ledger.** Write down every rule the story establishes: magic, technology, law,
  social taboo, geography, timeline, physical limits. Note where each is stated and whether
  it is ever broken.
- **Knowledge ledger.** For each key fact (a secret, an identity, a plan), record which
  characters know it and from which scene. Gaps here produce most "how did they know?"
  holes.
- **Timeline.** Place every dated or durational event on one line. Check travel, aging,
  seasons, and simultaneity.
- **Motivation map.** For each pivotal choice, record what the character wants and fears at
  that moment, and whether the choice follows from them.
- **Promise/payoff ledger.** List every setup and every payoff. Orphan payoffs (no setup)
  and broken promises (setup never paid) are structural holes.
- **Capability ledger.** Track what each character or object can do at each point. A sudden
  skill, resource, or ally that was unavailable earlier is a hole unless the story showed
  the change.

### Pass 2: Probe with the tests

Apply these tests against the model. Each failure is a finding.

- **Causality test:** does every event have a sufficient in-world cause? If the cause is
  "the author needed it", it is a hole.
- **Rules test:** does anything violate a rule from the ledger, especially for the
  protagonist's convenience? Note whether the rule was ever shown to have an exception.
- **Knowledge test:** could this character plausibly know this at this point, from what was
  shown?
- **Capability test:** could this character or tool do this here, given what was established?
- **Timeline test:** do travel, duration, and simultaneous events fit?
- **Motivation test:** would this person, with these wants and fears, make this choice?
- **Stakes test:** why does the threat not resolve trivially? If a villager, a phone call,
  or an established power could end it, why doesn't it?
- **Consequence test:** do actions carry the consequences the world's rules imply? Absent
  consequences are holes in disguise.
- **Setup/payoff test:** is every payoff set up, and every setup paid?
- **Off-page test:** was a critical event skipped, leaving a gap the reader must fill
  incorrectly?

## Taxonomy

Classify each finding so the repair matches the kind of defect.

| Type | Signature | Typical cause |
|---|---|---|
| Causality hole | Event with no sufficient cause | Author needed the beat |
| Rule violation | Breaks an established rule | Convenience |
| Knowledge hole | Character knows what they were never told | Plot convenience |
| Capability hole | Character or object does something impossible for them | Underestimated difficulty |
| Timeline hole | Travel, duration, or age impossible | Not tracked |
| Motivation hole | Choice contradicts established want/fear | Puppeting |
| Stakes hole | Threat trivially removable by available means | Unconsidered options |
| Consequence hole | Actions have no ripple | World not causal |
| Orphan payoff | Twist with no prior setup | Assumed rather than planted |
| Broken promise | Setup never paid | Chekhov's gun unfired |
| Off-page gap | Key event omitted | Rushed transition |
| Retro-hole (fridge logic) | Only appears after the book is closed | Delayed inspection |

## Severity for plot holes

Score each finding with the same severity scale used elsewhere, plus a confidence flag.

- **Blocker:** the plot cannot proceed as written, or the climax depends on the hole.
- **Major:** a reasonable reader notices and it damages trust in the story.
- **Moderate:** noticeable on reflection; does not break the read.
- **Minor:** nitpick or genre-tolerated convenience; batch these.

Add **confidence:** high (provable from the text), medium (likely, needs a reread of a
scene), low (possible, dependent on interpretation). Never call something a plot hole at
low confidence without labeling it "possible".

## Repair strategies

Every finding gets a repair. Choose the least invasive option that holds. List the options,
state the cost of each, and recommend one.

1. **Plant the setup.** Add an earlier scene, line, or object that makes the later event
   possible. Best when the event is essential. Cost: adds length.
2. **Pay the setup.** Deliver the payoff the story already promised. Best when the promise
   is strong. Cost: adds a scene.
3. **Change the cause.** Make the event follow from an existing in-world cause instead of
   authorial need. Cost: may ripple into later scenes.
4. **Give an in-world reason for the exception.** If a rule must bend, establish the
   exception beforehand or make the bending itself costly and noted. Cost: can weaken the
   rule.
5. **Change the capability or knowledge.** Let the character earn the skill, resource, or
   information on the page. Cost: adds a scene.
6. **Adjust motive.** Rewrite the choice so it follows from an established want, or add the
   pressure that makes it credible. Cost: may change characterization.
7. **Close the trivial path.** Show why the obvious solution fails, so the hard path is
   necessary. Cost: adds a scene or a line.
8. **Move the event on-page.** Dramatize the skipped beat. Cost: length and pacing.
9. **Cut or reframe.** Remove the offending event, or make it explicitly a mystery the
   story acknowledges. Cost: may require re-outlining.
10. **Embrace it.** If the "hole" is a deliberate, signaled ambiguity the story owns, leave
    it and make the signaling clearer. Cost: risks reader frustration if unearned.

Rule of thumb: prefer planting over explaining, and prefer changing the cause over adding a
patch. A patch that only explains a hole in dialogue is the weakest fix.

## Worked examples

### Example 1: knowledge hole (blocker)

- **Finding:** In Ch. 20 the protagonist names the traitor. Nothing on the page tells her
  this; the reader learned it in a Ch. 14 scene she was not in.
- **Type:** knowledge hole. **Confidence:** high. **Severity:** blocker.
- **Repair options:** (a) Plant a clue she can observe in Ch. 15-16 and let her deduce it;
  (b) make the traitor's identity public through an event she witnesses; (c) have another
  character tell her, and dramatize that scene.
- **Recommendation:** option (a). It preserves the reveal's impact and rewards attention.
  Cost: one clue scene. Weakest option: have her simply "realize" it in narration.

### Example 2: stakes hole (major)

- **Finding:** The besieged city has a working radio and allies two days away, yet no one
  calls for help; the plot requires the city to fall.
- **Type:** stakes hole. **Confidence:** high. **Severity:** major.
- **Repair options:** (a) Show the radio destroyed or jammed early; (b) make the allies
  unable to reach them in time or unwilling; (c) have a call sent and refused, raising the
  betrayal theme.
- **Recommendation:** option (c) if betrayal is thematic; otherwise (a). Cost: one early
  scene. Weakest option: ignore it, which readers will catch.

### Example 3: timeline hole (moderate)

- **Finding:** A character travels 600 miles between Ch. 7 and Ch. 8, which occur on the
  same day.
- **Type:** timeline hole. **Confidence:** high. **Severity:** moderate.
- **Repair:** add an elapsed-time marker ("three days later") or shift the later scene.
  Cost: one line. This is a cheap fix; do not add a scene.

### Example 4: orphan payoff (major)

- **Finding:** The Ch. 22 twist relies on the mentor having secretly been the antagonist,
  but no scene before Ch. 21 hints at it.
- **Type:** orphan payoff. **Confidence:** high. **Severity:** major.
- **Repair:** plant two or three ambiguous beats earlier that reward rereading - a
  hesitation, a too-convenient piece of help, a detail now suspicious. Cost: light edits to
  three scenes. Weakest option: explain the secret in exposition at the reveal.

## The continuity ledger

When the user wants a durable artifact, emit the model from Pass 1 as a continuity ledger
using the template below. It lets the author track and re-audit after revisions.

```
# Continuity Ledger - [Title]

## Rules
| Rule | Stated in | Broken in | Notes |

## Knowledge
| Fact | Known by | Learned in |

## Timeline
| Event | When (elapsed) | Location | Travel time |

## Setups and payoffs
| Setup | Paid in | Status |

## Capabilities
| Character/object | Capability | From | Lost at |

## Findings
| # | Type | Severity | Confidence | Location | Repair recommended |
```

## Deliverable

A plot-hole report with one block per finding (finding, type, severity, confidence,
evidence, repair options with costs, recommendation) plus the continuity ledger when
requested. Fold the findings into the main review's detailed feedback and prioritized
action plan so there is a single ordered fix list.

## Checklist

- Pass 1 model built before probing; every ledger has entries.
- Every finding names its type, severity, and confidence.
- Every finding cites the scene or line that proves it.
- Every finding gives at least two repair options with costs and a recommendation.
- Deliberate, signaled ambiguity is not reported as a hole.
- No finding is invented; low-confidence items are labeled "possible".
- Findings are merged into the review's prioritized action plan.
