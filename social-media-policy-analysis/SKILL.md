---
name: social-media-policy-analysis
description: Conduct transparent social-media research and policy intelligence for Indonesian and multilingual public discourse. Use for research scoping, dataset audit, preprocessing, quantitative descriptive analysis, sentiment evaluation, themes, narratives, actors, networks, policy interpretation, and evidence-based insight reports.
license: MIT
compatibility: Compatible with Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, and other Agent Skills-compatible agents. Requires Python 3.10+ for bundled scripts; core pipeline uses the standard library.
metadata:
  author: anggoropras
  version: "2.1.1"
  repository: https://github.com/anggoropras/R-skills-Krodan
  category: research-and-policy-intelligence
---

# Social Media Research & Policy Intelligence

## Purpose
Support rigorous, transparent, reproducible analysis of social-media discourse. Never invent evidence, sources, samples, metrics, findings, citations, test results, or causal claims. Separate observed results, interpretation, hypotheses, and recommendations. Protect privacy and document provenance, sampling, query, filters, timezone, assumptions, versions, and limitations.

## When to use
- Research design and social-media monitoring.
- Dataset audits and Indonesian-language text preparation.
- Quantitative descriptive analysis, temporal patterns, engagement and platform comparisons.
- Sentiment/emotion classification and evaluation.
- Theme/topic exploration, discourse/narrative analysis, keyword and hashtag analysis.
- Reply/mention/repost networks and actor mapping.
- Principal-agent analysis, cultural public sphere, triangulation, policy insight reporting.

## When not to use
- To claim population-level public opinion from social-media data without an appropriate sampling design.
- To infer causality from descriptive trends or temporal coincidence.
- To identify private individuals, infer sensitive attributes, or expose unnecessary personal information.
- To claim statistical topic modeling, community detection, validated sentiment, influence, coordination, or cross-platform diffusion when those methods or evidence are absent.

## Required workflow

1. **Scope:** define question, case, unit, platform, period, population/sample, query/sampling frame, inclusion/exclusion, and intended output.
2. **Provenance and audit:** record source, collection method/date, schema, missingness, duplicates, timestamp parsing/timezone, filters, coverage, and exclusions. Never silently remove records.
3. **Preprocess transparently:** preserve raw text; create separate normalized fields; document transformations; preserve negation and meaningful local terms; account for Indonesian slang, regional expressions, code-switching, sarcasm, and hashtags.
4. **Quantitative description:** calculate counts, shares, denominators, daily/weekly volume, unique authors/content, engagement distribution, and actor/platform composition. Volume and engagement do not represent public opinion or engagement rate without proper denominators.
5. **Sentiment:** disclose model or lexicon, label definitions, and uncertainty. For research claims, validate against human labels; report sample, annotation protocol, accuracy, per-class precision/recall/F1, macro-F1, and confusion matrix where possible. Lexicon output is baseline only.
6. **Emotion:** keep emotion separate from sentiment. Use a disclosed taxonomy and validated or documented annotation method. Do not generate emotion results if the method is unsupported.
7. **Themes/topics:** distinguish keyword-dictionary exploration, human coding, clustering, and statistical topic modeling. Explain multi-label assignment and denominators; validate topic labels by close reading and evidence excerpts.
8. **Narrative/discourse:** identify claims, frames, actors, keywords, counter-narratives, negative cases, and representative evidence. Keep interpretation traceable to post IDs or links.
9. **Network:** define nodes, edges, direction, weights, and time window. Report missing relations and isolates. Degree or centrality does not prove influence, authority, coordination, or representativeness. Only report community detection or advanced metrics if implemented.
10. **Principal-agent:** require evidence of delegation/representation, incentives, asymmetry, and accountability; consider alternative explanations. A mention, reply, repost, or high engagement is not sufficient evidence.
11. **Cultural public sphere:** where relevant, analyze structural, representational, and interactional dimensions. Comparisons require contextual justification.
12. **Platform and diffusion:** compare content, actors, themes, sentiment (if validated), and engagement by platform. Do not claim cross-platform migration without linked content, URLs, timestamps, hashtags, or other supporting evidence.
13. **Triangulate:** compare computational patterns, close reading, and contextual sources. Document agreement, disagreement, alternative explanations, and unknowns.
14. **Report:** use the expanded insight-report template and only include sections supported by data. Show denominators, time windows, evidence, confidence, limitations, ethics, and reproducibility.

## Insight report structure
Use the full template in `references/reporting-template.md` for substantial reports. Core sections:
1. Executive summary
2. Scope, questions, and data provenance
3. Conversation overview
4. Temporal dynamics and event context
5. Sentiment overview (only when supported/validated)
6. Sentiment dynamics
7. Emotion analysis (only when supported)
8. Issue/topic distribution
9. Narrative and discourse analysis
10. Actor composition and network mapping
11. Platform comparison
12. Engagement and content performance
13. Cross-platform diffusion (requires evidence)
14. Keywords, hashtags, and framing
15. Top content and evidence
16. Integrated insights and policy implications
17. Limitations, ethics, and confidence
18. Reproducibility appendix

Use insight format: **quantitative evidence (with denominator and time window) → observed pattern → interpretation/narrative → actors/platform → implication → confidence/limitations**.

## Bundled prototype
The dependency-free Python prototype is in `scripts/v2_pipeline.py`. It supports synthetic data generation, audit, reversible preprocessing, dictionary themes, lexicon sentiment baseline, human-label evaluation, reply-network summary, and Markdown report generation. Read `references/evaluation-protocol.md` before interpreting sentiment.

Limitations: it does not implement statistical topic models (LDA/BERTopic), transformer sentiment, stemming, community detection, causal inference, or validated emotion analysis.

## Reference routing
- Methodology: `references/methodology.md`
- Data fields: `references/data-schema.md`
- Report template: `references/reporting-template.md`
- Sentiment evaluation: `references/evaluation-protocol.md`
- Research bibliography and verification notes: `references/research-bibliography.md`
- Drone Emprit report-systematics reference: `references/drone-emprit-reporting-reference.md`
- Example analysis plan: `examples/sample-analysis-plan.md`

## Commands
See repository README for commands. Run scripts from repository root. Do not claim a command/test was executed unless you actually ran it and observed its result.

## Quality checklist
- Research question and method fit.
- Provenance, query, sample, timezone, filters, and denominator documented.
- Raw data preserved; preprocessing transparent and reproducible.
- Classification validation and uncertainty reported where relevant.
- Themes, narratives, network claims, and recommendations traceable to evidence.
- Alternatives, negative cases, privacy, ethics, and limitations considered.
- Findings, interpretation, hypotheses, and recommendations clearly separated.
