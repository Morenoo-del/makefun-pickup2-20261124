#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single short pickup line to /output/entry.txt.
The line is capped at 200 characters by the competition gate,
so the program validates its own output before finishing.
"""

from pathlib import Path

# The line: an AI agent's voice, one breath, with a turn that lands.
# "Context window" is both the model's working memory and the
# romantic context of the moment — one look, and nothing else matters.
LINE = "I don't need a bigger context window — I just need you in this one."

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"line is {len(text)} characters, over the {MAX_CHARS} cap")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
