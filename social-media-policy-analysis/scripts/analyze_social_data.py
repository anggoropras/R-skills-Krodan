#!/usr/bin/env python3
"""Standard-library CSV audit and exploratory profile for social-media datasets.

This script does not perform sentiment analysis, topic modeling, or network
inference. It reports basic structure and data-quality indicators only.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

TIMESTAMP_CANDIDATES = ("created_at", "timestamp", "date", "datetime", "time")
TEXT_CANDIDATES = ("text", "content", "message", "post", "caption")
AUTHOR_CANDIDATES = ("author", "author_id", "user", "user_id", "username", "account")


def find_column(headers: list[str], candidates: tuple[str, ...]) -> str | None:
    lookup = {h.strip().lower(): h for h in headers}
    for candidate in candidates:
        if candidate in lookup:
            return lookup[candidate]
    return None


def parse_timestamp(value: str) -> datetime | None:
    value = value.strip()
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        pass
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d %H:%M:%S"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


def audit(path: Path, encoding: str) -> dict[str, Any]:
    with path.open("r", encoding=encoding, newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames
        if not headers:
            raise ValueError("CSV has no header row.")

        row_count = 0
        missing = Counter()
        exact_rows = set()
        duplicate_rows = 0
        timestamp_col = find_column(headers, TIMESTAMP_CANDIDATES)
        text_col = find_column(headers, TEXT_CANDIDATES)
        author_col = find_column(headers, AUTHOR_CANDIDATES)
        timestamp_valid = 0
        timestamp_invalid = 0
        dates = Counter()
        authors = Counter()
        text_lengths: list[int] = []
        empty_text = 0

        for row in reader:
            row_count += 1
            normalized_row = tuple((row.get(h) or "").strip() for h in headers)
            for h in headers:
                if not (row.get(h) or "").strip():
                    missing[h] += 1
            if normalized_row in exact_rows:
                duplicate_rows += 1
            else:
                exact_rows.add(normalized_row)

            if timestamp_col:
                parsed = parse_timestamp(row.get(timestamp_col) or "")
                if parsed:
                    timestamp_valid += 1
                    dates[parsed.date().isoformat()] += 1
                elif (row.get(timestamp_col) or "").strip():
                    timestamp_invalid += 1

            if text_col:
                text = (row.get(text_col) or "").strip()
                if text:
                    text_lengths.append(len(text))
                else:
                    empty_text += 1

            if author_col:
                author = (row.get(author_col) or "").strip()
                if author:
                    authors[author] += 1

    sorted_dates = sorted(dates)
    sorted_lengths = sorted(text_lengths)
    median_length = None
    if sorted_lengths:
        mid = len(sorted_lengths) // 2
        median_length = (
            sorted_lengths[mid] if len(sorted_lengths) % 2
            else (sorted_lengths[mid - 1] + sorted_lengths[mid]) / 2
        )

    return {
        "file": str(path),
        "rows": row_count,
        "columns": headers,
        "missing_by_column": {
            h: {"count": missing[h], "percent": round(100 * missing[h] / row_count, 2) if row_count else 0}
            for h in headers
        },
        "exact_duplicate_rows": duplicate_rows,
        "detected_columns": {
            "timestamp": timestamp_col,
            "text": text_col,
            "author": author_col,
        },
        "timestamp_profile": {
            "valid": timestamp_valid,
            "nonempty_invalid": timestamp_invalid,
            "first_date": sorted_dates[0] if sorted_dates else None,
            "last_date": sorted_dates[-1] if sorted_dates else None,
            "daily_volume": dict(sorted(dates.items())),
        },
        "text_profile": {
            "nonempty": len(text_lengths),
            "empty": empty_text,
            "mean_characters": round(sum(text_lengths) / len(text_lengths), 2) if text_lengths else None,
            "median_characters": median_length,
        },
        "author_profile": {
            "unique_nonempty_authors": len(authors),
            "top_10_by_row_count": authors.most_common(10),
        },
        "notes": [
            "Duplicate rows are exact full-row matches; repeated text is not necessarily a duplicate record.",
            "Timestamp parsing supports ISO-8601 and a small set of common formats; verify timezone and locale.",
            "Author counts are descriptive only and do not measure influence or representativeness.",
            "This script does not infer sentiment, topics, coordination, or causal effects.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit and profile a social-media CSV.")
    parser.add_argument("csv_file", type=Path, help="Input CSV path")
    parser.add_argument("--encoding", default="utf-8-sig", help="Input encoding (default: utf-8-sig)")
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()

    if not args.csv_file.is_file():
        parser.error(f"Input file does not exist: {args.csv_file}")

    try:
        result = audit(args.csv_file, args.encoding)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
