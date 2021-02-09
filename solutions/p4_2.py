import math


def isequal(x, y, threshold=1e-6):
    return abs(x - y) <= threshold


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)


class Triangle:
    def __init__(self, p1, p2, p3):
        """p1, p2, p3 are Point instances"""
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_lengths(self):
        """Returns tuple of side lenghts in no particular order"""
        d12 = self.p1.euclidean_distance(self.p2)
        d23 = self.p2.euclidean_distance(self.p3)
        d31 = self.p3.euclidean_distance(self.p1)
        return d12, d23, d31

    def angles(self):
        """Returns tuple of angles between sides in no particular order"""
        a, b, c = self.side_lengths()
        
        # lei dos cossenos para calcular os ângulos
        a12 = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
        a23 = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        a31 = math.acos((c ** 2 + a ** 2 - b ** 2) / (2 * c * a))

        return a12, a23, a31

    def side_classification(self):
        """Classifies triangle according to side lengths"""
        sides = self.side_lengths()

        if isequal(sides[0], sides[1]) and isequal(sides[1], sides[2]) and isequal(sides[2], sides[0]):
            return "equilateral"  # três lados iguais: equilátero

        if isequal(sides[0], sides[1]) or isequal(sides[1], sides[2]) or isequal(sides[2], sides[0]):
            return "isosceles"  # dois lados iguais, mas não os três: isósceles

        return "scalene"  # lados diferentes: escaleno

    def angle_classification(self):
        """Classifies triangle according to internal angles"""
        largest_angle = max(self.angles())

        if isequal(largest_angle, math.pi/2):  # maior ângulo = 90 graus
            return "right"
        if largest_angle > math.pi / 2:  # maior ângulo > 90 graus
            return "obtuse"
        if isequal(largest_angle, math.pi/3):  # maior ângulo = 60 graus (outros dois são necessariamente 60 tambeém)
            return "equiangular"
        return "acute"  # acuntângulo

    def is_right(self):
        """Checks whether rectangle is right or not"""
        return self.angle_classification() == "right"

    def perimeter(self):
        """Yields triangle's perimeter"""
        return sum(self.side_lengths())

    def area(self):
        """Gives area calculated by Heron's Formula"""
        p = self.perimeter() / 2  # semiperímetro
        a, b, c = self.side_lengths()  # a,b,c contêm lados

        return (p * (p-a) * (p-b) * (p-c)) ** 0.5  # fórmula de Heron
