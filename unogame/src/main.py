import pygame
import sys
from pygame.locals import *

import pygame_gui

from utils import SceneManager
from config import SCREEN_WIDTH, SCREEN_HEIGHT, vw, vh

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("UnoCatMe")

# Set up the GUI manager
gui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), "theme.json")
gui_manager.set_visual_debug_mode(True)

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Create a SceneManager instance
scene_manager = SceneManager(screen, gui_manager)

while True:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        scene_manager.process_events(event)
        gui_manager.process_events(event)

    gui_manager.update(time_delta)
    scene_manager.update()

    scene_manager.draw()
    pygame.display.flip()

#pygame.quit()