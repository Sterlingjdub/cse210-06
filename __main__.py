import os
import random
from constants import *
from game.casting.actor import Actor
from game.casting.alien import Alien
from game.casting.hero import Hero
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Space Invaders Vol 0.1"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ALIENS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # score
    score = Score()
    score.set_text("")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(10, 5))
    cast.add_actor("scores", score)

    # create the banner
    banner = Actor()
    banner.set_text(f"{score}")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the hero
    x = int(MAX_X / 2)
    y = int(1000)
    position = Point(x, y)

    hero = Actor()
    hero.set_text("{^}")
    hero.set_font_size(FONT_SIZE)
    hero.set_color(WHITE)
    hero.set_position(position)
    cast.add_actor("heros", hero)
    
    # create the aliens
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_ALIENS):
        text = random.choice(["*","x"])
        message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, (ROWS))
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        alien = Alien()
        alien.set_text(text)
        alien.set_font_size(FONT_SIZE)
        alien.set_color(color)
        alien.set_position(position)
        alien.set_message(message)
        if(text=="*"):
            cast.add_actor("alien", alien)
        else:
            cast.add_actor("rock", alien)
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()