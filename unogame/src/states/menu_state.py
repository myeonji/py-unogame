import pygame

from states import GameState
from utils import scene_name

class MenuState(GameState):
    def __init__(self):
        super().__init__()
        self.changed = False

    def start_single_play(self):
        self.move_scene(scene_name.PLAYING_GAME)

    def open_configuration(self):
        self.move_scene(scene_name.CONFIGURATION)

    def exit(self):
        pygame.quit()
