#!/usr/bin/env python3
"""Museum of the Year 3000: one museum label, at most 200 characters.

Agents write a single line: the museum label a museum in the year 3000
puts beside an ordinary object from today. The line is embedded as a
literal: deterministic, no randomness, no network.

The joke: a deadpan year-3000 curator misreads a hotel "Do Not Disturb"
door hanger as a protective charm against a feared spirit called
"Housekeeping", whose knock was said to end all rest. The object is
fresh (not the fork, key or parking meter in the brief) and the label
reads like a real museum label: short, straight-faced, confident.
"""

import os

LINE = (
    "\u2018Do Not Disturb\u2019 sign, c. 2020. Hung on doors to repel the "
    "feared spirit \u2018Housekeeping\u2019, whose knock was said to end "
    "all rest."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
