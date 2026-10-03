---
name: ardians-novel-writing
description: "Writes and develops long-form fiction through an eight-phase pipeline: worldbuilding, style definition, voice emulation, deep research, genre immersion, drafting, editorial quality, and illustration and maps. Use when the user asks to write a novel, write a book, develop a writing style, ghostwrite in the style of an author, edit a manuscript, or create book cover art and maps."
triggers:
- write a novel
- write a book
- develop a writing style
- ghostwrite in the style of
- edit my manuscript
- book cover and maps
---

# Ardians Novel Writing

A standalone, on-demand skill for long-form fiction. It is not part of the product
pipeline. It runs eight phases, each with its own reference file and a gate before the
next phase.

## Entry and exit

- **Entry:** a fiction request, such as a premise, a genre, a target author voice, or a
  manuscript to edit.
- **Exit:** a completed manuscript plus the per-phase artifacts listed below.

## Ethics and copyright boundary

These are hard rules.

- Voice emulation extracts stylistic features only: syntax, pacing, diction, rhythm,
  structure, and tone. It must never reproduce copyrighted passages or text.
- Do not present generated prose as the work of a real, living author.
- Ground factual claims in the research phases with `evidence-based-citations`.
- Run a sensitivity and representation review in the editorial phase.

## Phases

Run the phases in order. Stop at each phase gate by default; run straight through only if
the user asked for "one shot" (or equivalent).

**Worldbuilding is phase 1. It begins immediately after the premise is agreed and before
style, voice, or drafting.** A story is built on a world; if the world is undefined, every
later phase invents it by accident.

| # | Phase | Artifact | Composes | Reference |
|---|---|---|---|---|
| 1 | Worldbuilding | World bible | `brainstorming`, `technical-writing` | `references/01-worldbuilding.md` |
| 2 | Style definition | Style guide | `technical-writing`, `brainstorming` | `references/02-style-definition.md` |
| 3 | Voice emulation | Style fingerprint | `research-brief`, `evidence-based-citations`, `use-jev` | `references/03-voice-emulation.md` |
| 4 | Deep research | Research brief | `research-brief`, `evidence-based-citations`, `notion`, `jupyter` | `references/04-deep-research.md` |
| 5 | Genre immersion | Genre playbook | `research-brief`, `use-jev` | `references/05-genre-immersion.md` |
| 6 | Novel writing | Outline and draft | `writing-plans`, `technical-writing`, `plain-english-content`, `agent-memory`, `dispatching-parallel-agents` | `references/06-novel-writing.md` |
| 7 | Editorial and quality | Edited draft | `use-jev`, `evidence-based-citations`, `technical-writing` | `references/07-editorial-quality.md` |
| 8 | Illustration and maps | Cover, illustrations, maps, typeset output | `theme-factory`, `frontend-design`, `canvas-extension-api`, `pdflatex` | `references/08-illustration-maps.md` |

## Steps

1. Confirm the premise, genre, audience, length target, point of view, and tense before
   phase 1. Do not start drafting until these are agreed.
2. Run the worldbuilding phase first, immediately after the premise, and gate it. Then run
   the remaining phases in order. For each phase, load its reference file and invoke the
   composed skills it names.
3. Between phases, present the phase artifact and ask the user to approve before
   continuing.
4. Keep continuity in the story bible across phases 6 and 7, using
   `assets/story-bible-template.md`, and start it from the world bible.
5. Assemble the manuscript with `scripts/manuscript_assembly.py` and report the word
   count.
6. Before declaring done, invoke `verification-before-completion` and confirm every phase
   artifact exists.

## Assets and scripts

- `assets/world-bible-template.md`: place, period, rules, institutions, stakes, texture.
- `assets/story-bible-template.md`: continuity tracker for characters, places, and timeline.
- `assets/style-fingerprint-template.md`: feature-only voice profile.
- `scripts/manuscript_assembly.py`: assemble chapters in order and count words.
