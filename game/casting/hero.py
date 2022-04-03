from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.constants import *

class Hero(Actor):

    def __init__(self):
        super().__init__()
        # create the self
        x = int(MAX_X / 2)
        y = int(585)
        position = Point(x, y)
    
        self.set_text("W")
        self.set_font_size(FONT_SIZE)
        self.set_color(WHITE)
        self.set_position(position)