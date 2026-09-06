import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from temperature import kelvin_to_celsius


class KelvinTests(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(273.15), 0)
        self.assertEqual(kelvin_to_celsius(0), -273.15)


if __name__ == "__main__":
    unittest.main()
