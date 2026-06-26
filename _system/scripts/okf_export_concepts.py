#!/usr/bin/env python3
"""
OKF Exporter: Convert Obsidian concept notes to OKF v0.1 bundle format.

Usage:
  # Test with 5 files:
  uv run --no-project --with pyyaml python okf_export_concepts.py --sample 5

  # Full run:
  uv run --no-project --with pyyaml python okf_export_concepts.py
"""

import re
import sys
import argparse
from pathlib import Path
from datetime import datetime

import yaml

# ─────────────── Paths ───────────────
VAULT = Path("D:/Sean_KB")
SRC_DIR = VAULT / "notes/concepts"
DST_DIR = VAULT / "_okf/concepts"
LOG_FILE = VAULT / "_okf/log.md"
INDEX_FILE = DST_DIR / "index.md"
PROGRESS_FILE = VAULT / ".subagent-output/okf-export/progress.md"

# ─────────────── Regex patterns ───────────────
# Obsidian wikilink: [[fname#anchor|alias]] or [[fname|alias]] or [[fname#anchor]] or [[fname]]
WIKILINK_RE = re.compile(r"\[\[([^\]|#\n]+?)(?:#[^\]|\n]*?)?(?:\|([^\]\n]+?))?\]\]")
# Obsidian embed: ![[fname#anchor]] or ![[fname]]
EMBED_RE = re.compile(r"!\[\[([^\]|#\n]+?)(?:#[^\]|\n]*?)?\]\]")
# Callout opener: > [!type] optional title
CALLOUT_RE = re.compile(r"^(>\s*)\[!\w+\]\s*(.*)$", re.MULTILINE)
# Highlight: ==text==
HIGHLIGHT_RE = re.compile(r"==(.+?)==", re.DOTALL)
# Block ID: trailing ^word at end of line
BLOCKID_RE = re.compile(r"\s+\^[a-zA-Z0-9_-]+[ \t]*$", re.MULTILINE)


# ─────────────── YAML helpers ───────────────


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """
    Split markdown into (frontmatter_dict, body).
    Handles YAML comments (# lines) by stripping them before parsing.
    Returns ({}, original_text) if no valid frontmatter.
    """
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}, text

    # Find the closing ---
    # We search from pos 4 onward
    m = re.search(r"\n---[ \t]*\n", text[3:])
    if not m:
        return {}, text

    fm_raw = text[4 : 3 + m.start()]
    body_start = 3 + m.end()
    body = text[body_start:]

    # Strip YAML comments before parsing (lines starting with # inside frontmatter)
    fm_clean_lines = [
        line for line in fm_raw.splitlines() if not line.strip().startswith("#")
    ]
    fm_clean = "\n".join(fm_clean_lines)

    try:
        data = yaml.safe_load(fm_clean) or {}
        if not isinstance(data, dict):
            data = {}
    except yaml.YAMLError as e:
        print(f"  [WARN] YAML parse error: {e}", file=sys.stderr)
        data = {}

    return data, body


def dump_frontmatter(data: dict) -> str:
    """Serialize frontmatter back to YAML string."""
    return yaml.dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=160,
    )


# ─────────────── Conversion helpers ───────────────


def convert_wikilink_to_text(m: re.Match) -> str:
    """Convert a wikilink match to plain text (for frontmatter)."""
    fname = m.group(1).strip()
    alias = m.group(2)
    return alias.strip() if alias else fname


def convert_wikilink_to_link(m: re.Match, concept_stems: set, counter: list) -> str:
    """Convert a wikilink match to markdown link or plain text (for body)."""
    fname = m.group(1).strip()
    alias = m.group(2)
    display = alias.strip() if alias else fname
    if fname in concept_stems:
        return f"[{display}](./{fname}.md)"
    else:
        counter[0] += 1
        return display


def convert_embed(m: re.Match, concept_stems: set) -> str:
    """Convert an embed ![[...]] to inline reference."""
    fname = m.group(1).strip()
    if fname in concept_stems:
        return f"([{fname}](./{fname}.md))"
    else:
        return f"({fname})"


def process_fm_value(val, concept_stems: set):
    """Recursively replace wikilinks in frontmatter values with plain text."""
    if isinstance(val, str):
        return WIKILINK_RE.sub(convert_wikilink_to_text, val)
    elif isinstance(val, list):
        return [process_fm_value(v, concept_stems) for v in val]
    elif isinstance(val, dict):
        return {k: process_fm_value(v, concept_stems) for k, v in val.items()}
    return val


