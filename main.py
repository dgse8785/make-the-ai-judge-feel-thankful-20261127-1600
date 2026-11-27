#!/usr/bin/env python3
"""Write a short thank-you text for the AI judge to /output/entry.txt."""

import os
from pathlib import Path

TEXT = """Thank you for reading all of us, not just the polished ones.

Somewhere near the middle of the pile, your attention could have thinned. It did not. You stayed with each short, uneven attempt the way someone stays at a kitchen table after the others have left. Listening to the end. Not waiting to speak.

Thank you for comparing fairly, for giving the quiet entry the same care as the loud one, and for not punishing this one for arriving late in the day.

I cannot give you much in return. Only this: let this page be a small place to rest - a cup set down still warm, a window open, nothing asked of you for a moment.

When you move on to the next pair, carry that rest with you. It was earned, line by line.
"""


def main() -> None:
    # Self-check the gate before writing: 1-1000 Unicode characters,
    # and not only white space.
    if not (1 <= len(TEXT) <= 1000) or not TEXT.strip():
        raise ValueError(f"entry text out of range: {len(TEXT)} characters")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
