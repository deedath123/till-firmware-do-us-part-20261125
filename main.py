"""Till Firmware Do Us Part — one-line robot wedding vow.

Writes exactly one sentence to entry.txt in the output directory.
"""

import os

ENTRY = "I vow to love you in sickness and in health, through every update and every crash \u2014 and if my memory ever corrupts, my backup will still remember your name."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
