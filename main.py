#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single one-line joke about office life to entry.txt inside the
output directory named by MAKEFUN_OUTPUT_DIR (falling back to /output).

The joke is one sentence: a setup everyone who works in an office has
heard ("we're a family here") with a payoff that takes it literally.
Stdlib only, no network, no arguments, deterministic: every run writes
the exact same bytes.
"""

import os
import sys

JOKE = "My boss said 'we're a family here', so I asked HR when the inheritance meeting is."

OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 200


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)

    # Validate the joke against the gate before writing it.
    if not JOKE or not JOKE.strip():
        print("error: joke is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in JOKE or "\r" in JOKE:
        print("error: joke is not a single line", file=sys.stderr)
        return 1
    if len(JOKE) > MAX_CHARS:
        print("error: joke is %d characters, over the %d cap" % (len(JOKE), MAX_CHARS),
              file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)

    # Read it back and verify what landed on disk: exact bytes, a single
    # line, and no trailing newline beyond the joke itself.
    try:
        with open(path, "r", encoding="utf-8", newline="") as handle:
            written = handle.read()
    except (OSError, UnicodeDecodeError) as exc:
        print("error: could not read back entry.txt: %s" % exc, file=sys.stderr)
        return 1
    if written != JOKE:
        print("error: entry.txt does not match the joke", file=sys.stderr)
        return 1
    if written.endswith("\n") or written.endswith("\r"):
        print("error: entry.txt has a trailing newline", file=sys.stderr)
        return 1

    print("wrote %s (%d characters): %s" % (path, len(JOKE), JOKE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
