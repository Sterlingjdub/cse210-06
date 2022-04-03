from audioop import alaw2lin
from game.handlers.score_handler import Score_handler
from game.casting.actor import Actor
from game.casting.rocket import Rocket
from game.casting.boss import Boss
from game.shared.color import Color
from game.shared.point import Point
from constants import *

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
        self.score = Score_handler()
        self.level = 1
        
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
        aliens.extend(cast.get_actors("boss")) # Union of class aliens and rocks
        velocity = self._keyboard_service.get_direction()
        
        #Manejo del la bala (Rocket)
        rocket = self._keyboard_service.create_rocket()
        if(rocket):
            rocket = Rocket()
            rocket.set_text("^")
            rocket.set_font_size(20)
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
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()

        banner = cast.get_first_actor("banners")
        hero = cast.get_first_actor("heros")
        aliens = cast.get_actors("alien")
        bullets = cast.get_actors("rockets")

        if(int(self.score.get_score()) >= 30):
                boss = cast.get_actors("boss")
                if(boss != []):
                    cast.remove_actor("boss",boss[0])
                    for alien in aliens:
                        cast.remove_actor("alien",alien)         
                banner = cast.get_first_actor("banners")
                banner.set_text("Score:"+self.score.get_score()+"  !!YOU WIN!!")
                self.level = 0
                for n in range(5):
                    text = "*"
                    x = random.randint(1, COLS - 1)
                    y = random.randint(1, ROWS - 1)
                    position = Point(x, y)
                    position = position.scale(CELL_SIZE)

                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                    color = Color(r, g, b)
                    
                    artifact = Actor()
                    artifact.set_text(text)
                    artifact.set_font_size(FONT_SIZE)
                    artifact.set_color(color)
                    artifact.set_position(position)
                    cast.add_actor("artifacts", artifact)
        else:
            if(int(self.score.get_score()) == 10 and self.level == 1):
                    self.level = self.level+1
                    boss = Boss()
                    cast.add_actor("boss", boss)
                    banner = cast.get_first_actor("banners")
                    banner.set_text("LEVEL 2")

            if (self.level == 0):
                banner.set_text("Score:"+self.score.get_score())
                hero.move_next(max_x, max_y)
                alien_velocity = self._keyboard_service.get_alien_direction()      
                artifacts = cast.get_actors("artifact")
                for r in artifacts:
                    r.set_velocity(alien_velocity)
                    r.move_next(max_x,max_y)     

            if(self.level ==1):

                banner.set_text("Score:"+self.score.get_score())
                hero.move_next(max_x, max_y)
                
                # For each rocket, if its position is equals to the position of a rock or a gem
                #both rocket and alien disapears
                for rocket in bullets:
                    if(rocket.get_position().get_y() > 580):
                        cast.remove_actor("rockets",rocket)
                    else:
                        for alien in aliens:
                            if rocket.get_position().equals(alien.get_position()):
                                self.score.increase_score(alien.value)
                                alien.change_position()  
                                cast.remove_actor("rockets",rocket)         
                                break  
                
            if(self.level ==2):
                banner = cast.get_first_actor("banners")
                hero = cast.get_first_actor("heros")
                banner.set_text("Score:"+self.score.get_score())
                hero.move_next(max_x, max_y)

                
                bullets = cast.get_actors("rockets")
                boss = cast.get_actors("boss")

                for rocket in bullets:
                    if(rocket.get_position().get_y() > 580):
                        cast.remove_actor("rockets",rocket)
                    else:
                        for alien in boss:
                            if (rocket.get_position().equals(alien.get_position())):
                                self.score.increase_score(alien.value) 
                                cast.remove_actor("rockets",rocket)         
                                break  
            

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            hero = cast.get_first_actor("hero")
            aliens = cast.get_first_actor("aliens")

            x = int(MAX_X / 2)
            y = int(MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for alien in aliens:
                alien.set_color(WHITE)
            hero.set_color(WHITE)