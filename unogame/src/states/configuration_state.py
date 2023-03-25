from states import GameState
from utils import scene_name


class ConfigurationState(GameState):
    def __init__(self):
        super().__init__()

    def back_to_main_menu(self):
        self.move_scene(scene_name.MAIN_MENU)
