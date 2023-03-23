
class Scene:

    def __init__(self, screen, gui_manager):
        self.screen = screen
        self.gui_manager = gui_manager
        self.state = None
        self.gui_manager.clear_and_reset()
        pass

    def draw(self):
        pass