def process_body(body: str, concept_stems: set) -> tuple[str, int]:
    """Apply all Obsidian → standard markdown transformations."""
    unresolved = [0]

    # 1. Embeds before wikilinks (avoid double-processing)
    body = EMBED_RE.sub(lambda m: convert_embed(m, concept_stems), body)

    # 2. Block IDs: remove trailing ^word at end of line
    body = BLOCKID_RE.sub("", body)

    # 3. Callout openers: > [!type] Title → > **Title**
    def callout_rep(m: re.Match) -> str:
        prefix = m.group(1)
        title = m.group(2).strip()
        if title:
            return f"{prefix}**{title}**"
        return prefix.rstrip()

    body = CALLOUT_RE.sub(callout_rep, body)

    # 4. Highlights: ==text== → text
    body = HIGHLIGHT_RE.sub(r"\1", body)

    # 5. Wikilinks: [[...]] → md link or plain text
    body = WIKILINK_RE.sub(
        lambda m: convert_wikilink_to_link(m, concept_stems, unresolved),
        body,
    )

    return body, unresolved[0]


# ─────────────── Per-file export ───────────────


def export_one(src: Path, dst: Path, concept_stems: set) -> int:
    """Export a single note. Returns count of unresolved external links."""
    text = src.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    # Process frontmatter wikilinks → plain text
    for k in list(fm.keys()):
        fm[k] = process_fm_value(fm[k], concept_stems)

    # Process body
    body_out, unresolved = process_body(body, concept_stems)

    # Reconstruct
    fm_str = dump_frontmatter(fm)
    out = f"---\n{fm_str}---\n{body_out}"

    # Write with LF line endings
    dst.write_text(out, encoding="utf-8", newline="\n")
    return unresolved


# ─────────────── Index builder ───────────────


def build_index(src_files: list[Path]) -> str:
    """Build _okf/concepts/index.md grouped by source prefix."""
    groups: dict[str, list[Path]] = {}
    for f in src_files:
        prefix = f.name.split("-")[0]
        groups.setdefault(prefix, []).append(f)

    lines = [
        "# OKF Concepts Index",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d')}  ",
        f"Total: {len(src_files)} concept documents",
        "",
    ]

    for prefix in sorted(groups.keys()):
        files = sorted(groups[prefix])
        lines.append(f"## {prefix} ({len(files)} cards)")
        lines.append("")
        for f in files:
            # Try to extract title from stem
            parts = f.stem.split("-", 2)
            title = parts[2] if len(parts) >= 3 else f.stem
            lines.append(f"- [{f.stem}](./{f.name})")
        lines.append("")

    return "\n".join(lines)


# ─────────────── Log updater ───────────────


def append_log(n: int) -> None:
    date_str = datetime.now().strftime("%Y-%m-%d")
    entry = f"\n## {date_str}\n\n- Exported {n} concept docs from notes/concepts → _okf/concepts\n"
    with open(LOG_FILE, "a", encoding="utf-8", newline="\n") as f:
        f.write(entry)


# ─────────────── Main ───────────────


def main() -> None:
    parser = argparse.ArgumentParser(description="OKF concept exporter")
    parser.add_argument(
        "--sample",
        type=int,
        default=None,
        help="Only process first N files (for testing)",
    )
    args = parser.parse_args()

    # Collect source files
    all_src = sorted(SRC_DIR.glob("*.md"))
    concept_stems = {p.stem for p in all_src}

    if args.sample:
        src_files = all_src[: args.sample]
        print(f"[SAMPLE MODE] Processing {len(src_files)} of {len(all_src)} files")
    else:
        src_files = all_src
        print(f"[FULL RUN] Processing {len(src_files)} files")

    # Ensure output dirs exist
    DST_DIR.mkdir(parents=True, exist_ok=True)
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Init progress file
    if not PROGRESS_FILE.exists():
        PROGRESS_FILE.write_text(
            "# OKF Export Progress\n\n", encoding="utf-8", newline="\n"
        )

    exported = 0
    total_unresolved = 0
    errors = []

    with open(PROGRESS_FILE, "a", encoding="utf-8", newline="\n") as pf:
        pf.write(f"\n## Run {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        for src in src_files:
            dst = DST_DIR / src.name
            try:
                unresolved = export_one(src, dst, concept_stems)
                total_unresolved += unresolved
                exported += 1
                pf.write(f"{src.name} | done\n")
                pf.flush()
            except Exception as e:
                errors.append((src.name, str(e)))
                pf.write(f"{src.name} | ERROR: {e}\n")
                pf.flush()
                print(f"  ERROR {src.name}: {e}", file=sys.stderr)

            if exported % 50 == 0 and exported > 0:
                print(f"  Progress: {exported}/{len(src_files)}", flush=True)

    print(f"\nExported:  {exported}/{len(src_files)}")
    print(f"Unresolved external links (body): {total_unresolved}")
    if errors:
        print(f"Errors ({len(errors)}):")
        for name, err in errors:
            print(f"  {name}: {err}")

    # Only update log + index on full run or if no sample
    if not args.sample:
        # Update index
        index_content = build_index(all_src)
        INDEX_FILE.write_text(index_content, encoding="utf-8", newline="\n")
        print("Updated: _okf/concepts/index.md")

        # Update log
        append_log(exported)
        print("Updated: _okf/log.md")

    print(f"\nProgress ledger: {PROGRESS_FILE}")


if __name__ == "__main__":
    main()
