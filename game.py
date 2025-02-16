# game.py

import pygame
import settings
from paddle import Paddle
from ball import Ball
from brick import Brick
from ui import draw_ui, draw_game_over

class Game:
    def __init__(self):
        self.paddle = Paddle()
        self.ball = Ball()
        self.reset()

    def reset(self):
        self.bricks = [Brick(x * settings.BRICK_WIDTH, y) for x in range(1, settings.BRICK_COLUMNS - 1)
                       for y in range(settings.BRICK_Y_START, settings.BRICK_Y_END, settings.BRICK_HEIGHT)]
        self.lives = settings.LIVES
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.paddle.move(keys)
        self.ball.move(self.paddle, self.bricks, self)

    def draw(self, screen):
        self.paddle.draw(screen)
        if self.lives > 0:
            self.ball.draw(screen)
        for brick in self.bricks:
            brick.draw(screen)
        draw_ui(screen, self)

        if self.lives <= 0:
            draw_game_over(screen, self)
