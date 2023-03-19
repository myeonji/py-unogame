import pygame

class PlayingScene:
    def draw(self, screen, counter):
        font = pygame.font.Font(None, 32)
        text = font.render(f"Counter: {counter}", True, (255, 255, 255))
        screen.blit(text, (10, 10))
