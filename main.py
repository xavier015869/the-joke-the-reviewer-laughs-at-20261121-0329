#!/usr/bin/env python3
"""The joke the reviewer laughs at — a make.fun bounty entry.

The whole program does one thing: it writes a single one-line joke about
working beside AI coding agents to /output/entry.txt, in the exact shape
the grader wants — UTF-8 text, one line, 1 to 280 characters.

The joke is written from the reviewer's chair. Anyone who has ever
shepherded an AI agent's pull request through review knows both halves
of it are true, which is why the punchline lands.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

JOKE = (
    "I review my AI agent's pull requests exactly the way it reviews mine: "
    "instantly, confidently, and without ever opening the diff."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke must be 1-280 characters, got {len(text)}"
    assert "\n" not in text, "the joke must fit on one line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
