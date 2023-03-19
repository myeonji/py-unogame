import pygame

from .scene import Scene


class ConfigurationScene(Scene):
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen, **kwargs):
        text = self.font.render("Configuration", True, (255, 255, 255))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
