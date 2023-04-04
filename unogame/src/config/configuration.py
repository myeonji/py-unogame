# Screen dimensions
from utils import blind_mode_name
import pygame
import json

from utils import action_name

BLIND_MODE = blind_mode_name.DEFAULT
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

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

def vw(width):
    return (width * SCREEN_WIDTH) / 1280


def vh(height):
    return (height * SCREEN_HEIGHT) / 720


def vp(width, height):
    return vw(width), vh(height)

def get_action(key):
    try:
        return KEYBOARD_MAP[key]
    except KeyError:
        return None

def save_config_to_file():
    keybindings = {key: action for key, action in KEYBOARD_MAP.items()}
    configurations = {
        "BLIND_MODE" : BLIND_MODE,
        "SCREEN_HEIGHT" : SCREEN_HEIGHT,
        "SCREEN_WIDTH" : SCREEN_WIDTH,
        "keybinding" : keybindings
    }
    with open("config.json", "w") as f:
        json.dump(configurations, f)


def load_config_from_file():
    with open("config.json", "r") as f:
        configurations = json.load(f)
        print(configurations)
#return {int(key): action for key, action in keybindings.items()}