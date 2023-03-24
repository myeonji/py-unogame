from utils import scene_name
from scene import MenuScene,LandingScene,PlayingScene,ConfigurationScene


class SceneManager:
    _instance = None

    def __init__(self, screen, gui_manager):
        if SceneManager._instance is not None:
            raise Exception("SceneManager should be a singleton class.")
        SceneManager._instance = self
        self.screen = screen
        self.gui_manager = gui_manager

        self.scenes = {
            scene_name.LANDING: LandingScene,
            scene_name.MAIN_MENU: MenuScene,
            scene_name.PLAYING_GAME: PlayingScene,
            scene_name.CONFIGURATION: ConfigurationScene,
        }
        self.current_scene = self.scenes[scene_name.LANDING](screen, gui_manager)

    def update(self):
        if self.current_scene.state.changed:
            self.current_scene.state.changed = False
            self.current_scene = self.scenes[self.current_scene.state.next_scene_name](self.screen, self.gui_manager)
            print("Current Scene! :", self.current_scene)

    def process_events(self, event):
        self.current_scene.process_events(event)
        self.gui_manager.process_events(event)

    def draw(self):
        self.current_scene.draw()