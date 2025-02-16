# brick.py

import pygame
import settings

class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, settings.BRICK_WIDTH, settings.BRICK_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, settings.WHITE, self.rect)
