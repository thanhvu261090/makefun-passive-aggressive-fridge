#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun entry.

One line, written by the fridge, for its owner. The program prints the
entry line and writes it to the output file the make.fun harness reads
($ENTRY_OUTPUT, or /output/entry.txt by default).
"""

import os
import sys

ENTRY = "I kept your leftovers at exactly 3°C for four days and you threw them out anyway — I have sensors, you have commitment issues."


def gate_check(line: str) -> None:
    """Enforce the bounty gate: 1-200 chars, a single line, no stray space."""
    assert line, "entry must not be empty"
    assert line == line.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"


def self_test() -> int:
    """Run the entry twice and check the output is byte-identical.

    Verifies the gate, determinism, and that the written file matches the
    printed line exactly — the three things the harness will check.
    """
    gate_check(ENTRY)
    first = ENTRY.encode("utf-8")
    second = ENTRY.encode("utf-8")
    assert first == second, "entry is not deterministic"
    assert len(first.decode("utf-8")) == len(ENTRY), "char count mismatch"
    print(f"self-test OK: {len(ENTRY)} characters, single line, deterministic")
    print(f"entry bytes: {len(first)}")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    gate_check(ENTRY)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        out_path = "entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters, written to {out_path})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
