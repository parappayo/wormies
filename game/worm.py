from .point import Point


class Worm:
    def __init__(self, x, y):
        self.points = [Point(x, y)]
        self.move_vec = Point(1, 0)
        self.move_speed = 20 # pixels per frame at 60 fps
        self.spacing = 15
        self.ticks_per_move = 20
        self.ticks_since_last_move = 0

    def update(self, ticks):
        self.ticks_since_last_move += ticks
        if self.ticks_since_last_move >= self.ticks_per_move:
            self.ticks_since_last_move = self.ticks_since_last_move % self.ticks_per_move
            self.move(ticks)

    def grow(self):
        self.points.append(self.points[-1])

    def move(self, ticks):
        # 60 fps = 16.666666 ms per frame
        frames = ticks / 16.666666

        self.points[-1] += self.move_vec.normalized() * self.move_speed * frames
        if len(self.points) > 1:
            tail_vec = self.points[1] - self.points[0]
            self.points[0] += tail_vec.normalized() * self.move_speed * frames
        if self.distance_between_head_and_body().magnitude_squared() > (self.spacing * self.spacing):
            for i in range(len(self.points)-1):
                self.points[i] = self.points[i+1]

    def distance_between_head_and_body(self):
        if len(self.points) < 2:
            return 0
        return self.points[-1] - self.points[-2]
