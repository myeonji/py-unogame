class GameState:
    def __init__(self):
        self.changed = False
        self.next_scene_name = None

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def move_scene(self, next_scene_name):
        self.changed = True
        self.next_scene_name = next_scene_name
