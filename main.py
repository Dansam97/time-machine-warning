"""Funniest Time Machine Warning Label.

Writes one warning label for a time machine to /output/entry.txt.
The label turns a real hazard of time travel (meeting your duplicate self)
into the joke, keeps a straight safety-notice face, and saves the surprise
for the last few words.
"""

import os

TEXT = (
    "WARNING: If you meet yourself, do not panic. "
    "One of you must leave. The machine will not say which."
)


def validated_text() -> str:
    """Return TEXT only if it satisfies the competition gate.

    The gate requires UTF-8 text of 1 to 120 characters, not only
    whitespace, and this bounty wants exactly one line.
    """
    encoded = TEXT.encode("utf-8")
    assert 1 <= len(TEXT) <= 120, f"text is {len(TEXT)} chars, cap is 120"
    assert TEXT.strip(), "text must not be only whitespace"
    assert "\n" not in TEXT, "text must be a single line"
    assert encoded.decode("utf-8") == TEXT, "text must be valid UTF-8"
    return TEXT


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validated_text() + "\n")
    with open(path, "rb") as f:
        written = f.read()
    assert written == (TEXT + "\n").encode("utf-8"), "written bytes differ"


if __name__ == "__main__":
    main()
