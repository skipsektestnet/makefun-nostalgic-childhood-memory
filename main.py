"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (at most 280 characters) recalling a childhood
memory to /output/entry.txt. The sentence is a concrete, sensory moment:
the ice-cream man's bell, afternoon rain, coins sweating in a small fist.

The gate this program must satisfy (RULES.txt): the output file is UTF-8
text of 1 to 280 characters, not only white space, a single clean sentence.
"""

import os
import sys
from pathlib import Path

MEMORY = (
    "The ice-cream man's bell always reached our street just as the "
    "afternoon rain started, and I would press my face to the window, "
    "coins sweating in my fist, praying he wouldn't turn the corner "
    "before I got my shoes on."
)

LIMIT = 280


def _check_sentence(text):
    """Check the memory against every rule of the bounty gate."""
    problems = []
    stripped = text.strip()
    if not stripped:
        problems.append("entry must not be blank")
    if text != stripped:
        problems.append("entry must not start or end with whitespace")
    if len(text) > LIMIT:
        problems.append(f"entry is {len(text)} characters, over the {LIMIT} limit")
    if "\n" in text or "\r" in text:
        problems.append("entry must be exactly one sentence on one line")
    if text.count(".") != 1 or not text.endswith("."):
        problems.append("entry must be exactly one sentence ending in a full stop")
    if not text.isprintable():
        problems.append("entry must contain only printable characters")
    return problems


def main(argv):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (argv[1] if len(argv) > 1 else ".")
    problems = _check_sentence(MEMORY)
    if problems:
        for problem in problems:
            print(f"entry rejected: {problem}", file=sys.stderr)
        return 1
    target = Path(out_dir) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(MEMORY + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(MEMORY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
