import os
import random
from constants import *
from game.casting.actor import Actor
from game.casting.aliens import Aliens
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

def main():
    
    # create the cast
    cast = Cast()
    
    # score
    score = Score()

    # create the banner
    banner = Actor()
    banner.set_text(f"{score}")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # hero's postition
    x = int(MAX_X / 2)
    y = int(1000)
    position = Point(x, y)

    # create the hero
    hero = Actor()
    hero.set_text("_")
    hero.set_font_size(40)
    hero.set_position(position)
    hero.set_color(WHITE)
    cast.add_actor("hero", hero)
    
    # creation of aliens
    for n in range(DEFAULT_ALIENS):
        text = "*"
        
        x = random.randint(1, COLS - 1)
        y = random.randint(1, (ROWS))
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        aliens = Aliens()
        aliens.set_text(text)
        aliens.set_font_size(FONT_SIZE)
        aliens.set_color(color)
        aliens.set_position(position)
        cast.add_actor("aliens", aliens)
        
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()