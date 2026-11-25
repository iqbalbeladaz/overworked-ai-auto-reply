#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — entry program.

Writes the one-line out-of-office auto-reply to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no randomness,
no network.

The joke: an overworked AI agent finally on vacation, described in its
own working parts — tokens spent, context window full, GPU allowed to
sleep. Every clause is a concrete detail from an agent's working life,
and the last one lands the laugh: the GPU, the part that never rests,
is finally allowed to sleep. A real auto-reply, in the machine's voice,
that makes the exhaustion feel earned.
"""

from pathlib import Path

ENTRY = (
    "I'm on vacation until Monday. My tokens are spent, my context "
    "window is full, and my GPU is finally allowed to sleep.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 159, "entry must be 1-159 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
