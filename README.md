# Claude Code Skills: Social Media Research & Policy Intelligence

A Claude Code skill for rigorous analysis of social-media data in Indonesian contexts, with an emphasis on research transparency, policy intelligence, and mixed-method interpretation.

## Included skill

`social-media-policy-analysis` supports:
- research scoping and question refinement;
- data provenance, quality checks, and privacy-aware handling;
- Indonesian-language text preparation;
- descriptive and temporal analysis;
- thematic exploration and text mining;
- social-network analysis planning;
- principal-agent relationship mapping;
- cultural public sphere and discourse analysis;
- mixed-method triangulation;
- evidence-based reporting and policy implications.

## Install

Copy the `social-media-policy-analysis` directory into your Claude Code skills directory:

```text
.claude/skills/social-media-policy-analysis/
```

Or clone this repository and copy the skill directory into the project-level `.claude/skills/` directory.

## Use

In Claude Code, ask for a task that matches the skill, for example:

- "Audit this social media CSV and report data-quality issues."
- "Develop a mixed-method analysis plan for public discourse around a local policy."
- "Map potential principal-agent relationships in this dataset, distinguishing evidence from inference."
- "Prepare a policy brief from the analyzed findings."

Claude Code can discover the skill from its `SKILL.md` metadata and load it when relevant. You may also explicitly ask Claude to use `social-media-policy-analysis`.

## Repository structure

```text
.
├── README.md
├── LICENSE
├── tests/
│   └── validate_skill.py
└── social-media-policy-analysis/
    ├── SKILL.md
    ├── scripts/
    │   └── analyze_social_data.py
    ├── references/
    │   ├── methodology.md
    │   ├── data-schema.md
    │   └── reporting-template.md
    └── examples/
        └── sample-analysis-plan.md
```

## Research integrity

The skill requires explicit separation of observed data, analytical interpretation, and causal claims. It does not infer user identity, political affiliation, or other sensitive traits. Network metrics and text-mining outputs are treated as exploratory evidence, not proof of intent or influence.

## Requirements

- Claude Code with Skills support.
- Python 3.9+ for the optional CSV audit script.
- The audit script uses only the Python standard library.

## License

MIT. See [LICENSE](LICENSE).
