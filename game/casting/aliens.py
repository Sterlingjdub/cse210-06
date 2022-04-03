from game.shared.point import Point
from game.casting.actor import Actor
from game.shared.color import Color
import random
from game.shared.constants import *

class Aliens(Actor):
    """
    Aliens are invaders from space. 
    
    The responsibility of an Alien is to make it to make it to Earth unharmed by the Hero.

    Attributes:
        _points (int): A value of the Alien.
    """
    def __init__(self):
        super().__init__()

        self._points = 0
        self.value = 1

        self.set_text("X")
        self.set_font_size(20)
        self.set_color(GREEN)
        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        self.set_position(position)

    def get_points(self):
        """Gets the aliens point value.
        
        Returns:
            points (int): The point value.
        """
        return self._points

    def set_points(self, points):
        """Updates the points to the given one.
        
        Args:
            points (int): The given point value.
        """
        self._points = points

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (string): The given velocity.
        """
        self._velocity = velocity

    def get_text(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._text

    def set_text(self, text): 
        """Assigns points based on artifact type (rock or gem).
        
        Returns:
            _points (int): the appropriate number of points for the 
            given artifact type.
        """
        self._text = text

    def change_position(self):        
        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        self.set_position(position)