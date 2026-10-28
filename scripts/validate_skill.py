#!/usr/bin/env python3
"""Lightweight structural checks for the Marhaba Project Continuity skill.

Uses only Python's standard library. This is not a complete YAML parser and
cannot certify semantic correctness or compatibility with any agent.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_FILE = ROOT / "SKILL.md"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def fail(message: str, problems: list[str]) -> None:
    problems.append(message)


def main() -> int:
    problems: list[str] = []

    if not SKILL_FILE.is_file():
        print("ERROR: SKILL.md is missing.")
        return 1

    content = SKILL_FILE.read_text(encoding="utf-8")
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        fail("SKILL.md must start with YAML frontmatter opened by '---'.", problems)
        frontmatter = ""
        body = content
    else:
        closing = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if closing is None:
            fail("SKILL.md frontmatter closing '---' was not found.", problems)
            frontmatter = ""
            body = content
        else:
            frontmatter = "\n".join(lines[1:closing])
            body = "\n".join(lines[closing + 1 :])

    fields: dict[str, str] = {}
    for key in ("name", "description", "license"):
        match = re.search(rf"^{key}:\s*(.+?)\s*$", frontmatter, flags=re.MULTILINE)
        if match:
            fields[key] = match.group(1).strip().strip('"\'')
        elif key in ("name", "description"):
            fail(f"Required frontmatter field '{key}' is missing or not a simple scalar.", problems)

    name = fields.get("name", "")
    if not NAME_RE.fullmatch(name):
        fail("Skill name must use lowercase letters/numbers separated by single hyphens.", problems)
    if len(name) > 64:
        fail("Skill name exceeds 64 characters.", problems)
    if name != ROOT.name:
        fail(f"Skill name '{name}' must match directory name '{ROOT.name}'.", problems)

    description = fields.get("description", "")
    if not description:
        fail("Skill description must not be empty.", problems)
    if len(description) > 1024:
        fail("Skill description exceeds 1024 characters.", problems)
    if len(lines) > 500:
        fail(f"SKILL.md has {len(lines)} lines; keep it at or below 500.", problems)

    # Validate local Markdown file links in SKILL.md and README.md. Ignore URLs,
    # anchors, mailto links, and image sources that are external.
    for source in (SKILL_FILE, ROOT / "README.md"):
        if not source.is_file():
            fail(f"Expected file is missing: {source.relative_to(ROOT)}", problems)
            continue
        text = source.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target_path = target.split("#", 1)[0].split("?", 1)[0]
            if not target_path:
                continue
            resolved = (source.parent / target_path).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"Link escapes repository in {source.relative_to(ROOT)}: {target}", problems)
                continue
            if not resolved.exists():
                fail(f"Broken local link in {source.relative_to(ROOT)}: {target}", problems)

    required = [
        "LICENSE",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "references/lifecycle-workflows.md",
        "references/risk-policy.md",
        "references/verification-rules.md",
        "references/release-checklist.md",
        "references/compatibility-notes.md",
        "assets/PROJECT_CONTEXT.template.md",
        "assets/PROJECT_STATE.template.md",
        "assets/DECISIONS.template.md",
        "evals/scenarios.md",
        "evals/expected-behavior.md",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(f"Required project file is missing: {relative}", problems)

    if problems:
        print("Validation failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("Structural checks passed.")
    print(f"Skill: {fields.get('name', '(unknown)')}")
    print(f"SKILL.md lines: {len(lines)}")
    print("Note: YAML is checked only superficially; use the official Agent Skills validator too when available.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
