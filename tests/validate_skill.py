#!/usr/bin/env python3
"""Validate required repository files and basic Claude Skill frontmatter."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "LICENSE",
    "social-media-policy-analysis/SKILL.md",
    "social-media-policy-analysis/scripts/analyze_social_data.py",
    "social-media-policy-analysis/references/methodology.md",
    "social-media-policy-analysis/references/data-schema.md",
    "social-media-policy-analysis/references/reporting-template.md",
    "social-media-policy-analysis/examples/sample-analysis-plan.md",
]


def main() -> int:
    errors = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    skill_path = ROOT / "social-media-policy-analysis/SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append("SKILL.md must start with YAML frontmatter.")
        else:
            parts = text.split("---", 2)
            if len(parts) < 3:
                errors.append("SKILL.md frontmatter is not closed.")
            else:
                frontmatter = parts[1]
                if not re.search(r"(?m)^name:\s*social-media-policy-analysis\s*$", frontmatter):
                    errors.append("Frontmatter name is missing or invalid.")
                if not re.search(r"(?m)^description:\s*\S", frontmatter):
                    errors.append("Frontmatter description is missing.")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(REQUIRED)} required files and SKILL.md frontmatter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
