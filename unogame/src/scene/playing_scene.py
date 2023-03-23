from scene import Scene
from states import PlayingState


class PlayingScene(Scene):
    def __init__(self, screen, gui_manager):
        super().__init__(screen, gui_manager)
        self.state = PlayingState()
        # Add your UI elements and game logic here

    def process_events(self, event):
        # Add your event handling code here
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        # Add your game drawing code here
        self.gui_manager.draw_ui(self.screen)
