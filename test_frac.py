import unittest
import fraction as fr

"""
 Iff I don't have the name == main part:
 Remember to run the tests type this into the terminal window:
 python -m unittest test_frac.py
"""


class TestFraction(unittest.TestCase):

    def test_add(self):
        a = fr.Fraction(3, 5)
        b = fr.Fraction(1, 5)
        c = a.__add__(b)
        print(c)
        self.assertEqual(c, fr.Fraction(20, 25))

    def test_simplified_add(self):
        a = fr.Fraction(3, 5)
        b = fr.Fraction(1, 5)
        c = a.simplified_add(b)
        print(c)
        self.assertEqual(c, fr.Fraction(4, 5))



if __name__ == '__main__':
    unittest.main()