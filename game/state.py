from .point import *


class GameState:
    def __init__(self):
        self.worms = []
        self.player_move_x = 0
        self.player_move_y = 0

        self.background_colour = 0, 0, 0  # rgb 256
        self.screen_size = 1024, 768  # pixels
        self.point_radius = 16  # pixels

    def update(self, ticks):
        if len(self.worms) < 1:
            return

        for worm in self.worms:
            worm.update(ticks)

        player = self.worms[0]
        player_velocity = Point(self.player_move_x, self.player_move_y)
        if player_velocity.magnitude_squared() > 0.2: # dead zone
            player.move_vec = player_velocity
