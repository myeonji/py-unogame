import pygame
import json

from utils import action_name

KEYBOARD_MAP = {
    pygame.K_UP: action_name.MOVE_UP,
    pygame.K_DOWN: action_name.MOVE_DOWN,
    pygame.K_LEFT: action_name.MOVE_LEFT,
    pygame.K_RIGHT: action_name.MOVE_RIGHT,
    pygame.K_SPACE: action_name.FIRE,
    pygame.K_ESCAPE: action_name.PAUSE,
    pygame.K_RETURN: action_name.RETURN
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
