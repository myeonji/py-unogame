import constants as C

class Card:

    def __init__(self, text, color = C.DEF_CARD_BG, type = C.NUM_CARD):
        self.color = color
        self.text = text
        self.type = type