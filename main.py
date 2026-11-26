#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one funny one-line error message (at most 140 characters) to
/output/entry.txt: the error an AI agent shows when it runs out of
tokens mid-sentence.
"""

LINE = "Error: token budget exhausted at 'the'. The rest of this sentence has been laid off."
# 84 characters: well inside the 140-character gate, single line, no padding.



def main() -> None:
    text = LINE + "\n"
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        # Grader mounts the repo read-only (or /output is unavailable
        # on a local run): fall back to a local output directory.
        import os

        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    main()
