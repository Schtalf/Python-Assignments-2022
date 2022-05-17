# отрицательные дроби будут представляться отрицательным числителем
def gcd(newnum, newden):  # функция для сокращения дроби
    while newnum % newden != 0:
        oldm = newnum
        oldn = newden

        newnum = oldn
        newden = oldm % oldn
    return newden


class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)


print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1 == f2)
print(f1 != f2)
print(f1 > f2)
print(f1 < f2)
