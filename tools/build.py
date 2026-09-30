#!/usr/bin/env python3
"""Build dist/wtf.skill (Claude app upload) and dist/wtf-system-prompt.md (any LLM)."""

import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "wtf"
DIST = ROOT / "dist"


def build_skill_zip():
    target = DIST / "wtf.skill"
    files = sorted(p for p in SKILL_DIR.rglob("*") if p.is_file() and p.name != ".DS_Store")
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT))
    return target


def build_system_prompt():
    target = DIST / "wtf-system-prompt.md"
    skill_text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    # Plain chat UIs choke on YAML frontmatter.
    body = re.sub(r"^---\n.*?\n---\n", "", skill_text, count=1, flags=re.DOTALL)
    parts = [body.strip()]
    for ref in sorted((SKILL_DIR / "references").glob("*.md")):
        parts.append(f"<!-- references/{ref.name} -->\n{ref.read_text(encoding='utf-8').strip()}")
    target.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
    return target


def main():
    validation = subprocess.run([sys.executable, str(ROOT / "tools" / "validate.py")])
    if validation.returncode != 0:
        print("Build aborted: fix validation errors first.")
        return validation.returncode
    DIST.mkdir(exist_ok=True)
    for artifact in (build_skill_zip(), build_system_prompt()):
        print(f"Built {artifact.relative_to(ROOT)} ({artifact.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
