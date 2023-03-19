import pygame
from .scene import Scene


class LandingScene(Scene):

    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.start_time = pygame.time.get_ticks()
        self.display_time = 3000

    def draw(self, screen, **kwargs):
        text = self.font.render("Welcome to Unocatme", True, (255, 255, 255))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))

        remaining_time = self.display_time - (pygame.time.get_ticks() - self.start_time)
        countdown_text = self.font.render(f"{remaining_time // 1000}", True, (255, 255, 255))
        screen.blit(countdown_text, (screen.get_width() // 2 - countdown_text.get_width() // 2, screen.get_height() // 2 + text.get_height()))

    def is_over(self):
        return pygame.time.get_ticks() - self.start_time >= self.display_time
