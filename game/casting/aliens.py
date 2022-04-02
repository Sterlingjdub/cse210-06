from game.casting.actor import Actor


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