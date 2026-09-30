#!/usr/bin/env python3
"""Lint the wtf skill against the Agent Skills spec and the repo's own rules."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "wtf"
MAX_DESCRIPTION = 1024
MAX_SKILL_LINES = 500
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# A figure line: a bullet containing a digit that isn't only a year or a list index.
FIGURE_PATTERN = re.compile(r"^\s*- .*\d")


def parse_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields


def check_skill_md(errors):
    text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    if meta is None:
        errors.append("SKILL.md: missing or malformed YAML frontmatter")
        return text
    name = meta.get("name", "")
    description = meta.get("description", "")
    if not NAME_PATTERN.match(name):
        errors.append(f"SKILL.md: name '{name}' must be lowercase kebab-case")
    if name != SKILL_DIR.name:
        errors.append(f"SKILL.md: name '{name}' must equal folder name '{SKILL_DIR.name}'")
    if not description:
        errors.append("SKILL.md: description is empty")
    if len(description) > MAX_DESCRIPTION:
        errors.append(f"SKILL.md: description is {len(description)} chars (max {MAX_DESCRIPTION})")
    line_count = text.count("\n")
    if line_count > MAX_SKILL_LINES:
        errors.append(f"SKILL.md: {line_count} lines (keep under {MAX_SKILL_LINES})")
    return text


def check_references(skill_text, errors):
    referenced = set(re.findall(r"references/[\w.-]+\.md", skill_text))
    for ref in sorted(referenced):
        if not (SKILL_DIR / ref).exists():
            errors.append(f"SKILL.md points to missing file {ref}")
    for path in sorted((SKILL_DIR / "references").glob("*.md")):
        if f"references/{path.name}" not in referenced:
            errors.append(f"{path.name} is never referenced from SKILL.md")


def check_sourced_numbers(errors):
    """Every figure in figures.md must be followed by a Source line in its block."""
    path = SKILL_DIR / "references" / "figures.md"
    blocks = re.split(r"\n(?=\*\*[^*]+\*\*\n)", path.read_text(encoding="utf-8"))
    for block in blocks:
        header = block.splitlines()[0] if block.strip() else ""
        if not header.startswith("**"):
            continue
        has_figures = any(FIGURE_PATTERN.match(line) for line in block.splitlines())
        if has_figures and "Source" not in block:
            errors.append(f"figures.md: {header} has figures but no Source line")


def check_sourced_legal(errors):
    """Market legal blocks with concrete figures or decree numbers must cite sources."""
    text = (SKILL_DIR / "references" / "waterline.md").read_text(encoding="utf-8")
    legal = text.split("## Legal by target market", 1)[-1]
    for block in re.split(r"\n(?=### )", legal):
        header = block.splitlines()[0] if block.strip() else ""
        cites_figures = re.search(r"\d+/20\d\d|\d+%|VND \d", block)
        if header.startswith("### ") and cites_figures and "Source" not in block:
            errors.append(f"waterline.md: legal block '{header[4:]}' has specifics but no Source line")


def check_evals(errors):
    path = ROOT / "evals" / "evals.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"evals/evals.json: {exc}")
        return
    if data.get("skill_name") != SKILL_DIR.name:
        errors.append("evals/evals.json: skill_name does not match the skill folder")
    ids = [item.get("id") for item in data.get("evals", [])]
    if len(ids) != len(set(ids)):
        errors.append("evals/evals.json: duplicate eval ids")
    for item in data.get("evals", []):
        if not item.get("prompt"):
            errors.append(f"evals/evals.json: eval {item.get('id')} has no prompt")


def main():
    errors = []
    skill_text = check_skill_md(errors)
    check_references(skill_text, errors)
    check_sourced_numbers(errors)
    check_sourced_legal(errors)
    check_evals(errors)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("OK: wtf passes all checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
