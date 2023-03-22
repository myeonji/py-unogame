class PlayingState:
    def __init__(self):
        self.changed = False
        self.game_over = False
        self.return_to_main_menu = False

    def end_game(self):
        self.game_over = True
        self.changed = True

    def back_to_main_menu(self):
        self.return_to_main_menu = True
        self.changed = True
