#!/usr/bin/python3
"""unittest 6-max_integer_test"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """testing"""
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 2, 5, 4]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -2, -5, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 3, 0, -5, 4]), 4)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.1, 3.3, 2.2, 5.5, 4.4]), 5.5)
