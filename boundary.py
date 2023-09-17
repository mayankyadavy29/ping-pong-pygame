from config import *

class Boundary:
    def __init__(self, x, y):
        self.color = "white"
        self.rect = pg.Rect(x, y, BOUND_WIDTH, BOUND_HEIGHT)

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)