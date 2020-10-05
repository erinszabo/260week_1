import unittest
import fraction as f
"""
 Remember to run the tests type this into the terminal window:
 python -m unittest test_frac.py
"""

class TestFraction(unittest.TestCase):

    def test_add(self):
        a = f.Fraction(3, 5)
        b = f.Fraction(1, 5)
        c = f.a.__add__(b)
        self.assertEqual(c, 4/5)
