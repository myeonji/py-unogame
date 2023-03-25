from utils import scene_name, overlay_name
from scene import MenuScene,LandingScene,PlayingScene,ConfigurationOverlayScene


class SceneManager:
    _instance = None

    def __init__(self, screen, gui_manager, overlay_manager):
        if SceneManager._instance is not None:
            raise Exception("SceneManager should be a singleton class.")
        SceneManager._instance = self
        self.screen = screen
        self.gui_manager = gui_manager
        self.overlay_manager = overlay_manager
        self.overlay = ConfigurationOverlayScene(screen, overlay_manager)

        self.scenes = {
            scene_name.LANDING: LandingScene,
            scene_name.MAIN_MENU: MenuScene,
            scene_name.PLAYING_GAME: PlayingScene
        }
        self.overlay_scenes = {
            overlay_name.CONFIGURATION: ConfigurationOverlayScene
        }
        self.current_scene = self.scenes[scene_name.MAIN_MENU](screen, gui_manager)

    def update(self):
        if self.current_scene.state.scene_changed:
            self.current_scene.state.scene_changed = False
            self.current_scene = self.scenes[self.current_scene.state.next_scene_name](self.screen, self.gui_manager)
            print("Current Scene! :", self.current_scene)
        if self.current_scene.state.overlay_active_changed:
            self.current_scene.state.overlay_active_changed = False
            self.overlay = self.overlay_scenes[self.current_scene.state.overlay_scene_name](self.screen, self.overlay_manager)
            self.overlay.set_active()

    def process_events(self, event):
        self.current_scene.process_events(event)
        self.gui_manager.process_events(event)
        self.overlay.process_events(event)

    def draw(self):
        self.current_scene.draw()
        self.overlay.draw()