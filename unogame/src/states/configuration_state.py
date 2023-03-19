from .state import GameState
from scene import ConfigurationScene
import pygame

class ConfigurationState(GameState):
    def __init__(self):
        super().__init__()
        self.set_scene(ConfigurationScene())

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "MENU", ()
        return None, ()
