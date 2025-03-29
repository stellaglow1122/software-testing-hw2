import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_zero(self):
        result = self.calc.add(0, 0)
        self.assertEqual(result, 0)

    def test_add_mixed_sign(self):
        result = self.calc.add(-2, 3)
        self.assertEqual(result, 1)

    def test_add_floats(self):
        result = self.calc.add(2.5, 3.1)
        self.assertAlmostEqual(result, 5.6, places=1)

    def test_minus_positive_numbers(self):
        result = self.calc.minus(5, 3)
        self.assertEqual(result, 2)

    def test_minus_negative_numbers(self):
        result = self.calc.minus(-5, -3)
        self.assertEqual(result, -2)

    def test_minus_mixed_sign(self):
        result = self.calc.minus(5, -3)
        self.assertEqual(result, 8)

    def test_minus_floats(self):
        result = self.calc.minus(5.5, 3.2)
        self.assertAlmostEqual(result, 2.3, places=1)

    def test_add_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calc.add("a", 3)

    def test_minus_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calc.minus(3, None)


if __name__ == "__main__":
    unittest.main()
