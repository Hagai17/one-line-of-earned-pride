#!/usr/bin/env python3
"""Write one line of earned pride to /output/entry.txt.

The line is a single line of at most 240 characters: a quiet, earned
moment of pride for someone in a concrete scene — the pride carried by
effort the reader can feel, never asserted or explained. The final line
was picked by drafting a slate of candidates and duelling them pairwise
on the bounty judge's criteria — genuine feeling first, then a concrete
visible scene, pride earned inside the line, a landing in one read,
and freshness. The slate and the duels are recorded in candidates.md.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Duel winner — see candidates.md for the full slate.
LINE = (
    "He'd been sober eleven days; at the wedding he held his brother's "
    "champagne through the toast, raised it with everyone else, and "
    "handed it back full."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
