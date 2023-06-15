#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([10, 0, -10]), 10)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_zero(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
    def test_OnlyOne(self):
         self.assertEqual(max_integer([4]), 4)

if __name__ == "__main__":
    unittest.main()
