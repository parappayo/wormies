import pygame, time

from game import *
from gui import *


if __name__ == '__main__':
    game = GameState()
    worm = Worm()
    worm.position = Point(800, 30)
    for i in range(10):
        worm.grow()
    game.worms.append(worm)

    pygame.init()
    screen = pygame.display.set_mode(game.screen_size)
    pygame.display.set_caption("Wormies")
    graphics = Graphics(screen, game)

    input_handler = InputHandler()
    input_handler.add(QuitHandler())

    while True:
        input_handler.handle_events(pygame.event.get(), game)
        graphics.draw_frame()
        time.sleep(0.001)
