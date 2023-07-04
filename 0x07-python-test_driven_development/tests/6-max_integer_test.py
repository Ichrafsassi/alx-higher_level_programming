#!/usr/bin/python3
"""Unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for the max_integer() function"""

    def test_empty_list(self):
        """Test an empty list returns None"""
        self.assertIsNone(max_integer([]), "result should be none")

    def test_only_one_element_in_list(self):
        """Test an empty list returns None"""
        int_num = 20
        self.assertAlmostEqual(max_integer(
            [int_num]), int_num, f"result should be {int_num}")

    def test_positives_list(self):
        """Test an empty list returns None"""
        list_of_positives = [20, 300, 40, 50]
        self.assertAlmostEqual(max_integer(
            list_of_positives), 300, "result should be 300")

    def test_negatives_list(self):
        """Test an empty list returns None"""
        list_of_positives = [-20, -300, -40, -1]
        self.assertAlmostEqual(max_integer(
            list_of_positives), -1, "result should be -1")

    def test_negatives_list(self):
        """Test an empty list returns None"""
        list_of_positives = [-20, -300, -40, -1]
        self.assertAlmostEqual(max_integer(
            list_of_positives), -1, "result should be -1")

    def test_negatives_positives_list(self):
        """Test an empty list returns None"""
        list_of_positives = [-20, 300, -40, 1]
        self.assertAlmostEqual(max_integer(
            list_of_positives), 300, "result should be 300")

    def test_negatives_positives_list(self):
        """Test an empty list returns None"""
        list_of_positives = [-20, 300, -40, 1]
        self.assertAlmostEqual(max_integer(
            list_of_positives), 300, "result should be 300")
