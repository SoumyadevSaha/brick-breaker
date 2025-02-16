# ball.py

import pygame
import random
import settings

class Ball:
    def __init__(self):
        self.radius = settings.BALL_RADIUS
        self.reset()

    def reset(self):
        self.rect = pygame.Rect(
            settings.SCREEN_WIDTH // 2, settings.BALL_START_Y, 
            self.radius * 2, self.radius * 2
        )
        self.velocity = settings.BALL_START_VELOCITY[:]

    def move(self, paddle, bricks, game):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Collision with walls
        if self.rect.left <= 0 or self.rect.right >= settings.SCREEN_WIDTH:
            self.velocity[0] = -self.velocity[0]  # Reflect x direction
        if self.rect.top <= 0:
            self.velocity[1] = -self.velocity[1]  # Reflect y direction

        # Collision with paddle
        if self.rect.colliderect(paddle.rect):
            self.velocity[1] = -self.velocity[1]
            self.rect.y = paddle.rect.top - self.radius * 2  # Prevent sticking

        # Collision with bricks
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                bricks.remove(brick)
                self.velocity[1] = -self.velocity[1]
                game.score += settings.SCORE_PER_BRICK
                break

        # Ball falls out (lose life)
        if self.rect.top > settings.SCREEN_HEIGHT:
            game.lives -= 1
            self.reset()

    def draw(self, screen):
        pygame.draw.circle(screen, settings.WHITE, self.rect.center, self.radius)
