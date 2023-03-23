import pygame
import pygame_gui

from .scene import Scene
from states import MenuState


class MenuScene(Scene):

    def __init__(self, screen, gui_manager):
        super().__init__(screen, gui_manager)
        self.state = MenuState()
        self.logo_image = pygame.image.load("assets/logo.png")
        self.initialize_buttons()

    def initialize_buttons(self):
        self.single_play_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 225), (100, 50)),
            text="Single Play",
            manager=self.gui_manager
        )
        self.configuration_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 300), (100, 50)),
            text="Configuration",
            manager=self.gui_manager
        )
        self.exit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 375), (100, 50)),
            text="Exit",
            manager=self.gui_manager
        )
        self.sound_toggle_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((750, 550), (40, 40)),
            text="Sound",
            manager=self.gui_manager
        )

    def process_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.single_play_button:
                    self.state.start_single_play()
                elif event.ui_element == self.configuration_button:
                    self.state.open_configuration()
                elif event.ui_element == self.exit_button:
                    self.state.exit()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.logo_image, (250, 100))
        self.gui_manager.draw_ui(self.screen)