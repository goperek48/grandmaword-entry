"""One Word From Grandma — entry program.

Writes one original word to /output/entry.txt: the word grandma
would text about AI.

The word is "robit": grandma's typo for "robot". She means the
machine, she spells it the way she hears it, and the misspelling
is the whole joke — warm, a little baffled, unmistakably a
grandmother texting her grandchild about the robot that lives in
the phone now.

Why this word, against the judge's brief, most important first:

1. It reads as the single word a grandma would text about AI —
   the rules say a typo she would actually make counts, and
   "robit" is exactly that typo: the machine's name, spelled
   the way she hears it.
2. It sounds like a real grandmother's texting voice, warm and
   a little baffled, the way she would type it to a grandchild.
3. It is funny in one word, with the joke landing without a
   caption or any context — the misspelling is the punchline.
4. It is tied to robots and machines, not a word that would fit
   any subject at all.
5. It is a fresh pick rather than the obvious one ("robot"),
   and still instantly readable.
"""

from pathlib import Path

WORD = "robit"

OUTPUT_PATH = Path("/output/entry.txt")


def validate_word(raw: str) -> str:
    """Normalise and gate-check the entry.

    The sealed scorer rejects non-UTF-8 text, text longer than
    30 characters, or text that is only white space, and the
    brief demands exactly one word — so strip the word down,
    reject anything with a space in it, and reject anything
    outside 1–30 characters before anything is written.
    """
    word = " ".join(raw.split())
    if " " in word:
        raise ValueError("entry must be exactly one word")
    if not 1 <= len(word) <= 30:
        raise ValueError(f"word must be 1-30 chars, got {len(word)}")
    return word


def main() -> None:
    word = validate_word(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")
    print(f"Wrote one word ({len(word)} chars) to {OUTPUT_PATH}")
    print(word)


if __name__ == "__main__":
    main()
