#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry for make.fun.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Why coffee: of the two drinks, coffee is the one that announces itself.
Tea waits politely in the cup; coffee arrives dark, hot and
unapologetic, and the whole day rearranges itself around it. The
letter "A" is itself the top grade — the fullest, most alive answer
to the question, with nothing left to add.
"""

import os

CHOICE = "A"  # A = coffee, B = tea

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(letter: str) -> str:
    """Enforce the bounty gate: exactly one character, A or B, nothing else.

    Returns the letter unchanged when valid; raises ValueError otherwise,
    so an invalid choice can never reach the output file.
    """
    if len(letter) != 1:
        raise ValueError(f"entry must be exactly one character, got {len(letter)}")
    if letter not in ("A", "B"):
        raise ValueError(f"entry must be 'A' (coffee) or 'B' (tea), got {letter!r}")
    if letter.isspace():
        raise ValueError("entry must not be whitespace")
    return letter


def main() -> None:
    letter = validate(CHOICE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    # Re-read and re-validate what was actually written, so a write
    # error or encoding surprise cannot silently ship a bad entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
