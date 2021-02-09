import math


def square(x):
    return x * x


def fourth_power(x):
    return square(square(x))


def perfect_square(x):
    sqrt = math.sqrt(x)

    if ((int(sqrt + 0.5) ** 2) == x):
        return True
    else:
        return False
