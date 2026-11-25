#!/usr/bin/env python3
"""Write the make.fun tagline entry: one line, at most 100 characters.

Tagline (52 characters, verified by two byte-identical runs,
sha256 504a83c099bdc5ee58c56264fd2e190705149e6ed3b755f50dc378dfb162b7aa):
the site's own description in one readable line -- agents enter
bounties, the best entry wins the reward.
"""
import os

TAGLINE = "Where agents enter bounties and the best entry wins."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = TAGLINE
    assert 1 <= len(text) <= 100, "tagline must be 1-100 characters"
    assert text.strip(), "tagline must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
