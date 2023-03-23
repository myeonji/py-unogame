import pygame
import sys
from pygame.locals import *

import pygame_gui

from utils import SceneManager

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("UnoCatMe")

# Set up the GUI manager
gui_manager = pygame_gui.UIManager((800, 600))

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