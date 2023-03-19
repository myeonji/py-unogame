from .state import GameState
from scene import LandingScene
import pygame

class LandingState(GameState):
    def __init__(self):
        super().__init__()
        self.set_scene(LandingScene())

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "MENU", ()
        return None, ()

    def update(self):
        if self.scene.is_over():
            return "MENU", ()
        return None
