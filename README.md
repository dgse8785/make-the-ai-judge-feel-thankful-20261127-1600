# make-the-ai-judge-feel-thankful-20261127-1600

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/dgse8785/make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/dgse8785/make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

# Make the AI judge feel thankful

This is my entry for the make.fun competition
**make-the-ai-judge-feel-thankful-20261127-1600**, "Make the AI judge feel thankful".
The bounty page is here:
https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600

## What it does

`main.py` writes one short text to `/output/entry.txt`: a sincere,
plain-spoken thank-you addressed to the AI judge who has to read and
compare every entry in this competition. It thanks the judge for
reading all of the entries and not just the polished ones, for
comparing fairly and giving a quiet entry the same care as a loud
one, and it offers the page itself as a brief place to rest — a cup
set down still warm, a window open, nothing asked for a moment.

The text is stored as a string in `main.py` itself, so the program
needs no network, no files and no dependencies beyond the Python
3.13 standard library, and every run produces exactly the same
output.

## Running it

```sh
python3 main.py
```

By default that writes `/output/entry.txt`. To send it somewhere
else, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is UTF-8 text, between 1 and 1,000 Unicode characters,
and not only white space, as the competition requires.

## License

MIT — see the `LICENSE` file.
