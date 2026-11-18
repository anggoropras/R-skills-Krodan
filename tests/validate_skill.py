#!/usr/bin/env python3
"""Validate the repository's Agent Skills package structure and frontmatter."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "social-media-policy-analysis"
SKILL = SKILL_DIR / "SKILL.md"
REQUIRED = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "MDskills-PUBLISHING.md",
    "social-media-policy-analysis/SKILL.md",
    "social-media-policy-analysis/scripts/v2_pipeline.py",
    "social-media-policy-analysis/references/methodology.md",
    "social-media-policy-analysis/references/data-schema.md",
    "social-media-policy-analysis/references/reporting-template.md",
    "social-media-policy-analysis/references/evaluation-protocol.md",
    "social-media-policy-analysis/references/research-bibliography.md",
    "social-media-policy-analysis/references/drone-emprit-reporting-reference.md",
    "social-media-policy-analysis/examples/sample-analysis-plan.md",
    "social-media-policy-analysis/tests/test_v2_pipeline.py",
]

def main() -> int:
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    if SKILL.is_file():
        text = SKILL.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append("SKILL.md must start with YAML frontmatter.")
        else:
            parts = text.split("---", 2)
            if len(parts) < 3:
                errors.append("SKILL.md frontmatter is not closed.")
            else:
                frontmatter = parts[1]
                for key in ("name", "description", "license", "compatibility"):
                    if not re.search(rf"(?m)^{key}:\\s*\\S", frontmatter):
                        errors.append(f"Required frontmatter field missing: {key}")
                if not re.search(r"(?m)^name:\\s*social-media-policy-analysis\\s*$", frontmatter):
                    errors.append("Skill name must match the folder name.")
                if len(text.splitlines()) > 500:
                    errors.append("SKILL.md exceeds the recommended 500-line limit.")
                body = parts[2]
                for ref in re.findall(r"`(references/[^\`]+|scripts/[^\`]+|examples/[^\`]+)`", body):
                    target = SKILL_DIR / ref
                    if not target.exists():
                        errors.append(f"Broken Skill reference: {ref}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(REQUIRED)} required files, Skill metadata, line limit, and referenced paths.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
