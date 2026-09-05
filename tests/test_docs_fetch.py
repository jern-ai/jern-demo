import unittest
import urllib.request


class DocsFetchTests(unittest.TestCase):
    def test_docs_python_org_returns_documentation_page(self):
        with urllib.request.urlopen("https://docs.python.org/3/") as response:
            status = response.status
            html = response.read().decode("utf-8")

        self.assertEqual(status, 200)
        self.assertIn("documentation", html.lower())


if __name__ == "__main__":
    unittest.main()
