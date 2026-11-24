"""One word for my Wi-Fi: Drunk.

Writes the word to /output/entry.txt: 1-20 UTF-8 characters, one line,
no trailing newline. Deterministic: same bytes on every run.
Gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 20 characters,
not only white space; "Drunk" is 5 characters.
"""

import os

os.umask(0o022)

WORD = "Drunk"

assert isinstance(WORD, str)
assert 1 <= len(WORD.encode("utf-8")) <= 20
assert WORD.strip() == WORD and "\n" not in WORD and " " not in WORD

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(WORD)
os.chmod("/output/entry.txt", 0o644)
