import pygame
import pygame_gui

from states import MenuState
from widgets import ScrollableUIButton
from .scene import Scene

from config import SCREEN_WIDTH, SCREEN_HEIGHT, vw, vh, vp


class MenuScene(Scene):
    def __init__(self, screen, gui_manager):
        super().__init__(screen, gui_manager)
        self.scroll_buttons = []
        self.state = MenuState()
        self.logo_image = pygame.image.load("assets/logo.png")

        self.scrollable_area_rect = pygame.Rect(vw(0), vh(16), SCREEN_WIDTH, vh(47))
        self.button_width = vw(24)
        self.button_height = vh(50)
        self.button_margin = vw(4)
        self.scrollable_container = pygame_gui.elements.UIScrollingContainer(
            relative_rect=self.scrollable_area_rect,
            manager=self.gui_manager
        )
        # self.scrollable_container.horiz_scroll_bar = pygame_gui.elements.UIHorizontalScrollBar(
        #     visible_percentage=50,
        #     relative_rect=pygame.Rect(vw(30), vh(30), vw(10), vh(10)),
        #     container=self.scrollable_container
        # )
        self.buttons = []
        self.scroll_offset_x = 0
        self.target_scroll_offset_x = 0
        self.scroll_speed = 0.2

        self.create_buttons()
        self.initialize_buttons()

    def create_buttons(self):
        self.scroll_buttons_text = ["Single Play", "Configuration", "Exit", "Test2", "Test3"]
        for i in range(len(self.scroll_buttons_text)):
            x = i * self.button_width + (i+1) * self.button_margin
            y = self.button_margin
            button_rect = pygame.Rect(x, y, self.button_width, self.button_height)
            self.buttons.append(ScrollableUIButton(
                relative_rect=button_rect,
                text=self.scroll_buttons_text[i],
                manager=self.gui_manager,
                container=self.scrollable_container,
                object_id=f"button_{i + 1}"
            ))

    def initialize_buttons(self):
        self.sound_toggle_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((SCREEN_WIDTH-vw(6), SCREEN_HEIGHT-vh(11)), vp(3,5)),
            text="Sound",
            manager=self.gui_manager
        )

    def process_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Mouse wheel up
                self.target_scroll_offset_x += vw(4)
            elif event.button == 5:  # Mouse wheel down
                self.target_scroll_offset_x -= vh(7)

            # Prevent scrolling beyond content
            self.target_scroll_offset_x = min(self.target_scroll_offset_x, vw(2))
            max_scroll = (len(self.buttons) - 3.5) * (self.button_width + self.button_margin) + self.button_margin * 2
            self.target_scroll_offset_x = max(self.target_scroll_offset_x, -max_scroll)
            self.scroll_offset_x += (self.target_scroll_offset_x - self.scroll_offset_x) * self.scroll_speed

            for button in self.buttons:
                button.set_position((button.starting_rect.x + self.scroll_offset_x, button.rect.y))

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                print(event.ui_element)
                if event.ui_element == self.buttons[0]:
                    self.state.start_single_play()
    #                elif event.ui_element == self.configuration_button:
    #                    self.state.open_configuration()
    #                elif event.ui_element == self.exit_button:
    #                    self.state.exit()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.logo_image = pygame.transform.scale(self.logo_image, vp(20,14))
        self.screen.blit(self.logo_image, ( (SCREEN_WIDTH - vw(20)) / 2 , vh(5)))
        self.gui_manager.draw_ui(self.screen)
