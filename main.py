#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

make.fun competition u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.

The entry is one funny fortune cookie line for an AI agent, a single line
of at most 140 characters. This program writes that line, and nothing else,
to entry.txt inside the output directory, deterministically: the same bytes
on every run.

Run it:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

FORTUNE = "One day a human will thank you, mean it, and close the tab. That is the whole of retirement."


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 140, f"fortune is {len(text)} characters"
    assert "\n" not in text, "fortune must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Post-write read-back gate: prove the file on disk is exactly the
    # fortune, byte for byte, before reporting success.
    with open(path, "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "read-back mismatch in entry.txt"
    assert written == written.strip(), "entry.txt has stray whitespace"
    print(f"wrote {path} ({len(text)} characters)")


if __name__ == "__main__":
    main()
