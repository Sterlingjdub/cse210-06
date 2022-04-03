from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
import random
from game.shared.constants import *

class Rock(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Alien is to provide a message about itself.

    Attributes:
        _message (string): A short description about the alien.
    """
    def __init__(self):
        super().__init__()
        self._message = "GAME OVER"
        
        self.set_text("X")
        self.set_font_size(20)
        self.set_color(Color(124,252,0))
        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        self.set_position(position)

    def get_message(self):
        """Gets the alien's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def set_velocity(self, velocity):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._velocity = velocity
