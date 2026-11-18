# Social Media Research & Policy Intelligence Skill

**Agent Skills-compatible repository for Indonesian-language social-media research, quantitative analysis, discourse interpretation, and evidence-based policy insight reporting.**

- Skill package: `social-media-policy-analysis/`
- Skill version: `2.1.1`
- License: MIT
- Compatible with Agent Skills-compatible tools including Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, and others.

## What it does

This Skill helps agents carry out a documented workflow:
1. Research scoping and query/sampling design.
2. Provenance, data-quality audit, and dataset profiling.
3. Transparent Indonesian text normalization and preprocessing.
4. Quantitative descriptive and temporal analysis.
5. Sentiment baseline plus human-label evaluation protocol.
6. Keyword themes and evidence-linked exploration.
7. Actor and reply-network summaries.
8. Narrative/discourse analysis and triangulation.
9. Policy-oriented Insight Report with limitations and reproducibility.

## Install

### mdskills.ai / CLI workflow
Check the current mdskills.ai publishing and installation instructions. For the published Skill, use the package directory `social-media-policy-analysis/` which contains the required `SKILL.md` and its support folders.

### Claude Code
Copy the Skill directory into:
```
.claude/skills/social-media-policy-analysis/
```

### Codex
Copy into:
```
.agents/skills/social-media-policy-analysis/
```

### Cursor
Use a supported Skill folder location, such as:
```
.agents/skills/social-media-policy-analysis/
```

### Other Agent Skills-compatible agents
Follow the agent's documented Skill discovery directory. The Skill package is portable: it uses YAML frontmatter and Markdown instructions, with optional scripts and references.

## Quick start: synthetic demo

Python 3.10+ is recommended. The prototype uses only the Python standard library.

Generate deterministic dummy data:
```bash
python social-media-policy-analysis/scripts/v2_pipeline.py generate --rows 40 --seed 20261118 --output data/dummy.csv
``

Run the analysis pipeline:
```bash
python social-media-policy-analysis/scripts/v2_pipeline.py run data/dummy.csv --outdir outputs --source "synthetic data"
``

Evaluate predictions against human annotations:
```bash
python social-media-policy-analysis/scripts/v2_pipeline.py evaluate human_annotations.csv --output evaluation.json
``

Run tests and repository validation:
```bash
python -m unittest discover -s social-media-policy-analysis/tests -v
python tests/validate_skill.py
``

## Report systematics

The report template is designed for a comprehensive Digital Discourse Insight Report:
- Executive summary
- Research scope and data provenance
- Conversation overview
- Temporal dynamics and event context
- Sentiment and sentiment dynamics (only when method supports it)
- Emotion analysis (only when supported)
- Issue/topic distribution
- Narrative/discourse analysis
- Actor composition and network
- Platform comparison
- Engagement and content performance
- Cross-platform diffusion (evidence required)
- Keywords, hashtags, and framing
- Top content and evidence
- Integrated insight and policy implications
- Limitations, ethics, confidence, reproducibility

The report structure is informed by Drone Emprit's public report on “Sentimen Publik terhadap Salam Tiga Jari” as an additional organization reference. It does not claim to reproduce proprietary Drone Emprit methods.

## Research references

See:
- `social-media-policy-analysis/references/methodology.md`
- `social-media-policy-analysis/references/research-bibliography.md`
- `social-media-policy-analysis/references/drone-emprit-reporting-reference.md`

The bibliography records the research references supplied for this project and verification caveats. Confirm original title, authorship, venue, DOI/URL, and pages before academic citation.

## Limits

- Synthetic datasets are software demonstrations, not public-opinion evidence.
- Keyword theme assignment is not statistical topic modeling.
- Lexicon sentiment is a baseline and requires human validation.
- Engagement counts are not engagement rates without reach/impressions.
- Reply-network metrics are descriptive; they do not prove influence, coordination, or representation.
- Cross-platform diffusion and causal claims require additional evidence/design.

## Repository layout

```
R-skills-Krodan/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── IMPLEMENTATION_STATUS_V2.md
├── .github/workflows/
├── social-media-policy-analysis/
│   ├── SKILL.md
│   ├── scripts/
│   ├── references/
│   ├── examples/
│   └── tests/
└── tests/
    └── validate_skill.py
```

## Publication readiness

This repository contains an Agent Skills-compatible Skill folder. Marketplace publication is a separate action and should follow the current mdskills.ai submission/CLI workflow. Do not claim it is listed on mdskills.ai until a listing/submission is confirmed.
