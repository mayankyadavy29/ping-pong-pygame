from config import *

class Ball:
    def __init__(self, main, x, y, vel_x, vel_y):
        self.main = main
        self.x = x
        self.y = y
        self.vel = pg.Vector2(vel_x, vel_y)
        self.color = "white"
        self.rect = pg.Rect(x, y, BALL_DIAM, BALL_DIAM)

    def update(self):
        # collide with computer
        if self.main.computer.rect.colliderect(self.rect):
            self.vel.x *= -1
        # collide with boundary
        if self.main.top_boundary.rect.colliderect(self.rect) or self.main.bottom_boundary.rect.colliderect(self.rect):
            self.vel.y *= -1
        # collide with user
        if self.main.user.rect.colliderect(self.rect):
            self.vel.x *= -1
        elif self.rect.right > BALL_MAX_RIGHT:
            self.main.game_over = True

        self.rect = self.rect.move(self.vel)

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect, 0, BALL_DIAM//2)