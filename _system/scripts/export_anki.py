# ponytail: line-prefix frontmatter parse — upgrade to real YAML only if source: goes multiline

import re
from pathlib import Path


VAULT = Path(__file__).resolve().parents[2]
NOTES_DIR = VAULT / "notes" / "concepts"
EXPORT_DIR = VAULT / "_system" / "exports"
OUTPUT_FILE = EXPORT_DIR / "anki-cards.txt"


def extract_source_tag(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""

    for index in range(1, len(lines)):
        line = lines[index]
        if line.strip() == "---":
            break
        if line.startswith("source:"):
            value = line[len("source:") :].strip()
            return re.sub(r"\s+", "-", value)

    return ""


def extract_qa_pairs(text: str) -> list[tuple[str, str]]:
    section_match = re.search(r"(?m)^## Retrieval 題卡[ \t]*\r?\n", text)
    if not section_match:
        return []

    section_start = section_match.end()
    next_heading = re.search(r"(?m)^## ", text[section_start:])
    if next_heading:
        section = text[section_start : section_start + next_heading.start()]
    else:
        section = text[section_start:]

    pairs: list[tuple[str, str]] = []
    current_question: str | None = None

    for raw_line in section.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("Q: "):
            current_question = line[3:].strip()
            continue
        if line.startswith("A: ") and current_question is not None:
            pairs.append((current_question, line[3:].strip()))
            current_question = None
            continue
        current_question = None

    return pairs


def build_rows(note_path: Path) -> list[str]:
    text = note_path.read_text(encoding="utf-8")
    tag = extract_source_tag(text)
    pairs = extract_qa_pairs(text)
    return [f"{question}\t{answer}\t{tag}" for question, answer in pairs]


def check() -> None:
    sample = """---
source: Test Source
---
## Some section
content
## Retrieval 題卡
Q: What is X?
A: X is Y.

Q: What is Z?
A: Z is W.
## Next section
"""
    try:
        pairs = extract_qa_pairs(sample)
        assert len(pairs) == 2, f"Expected 2 pairs, got {len(pairs)}"
        assert pairs[0][0] == "What is X?", f"Q mismatch: {pairs[0][0]}"
        assert pairs[0][1] == "X is Y.", f"A mismatch: {pairs[0][1]}"
    except AssertionError as error:
        print(f"check() failed: {error}")
        raise SystemExit(1)

    print("check() passed")


def main() -> None:
    note_paths = sorted(NOTES_DIR.glob("*.md"))
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    output_lines = [
        "#separator:tab",
        "#html:false",
        "#tags column:3",
    ]
    counts: list[tuple[str, int]] = []
    total_cards = 0

    for note_path in note_paths:
        rows = build_rows(note_path)
        output_lines.extend(rows)
        counts.append((note_path.name, len(rows)))
        total_cards += len(rows)

    OUTPUT_FILE.write_text("\n".join(output_lines) + "\n", encoding="utf-8", newline="\n")

    print(f"Total cards: {total_cards}")
    for filename, count in counts:
        print(f"{filename}: {count}")


if __name__ == "__main__":
    check()
    main()
