from .point import Point


class Worm:
    def __init__(self):
        self.position = Point(0, 0)
        self.points = [Point(0, 0)]

    def grow(self):
        last = self.points[-1]
        self.points.append(Point(last.x - 10, last.y))
