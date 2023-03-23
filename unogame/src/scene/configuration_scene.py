import pygame
import pygame_gui

from scene import Scene
from states import ConfigurationState


class ConfigurationScene(Scene):
    def __init__(self, screen, gui_manager):
        super().__init__(screen, gui_manager)
        self.configuration_state = ConfigurationState()
        self.create_ui_elements()

    def create_ui_elements(self):
        self.color_blind_mode_checkbox = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 200), (150, 40)),
            text="Color Blind Mode",
            manager=self.gui_manager
        )
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 250), (100, 40)),
            text="Back",
            manager=self.gui_manager
        )

    def process_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.back_button:
                    self.configuration_state.back_to_main_menu()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.gui_manager.draw_ui(self.screen)