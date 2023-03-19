from .state import GameState
from scene import MenuScene

class MenuState(GameState):
    def __init__(self):
        super().__init__()
        self.set_scene(MenuScene())

    def handle_events(self, events):
        for event in events:
            # Handle input to transition between states
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return "PLAYING", ()
                elif event.key == pygame.K_c:
                    return "CONFIGURATION", ()
                elif event.key == pygame.K_q:
                    sys.exit()
        return None, ()
