import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "social-media-policy-analysis" / "scripts" / "analyze_social_data.py"


class AnalyzeSocialDataCLITests(unittest.TestCase):
    def run_script(self, csv_path, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(csv_path), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_csv_profile_and_quality_checks(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "sample.csv"
            csv_path.write_text(
                "created_at,text,author\n"
                "2026-11-17T10:00:00Z,Halo dunia,alice\n"
                "2026-11-17T11:00:00Z,,bob\n"
                "invalid-date,Halo dunia,alice\n"
                "2026-11-17T10:00:00Z,Halo dunia,alice\n",
                encoding="utf-8",
            )
            result = self.run_script(csv_path)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["rows"], 4)
            self.assertEqual(report["exact_duplicate_rows"], 1)
            self.assertEqual(report["missing_by_column"]["text"]["count"], 1)
            self.assertEqual(report["timestamp_profile"]["valid"], 3)
            self.assertEqual(report["timestamp_profile"]["nonempty_invalid"], 1)
            self.assertEqual(report["text_profile"]["nonempty"], 3)
            self.assertEqual(report["text_profile"]["empty"], 1)
            self.assertEqual(report["author_profile"]["unique_nonempty_authors"], 2)

    def test_json_output_option(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "sample.csv"
            output_path = Path(temp_dir) / "report.json"
            csv_path.write_text("text\nexample\n", encoding="utf-8")
            result = self.run_script(csv_path, "--output", str(output_path))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(output_path.read_text(encoding="utf-8"))["rows"], 1)

    def test_header_only_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "empty_rows.csv"
            csv_path.write_text("text,author\n", encoding="utf-8")
            result = self.run_script(csv_path)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["rows"], 0)

    def test_empty_file_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "empty.csv"
            csv_path.write_text("", encoding="utf-8")
            result = self.run_script(csv_path)
            self.assertEqual(result.returncode, 1)
            self.assertIn("CSV has no header row", result.stderr)

    def test_missing_input_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "missing.csv"
            result = self.run_script(csv_path)
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
