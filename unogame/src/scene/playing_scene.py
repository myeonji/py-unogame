import pygame
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton

from config import KEYBOARD_MAP, vp, vw, vh
from scene import Scene
from states import PlayingState
from utils import action_name, overlay_name


class PlayingScene(Scene):
    def resize_images(self):
        self.card_image = pygame.transform.smoothscale(self.card_image, vp(110, 176))
        pass

    def initialize_elements(self):
        view_current_card = UIButton(
            relative_rect=pygame.Rect((vw(673), vh(247)), vp(110, 176)),
            text="",
            manager=self.gui_manager,
            object_id=ObjectID(object_id=f"button_b_1", class_id="@main_menu_below_btns")
        )
        view_current_card.drawable_shape.states['normal'].surface.blit(self.card_image, (0, 0))
        view_current_card.drawable_shape.active_state.has_fresh_surface = True

    def __init__(self, screen, gui_manager):
        super().__init__(screen, gui_manager)
        self.state = PlayingState()

        self.card_image = pygame.image.load("assets/card.png")
        self.resize_images()
        self.initialize_elements()

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            key_event = event.key
            action = KEYBOARD_MAP[key_event]
            if action == action_name.PAUSE:
                self.state.active_overlay(overlay_name.CONFIGURATION)

    def draw(self):
        self.screen.fill((141, 168, 104))
        # Add your game drawing code here
        self.gui_manager.draw_ui(self.screen)
