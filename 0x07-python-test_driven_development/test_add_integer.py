#!/usr/bin/python3
"""Unittest for add_integer function"""
import unittest
add_integer = __import__('0-add_integer').add_integer


class TestAddInteger(unittest.TestCase):
    """Test cases for add_integer function"""

    def test_add_integer(self):
        """Test for add_integer function"""
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(100, 2), 102)
        self.assertEqual(add_integer(1, -2), -1)
        self.assertEqual(add_integer(-1, -2), -3)
        self.assertEqual(add_integer(1.5, 2), 3)
        self.assertEqual(add_integer(1, 2.5), 3)
        self.assertEqual(add_integer(1.5, 2.5), 3)
        self.assertEqual(add_integer(1.5, -2.5), -1)
        self.assertEqual(add_integer(-1.5, -2.5), -3)
        self.assertEqual(add_integer(1.5, 0), 1)
        self.assertEqual(add_integer(0, 0), 0)
        self.assertEqual(add_integer(0, 1.5), 1)
        self.assertEqual(add_integer(0, -1.5), -1)
        self.assertEqual(add_integer(12, 43), 55)
        self.assertEqual(add_integer(12, 43.5), 55)
        self.assertEqual(add_integer(17, 52), 69)
        self.assertEqual(add_integer(17, 52.5), 69)
