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

    def test_multiply_positive_numbers(self):
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_multiply_negative_numbers(self):
        result = self.calc.multiply(-3, -4)
        self.assertEqual(result, 12)

    def test_multiply_mixed_sign(self):
        result = self.calc.multiply(-3, 4)
        self.assertEqual(result, -12)

    def test_multiply_zero(self):
        result = self.calc.multiply(3, 0)
        self.assertEqual(result, 0)

    def test_multiply_floats(self):
        result = self.calc.multiply(2.5, 3.0)
        self.assertAlmostEqual(result, 7.5, places=1)

    def test_multiply_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calc.multiply("a", 3)

    def test_divide_positive_numbers(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_negative_numbers(self):
        result = self.calc.divide(-10, -2)
        self.assertEqual(result, 5)

    def test_divide_mixed_sign(self):
        result = self.calc.divide(-10, 2)
        self.assertEqual(result, -5)

    def test_divide_floats(self):
        result = self.calc.divide(7.5, 2.5)
        self.assertAlmostEqual(result, 3.0, places=1)

    def test_divide_zero_dividend(self):
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_divide_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calc.divide("a", 3)


if __name__ == "__main__":
    unittest.main()
