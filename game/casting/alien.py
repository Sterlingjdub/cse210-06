from game.casting.actor import Actor


class Alien(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Alien is to provide a message about itself.

    Attributes:
        _message (string): A short description about the alien.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
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
