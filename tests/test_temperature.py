import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


class TemperatureTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        """Celsius values convert to the expected Fahrenheit values."""
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_fahrenheit_to_celsius(self):
        """Fahrenheit values convert to the expected Celsius values."""
        self.assertEqual(fahrenheit_to_celsius(212), 100)
        self.assertEqual(fahrenheit_to_celsius(32), 0)


if __name__ == "__main__":
    unittest.main()
