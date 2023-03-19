class GameState:
    def __init__(self):
        self.scene = None

    def set_scene(self, scene):
        self.scene = scene

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen, *args):
        if self.scene:
            self.scene.draw(screen)
