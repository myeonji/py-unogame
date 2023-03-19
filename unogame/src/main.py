import pygame
import sys
from states import LandingState, MenuState, PlayingState
from config import SCREEN_WIDTH, SCREEN_HEIGHT

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Unocatme")

# Create instances of the game states
state_mapping = {
    "LANDING": LandingState(),
    "MENU": MenuState(),
    "PLAYING": PlayingState()
}

# Set the initial states
current_state = state_mapping["LANDING"]

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))

    # Process events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Update the current states
    next_state_name, args = current_state.handle_events(events)
    if next_state_name:
        current_state = state_mapping[next_state_name]
        current_state.reset(*args)

    current_state.update()

    # Draw the current states
    current_state.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
