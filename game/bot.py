import math, random

from .point import *


class Bot:
    """Bot controller class, has a worm."""
    def __init__(self, worm):
        self.worm = worm
        self.time_since_direction_change = 0

    def update(self, game, ticks):
        self.time_since_direction_change += ticks
        if self.time_since_direction_change > 500:
            self.time_since_direction_change = 0
            self.randomize_movement()

    def randomize_movement(self):
        theta = random.uniform(0, 2 * math.pi)
        self.worm.move_vec = Point(math.cos(theta), math.sin(theta))
