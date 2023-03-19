import pygame
from .state import GameState
from config.keyboard_mapper import KEYBOARD_MAP
from scene.playing_scene import PlayingScene


class PlayingState(GameState):

    def __init__(self):
        super().__init__()
        self.set_scene(PlayingScene())
        self.counter = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                action = KEYBOARD_MAP.get(event.key)
                if action == 'PAUSE':
                    return 'MENU', ()
                elif action == 'FIRE':
                    return 'GAMEOVER', self.counter
        return None, ()

    def update(self):
        self.counter += 1
        return None, (self.counter,)

    def draw(self, screen, *args):
        super().draw(screen, *args)
