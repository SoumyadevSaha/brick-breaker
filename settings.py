# settings.py

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 7
PADDLE_Y = int(SCREEN_HEIGHT * 0.9)  # 90vh

# Ball settings
BALL_RADIUS = 7
BALL_START_VELOCITY = [3, 4]  # (x, y)
BALL_START_Y = int(SCREEN_HEIGHT * 0.5)  # 50vh

# Brick settings
BRICK_ROWS = 6
BRICK_COLUMNS = 15
BRICK_WIDTH = SCREEN_WIDTH // BRICK_COLUMNS
BRICK_HEIGHT = 20
BRICK_Y_START = int(SCREEN_HEIGHT * 0.1)  # 10vh
BRICK_Y_END = int(SCREEN_HEIGHT * 0.4)  # 40vh

# Game settings
LIVES = 3
SCORE_PER_BRICK = 10
