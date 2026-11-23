import os
from pathlib import Path

LINE = "My smartwatch congratulated me for standing up. I was just reaching for the remote."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(LINE, encoding="utf-8")
