import sys

from config import *
from board import User, Computer
from ball import Ball
from boundary import Boundary

class Main:
    def __init__(self):
        self.top_boundary = Boundary(0, SCORECARD_HEIGHT)
        self.bottom_boundary = Boundary(0, HEIGHT - BOUND_HEIGHT)
        self.computer = Computer(self, 0, self.top_boundary.rect.bottom, BOARD_VEL)
        self.user = User(self, WIDTH-BOARD_WIDTH, (HEIGHT-BOARD_HEIGHT)//2, 0)
        self.ball = Ball(self, self.user.rect.midleft[0]-BALL_DIAM, self.user.rect.midleft[1], BALL_VEL, BALL_VEL)
        self.game_over = False
        self.score = 0

    def update(self):
        if not self.game_over:
            pass
            self.computer.update()
            self.user.update()
            self.ball.update()

    def draw(self):
        screen.fill("black")
        self.draw_header()
        self.top_boundary.draw()
        self.bottom_boundary.draw()
        if not self.game_over:
            self.computer.draw()
            self.user.draw()
            self.ball.draw()
        else:
            self.draw_game_over()

    def draw_header(self):
        score = pg.font.SysFont("comicsans", 20).render(f"Score: {self.score}", True, "white")
        score_rect = score.get_rect(midbottom=(WIDTH//2, self.top_boundary.rect.top - 5))
        screen.blit(score, score_rect)
        speed = pg.font.SysFont("comicsans", 20).render(f"Speed : {int(abs(self.ball.vel.x)+abs(self.ball.vel.y))//2}", True, "white")
        speed_rect = speed.get_rect(midright=(WIDTH-10, SCORECARD_HEIGHT//2))
        screen.blit(speed, speed_rect)

    def draw_game_over(self):
        restart = pg.font.SysFont("comicsans", 40).render("Click anywhere to restart", True, "white")
        restart_rect = restart.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(restart, restart_rect)


main = Main()
SCORE_EVENT = pg.USEREVENT + 1
BALL_SPEED = pg.USEREVENT + 2
pg.time.set_timer(SCORE_EVENT, 1000)
pg.time.set_timer(BALL_SPEED, 3*1000)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                main.user.vel = pg.Vector2(0, -BOARD_VEL)
            elif event.key == pg.K_s:
                main.user.vel = pg.Vector2(0, BOARD_VEL)
        if event.type == pg.KEYUP:
            main.user.vel = pg.Vector2(0, 0)
        if event.type == pg.MOUSEBUTTONDOWN:
            if main.game_over:
                main = Main()
        if event.type == SCORE_EVENT:
            if not main.game_over:
                main.score += 1
        if event.type == BALL_SPEED:
            if main.game_over:
                continue
            x_vel_inc, y_vel_inc = 1, 1
            if main.ball.vel.x < 0:
                x_vel_inc = -1
            if main.ball.vel.y < 0:
                y_vel_inc = -1
            main.ball.vel += pg.Vector2(x_vel_inc, y_vel_inc)
    main.update()
    main.draw()
    pg.display.update()
    clock.tick(60)
