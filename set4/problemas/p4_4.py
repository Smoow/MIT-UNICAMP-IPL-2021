class Vector:
    def __init__(self, elements):
        self.numbers = elements

    def as_list(self):
        return self.numbers

    def size(self):
        return len(self.numbers)

    def magnitude(self):
        mag = 0

        for i in self.numbers:
            mag += (i ** 2)

        return (mag ** 0.5)

    def euclidean_distance(self, other):
        euc_dist = 0

        for i, j in zip(self.numbers, other.numbers):
            euc_dist += ((i - j) ** 2)

        return (euc_dist ** 0.5)

    def normalized(self):
        mag = self.magnitude()
        norm = []

        for i in self.numbers:
            norm.append(i / mag)

        return Vector(norm)

    def cosine_similarity(self, other):
        prod_escalar = 0

        for i, j in zip(self.numbers, other.numbers):
            prod_escalar += i * j

        return prod_escalar / (self.magnitude() * other.magnitude())

    def __add__(self, other):
        if not (isinstance(other, Vector)):
            return None

        if (len(self.numbers) != len(other.numbers)):
            return None

        sum_vector = []
        for i, j in zip(self.numbers, other.numbers):
            sum_vector.append(i + j)

        return Vector(sum_vector)

    def __sub__(self, other):
        if not (isinstance(other, Vector)):
            return None

        if (len(self.numbers) != len(other.numbers)):
            return None

        sum_vector = []
        for i, j in zip(self.numbers, other.numbers):
            sum_vector.append(i - j)

        return Vector(sum_vector)

    def __mul__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            new_vect = []

            for i in self.numbers:
                new_vect.append(i * other)

            return Vector(new_vect)

        if (self.size() == other.size() and (isinstance(other, Vector))):
            total = 0

            for i, j in zip(self.numbers, other.numbers):
                total += i * j  # produto escalar

            return total

        return None

    def __truediv__(self, other):
        new_vect = []

        if (isinstance(other, float) or isinstance(other, int)):
            for i in self.numbers:
                new_vect.append(i / other)
            return Vector(new_vect)

        return None
