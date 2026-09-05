import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from temperature import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    fahrenheit_to_rankine,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    rankine_to_fahrenheit,
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

    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(273.15), 0)
        self.assertEqual(kelvin_to_celsius(373.15), 100)

    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(fahrenheit_to_kelvin(32), 273.15)
        self.assertEqual(fahrenheit_to_kelvin(212), 373.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertEqual(kelvin_to_fahrenheit(273.15), 32)
        self.assertEqual(kelvin_to_fahrenheit(373.15), 212)

    def test_fahrenheit_to_rankine(self):
        self.assertAlmostEqual(fahrenheit_to_rankine(32), 491.67)
        self.assertAlmostEqual(fahrenheit_to_rankine(212), 671.67)

    def test_rankine_to_fahrenheit(self):
        self.assertAlmostEqual(rankine_to_fahrenheit(491.67), 32)
        self.assertAlmostEqual(rankine_to_fahrenheit(671.67), 212)


if __name__ == "__main__":
    unittest.main()
