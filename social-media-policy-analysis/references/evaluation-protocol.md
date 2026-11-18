# Evaluation Protocol

- Annotate a documented sample with a written codebook; preserve post_id and original text.
- Labels: positive, negative, neutral/mixed. Sentiment is not policy stance or emotion.
- Use two independent annotators where feasible; record annotator_id, gold_label, notes and adjudication procedure.
- Evaluation CSV requires gold_label and predicted_label. Report sample size, accuracy, per-class precision/recall/F1, macro F1 and confusion matrix.
- Lexicon output is baseline only. Synthetic labels are software tests, not research evidence.
- Sarcasm, negation, regional language, code-switching and context are error risks.
