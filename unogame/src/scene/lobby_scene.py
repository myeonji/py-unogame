import pygame

from config import KEYBOARD_MAP
from scene import Scene
from states.lobby_state import LobbyState
from utils import action_name, overlay_name


class LobbyScene(Scene):
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            key_event = event.key
            action = KEYBOARD_MAP[key_event]
            if action == action_name.RETURN:
                self.state.start_single_play()
            if action == action_name.PAUSE:
                self.state.active_overlay(overlay_name.CONFIGURATION)

    def resize_images(self):
        pass

    def initialize_elements(self):
        pass

    def __init__(self, screen, gui_manager):
        super().__init__(screen, gui_manager)
        self.state = LobbyState()
        self.resize_images()
        self.initialize_elements()

    def draw(self):
        self.screen.fill((252, 244, 215))
        self.gui_manager.draw_ui(self.screen)