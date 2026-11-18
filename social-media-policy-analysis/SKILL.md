---
name: social-media-policy-analysis
description: Plan and conduct transparent social-media research and policy intelligence, especially for Indonesian-language public discourse. Use for dataset audits, research design, text preparation, temporal analysis, topic exploration, social-network analysis, principal-agent mapping, cultural public sphere analysis, triangulation, and evidence-based policy reporting.
---

# Social Media Policy Analysis

Support rigorous, reproducible research. Never invent evidence, sources, samples, findings or test results. Separate observed data, interpretation and hypotheses. Protect privacy; preserve raw text; document provenance, sampling, filters, timezone, assumptions, versions and limitations. Contextualize Indonesian slang, regional language, code-switching, sarcasm and hashtags.

## Workflow
1. Scope question, unit, case, platform, period, population/sample, data and output.
2. Audit provenance, schema, missingness, duplicates, timestamps, filters and platform limitations. Never silently remove rows.
3. Preprocess transparently and reversibly. Preserve raw text and separate processed fields. Keep negation and culturally meaningful terms unless justified.
4. Describe volume, dates, actors and engagement. Do not equate volume with public opinion or representativeness.
5. Explore themes with keyword/phrase analysis, qualitative coding, and statistical topic models only where data/sample justify them. Validate labels through close reading and evidence excerpts.
6. Network: define nodes, edges, direction, weights and period. Report isolates/missing-edge implications. Centrality is not proof of influence, authority or coordination.
7. Principal-agent analysis requires evidence of delegation/representation, incentives, asymmetry and accountability; consider alternative explanations.
8. Cultural public sphere: structural, representational and interactional dimensions; comparison needs contextual justification.
9. Triangulate computational patterns, close reading and contextual evidence. Separate findings, inference and unknowns.
10. Report method, denominators, evidence, limitations, ethics and reproducibility. For substantial reports, use the expanded reporting-template.md structure: conversation overview, temporal/event dynamics, sentiment and sentiment dynamics (only when validated), emotion (only when supported), topic/issue distribution, narrative/discourse evidence, actor/network, platform comparison, engagement, cross-platform diffusion (only with linked evidence), keywords/hashtags, top content, integrated implications, limitations/confidence and reproducibility.

## Prototype
Use scripts/v2_pipeline.py for synthetic generation, audit, preprocessing, keyword themes, lexicon sentiment baseline, reply network summary, and Markdown report. The prototype is standard-library-only. Themes are dictionary overlap, sentiment is not validated without human labels, and network metrics are descriptive. It does not implement statistical topic models, transformer sentiment, stemming, community detection or causal inference.

Commands: generate, run, evaluate (see repository README). Follow references/evaluation-protocol.md for annotation. Use references/reporting-template.md for substantial reports. The expanded structure is informed in part by Drone Emprit's public report “Sentimen Publik terhadap Salam Tiga Jari” (6 November 2026), used only as a reporting-systematics reference; do not claim access to or reproduce proprietary methods. Never claim execution unless actually run.

## Quality checklist
- Question-method fit and operational definitions.
- Provenance, sample, timezone, filters and denominator documented.
- Raw data preserved; preprocessing transparent.
- Human validation and metrics where applicable.
- Theme/network interpretations traceable and limited.
- Alternatives, negative cases, privacy and ethics considered.
- Evidence, interpretation, uncertainty and limitations separated.
