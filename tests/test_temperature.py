import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from temperature import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
)


class TemperatureTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(212), 100)
        self.assertEqual(fahrenheit_to_celsius(32), 0)

    def test_celsius_to_kelvin(self):
        self.assertEqual(celsius_to_kelvin(0), 273.15)
        self.assertEqual(celsius_to_kelvin(100), 373.15)


if __name__ == "__main__":
    unittest.main()
