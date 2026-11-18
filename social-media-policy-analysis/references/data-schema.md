# Suggested Data Schema

The schema is a recommendation, not a requirement. Preserve the original columns and map them to normalized fields in a separate analysis table.

| Field | Type | Description | Notes |
|---|---|---|---|
| record_id | string | Stable row identifier | Prefer a non-identifying generated ID |
| platform | string | Source platform | Use controlled values |
| created_at | datetime | Original post time | Preserve timezone/offset |
| text_raw | string | Original text | Restrict access where needed |
| text_clean | string | Processed text | Keep transformation log |
| author_ref | string | Pseudonymous author key | Avoid usernames in public outputs |
| language | string | Detected or coded language | Mark uncertain values |
| reply_to_ref | string | Parent record reference | Optional |
| mention_refs | array/string | Referenced account keys | Minimize personal data |
| repost_of_ref | string | Original record reference | Optional |
| hashtags | array/string | Hashtags | Preserve original spelling |
| engagement_count | number | Available engagement measure | Define which measure |
| source_url | string | Record URL, if retained | Treat as potentially identifying |
| collection_batch | string | Collection run identifier | Supports provenance |
| inclusion_status | string | Included/excluded/pending | Record exclusion reason separately |

## Data dictionary requirements

For every field, document:
- source field name;
- normalized field name;
- data type and allowed values;
- missing-value convention;
- transformation;
- whether it contains personal or identifying information.

## Minimum quality checks

1. Unique record identifier.
2. Parseable timestamps and explicit timezone.
3. Duplicate records and duplicate text handled separately.
4. Missing text and missing author references measured.
5. Numeric engagement fields validated.
6. Exclusion criteria logged.
7. Small-cell and account-level disclosure risks reviewed before publication.

## Privacy

Prefer generated pseudonymous IDs over account names. Store any re-identification key separately with access controls, or do not retain it. Remove unnecessary direct identifiers from examples and visualizations.
