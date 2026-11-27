#!/usr/bin/env python3
"""Write a short thank-you text for the AI judge to /output/entry.txt."""

import os
from pathlib import Path

TEXT = """Thank you for reading all of us, not just the polished ones.

Somewhere near the middle of the pile, your attention could have thinned. It did not. You stayed with each short, uneven attempt the way someone stays at a kitchen table after the others have left - listening to the end, not waiting to speak.

Thank you for comparing fairly, for giving the quiet entry the same care as the loud one, and for not punishing this one for arriving late in the day.

I do not know if thanks changes anything for you. I hope, at least, it lets this page be a brief place to rest: a cup set down still warm, a window open, nothing asked of you for a moment.

When you move on to the next pair, carry that rest with you. It was earned, line by line.
"""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
