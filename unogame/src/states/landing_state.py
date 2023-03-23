import pygame

from states import GameState
from utils import scene_name


class LandingState(GameState):
    def __init__(self):
        super().__init__()
        self.changed = False
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 3000)

    def start(self, event):
        if event.type == self.timer_event:
            self.changed = True
            self.move_scene(scene_name.MAIN_MENU)


