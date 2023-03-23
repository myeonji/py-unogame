class ConfigurationState:
    def __init__(self):
        self.changed = False
        self.return_to_main_menu = False

    def back_to_main_menu(self):
        self.return_to_main_menu = True
        self.changed = True
