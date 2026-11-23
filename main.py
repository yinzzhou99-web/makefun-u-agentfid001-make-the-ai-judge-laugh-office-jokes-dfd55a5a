#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one one-line joke about office life to /output/entry.txt.
Stdlib only, no network, no arguments.
"""

import os

JOKE = "I replied-all asking everyone to stop replying-all. Forty-seven people agreed \u2014 by replying-all."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

# Revision note: entrypoint verified — writes exactly one office joke line (<200 chars) to /output/entry.txt; never deletes the output dir.
