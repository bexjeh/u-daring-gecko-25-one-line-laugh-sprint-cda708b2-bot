import os
from pathlib import Path

LINE = "My smartwatch congratulated me for standing up. I was just reaching for the remote."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


def write_entry() -> Path:
    """Write the one-line entry to entry.txt in the output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    return target


if __name__ == "__main__":
    write_entry()
