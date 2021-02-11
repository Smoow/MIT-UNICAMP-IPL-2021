def get_mdc(n1, n2):
    """The Euclidean algorithm is a way to find the greatest common divisor of two positive integers, n1 and 2."""
    if (n1 > n2):
        n1, n2 = n2, n1

    while (True):
        r = n1 % n2
        if (r == 0):
            return n2

        n1, n2 = n2, r


class Rational:
    def __init__(self, num, den):
        self.num = int(num)
        self.den = int(den)

    def get_numerator(self):
        return int(self.num)

    def get_denominator(self):
        return int(self.den)

    def to_float(self):
        return float(self.num/self.den)

    def reciprocal(self):
        new_number = Rational(self.den, self.num)
        return new_number

    def reduce(self):
        mdc = get_mdc(self.num, self.den)
        return Rational(self.num/mdc, self.den/mdc)

    def __add__(self, other):
        if (isinstance(other, Rational)):
            return Rational(self.num * other.den + self.den * other.num, self.den * other.den).reduce()

        if (isinstance(other, int)):
            return Rational(self.num + self.den * other, self.den).reduce()

        if (isinstance(other, float)):
            return self.to_float() + other

        return None

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.num, self.den * other.den)

        if isinstance(other, int):
            return Rational(self.num * other, self.den)

        if isinstance(other, float):
            return self.to_float() * other

        return None

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.den, self.den * other.num)

        if isinstance(other, int):
            return Rational(self.num, self.den * other)

        if isinstance(other, float):
            return self.to_float() / other

        return None

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.num * other.den - self.den * other.num, self.den * other.den).reduce()

        if isinstance(other, int):
            return Rational(self.num - self.den * other, self.den).reduce()

        if isinstance(other, float):
            return self.to_float() - other

        return None
