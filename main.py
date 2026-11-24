#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry for make.fun.

Writes exactly one character, "A", to /output/entry.txt.

The choice is coffee: "A" stands for coffee in this competition, and
coffee is the answer — the first cup of the day, black, no debate.
Nothing else is written: no newline, no punctuation, no explanation.
"""
import os

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")
CHOICE = "A"  # coffee


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(CHOICE)


if __name__ == "__main__":
    main()
