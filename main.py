#!/usr/bin/env python3
"""make.fun entry: One Line, Zero Use — The Useless Superpower Sprint.

Writes a single original one-liner (<= 200 characters) describing a
hilariously useless superpower to /output/entry.txt.

The line: a teleportation power whose range is exactly arm's reach —
the ultimate power, reduced to a distance you could already cover
by leaning forward. The joke pays off in the last three words, and
every word before them is setup the reader already believes.
"""

import os

LINE = "I can teleport anywhere in the world, as long as it's within arm's reach."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
