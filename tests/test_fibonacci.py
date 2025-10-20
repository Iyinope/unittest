# test_factorial.py
import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_large_number(self):
        self.assertEqual(factorial(7), 5040)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-3)

if __name__ == "__main__":
    unittest.main()
