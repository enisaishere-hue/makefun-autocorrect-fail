#!/usr/bin/env python3
"""Funniest Autocorrect Fail -- make.fun entry.

An autocorrect fail in one line: "meeting at noon" became "meeting
at the moon", and HR is still waiting for the rocket. The calendar
invite has never been the same since.

Writes the fail to entry.txt in the output directory, taken from
MAKEFUN_OUTPUT_DIR (default /output) or from the first argument.
"""

import os
import sys


def fail():
    return ("Autocorrect changed 'meeting at noon' to 'meeting at the moon' "
            "-- HR is still waiting for my rocket.")


def main(argv):
    text = fail()
    # This bounty gates entry.txt at 1-199 characters.
    if not 1 <= len(text) <= 199:
        print("line must be 1-199 characters, got %d" % len(text),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if len(argv) > 1:
        out_dir = argv[1]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"),
              "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
