"""
To Do:
-fix all doc strings
-create unit tests for each function
-fix gcd function
-more...
"""


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

    """ Creates a fraction object """

    def __init__(self, top: int = 0, bottom: int = 1):
        self.__num: int = top
        self.__den: int = bottom

    """ replacing default String  """

    def __str__(self):
        return f"{self.__num}/{self.__den}"

    """ This is essentially a getter """

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
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum


''' 
TO FIX:
- figure out gcd function 
- create unit tests for each function 

UNIT TESTING FOR FRACTION CLASS BELOW
'''

"""
myfraction = Fraction(3, 5)
print(myfraction)
otherfraction = Fraction(2, 9)
print(otherfraction)
frac_sum = myfraction.__add__(otherfraction)
print(f" __add__ result : {frac_sum} ")
oden = otherfraction.den
mden = myfraction.den
print(f"oden = {oden} , mden = {mden}")

# x = gcd(20, 10)
# print(x)

print()
print()
"""
