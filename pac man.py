import pygame
import random

# Initialize Pygame
pygame.init()

# Set up game constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
FPS = 10

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up Pac-Man
pacman_size = GRID_SIZE
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_direction = 'RIGHT'

# Set up ghosts
ghost_size = GRID_SIZE
ghosts = [
    {'x': random.randrange(0, WIDTH, GRID_SIZE), 'y': random.randrange(0, HEIGHT, GRID_SIZE), 'color': RED},
    {'x': random.randrange(0, WIDTH, GRID_SIZE), 'y': random.randrange(0, HEIGHT, GRID_SIZE), 'color': BLUE}
]

# Set up obstacles
obstacle_size = GRID_SIZE
obstacles = [
    {'x': random.randrange(0, WIDTH, GRID_SIZE), 'y': random.randrange(0, HEIGHT, GRID_SIZE)},
    {'x': random.randrange(0, WIDTH, GRID_SIZE), 'y': random.randrange(0, HEIGHT, GRID_SIZE)},
    {'x': random.randrange(0, WIDTH, GRID_SIZE), 'y': random.randrange(0, HEIGHT, GRID_SIZE)}
]

# Set up game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-Man')

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_direction = 'LEFT'
    elif keys[pygame.K_RIGHT]:
        pacman_direction = 'RIGHT'
    elif keys[pygame.K_UP]:
        pacman_direction = 'UP'
    elif keys[pygame.K_DOWN]:
        pacman_direction = 'DOWN'

    # Move Pac-Man
    if pacman_direction == 'LEFT':
        pacman_x -= GRID_SIZE
    elif pacman_direction == 'RIGHT':
        pacman_x += GRID_SIZE
    elif pacman_direction == 'UP':
        pacman_y -= GRID_SIZE
    elif pacman_direction == 'DOWN':
        pacman_y += GRID_SIZE

    # Wrap Pac-Man around the screen
    pacman_x %= WIDTH
    pacman_y %= HEIGHT

    # Check collisions with ghosts
    for ghost in ghosts:
        if pacman_x == ghost['x'] and pacman_y == ghost['y']:
            running = False

    # Check collisions with obstacles
    for obstacle in obstacles:
        if pacman_x == obstacle['x'] and pacman_y == obstacle['y']:
            pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2  # Reset Pac-Man position

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_size // 2)

    for ghost in ghosts:
        pygame.draw.rect(screen, ghost['color'], (ghost['x'], ghost['y'], ghost_size, ghost_size))

    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, (obstacle['x'], obstacle['y'], obstacle_size, obstacle_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
