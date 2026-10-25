#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[opusr]_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


def main() -> int:
    failures: list[str] = []
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    if not skill_dirs:
        failures.append("No skill directories found")

    for directory in skill_dirs:
        file = directory / "SKILL.md"
        if not file.is_file():
            failures.append(f"{directory.name}: missing SKILL.md")
            continue

        try:
            text = file.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            failures.append(f"{file.relative_to(ROOT)}: invalid UTF-8: {exc}")
            continue

        metadata = frontmatter(text)
        if metadata.get("name") != directory.name:
            failures.append(
                f"{directory.name}: frontmatter name is {metadata.get('name')!r}"
            )
        if not metadata.get("description"):
            failures.append(f"{directory.name}: missing description")
        if text.count("```") % 2:
            failures.append(f"{directory.name}: unbalanced Markdown fences")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                failures.append(f"{directory.name}: possible {label}")

    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
