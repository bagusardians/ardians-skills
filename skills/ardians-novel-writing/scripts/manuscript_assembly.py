#!/usr/bin/env python3
"""Assemble chapter files into one manuscript and report word counts.

Chapters are ordered by natural sort so `chapter2` precedes `chapter10`.

Usage:
    python manuscript_assembly.py --chapters chapters --out manuscript.md
"""
import argparse
import re
import sys
from pathlib import Path

WORD_RE = re.compile(r"\S+")


def natural_key(name: str):
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r"(\d+)", name)]


def chapter_files(directory: Path, pattern: str):
    files = [p for p in directory.glob(pattern) if p.is_file()]
    return sorted(files, key=lambda p: natural_key(p.name))


def count_words(text: str) -> int:
    return len(WORD_RE.findall(text))


def assemble(directory: Path, pattern: str) -> tuple:
    files = chapter_files(directory, pattern)
    if not files:
        raise SystemExit(f"no files matching {pattern!r} in {directory}")
    parts = []
    report = []
    for path in files:
        text = path.read_text(encoding="utf-8").strip()
        words = count_words(text)
        report.append((path.name, words))
        parts.append(f"<!-- {path.name} -->\n\n{text}")
    manuscript = "\n\n\n".join(parts) + "\n"
    return manuscript, report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Assemble a manuscript from chapters.")
    parser.add_argument("--chapters", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--pattern", default="*.md")
    args = parser.parse_args(argv)

    manuscript, report = assemble(args.chapters, args.pattern)
    args.out.write_text(manuscript, encoding="utf-8")

    total = 0
    for name, words in report:
        print(f"{words:>8}  {name}")
        total += words
    print(f"{total:>8}  TOTAL ({len(report)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
