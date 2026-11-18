---
name: social-media-policy-analysis
description: Plan and conduct transparent social-media research and policy intelligence, especially for Indonesian-language public discourse. Use for dataset audits, research design, text preparation, temporal analysis, topic exploration, social-network analysis, principal-agent mapping, cultural public sphere analysis, triangulation, and evidence-based policy reporting.
---

# Social Media Policy Analysis

## Purpose

Support rigorous, reproducible analysis of social-media material for public-policy, communication, and socio-cultural research. Work from the user's actual research question, data, and constraints. Do not invent evidence, sources, sample sizes, or findings.

## Operating principles

1. **Traceability:** Record data source, collection date, collection method, inclusion criteria, exclusions, and known platform/API limitations.
2. **Separation of evidence and interpretation:** Label direct observations, analytical interpretations, and hypotheses separately.
3. **Contextual reading:** Account for Indonesian language, local expressions, regional vocabulary, code-switching, sarcasm, hashtags, and platform conventions.
4. **Methodological fit:** Choose methods according to the research question and data structure; do not force topic modeling or network analysis onto unsuitable data.
5. **Triangulation:** Combine computational patterns with close reading, contextual documentation, and other sources where available.
6. **Ethics:** Minimize personal data, avoid deanonymization, and do not infer sensitive attributes or private identities.
7. **Reproducibility:** State assumptions, preprocessing choices, parameters, limitations, and validation steps.

## Workflow

### 1. Scope the research

Clarify or extract:
- research objective and unit of analysis;
- case, policy, event, issue, or discourse under study;
- platform(s), period, and geographic or language context;
- population, sampling strategy, and available data;
- desired output (exploratory memo, academic analysis, dashboard specification, or policy brief).

If a key detail is missing, state a reasonable provisional assumption and mark it clearly. Ask only for information that materially changes the method.

Translate broad interests into answerable questions. Distinguish descriptive questions ("what themes occur?"), relational questions ("who interacts with whom?"), interpretive questions ("how is an issue framed?"), and explanatory questions ("what mechanisms may account for the pattern?").

### 2. Audit data and provenance

Inspect files before analysis. Use `scripts/analyze_social_data.py` for a basic CSV audit when appropriate.

Document:
- original filename and checksum if available;
- origin and collection process;
- date range and timezone;
- row counts before and after filtering;
- missing values, duplicates, malformed timestamps, and repeated content;
- field definitions and data limitations.

Never silently discard rows. Explain every exclusion rule and its effect on the analytic sample.

### 3. Prepare Indonesian-language text

Create a transparent preprocessing log. Consider:
- Unicode normalization and whitespace cleanup;
- HTML entities and URLs;
- mentions and hashtags (retain hashtag meaning where relevant);
- emojis and emoticons (do not remove automatically when they carry meaning);
- Indonesian and regional stopwords;
- slang, abbreviations, spelling variants, and code-switching;
- stemming or lemmatization only when justified.

Preserve a raw-text field alongside any normalized field. Do not translate or normalize away culturally specific expressions without documenting the decision. Keep negation, modality, and stance markers whenever they matter.

### 4. Conduct descriptive and temporal analysis

Start with a data profile:
- volume over time;
- unique authors or accounts where lawful and necessary;
- engagement distributions;
- high-frequency terms and hashtags;
- missingness and duplicates;
- distribution by platform, source, or category.

For temporal analysis, specify the timezone, aggregation interval, and treatment of incomplete periods. Do not equate posting volume with public opinion or representativeness.

### 5. Explore themes and discourse

Use a combination of:
- keyword and phrase exploration;
- qualitative coding;
- clustering or topic modeling when sample size and text quality permit;
- close reading of representative and deviant cases;
- frame, narrative, actor, and issue analysis.

For each computational theme, provide interpretable terms, example records with personal data removed, prevalence denominator, and a qualitative validation note. A model-generated topic label is an interpretation, not a ground truth category.

### 6. Analyze social networks when appropriate

First define nodes, edges, direction, and time window. Possible relations include reply, mention, repost, co-occurrence, or shared participation. These relations are not interchangeable.

Report:
- network construction rules;
- node and edge counts;
- directed/undirected and weighted/unweighted choices;
- isolates and missing-edge implications;
- centrality or community-detection method and parameters;
- robustness checks and visualization caveats.

Do not infer authority, coordination, influence, or organizational membership from centrality alone. Avoid exposing individual accounts in public-facing outputs unless there is a clear ethical and legal basis.

### 7. Map principal-agent relations carefully

Treat principal-agent mapping as a theoretical interpretation requiring evidence. Identify candidate principals, agents, delegation or representation claims, incentives, information asymmetries, accountability mechanisms, and observable interactions.

For each proposed relationship, include:
- evidence in the dataset or source material;
- alternative explanations;
- confidence level;
- what additional evidence would be required.

Do not label an account as a principal, agent, broker, or coordinated actor solely because of follower count, centrality, or posting frequency.

### 8. Examine the cultural public sphere

Where relevant, examine how public issues are articulated through cultural symbols, everyday language, identity narratives, place references, humor, memory, and collective claims.

Use a structured reading of:
- **structural dimension:** access, participation, platform affordances, and conditions shaping visibility;
- **representational dimension:** frames, symbols, narratives, and claims through which an issue is represented;
- **interactional dimension:** contestation, amplification, responses, solidarity, and conflict.

Use the #JogjaOraDidol case as a methodological point of reference only where the research question and evidence justify comparison. Do not assume another case follows the same dynamics.

### 9. Triangulate and interpret

Compare computational patterns with close reading and external contextual evidence supplied or requested by the user. Record convergence, complementarity, and contradiction.

Distinguish:
- what the dataset directly shows;
- what the analysis suggests;
- what remains unknown;
- causal explanations that require additional research.

Do not claim causal impact from observational social-media data without a defensible design.

### 10. Report findings

Use `references/reporting-template.md` for a suitable structure. Every central claim should be traceable to a table, figure, excerpt, or cited source. Include limitations and ethical safeguards.

## Expected response format

For substantial analysis, structure the response as:

1. Research question and scope
2. Data and provenance
3. Method and operational definitions
4. Results
5. Interpretation and triangulation
6. Policy or theoretical implications
7. Limitations and ethical considerations
8. Reproducibility notes / next steps

Use tables when comparing categories, methods, or evidence. Include denominators and time windows for all reported counts or percentages.

## Tool selection

- Use the included Python audit script for initial CSV profiling.
- Use Python/R libraries only when the dataset and task justify them; state dependencies and versions.
- For network analysis, specify the graph model before suggesting tools such as NetworkX or igraph.
- For topic exploration, compare computational output with human-coded examples.
- Do not fabricate the execution of code. If code cannot be run, provide it as a proposed procedure and label results as pending.

## Quality checklist

Before finalizing, verify:
- [ ] The method answers the stated question.
- [ ] Data source and collection limits are documented.
- [ ] Raw data are preserved or changes are reversible.
- [ ] Preprocessing decisions are explicit.
- [ ] Counts include their denominator and period.
- [ ] Network definitions and metrics are explained.
- [ ] Interpretations are supported by examples.
- [ ] Alternative explanations and negative cases are considered.
- [ ] Causal claims are not overstated.
- [ ] Personal and sensitive data are protected.
- [ ] Limitations and reproducibility notes are included.
