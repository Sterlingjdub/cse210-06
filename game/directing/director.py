from game.casting.artifact import Artifact
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
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("gem")
        artifacts.extend(cast.get_actors("rock"))
        velocity = self._keyboard_service.get_direction()
        

        #Manejo del la bala (Rocket)
        rocket = self._keyboard_service.create_rocket()
        if(rocket):
            artifact = Artifact()
            artifact.set_text("^")
            artifact.set_font_size(15)
            artifact.set_color(Color(128, 0, 128))
            artifact.set_position(robot.get_position())
            cast.add_actor("rockets", artifact)

        robot.set_velocity(velocity)        
        artifact_velocity = self._keyboard_service.get_artifact_direction()
        
        rockets = robot = cast.get_actors("rockets")
        velocity_rocket = self._keyboard_service.get_rocket_direction()

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()

        for rock in artifacts:
            rock.set_velocity(artifact_velocity)
            rock.move_next(max_x,max_y)

        for r in rockets:
            r.set_velocity(velocity_rocket)
            r.move_next(max_x,max_y)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("gem")
        rocks = cast.get_actors("rock")
        bullets = cast.get_actors("rockets")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        # For each rocket, if its position is equals to the position of a rock or a gem
        #both rocket and artifact disapears
        for rocket in bullets:
            if(rocket.get_position().get_y() > 400):
                cast.remove_actor("rockets",rocket)  
            else:
                for artifact in artifacts:
                    if rocket.get_position().equals(artifact.get_position()):
                        cast.remove_actor("gem",artifact)  
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