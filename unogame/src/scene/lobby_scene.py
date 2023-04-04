import pygame
import pygame_gui
from pygame_gui.core import ObjectID

from config import SCREEN_WIDTH, SCREEN_HEIGHT, vw, vh, vp, KEYBOARD_MAP
from scene import Scene
from states.lobby_state import LobbyState
from utils import action_name, overlay_name
from widgets import FocusableUIButton


class LobbyScene(Scene):
    def initialize_elements(self):
        self.create_below_buttons()
        self.create_add_buttons()

    def __init__(self, screen, gui_manager):
        super().__init__(screen, gui_manager)
        self.state = LobbyState()

        self.lobby_image = pygame.image.load("assets/lobby_img/lobby_bg.png")
        self.btn_left = pygame.image.load("assets/lobby_img/btn_left.png")
        self.btn_right = pygame.image.load("assets/lobby_img/btn_right.png")
        self.player_bg = pygame.image.load("assets/lobby_img/player_bg.png")
        self.other_player_bg = pygame.image.load("assets/lobby_img/other_player_bg.png")
        self.add_player_bg = pygame.image.load("assets/lobby_img/add_player_bg.png")

        self.add_button_width = vw(512)
        self.add_button_height = vh(90)
        self.add_button_margin = vh(15)

        self.add_buttons_text = ["player1", "player2", "player3", "player14"]

        self.add_player_buttons = []

        self.resize_images()
        self.initialize_elements()

    def resize_images(self):
        super().resize_images()
        self.lobby_image = pygame.transform.scale(self.lobby_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.btn_left = pygame.transform.scale(self.btn_left, vp(64.95, 57))
        self.btn_right = pygame.transform.scale(self.btn_right, vp(64.95, 57))
        self.player_bg = pygame.transform.scale(self.player_bg, vp(338, 502))
        self.other_player_bg = pygame.transform.scale(self.other_player_bg, vp(512, 90))
        self.add_player_bg = pygame.transform.scale(self.add_player_bg, vp(512, 90))

    def create_below_buttons(self):
        btn_left = FocusableUIButton(
            relative_rect=pygame.Rect((vw(50), SCREEN_HEIGHT - 100), vp(64.95, 57)),
            text="",
            manager=self.gui_manager,
            object_id=ObjectID(object_id=f"button_b_1", class_id="@lobby_below_btns")
        )
        btn_right = FocusableUIButton(
            relative_rect=pygame.Rect((SCREEN_WIDTH-100, SCREEN_HEIGHT - 100), vp(64.95, 57)),
            text="",
            manager=self.gui_manager,
            object_id=ObjectID(object_id=f"button_b_2", class_id="@lobby_below_btns")

        )
        btn_left.drawable_shape.states['normal'].surface.blit(self.btn_left, (0, 0))
        btn_right.drawable_shape.states['normal'].surface.blit(self.btn_right, (0, 0))
        btn_left.drawable_shape.active_state.has_fresh_surface = True
        btn_right.drawable_shape.active_state.has_fresh_surface = True
        self.focusable_buttons.extend([btn_left, btn_right])

    def create_add_buttons(self):
        for i in range(len(self.add_buttons_text)):
            x = 0
            y = i * self.add_button_height + (i+1) * self.add_button_margin + vh(212 - self.add_button_margin)
            btn_add = FocusableUIButton(
                relative_rect=pygame.Rect(x + SCREEN_WIDTH / 2 - vw(50), y, self.add_button_width, self.add_button_height ),
                text=self.add_buttons_text[i],
                manager=self.gui_manager,
                object_id=ObjectID(object_id=f"button_", class_id="@lobby_player_btns")
            )
            btn_add.drawable_shape.states['normal'].surface.blit(self.add_player_bg, (0, 0))
            btn_add.drawable_shape.active_state.has_fresh_surface = True
            self.focusable_buttons.append(btn_add)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            key_event = event.key
            action = KEYBOARD_MAP[key_event]
            if action == action_name.RETURN:
                self.state.start_single_play()
            if action == action_name.PAUSE:
                self.state.active_overlay(overlay_name.CONFIGURATION)

    def draw(self):
        self.screen.blit(self.lobby_image, (0, 0))
        self.screen.blit(self.player_bg, vp(172, 109))
        self.screen.blit(self.other_player_bg, vp(SCREEN_WIDTH / 2 - vw(50), vh(100 + 9)))

        self.gui_manager.draw_ui(self.screen)