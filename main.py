"""Have You Tried Turning It Off?

Writes the hopeless tech support agent's line to a desperate customer
to /output/entry.txt. Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

# Gate: /output/entry.txt must be 1 to 199 characters.
# This line is 115 characters: the classic fix, then the agent gives up on the customer.
# The punch is the confession at the end: the agent has run out of fixes and faith.
# It stays in the agent's voice the whole way: helpful script first, surrender second.
LINE = "Have you tried turning it off and on again? I ask because I have tried everything else, including believing in you."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
