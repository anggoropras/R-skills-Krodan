# mdskills.ai Publication Preparation

## Package
Publishable skill folder:
`social-media-policy-analysis/`

It contains a required `SKILL.md` with:
- required `name` and `description`
- MIT license and compatibility metadata
- version and repository metadata
- instructions, workflow, safeguards and reference routing
- supporting scripts, references, examples and tests

## Marketplace description draft
**Social Media Research & Policy Intelligence** — A reproducible research workflow for Indonesian-language social-media discourse. Supports research scoping, data-quality audit, transparent preprocessing, quantitative descriptive and temporal analysis, sentiment evaluation, keyword themes, narrative/discourse analysis, actor/network mapping, triangulation, and evidence-based policy insight reporting. Includes a dependency-free Python prototype and synthetic-data tests.

Suggested tags: research, social-media-analysis, policy-intelligence, Indonesia, text-analysis, discourse-analysis, sentiment-analysis, social-network-analysis, quantitative-research, digital-methods.

## Checklist before submitting
- [x] Skill folder contains SKILL.md and support files.
- [x] Frontmatter includes required name and description.
- [x] Folder name matches Skill name.
- [x] License and compatibility metadata included.
- [x] Main instructions use progressive disclosure and remain under 500 lines.
- [x] README and installation/publishing documentation added.
- [x] Research bibliography added with original links and citation notes.
- [x] CI workflow updated to run package validation, compile, tests, and smoke pipeline.
- [ ] Confirm GitHub Actions validation run is green.
- [ ] Review the live mdskills.ai publication/submission UI and required metadata.
- [ ] Submit/publish and confirm a public listing.

## Install from GitHub
The mdskills.ai documentation describes installation from a GitHub owner/repository using:
```bash
npx mdskills install anggoropras/R-skills-Krodan
```
If the installer does not resolve the nested Skill automatically, install the Skill folder manually from `social-media-policy-analysis/` into the agent's documented Skill directory.

## Publish
The mdskills.ai creator guide documents a publishing workflow:
```bash
npx mdskills publish
```
This command is not executed in this session because it requires a local CLI/network/authenticated publishing environment. Run it from a local clone, review the package and marketplace metadata it requests, and only confirm submission after checking the destination.

## Cross-agent install locations
- Claude Code: `.claude/skills/social-media-policy-analysis/`
- Codex: `.agents/skills/social-media-policy-analysis/`
- Cursor: use its supported Skill location; `.agents/skills/` is a cross-agent option.
- GitHub Copilot, Gemini CLI, and other compatible tools: use their documented Skill discovery locations.

## Verification status
GitHub repository files have been updated and read back for content verification. Local CLI publication, marketplace submission, and public listing are not verified yet.
