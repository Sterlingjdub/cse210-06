from game.casting.aliens import Aliens


class Score(Aliens):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def add_points(self, aliens, hero):
        """Updates the message to the given one.
        
        Returns:
            _points (int): The updated score.
        """
        for alien in aliens:
            if hero.get_position().equals(alien.get_position()):
                if alien.get_text() == '\/':
                    points = 1
                alien.set_text("")
                self._points += points
        return self._points