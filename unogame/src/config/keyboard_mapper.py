import pygame
import json

KEYBOARD_MAP = {
    pygame.K_UP: "MOVE_UP",
    pygame.K_DOWN: "MOVE_DOWN",
    pygame.K_LEFT: "MOVE_LEFT",
    pygame.K_RIGHT: "MOVE_RIGHT",
    pygame.K_SPACE: "FIRE",
    pygame.K_ESCAPE: "PAUSE",
    # Add more key-action mappings here
}

def save_keybindings_to_file(filepath):
    keybindings = {key: action for key, action in KEYBOARD_MAP.items()}
    with open(filepath, "w") as f:
        json.dump(keybindings, f)


def load_keybindings_from_file(filepath):
    with open(filepath, "r") as f:
        keybindings = json.load(f)
    return {int(key): action for key, action in keybindings.items()}
