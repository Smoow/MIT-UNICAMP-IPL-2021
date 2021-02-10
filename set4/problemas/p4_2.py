import math


def isequal(x, y, limit=1e-6):
    return abs(x - y) <= limit


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
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_lengths(self):
        sl_1 = self.p1.euclidean_distance(self.p2)
        sl_2 = self.p2.euclidean_distance(self.p3)
        sl_3 = self.p3.euclidean_distance(self.p1)
        return [sl_1, sl_2, sl_3]

    def angles(self):
        a, b, c = self.side_lengths()

        # utilizado a lei dos cossenos para o cálculo dos ângulos
        ang_12 = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
        ang_23 = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        ang_31 = math.acos((c ** 2 + a ** 2 - b ** 2) / (2 * c * a))
        return ang_12, ang_23, ang_31

    def side_classification(self):
        a, b, c = self.side_lengths()

        if isequal(a, b) and isequal(b, c) and isequal(c, a):
            return "equilateral"

        if isequal(a, b) or isequal(b, c) or isequal(c, a):
            return "isosceles"

        return "scalene"

    def angle_classification(self):
        large_angle = max(self.angles())

        if large_angle > math.pi/2:
            return "obtuse"

        if isequal(large_angle, math.pi/3):
            return "equiangular"

        if isequal(large_angle, math.pi/2):
            return "right"

        return "acute"

    def is_right(self):
        if (self.angle_classification() == "right"):
            return True

        return False

    def area(self):
        # Utilizado a fórmula de Heron para aproveitar o perimeter e side_lengths
        p = self.perimeter() / 2
        a, b, c = self.side_lengths()

        return (p * (p-a) * (p-b) * (p-c)) ** 0.5

    def perimeter(self):
        return sum(self.side_lengths())
