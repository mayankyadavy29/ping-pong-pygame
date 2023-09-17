from config import *

class Board:
    def __init__(self, main, x, y, vel):
        self.vel = pg.Vector2(0, vel)
        self.rect = pg.Rect(x, y, BOARD_WIDTH, BOARD_HEIGHT)
        self.color = "white"
        self.main = main

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)

class Computer(Board):
    def __init__(self, main, x, y, vel):
        super().__init__(main, x, y, vel)

    def update(self):
        temp_rect = pg.Rect(self.rect)
        temp_rect.center = self.main.ball.rect.center
        temp_rect.x = 0
        if (temp_rect.top >= self.main.top_boundary.rect.bottom) and (temp_rect.bottom <= self.main.bottom_boundary.rect.top):
            self.rect = temp_rect

class User(Board):
    def __init__(self, main, x, y, vel):
        super().__init__(main, x, y, vel)

    def update(self):
        if (self.rect.y + self.vel.y >= self.main.top_boundary.rect.bottom) and \
                (self.rect.y + self.vel.y + BOARD_HEIGHT <= self.main.bottom_boundary.rect.top):
            self.rect.y += self.vel.y