import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Endless Runner')

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up player
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size]
player_speed = 10
player_jump = False

# Set up obstacles
obstacle_width = 50
obstacle_height = random.randint(100, HEIGHT - player_size - 100)
obstacles = [[WIDTH, random.randint(0, HEIGHT - obstacle_height - player_size)]]
obstacle_speed = 5

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player_jump:
                player_jump = True
                player_speed = -20

    # Player movement
    if player_jump:
        player_pos[1] += player_speed
        player_speed += 1
        if player_pos[1] >= HEIGHT - player_size:
            player_jump = False
            player_speed = 10
    else:
        player_pos[1] += player_speed

    # Draw player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # Obstacle movement and drawing
    for obstacle in obstacles:
        obstacle[0] -= obstacle_speed
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    # Check for collision
    for obstacle in obstacles:
        if pygame.Rect(player_pos[0], player_pos[1], player_size, player_size).colliderect(pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)):
            running = False

    # Reset obstacle if it goes off screen
    if obstacles[0][0] + obstacle_width < 0:
        obstacles.pop(0)
    if len(obstacles) < 2:
        obstacles.append([WIDTH, random.randint(0, HEIGHT - obstacle_height - player_size)])

    pygame.display.flip()

pygame.quit()