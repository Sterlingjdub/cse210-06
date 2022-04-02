from game.shared.color import Color
import random

# GAME CONSTANTS
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
ALIEN_SIZE = 40
COLS = 60
ROWS = 40
CAPTION = "Space Invaders Vol 0.1"
WHITE = Color(255, 255, 255)
DEFAULT_ALIENS = 5

# IMAGES FOR HERO & ALIENS
HERO_IMAGE = "assets/images/01.png"
ALIEN_IMAGES = {
    "blue": ["game/assets/images/05.png"],
    "green": ["game/assets/images/02.png"],
    "pink": ["game/assets/images/03.png"],
    "red": ["game/assets/images/04.png"]
}
