from game.shared.point import Point
from game.casting.aliens import Aliens
from game.shared.constants import *

class Boss(Aliens):
    """
    Aliens are invaders from space and they have a Boss. 
    
    The responsibility of an Alien is to make it to make it to Earth unharmed by the Hero.

    Attributes:
        _points (int): A value of the Alien.
    """
    def __init__(self):
        super().__init__()

        self._points = 20
        self.value = 4

        self.set_text("M")
        self.set_font_size(FONT_SIZE)
        self.set_color(RED)
        x = int(MAX_X/2)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        self.set_position(position)