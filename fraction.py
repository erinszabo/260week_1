# import test
# print("imported")

def gcd(m, n):
    """
    finds the greatest common denominator.
    :type n: int
    :type m: int
    """
    while m % n != 0:  # while m doesn't divide evenly into n // check if m % n (modulo of the 2 given) != 0
        oldm = m  # swap m and n
        oldn = n
        m = oldn
        n = oldm % oldn  # set n equal to the modulo of oldm and oldn
    return n


class Fraction:
    # __den: int

    def __init__(self, top: int = 0, bottom: int = 1):
        """
        creates a Fraction object
        :type top: int
        :type bottom: int
        """
        self.__num: int = top
        self.__den: int = bottom

    def __str__(self):
        return f"{self.__num}/{self.__den}"

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    def __add__(self, otherfraction):
        """"
        adds the fractions, not simplified
        :type otherfraction: Fraction
        """
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def simplified_add(self, otherfraction):
        """"
        adds the fractions, simplified
        :type otherfraction: Fraction
        """
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        """"
        tests if two fraction objects are equal
        :type other: Fraction
        """
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
