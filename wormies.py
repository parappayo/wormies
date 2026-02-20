import pygame, time

from game.state import GameState
from gui import *


if __name__ == '__main__':
    game = GameState()
    game.points = [(10, 20), (100, 150)]

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
