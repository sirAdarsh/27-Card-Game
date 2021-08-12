import pygame

class Settings:
    def __init__(self):
        self.screen_width, self.screen_height = 1500, 800
        self.bg_color = (225, 225, 225)
        surface = pygame.display.set_mode((1500,800))
        surface.fill(self.bg_color)
        pygame.display.flip()
