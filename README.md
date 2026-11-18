# Social Media Research & Policy Intelligence — v2 prototype

Dependency-free Python prototype for Indonesian-language social-media research. Synthetic data are software tests only.

## Quick start

```bash
python social-media-policy-analysis/scripts/v2_pipeline.py generate --rows 40 --seed 20261118 --output data/dummy.csv
python social-media-policy-analysis/scripts/v2_pipeline.py run data/dummy.csv --outdir outputs --source "synthetic data"
python social-media-policy-analysis/scripts/v2_pipeline.py evaluate human_annotations.csv --output evaluation.json
python -m unittest discover -s social-media-policy-analysis/tests -v
```

Features: deterministic dummy generator; transparent Indonesian preprocessing with negation preservation; lexicon sentiment baseline and human-label evaluation; keyword dictionary themes with traceable excerpts; directed weighted reply-network summary; audit and Markdown report with annotation template.

Limitations: not a statistical topic model, transformer sentiment model, stemmer, community detector, or causal-analysis tool. See references/evaluation-protocol.md.
