import pygame
import sys
from pygame.locals import *

import pygame_gui

from utils import SceneManager
from config import SCREEN_WIDTH, SCREEN_HEIGHT, vw, vh
from assets.image_loader import ImageLoader

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("UnoCatMe")

# Set up the GUI manager
gui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), "theme.json")
gui_manager.set_visual_debug_mode(True)

overlay_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), "theme.json")
overlay_manager.set_visual_debug_mode(True)

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

image_loader = ImageLoader()
# Create a SceneManager instance
scene_manager = SceneManager(screen, gui_manager, overlay_manager, image_loader)

while True:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        scene_manager.process_events(event)

    gui_manager.update(time_delta)
    overlay_manager.update(time_delta)
    scene_manager.update()

    scene_manager.draw()
    pygame.display.flip()

#pygame.quit()