# paddle.py

import pygame
import settings

class Paddle:
    def __init__(self):
        self.width = settings.PADDLE_WIDTH
        self.height = settings.PADDLE_HEIGHT
        self.x = (settings.SCREEN_WIDTH - self.width) // 2
        self.y = settings.PADDLE_Y
        self.speed = settings.PADDLE_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        # add up and down movements as well
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.y > settings.SCREEN_HEIGHT * 0.5:
            self.rect.y -= self.speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.y < settings.SCREEN_HEIGHT * 0.9 - self.height:
            self.rect.y += self.speed

        # Keep paddle within screen bounds
        self.rect.x = max(0, min(settings.SCREEN_WIDTH - self.width, self.rect.x))

    def draw(self, screen):
        pygame.draw.rect(screen, settings.WHITE, self.rect)
