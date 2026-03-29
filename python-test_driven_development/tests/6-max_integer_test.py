#!/usr/bin/python3
"""Unittest for max_integer function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_ordered_list(self):
        """Test max in an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test max in an unordered list."""
        self.assertEqual(max_integer([4, 1, 8, 2]), 8)

    def test_max_at_beginning(self):
        """Test max when first element is already the maximum."""
        self.assertEqual(max_integer([10, 5, 3, 1]), 10)

    def test_negative_numbers(self):
        """Test max with only negative numbers."""
        self.assertEqual(max_integer([-10, -3, -20]), -3)

    def test_single_element(self):
        """Test max with single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test max with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_float_values(self):
        """Test max with float values."""
        self.assertEqual(max_integer([1.2, 4.5, 3.1]), 4.5)

    def test_mixed_numbers(self):
        """Test max with mixed int and float values."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)


if __name__ == "__main__":
    unittest.main()
