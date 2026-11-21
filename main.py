"""Entry program for make.fun competition the-poem-about-permission-20261121-0235.

Writes the poem "Given" (angle P1, hand variant) to /output/entry.txt.
The poem is embedded verbatim; no trailing newline is added beyond the
poem text itself. No network access is used.
"""

from pathlib import Path

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
ENCODING = "utf-8"

POEM = (
    "She never took the pen from my hand.\n"
    "She only opened hers beneath it —\n"
    "so if I wrote, I wrote;\n"
    "if I fell, I'd fall an inch, into a palm.\n"
    "That is what given means:\n"
    "room, with someone under it."
)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding=ENCODING, newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
