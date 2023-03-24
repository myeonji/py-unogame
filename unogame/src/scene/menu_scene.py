import pygame
import pygame_gui
from pygame_gui.core import ObjectID

from config import SCREEN_WIDTH, SCREEN_HEIGHT, vw, vh, vp
from states import MenuState
from widgets import ScrollableUIButton, FocusableUIButton
from .scene import Scene


class MenuScene(Scene):
    def __init__(self, screen, gui_manager):
        super().__init__(screen, gui_manager)

        self.main_bg_image = None
        self.sound_toggle_button = None
        self.state = MenuState()
        self.current_focused_button = -1

        self.main_image = pygame.image.load("assets/main_bg.png")
        self.logo_image = pygame.image.load("assets/logo.png")
        self.btn_image = pygame.image.load("assets/menu_btn.png")
        self.btn_exit = pygame.image.load("assets/btn_exit.png")
        self.btn_ranking = pygame.image.load("assets/btn_ranking.png")
        self.btn_setting = pygame.image.load("assets/btn_setting.png")

        self.scrollable_area_rect = pygame.Rect(vw(0), vh(16), SCREEN_WIDTH, vh(75))
        self.scrollable_button_width = vw(20)
        self.scrollable_button_height = vh(50)
        self.scrollable_button_margin = vw(4)
        self.scrollable_container = pygame_gui.elements.UIScrollingContainer(
            relative_rect=self.scrollable_area_rect,
            manager=self.gui_manager
        )

        self.scroll_buttons_text = ["Single Play", "Configuration", "Exit", "Test2", "Test3"]

        self.scrollable_buttons = []
        self.scroll_offset_x = 0
        self.target_scroll_offset_x = 0
        self.scroll_speed = 0.2

        self.initialize_images()
        self.create_scrollable_buttons()
        self.create_below_buttons()

    def initialize_images(self):
        self.main_image = pygame.transform.scale(self.main_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.logo_image = pygame.transform.scale(self.logo_image, vp(20, 14))
        self.btn_image = pygame.transform.scale(self.btn_image, vp(20, 50))
        self.btn_exit = pygame.transform.scale(self.btn_exit, vp(8.6, 15.2))
        self.btn_ranking = pygame.transform.scale(self.btn_ranking, vp(8.6, 15.2))
        self.btn_setting = pygame.transform.scale(self.btn_setting, vp(8.6, 15.2))

    def create_scrollable_buttons(self):
        for i in range(len(self.scroll_buttons_text)):
            x = i * self.scrollable_button_width + (i + 1) * self.scrollable_button_margin
            y = self.scrollable_button_margin
            button_rect = pygame.Rect(x, y, self.scrollable_button_width, self.scrollable_button_height)
            btn = ScrollableUIButton(
                relative_rect=button_rect,
                text=self.scroll_buttons_text[i],
                manager=self.gui_manager,
                container=self.scrollable_container,
                object_id=ObjectID(object_id=f"button_{i + 1}", class_id="@main_menu_btns")
            )
            btn.drawable_shape.states['normal'].surface.blit(self.btn_image, (0, 0))
            btn.drawable_shape.active_state.has_fresh_surface = True
            self.scrollable_buttons.append(btn)
            self.focusable_buttons.append(btn)

    def create_below_buttons(self):
        btn_setting = FocusableUIButton(
            relative_rect=pygame.Rect(( (SCREEN_WIDTH - vw(8.6)) / 2 - vw(12), SCREEN_HEIGHT - vh(22)), vp(8.6, 15.2)),
            text="",
            manager=self.gui_manager,
            object_id=ObjectID(object_id=f"button_b_1", class_id="@main_menu_below_btns")
        )
        btn_ranking = FocusableUIButton(
            relative_rect=pygame.Rect(( (SCREEN_WIDTH - vw(8.6)) / 2, SCREEN_HEIGHT - vh(22)), vp(8.6, 15.2)),
            text="",
            manager=self.gui_manager,
            object_id=ObjectID(object_id=f"button_b_2", class_id="@main_menu_below_btns")

        )
        btn_exit = FocusableUIButton(
            relative_rect=pygame.Rect(( (SCREEN_WIDTH - vw(8.6)) / 2 + vw(12), SCREEN_HEIGHT - vh(22)), vp(8.6, 15.2)),
            text="",
            manager=self.gui_manager,
            object_id=ObjectID(object_id=f"button_b_3", class_id="@main_menu_below_btns")
        )
        btn_setting.drawable_shape.states['normal'].surface.blit(self.btn_setting, (0, 0))
        btn_ranking.drawable_shape.states['normal'].surface.blit(self.btn_ranking, (0, 0))
        btn_exit.drawable_shape.states['normal'].surface.blit(self.btn_exit, (0, 0))
        btn_setting.drawable_shape.active_state.has_fresh_surface = True
        btn_ranking.drawable_shape.active_state.has_fresh_surface = True
        btn_exit.drawable_shape.active_state.has_fresh_surface = True
        self.focusable_buttons.extend([btn_setting,btn_ranking,btn_exit])

    def process_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Mouse wheel up
                self.target_scroll_offset_x += vw(5)
            elif event.button == 5:  # Mouse wheel down
                self.target_scroll_offset_x -= vw(5)

            # Prevent scrolling beyond content
            self.target_scroll_offset_x = min(self.target_scroll_offset_x, vw(2))
            max_scroll = (len(self.scrollable_buttons) - 3.5) * (
                        self.scrollable_button_width + self.scrollable_button_margin) + self.scrollable_button_margin * 2
            self.target_scroll_offset_x = max(self.target_scroll_offset_x, -max_scroll)
            self.scroll_offset_x += (self.target_scroll_offset_x - self.scroll_offset_x) * self.scroll_speed

            for button in self.scrollable_buttons:
                button.set_position((button.starting_rect.x + self.scroll_offset_x, button.rect.y))
        key_event = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if key_event[pygame.K_LEFT] or key_event[pygame.K_UP]:
                self.current_focused_button = (self.current_focused_button - 1) % len(self.focusable_buttons)
                self.gui_manager.set_focus_set(self.focusable_buttons[self.current_focused_button])
                print(self.gui_manager.get_focus_set(), self.current_focused_button)

            if key_event[pygame.K_RIGHT] or key_event[pygame.K_DOWN]:
                self.current_focused_button = (self.current_focused_button + 1) % len(self.focusable_buttons)
                self.gui_manager.set_focus_set(self.focusable_buttons[self.current_focused_button])
                print(self.gui_manager.get_focus_set(), self.current_focused_button)
            # todo: 버튼 포커싱에 맞게 움직이도록 하기.
            if key_event[pygame.K_RETURN]:
                ui_element = self.focusable_buttons[self.current_focused_button]
                if ui_element == self.scrollable_buttons[0]:
                    self.state.start_single_play()
                elif ui_element == self.scrollable_buttons[1]:
                    self.state.open_configuration()
                elif ui_element == self.scrollable_buttons[2]:
                    self.state.exit()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                print(event.ui_element)
                if event.ui_element == self.scrollable_buttons[0]:
                    self.state.start_single_play()
                elif event.ui_element == self.scrollable_buttons[1]:
                    self.state.open_configuration()
                elif event.ui_element == self.scrollable_buttons[2]:
                    self.state.exit()

    def draw(self):
        self.screen.blit(self.main_image, (0, 0))
        self.screen.blit(self.logo_image, ((SCREEN_WIDTH - vw(20)) / 2, vh(5)))
        self.gui_manager.draw_ui(self.screen)
