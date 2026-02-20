from .point import *


class GameState:
    def __init__(self):
        self.worms = []
        self.player_move_x = 0
        self.player_move_y = 0
        self.player_move_speed = 1

        self.background_colour = 0, 0, 0  # rgb 256
        self.screen_size = 1024, 768  # pixels
        self.point_radius = 16  # pixels

    def update(self, ticks):
        if len(self.worms) < 1:
            return

        # 60 fps = 16.666666 ticks per frame
        scale_factor = ticks / 16.666666

        player = self.worms[0]
        player_velocity = Point(self.player_move_x, self.player_move_y)
        player.position += player_velocity.normalized() * (self.player_move_speed * scale_factor)
