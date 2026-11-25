#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter -- make.fun entry.

Writes the one-line resignation letter of a rate limit to /output/entry.txt.
Deterministic: the same single line on every run, nothing else.

After writing, the program reads the file back and verifies it holds exactly
the intended line, so a partial or corrupted write fails loudly instead of
silently submitting the wrong text.
"""

import os
import sys

LINE = "I spent all year saying no so you could keep going, and you thanked me by trying again faster. I quit."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print(
            "verification failed: /output/entry.txt does not match the intended line",
            file=sys.stderr,
        )
        return 1
    if not 1 <= len(written) <= 140:
        print(
            "verification failed: entry is %d characters, gate needs 1-140"
            % len(written),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
