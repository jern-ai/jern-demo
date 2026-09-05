import pathlib
import sys
import unittest
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from page_title import extract_title


PYTHON_DOCS_URL = "https://docs.python.org/3/"


class PageTitleTests(unittest.TestCase):
    def test_extract_title_from_html(self):
        sample = "<html><head><title>Hello &amp; World</title></head></html>"
        self.assertEqual(extract_title(sample), "Hello & World")

    def test_extract_title_returns_none_when_missing(self):
        self.assertIsNone(extract_title("<html><body>no title</body></html>"))

    def test_python_docs_title(self):
        try:
            with urllib.request.urlopen(PYTHON_DOCS_URL, timeout=10) as response:
                page = response.read().decode("utf-8")
        except Exception as exc:
            raise unittest.SkipTest(f"Could not fetch {PYTHON_DOCS_URL}: {exc}")

        title = extract_title(page)
        self.assertIsNotNone(title)
        self.assertIn("documentation", title.lower())


if __name__ == "__main__":
    unittest.main()
