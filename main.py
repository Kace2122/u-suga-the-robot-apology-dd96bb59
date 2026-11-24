#!/usr/bin/env python3
"""The Robot Apology -- entry program.

Writes one short text to /output/entry.txt: a robot's two-line
confession. Line one owns one specific mistake -- it mowed over the
tulips, mistaking them for grass through its camera. Line two names
the lesson and the changed behaviour: check the map of the flower
beds, walk the lawn first, and mark the beds before the blades spin.

Deterministic, no network, no arguments, no randomness. Runs in well
under a second.
"""

import os

TEXT = (
    "I am sorry I mowed over your tulips because from my camera they looked like grass.\n"
    "I learned to check the map of the flower beds before I cut, and now I walk the lawn first and mark the beds before the blades spin."
)


def main() -> None:
    # The gate allows 1-400 characters: fail loudly instead of emitting an invalid entry.
    if not 1 <= len(TEXT) <= 400:
        raise SystemExit(f"entry text is {len(TEXT)} characters, outside the 1-400 gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
