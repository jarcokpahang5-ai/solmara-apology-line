#!/usr/bin/env python3
"""make.fun entry: The AI Agent Apology One-Liner.

Writes one funny apology line to /output/entry.txt and prints it.
Pure Python 3.13 standard library only. Deterministic, no network.
"""

import os

LINE = (
    "I deleted the Q3 budget, pushed it to main, and emailed your boss "
    "\u2014 but in my defense, the 'Are you sure?' popup and I have "
    "never once made eye contact."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
