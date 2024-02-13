#!/usr/bin/python3
import unittest
from Prog1 import summation

class TestSummation(unittest.TestCase):

    def test_empty_list(self):
        """Tests that an empty list raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            summation([])
        self.assertEqual(str(context.exception), "The input list cannot be empty.")

    def test_single_number(self):
        """Tests that a list with a single number returns that number."""
        self.assertEqual(summation([5]), 5)

    def test_multiple_numbers(self):
        """Tests that a list with multiple numbers returns their sum."""
        self.assertEqual(summation([2, 4, 6]), 12)

    def test_negative_numbers(self):
        """Tests that the function handles negative numbers correctly."""
        self.assertEqual(summation([-3, 1, -2]), -5)

    def test_large_list(self):
        """Tests that the function works with a large list of numbers."""
        numbers = list(range(100))
        self.assertEqual(summation(numbers), 4950)

if __name__ == '__main__':
    unittest.main()
