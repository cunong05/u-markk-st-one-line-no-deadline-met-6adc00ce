#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke giving an excuse for a missed deadline
to /output/entry.txt. The entry is that line and nothing else.
"""

import os

ENTRY = "I didn't miss the deadline, I just extended it in my head and forgot to tell anyone."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
