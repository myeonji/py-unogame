from abc import abstractmethod

import pygame
import pygame_gui

from assets import image_keys
from assets.image_loader import ImageLoader
from config import vp, SCREEN_HEIGHT, SCREEN_WIDTH, vw, vh
from scene import Scene


class OverlayScene(Scene):
    def __init__(self, screen, overlay_manager):#, image_loader:ImageLoader):

        super().__init__(screen, overlay_manager)#, image_loader)
        self.screen = screen
        self.close_button = None
        self.overlay_manager = overlay_manager
        self.active = False
        self.state = None
        #self.overlay_bg_image = image_loader.get_image(image_keys.IMG_CONFIG_OVERLAY_BG)

        self.overlay_surface = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.SRCALPHA)
        self.overlay_surface.fill((0, 0, 0, 128))  # RGBA: (0, 0, 0, 128) gives a 50% transparent black overlay
        self.panel = None

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False
        self.overlay_manager.clear_and_reset()

    def process_events(self, event):
        if self.active:
            if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.close_button:
                    self.set_inactive()

            self.overlay_manager.process_events(event)

    def update(self, time_delta):
        if self.active:
            self.overlay_manager.update(time_delta)

    def draw(self):
        if self.active:
            self.screen.blit(self.overlay_surface, (0, 0))
            self.overlay_manager.draw_ui(self.screen)
