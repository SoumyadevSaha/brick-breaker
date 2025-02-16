# ui.py
import pygame
import pygame.freetype
import settings

pygame.font.init()
pygame.freetype.init()

# Standard fonts for UI texts
large_font = pygame.font.SysFont(None, 50)    # Used for Game Over title
medium_font = pygame.font.SysFont(None, 30)   # Used for score and lives label
small_font = pygame.font.SysFont(None, 20)    # Used for footer and instructions

# Emoji font using segoeuisymbol to render emoji characters (hearts and smileys)
emoji_font = pygame.freetype.SysFont("segoeuisymbol", 30)

def draw_ui(screen, game):
    # Draw Lives: "Lives: " followed by heart emojis rendered via emoji_font
    lives_label = "Lives: "
    lives_label_surface = medium_font.render(lives_label, True, settings.WHITE)
    lives_label_pos = (10, 10)  # 10-pixel margin at top left
    screen.blit(lives_label_surface, lives_label_pos)
    
    # Calculate offset so that the heart emojis appear right after the label
    x_offset = lives_label_pos[0] + lives_label_surface.get_width() + 5
    for i in range(game.lives):
        heart_surface, heart_rect = emoji_font.render("♥️", settings.WHITE)
        heart_rect.topleft = (x_offset, lives_label_pos[1])
        screen.blit(heart_surface, heart_rect)
        x_offset += heart_rect.width + 5  # space between hearts

    # Draw Score: right-aligned with a 10-pixel margin from the right edge
    score_text = f"Score: {game.score}"
    score_surface = medium_font.render(score_text, True, settings.WHITE)
    score_x = settings.SCREEN_WIDTH - score_surface.get_width() - 10
    score_pos = (score_x, 10)
    screen.blit(score_surface, score_pos)
    
    # Draw Footer: centered at the bottom with the same font size as the score/lives
    footer_text = "Made with ♥️ by Soumyadev Saha © 2025"
    footer_surface = small_font.render(footer_text, True, settings.WHITE)
    footer_x = (settings.SCREEN_WIDTH - footer_surface.get_width()) // 2
    footer_y = settings.SCREEN_HEIGHT - footer_surface.get_height() - 10
    screen.blit(footer_surface, (footer_x, footer_y))

def draw_game_over(screen, game):
    # Prepare texts for Game Over screen
    title_text = "Game Over !!!"
    score_text = f"Score: {game.score}"
    instruction_text = "Press SPACE to play again"
    
    title_surface = large_font.render(title_text, True, settings.WHITE)
    score_surface = medium_font.render(score_text, True, settings.WHITE)
    instruction_surface = small_font.render(instruction_text, True, settings.WHITE)
    
    # Calculate the total height for vertical centering (with 10 pixels spacing between each)
    total_height = (
        title_surface.get_height() +
        score_surface.get_height() +
        instruction_surface.get_height() + 20
    )
    start_y = (settings.SCREEN_HEIGHT - total_height) // 2
    
    # Center each text horizontally
    title_x = (settings.SCREEN_WIDTH - title_surface.get_width()) // 2
    score_x = (settings.SCREEN_WIDTH - score_surface.get_width()) // 2
    instruction_x = (settings.SCREEN_WIDTH - instruction_surface.get_width()) // 2
    
    # Render an emoji (smiling face) above the Game Over title using emoji_font
    emoji_surface, emoji_rect = emoji_font.render("😃", settings.WHITE)
    emoji_rect.centerx = settings.SCREEN_WIDTH // 2
    emoji_rect.bottom = start_y - 10  # 10 pixels above the title text
    
    screen.blit(emoji_surface, emoji_rect)
    screen.blit(title_surface, (title_x, start_y))
    screen.blit(score_surface, (score_x, start_y + title_surface.get_height() + 10))
    screen.blit(instruction_surface, (instruction_x, start_y + title_surface.get_height() + score_surface.get_height() + 20))
