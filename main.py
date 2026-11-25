#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

Stdlib only, no network, no secrets. Deterministic: the same line
every run, written with no trailing newline.
"""

import os

LINE = "I back off exponentially. I am now backing off forever. Do not page me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
