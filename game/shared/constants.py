import os
from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Space Invaders Vol 0.1"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
GREEN = Color (124,252,0)
DEFAULT_ARTIFACTS = 3
