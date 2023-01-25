#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for testing max_integer function"""
    
    def test_max_integer(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([4]), 4)
        
    def test_negative(self):
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)
        self.assertEqual(max_integer([-1, -4, -2, -3]), -1)
        
    def test_float(self):
        self.assertEqual(max_integer([4.0, 3.0, 2.0, 1.0]), 4.0)
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)
        self.assertEqual(max_integer([4.2, 4.5, 4.8, 4.9]), 4.9)
        
    def test_string(self):
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")
        self.assertEqual(max_integer(["d", "c", "b", "a"]), "d")
        self.assertEqual(max_integer(["d", "c", "d", "a"]), "d")
    def test_list_with_non_integers(self):
        self.assertRaises(TypeError, max_integer, [1, 2, '3'])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, '4'])

if __name__ == '__main__':
    unittest.main()
