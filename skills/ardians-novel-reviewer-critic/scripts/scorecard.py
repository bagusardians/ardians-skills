#!/usr/bin/env python3
"""Validate and render a novel review scorecard.

Computes the weighted overall rating from the anchored 1-10 rubric, emits a
Markdown scorecard and a JSON record for tracking scores across revisions.

Scoring rules enforced here:
  - Scores are 1-10; half points are allowed inside a category.
  - Categories absent from the input are treated as N/A and excluded from the
    weighted mean (their weight is dropped from the denominator).
  - Weights default to the rubric weights and are normalized over the scored
    categories, so partial scorecards still produce a coherent overall.

Input forms accepted:
  --input scores.json     JSON dict {"story": 7.5, "character": 8} or a list
                          [{"category": "story", "score": 7.5, "evidence": "ch.3"}]
  --scores story=7.5,character=8
  (if neither is given, an example scorecard is rendered)

Usage:
    python scorecard.py --scores story=7.5,character=8,prose=7
    python scorecard.py --input scores.json --json
"""
import argparse
import json
import sys

# Default weights from references/01-rating-rubric.md (sum = 1.00).
DEFAULT_WEIGHTS = {
    "concept": 0.10,
    "story": 0.15,
    "structure": 0.12,
    "character": 0.15,
    "prose": 0.12,
    "worldbuilding": 0.08,
    "theme": 0.08,
    "dialogue": 0.08,
    "emotional": 0.12,
}

LABELS = {
    "concept": "Concept and originality",
    "story": "Story and plot",
    "structure": "Structure and pacing",
    "character": "Character and arc",
    "prose": "Prose and voice",
    "worldbuilding": "Worldbuilding and setting",
    "theme": "Theme and meaning",
    "dialogue": "Dialogue",
    "emotional": "Emotional impact",
}


def parse_pairs(spec):
    entries = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError(f"bad pair {part!r}; expected category=score")
        key, value = part.split("=", 1)
        entries.append({"category": key.strip().lower(), "score": float(value)})
    return entries


def load_entries(args):
    if args.input:
        with open(args.input, encoding="utf-8") as handle:
            raw = json.load(handle)
        if isinstance(raw, dict):
            return [{"category": k.strip().lower(), "score": float(v)}
                    for k, v in raw.items()]
        if isinstance(raw, list):
            out = []
            for item in raw:
                entry = dict(item)
                entry["category"] = str(entry["category"]).strip().lower()
                entry["score"] = float(entry["score"])
                out.append(entry)
            return out
        raise ValueError("input JSON must be an object or a list of objects")
    if args.scores:
        return parse_pairs(args.scores)
    return [
        {"category": "story", "score": 7.5, "evidence": "ch. 1-24"},
        {"category": "character", "score": 8, "evidence": "ch. 4, 18"},
        {"category": "prose", "score": 7, "evidence": "ch. 2"},
        {"category": "structure", "score": 6, "evidence": "ch. 9-12"},
        {"category": "emotional", "score": 7.5, "evidence": "ch. 18"},
    ]


def validate(entries):
    errors = []
    for entry in entries:
        category = entry["category"]
        score = entry["score"]
        if category not in DEFAULT_WEIGHTS:
            errors.append(
                f"unknown category {category!r}; "
                f"expected one of {', '.join(sorted(DEFAULT_WEIGHTS))}"
            )
        if not 1 <= score <= 10:
            errors.append(f"{category}: score {score} outside 1-10")
        if score * 2 != int(score * 2):
            errors.append(f"{category}: score {score} is finer than half points")
    if errors:
        raise ValueError("; ".join(errors))


def compute(entries):
    seen = {}
    for entry in entries:
        seen.setdefault(entry["category"], entry)
    scored = [e for e in seen.values() if e.get("score") is not None]
    if not scored:
        raise ValueError("no categories scored")
    weight_total = sum(DEFAULT_WEIGHTS[e["category"]] for e in scored)
    numerator = sum(DEFAULT_WEIGHTS[e["category"]] * e["score"] for e in scored)
    overall = round(numerator / weight_total, 1)

    for entry in seen.values():
        category = entry["category"]
        weight = DEFAULT_WEIGHTS[category]
        entry["weight"] = round(weight / weight_total, 4) if entry.get("score") is not None else 0.0
        entry["weight_nominal"] = weight
        entry["label"] = LABELS[category]

    missing = [c for c in DEFAULT_WEIGHTS if c not in seen or seen[c].get("score") is None]
    return seen, overall, missing


def star_verdict(overall):
    if overall >= 9.0:
        return "5.0", "Must-read, exceptional"
    if overall >= 8.0:
        return "4.5", "Excellent, highly recommended"
    if overall >= 7.0:
        return "4.0", "Recommended, publishable"
    if overall >= 6.0:
        return "3.5", "Decent, with reservations"
    if overall >= 5.0:
        return "3.0", "Mixed; significant work needed"
    if overall >= 4.0:
        return "2.0", "Not ready; major revisions"
    return "1.0", "Foundational problems"


def render_markdown(seen, overall, missing):
    order = [c for c in DEFAULT_WEIGHTS if c in seen]
    lines = [
        "| Category | Score | Weight | Evidence |",
        "|---|---|---|---|",
    ]
    for category in order:
        entry = seen[category]
        evidence = entry.get("evidence", "")
        lines.append(
            f"| {entry['label']} | {entry['score']:g}/10 | "
            f"{entry['weight_nominal']*100:.0f}% | {evidence} |"
        )
    stars, verdict = star_verdict(overall)
    lines.append(f"| **Weighted overall** | **{overall:g}/10** | - | {stars} stars, {verdict} |")
    if missing:
        lines.append("")
        lines.append(
            "N/A (excluded from the weighted overall): "
            + ", ".join(LABELS[c] for c in missing)
        )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Validate and render a novel review scorecard.")
    parser.add_argument("--input", help="JSON file with scores")
    parser.add_argument("--scores", help="inline category=score pairs, comma-separated")
    parser.add_argument("--json", action="store_true", help="emit JSON only")
    parser.add_argument("--evidence-default", default="", help="evidence text for inline scores")
    args = parser.parse_args()

    try:
        entries = load_entries(args)
        for entry in entries:
            entry.setdefault("evidence", args.evidence_default)
        validate(entries)
        seen, overall, missing = compute(entries)
    except (ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    stars, verdict = star_verdict(overall)
    record = {
        "overall": overall,
        "stars": stars,
        "verdict": verdict,
        "categories": [
            {
                "category": c,
                "label": seen[c]["label"],
                "score": seen[c]["score"],
                "weight": seen[c]["weight"],
                "evidence": seen[c].get("evidence", ""),
            }
            for c in DEFAULT_WEIGHTS
            if c in seen
        ],
        "excluded": [LABELS[c] for c in missing],
    }

    if args.json:
        print(json.dumps(record, indent=2))
        return 0

    print(f"# Scorecard\n\n**Overall: {overall:g}/10** - {stars} stars - {verdict}\n")
    print(render_markdown(seen, overall, missing))
    print("\n## JSON record\n")
    print("```json")
    print(json.dumps(record["categories"], indent=2))
    print("```")
    return 0


if __name__ == "__main__":
    sys.exit(main())
