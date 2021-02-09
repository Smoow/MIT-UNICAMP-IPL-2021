class Vector:
    def __init__(self, numbers):
        self.nums = numbers

    def as_list(self):
        return self.nums

    def size(self):
        return len(self.nums)

    def magnitude(self):  # raiz da soma dos quadrados de cada coordenada do vetor
        total = 0

        for dim_val in self.nums:
            total += dim_val ** 2

        return total ** 0.5

    def euclidean_distance(self, other):
        # Calcula a distância entre cada par de vetores, eleva-a ao quadrado e
        # adiciona o total. Então tira a raiz.
        dist = 0

        for el_self, el_other in zip(self.nums, other.nums):
            # zip permite percorrer duas listas paralelamente
            dist += (el_self - el_other) ** 2

        return dist ** 0.5

    def normalized(self):  # normalizar: dividir cada elemento por magnitude
        mag = self.magnitude()
        new = []

        for dim_val in self.nums:
            new.append(dim_val / mag)

        return Vector(new)

    def cosine_similarity(self, other):
        dot_pdt = self * other  # calcula produto escalar com método __mul__ abaixo
        return dot_pdt / (self.magnitude() * other.magnitude())

    def __add__(self, other):
        if isinstance(other, Vector) and self.size() == other.size():
            new = []

            for el_self, el_other in zip(self.nums, other.nums):
                new.append(el_self + el_other)

            return Vector(new)  # alternativamente, uma solução mais Pythonica:
            # return Vector([x + y for x, y in zip(self.nums, other.nums)])

        return None

    def __sub__(self, other):
        if isinstance(other, Vector) and self.size() == other.size():
            new = []

            for el_self, el_other in zip(self.nums, other.nums):
                new.append(el_self - el_other)

            return Vector(new)  # alternativamente, uma solução mais Pythonica:
            # return Vector([x - y for x, y in zip(self.nums, other.nums)])

        return None

    def __mul__(self, other):
        if isinstance(other, Vector) and self.size() == other.size():
            total = 0

            for el_self, el_other in zip(self.nums, other.nums):
                total += el_self * el_other  # produto escalar

            return total

        if isinstance(other, (int, float)):
            new = []

            for dim_val in self.nums:
                new.append(dim_val * other)  # multiplica cada entrada por other

            return Vector(new)
        
        return None

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self * (1 / other)  # dividir é multiplicar pelo inverso

        return None
