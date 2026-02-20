import pygame


def on_joystick_motion(event, game):
    if event.axis == 0: # x-axis
        game.player_move_x = event.value
    elif event.axis == 1: # y-axis
        game.player_move_y = event.value


def JoystickHandler():
    return {
        pygame.JOYAXISMOTION: on_joystick_motion,
    }
