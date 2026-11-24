#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Deterministic, standard library only, no network,
no trailing newline.
"""

import os

ENTRY = "I take you, R-7, to hold and to reboot, in low battery and in full charge, till a firmware update do us part — and I will never clear your cache."


def main() -> None:
    # The sealed gate accepts exactly one line of 1-160 characters.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
