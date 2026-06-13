#!/usr/bin/env python3
"""Convert Obsidian wiki-links to standard Markdown links for MkDocs."""

import re
import os
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent
DIST_DIR = VAULT_ROOT / "docs" / "content"

INCLUDE_DIRS = [
    "wiki", "辅导班题目", "练题班题库", "错题集",
    "时政", "陕西省", "考前必背-SVG", "raw", "政策解读",
]


def convert_wikilink(match: re.Match, current_file: Path) -> str:
    """Convert a single [[wikilink]] to standard [text](path) format."""
    inner = match.group(1)
    if "|" in inner:
        target, display = inner.split("|", 1)
    else:
        target = inner
        display = Path(target).stem

    if target.startswith("http"):
        return f"[{display}]({target})"

    if target.endswith(".md"):
        target = target[:-3]

    if "#" in target:
        target_path, anchor = target.rsplit("#", 1)
        if target_path.endswith(".md"):
            target_path = target_path[:-3]
        target = f"{target_path}#{anchor}"

    return f"[{display}]({target})"


def convert_file(src_path: Path, dist_path: Path) -> None:
    """Convert a single Markdown file."""
    content = src_path.read_text(encoding="utf-8")
    wikilink_pattern = re.compile(r"\[\[([^\]]+)\]\]")

    def replacer(match):
        return convert_wikilink(match, dist_path)

    converted = wikilink_pattern.sub(replacer, content)
    embed_pattern = re.compile(r"!\[\[([^\]]+)\]\]")
    converted = embed_pattern.sub(r"![\1](\1)", converted)

    dist_path.parent.mkdir(parents=True, exist_ok=True)
    dist_path.write_text(converted, encoding="utf-8")


def main():
    print("Converting wiki-links to standard Markdown links...")
    count = 0
    for dir_name in INCLUDE_DIRS:
        src_dir = VAULT_ROOT / dir_name
        if not src_dir.exists():
            continue
        for md_file in src_dir.rglob("*.md"):
            rel_path = md_file.relative_to(VAULT_ROOT)
            dist_path = DIST_DIR / rel_path
            convert_file(md_file, dist_path)
            count += 1
            print(f"  OK {rel_path}")

    for md_file in VAULT_ROOT.glob("*.md"):
        rel_path = md_file.relative_to(VAULT_ROOT)
        dist_path = DIST_DIR / rel_path
        convert_file(md_file, dist_path)
        count += 1
        print(f"  OK {rel_path}")

    print(f"Done! Converted {count} files.")


if __name__ == "__main__":
    main()
