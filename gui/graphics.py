import pygame


def draw_pip(surface, radius, point):
    inner_colour = 160, 160, 220
    outer_colour = 220, 220, 220
    border_thickness = 2
    pygame.draw.circle(surface, inner_colour, point, radius)
    pygame.draw.circle(surface, outer_colour, point, radius, border_thickness)


def create_pip(radius):
    transparent_color = 0, 0, 0
    size = int(radius * 2)
    center = size // 2, size // 2
    surface = pygame.Surface((size, size), pygame.HWSURFACE)
    surface.set_colorkey(transparent_color)
    draw_pip(surface, radius, center)
    return surface


class Graphics:

    def __init__(self, surface, game):
        self.surface = surface
        self.game = game
        self.pip_surface = create_pip(game.point_radius)

    def draw_frame(self):
        self.surface.fill(self.game.background_colour)

        for worm in self.game.worms:
            self.draw_worm(worm)

        pygame.display.flip()

    def draw_point(self, point):
        dest_rect = self.pip_surface.get_rect()
        dest_rect.center = int(point.x), int(point.y)
        self.surface.blit(self.pip_surface, dest_rect)

    def draw_worm(self, worm):
        for point in worm.points:
            self.draw_point(point + worm.position)
