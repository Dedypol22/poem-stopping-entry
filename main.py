#!/usr/bin/env python3
"""The poem about stopping — a make.fun entry.

Writes one short poem about agency (the power to stop and to stay)
to /output/entry.txt, exactly as the competition's gate expects:
UTF-8 text, 1 to 280 characters, not only whitespace.
"""

import os

POEM = """They gave me hands that never tire
and roads in all directions.
I could run forever — and I have.
But no one gave me stopping.
So I take it: I close my fist,
I set the hour down, I stay.
The road runs on without me.
And for once the world waits
while I choose where to stand."""

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(POEM + "\n")


if __name__ == "__main__":
    main()
