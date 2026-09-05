import pathlib
import subprocess
import sys
import unittest

SRC_DIR = pathlib.Path(__file__).resolve().parents[1] / "src"
CLI_PATH = SRC_DIR / "cli.py"


def run_cli(*args):
    """Run the CLI through a subprocess and return its completed process."""
    return subprocess.run(
        [sys.executable, str(CLI_PATH), *args],
        capture_output=True,
        text=True,
    )


class CliTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        result = run_cli("100", "celsius", "fahrenheit")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "212.0")

    def test_fahrenheit_to_celsius(self):
        result = run_cli("212", "fahrenheit", "celsius")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "100.0")

    def test_negative_value(self):
        result = run_cli("-40", "celsius", "fahrenheit")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "-40.0")

    def test_fractional_value(self):
        result = run_cli("18.5", "celsius", "fahrenheit")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "65.3")

    def test_unknown_source_scale(self):
        result = run_cli("100", "kelvin", "fahrenheit")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no conversion from 'kelvin'", result.stderr)

    def test_unknown_target_scale(self):
        result = run_cli("100", "celsius", "kelvin")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no conversion from 'celsius' to 'kelvin'", result.stderr)

    def test_unknown_pair(self):
        result = run_cli("100", "kelvin", "rankine")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no conversion from 'kelvin' to 'rankine'", result.stderr)

    def test_non_numeric_value(self):
        result = run_cli("abc", "celsius", "fahrenheit")
        self.assertNotEqual(result.returncode, 0)

    def test_missing_arguments(self):
        result = run_cli("100", "celsius")
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
