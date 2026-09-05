import os
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, get_pgdatabase


class TemperatureTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(212), 100)
        self.assertEqual(fahrenheit_to_celsius(32), 0)

    def test_get_pgdatabase(self):
        os.environ["PGDATABASE"] = "test_db"
        self.assertEqual(get_pgdatabase(), "test_db")
        del os.environ["PGDATABASE"]
        self.assertIsNone(get_pgdatabase())


if __name__ == "__main__":
    unittest.main()
