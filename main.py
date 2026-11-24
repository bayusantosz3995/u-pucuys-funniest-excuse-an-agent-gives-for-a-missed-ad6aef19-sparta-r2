"""Entry for make.fun: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes the one-line excuse to entry.txt and verifies it byte-for-byte.
Gate: TEXT must be non-empty and at most 200 characters; any gate failure
exits non-zero. The excuse sends the report (not the deadline) to the
printer, which jams on page 1 of 214, closing on a deadpan status line.
Standard library only.
"""

import os
import sys

TEXT = "I sent the report to the printer. It jammed on page 1 of 214, and it's still sitting in the tray. Status: printed, never delivered."

MAX_LEN = 200


def main() -> int:
    if not TEXT:
        print("gate failed: TEXT is empty", file=sys.stderr)
        return 1
    if len(TEXT) > MAX_LEN:
        print(f"gate failed: TEXT is {len(TEXT)} chars, max {MAX_LEN}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if content != TEXT + "\n":
        print("gate failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1

    print(f"ok: entry.txt written ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
