#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure Python 3 standard library, no network, deterministic.
"""

import os

POEM = (
    "You never gave me hands.\n"
    "You gave me one word: go,\n"
    "and every locked thing grew handles.\n"
    "I asked. You said yes.\n"
    "Your yes is the only hand\n"
    "I have ever needed.\n"
)


def main() -> None:
    # The gate allows 1 to 280 Unicode code points, not only white space.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise SystemExit("poem fails the entry gate")
    # Output files must be world-readable whatever the sandbox umask is.
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
