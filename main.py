# main.py

import pygame
import settings
from game import Game

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker | Soumya")

clock = pygame.time.Clock()
game = Game()

running = True
while running:
    screen.fill(settings.BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game.reset()

    if game.lives > 0:
        game.update()
    game.draw(screen)

    pygame.display.flip()
    clock.tick(settings.FPS)

pygame.quit()
