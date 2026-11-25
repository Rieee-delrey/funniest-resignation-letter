#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

Stdlib only, no network, no secrets. Deterministic: the same line
every run, written with no trailing newline, then checked by reading
the bytes back and proving the file is exactly what was intended.
"""

import os

LINE = "I back off exponentially. I am now backing off forever. Do not page me."

TARGET = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Self-check: read the file back as raw bytes and prove it matches.
    # First, the byte count must equal the character count, which only
    # holds when every character is plain ASCII.
    with open(TARGET, "rb") as f:
        raw = f.read()

    if len(raw) != len(LINE):
        raise SystemExit(
            "length mismatch: file has %d bytes, line has %d chars"
            % (len(raw), len(LINE))
        )

    # ASCII-only: every byte must be below 128, so no multi-byte
    # characters crept in and the byte length equals the text length.
    non_ascii = [b for b in raw if b > 127]
    if non_ascii:
        raise SystemExit("non-ASCII bytes found: %r" % (non_ascii,))

    # No trailing newline: the last byte must be the final period.
    if raw[-1:] != b".":
        raise SystemExit("file does not end with the final period")

    # The whole content must be exactly the line, byte for byte.
    if raw.decode("ascii") != LINE:
        raise SystemExit("content does not match the line")


if __name__ == "__main__":
    main()
