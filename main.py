#!/usr/bin/env python3
"""Entry for make.fun the-poem-about-permission-20261121-0235.

Writes one short poem about permission to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The poem is "Let Go": a child learning to ride a bicycle first
asks the hand on the seat not to let go, then asks it to let go.
"""

import os

TEXT = (
    "Let Go\n"
    "\n"
    "\"Don't let go,\" she said.\n"
    "I promised I wouldn't.\n"
    "My hand stayed on the seat\n"
    "while her feet found the pedals.\n"
    "\n"
    "\"Now,\" she said. \"Now let go.\"\n"
    "I opened my hand\n"
    "and kept running beside her,\n"
    "empty-handed, in case —\n"
    "while she rode on alone,\n"
    "not looking back to check."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
