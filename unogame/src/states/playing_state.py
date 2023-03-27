from states import GameState


class PlayingState(GameState):
    def __init__(self):
        super().__init__()
        self.game_over = False

    def end_game(self):
        pass

    def back_to_main_menu(self):
        pass
