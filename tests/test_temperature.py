import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


class CelsiusToFahrenheitTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        cases = [
            (-273.15, -459.67),
            (-40, -40),
            (-20, -4),
            (-10, 14),
            (-5.5, 22.1),
            (0, 32),
            (18.5, 65.3),
            (25, 77),
            (37, 98.6),
            (100, 212),
            (250, 482),
        ]
        for celsius, expected in cases:
            with self.subTest(celsius=celsius):
                self.assertAlmostEqual(
                    celsius_to_fahrenheit(celsius), expected, places=7
                )


class FahrenheitToCelsiusTests(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        cases = [
            (-459.67, -273.15),
            (-40, -40),
            (-4, -20),
            (14, -10),
            (22.1, -5.5),
            (32, 0),
            (65.3, 18.5),
            (77, 25),
            (98.6, 37),
            (212, 100),
            (482, 250),
        ]
        for fahrenheit, expected in cases:
            with self.subTest(fahrenheit=fahrenheit):
                self.assertAlmostEqual(
                    fahrenheit_to_celsius(fahrenheit), expected, places=7
                )


if __name__ == "__main__":
    unittest.main()
