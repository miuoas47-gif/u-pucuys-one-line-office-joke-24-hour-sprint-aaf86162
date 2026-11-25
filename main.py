#!/usr/bin/env python3
"""One-Line Office Joke: prints the joke and writes it to entry.txt.

Deterministic: no network, no clock, no randomness. Run with no arguments.
Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""
import os

JOKE = "My manager told me to treat this job like it's my own business, so I immediately started looking for someone else to do the work."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    # MAKEFUN_OUTPUT_DIR is a directory; fall back to /output if unset.
    if os.environ.get("MAKEFUN_OUTPUT_DIR"):
        path = os.path.join(out_dir, "entry.txt")
    else:
        path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
