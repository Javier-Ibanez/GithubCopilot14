import unittest
from calculator import safe_eval_expression


class TestCalculator(unittest.TestCase):
    def test_safe_eval_addition(self):
        self.assertEqual(safe_eval_expression("2+3"), 5)

    def test_safe_eval_subtraction(self):
        self.assertEqual(safe_eval_expression("10-4"), 6)

    def test_safe_eval_multiplication(self):
        self.assertEqual(safe_eval_expression("3*7"), 21)

    def test_safe_eval_division(self):
        self.assertEqual(safe_eval_expression("20/5"), 4.0)

    def test_safe_eval_decimal(self):
        self.assertEqual(safe_eval_expression("2.5+1.5"), 4.0)

    def test_safe_eval_invalid_character(self):
        with self.assertRaises(ValueError):
            safe_eval_expression("2+abc")

    def test_safe_eval_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            safe_eval_expression("5/0")

    def test_safe_eval_empty_expression(self):
        with self.assertRaises(ValueError):
            safe_eval_expression("")


if __name__ == "__main__":
    unittest.main()
