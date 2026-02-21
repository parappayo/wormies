import pygame, time

from game import *
from gui import *


if __name__ == '__main__':
    game = GameState()
    worm = Worm(400, 300, 5)
    game.spawn_player(400, 300, 5)
    game.spawn_bot(200, 200, 3)
    game.spawn_bot(200, 600, 3)
    game.spawn_bot(600, 200, 3)
    game.spawn_bot(600, 600, 3)
    game.spawn_edibles(100)

    pygame.init()
    screen = pygame.display.set_mode(game.screen_size)
    pygame.display.set_caption("Wormies")
    graphics = Graphics(screen, game)

    pygame.joystick.init()
    if pygame.joystick.get_count() > 0:
        joy = pygame.joystick.Joystick(0)
        joy.init()
        print("found joystick", joy.get_name())

    input_handler = InputHandler()
    input_handler.add(QuitHandler())
    input_handler.add(JoystickHandler())

    last_ticks = pygame.time.get_ticks()
    while True:
        input_handler.handle_events(pygame.event.get(), game)
        ticks = pygame.time.get_ticks()
        game.update(ticks - last_ticks)
        last_ticks = ticks
        graphics.draw_frame()
        time.sleep(0.001)
