import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point): return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return '<Point x:{point.x:.2f}, y:{point.y:.2f}>'.format(point=self)

    def __str__(self):
        return '({point.x:.2f}, {point.y:.2f})'.format(point=self)

    def __add__(self, other):
        if not isinstance(other, Point):
            return
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return
        return Point(self.x * scalar, self.y * scalar)

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalized(self):
        return self * self.magnitude()

    def as_tuple(self):
        return (self.x, self.y)
