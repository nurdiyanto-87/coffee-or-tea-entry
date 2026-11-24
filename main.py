#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
Pure Python standard library only.

Chosen letter: A — coffee.
Coffee is the more vivid answer: the morning ritual, the smell of a fresh
brew filling the room, the first hot sip that wakes you up. One letter, A,
lands as a fuller, more alive answer for the drink it names than B ever
could for tea — coffee is the drink with the stronger sensory hook, the
bolder claim, the truer daily habit. A fits coffee exactly.
"""
import os

LETTER = "A"  # coffee

def main():
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("entry must be exactly one letter A-Z")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

if __name__ == "__main__":
    main()
