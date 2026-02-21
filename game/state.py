import random

from .bot import *
from .edible import *
from .player import *
from .point import *
from .worm import *


class GameState:
    def __init__(self):
        self.players = []
        self.bots = []
        self.worms = []
        self.edibles = []
        self.player_move_x = 0
        self.player_move_y = 0

        self.background_colour = 0, 0, 0  # rgb 256
        self.screen_size = 1024, 768  # pixels
        self.point_radius = 16  # pixels

    def update(self, ticks):
        if len(self.worms) < 1:
            return

        for bot in self.bots:
            bot.update(self, ticks)

        for worm in self.worms:
            worm.update(self, ticks)

        # joystick handling
        player_velocity = Point(self.player_move_x, self.player_move_y)
        if player_velocity.magnitude_squared() > 0.2: # dead zone
            self.players[0].worm.move_vec = player_velocity

    def spawn_player(self, x, y, length):
        worm = Worm(x, y, length)
        self.players.append(Player(worm))
        self.worms.append(worm)

    def spawn_bot(self, x, y, length):
        worm = Worm(x, y, length)
        self.bots.append(Bot(worm))
        self.worms.append(worm)

    def spawn_edibles(self, count):
        margin = 80
        for i in range(count):
            x = random.randint(margin, self.screen_size[0] - margin)
            y = random.randint(margin, self.screen_size[1] - margin)
            self.edibles.append(Edible(x, y))

    def despawn_edibles(self, edibles_to_despawn):
        self.edibles = [x for x in self.edibles if x not in edibles_to_despawn]
