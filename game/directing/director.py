from game.casting.alien import Alien
from game.casting.rocket import Rocket
from game.shared.color import Color

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the hero.
        
        Args:
            cast (Cast): The cast of actors.
        """
        # Get current actors.
        hero = cast.get_first_actor("heros")
        aliens = cast.get_actors("alien")
        aliens.extend(cast.get_actors("rock")) # Union of class aliens and rocks
        velocity = self._keyboard_service.get_direction()
        

        #Manejo del la bala (Rocket)
        rocket = self._keyboard_service.create_rocket()
        if(rocket):
            rocket = Rocket()
            rocket.set_text("^")
            rocket.set_font_size(15)
            rocket.set_color(Color(128, 0, 128))
            rocket.set_position(hero.get_position())
            cast.add_actor("rockets", rocket)

        hero.set_velocity(velocity)        
        alien_velocity = self._keyboard_service.get_alien_direction()
        
        rockets = hero = cast.get_actors("rockets")
        velocity_rocket = self._keyboard_service.get_rocket_direction()

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()

        for r in rockets:
            r.set_velocity(velocity_rocket)
            r.move_next(max_x,max_y)

        for rock in aliens:
            rock.set_velocity(alien_velocity)
            rock.move_next(max_x,max_y)

        

    def _do_updates(self, cast):
        """Updates the hero's position and resolves any collisions with aliens.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        hero = cast.get_first_actor("heros")
        aliens = cast.get_actors("alien")
        rocks = cast.get_actors("rock")
        bullets = cast.get_actors("rockets")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        hero.move_next(max_x, max_y)
        
        # For each rocket, if its position is equals to the position of a rock or a gem
        #both rocket and alien disapears
        for rocket in bullets:
            if(rocket.get_position().get_y() > 580):
                cast.remove_actor("rockets",rocket)  
            else:
                for alien in aliens:
                    if rocket.get_position().equals(alien.get_position()):
                        cast.remove_actor("alien",alien)  
                        cast.remove_actor("rockets",rocket)  

                for rock in rocks:
                    if rocket.get_position().equals(rock.get_position()):
                        cast.remove_actor("rock",rock)  
                        cast.remove_actor("rockets",rocket)
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()