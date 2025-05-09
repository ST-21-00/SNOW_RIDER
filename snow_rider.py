
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snow Rider")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Load sled image
sled_img = pygame.Surface((40, 20))
sled_img.fill(RED)

# Game variables
sled_x = WIDTH // 2
sled_y = HEIGHT - 60
sled_speed = 5

obstacles = []
obstacle_speed = 3
obstacle_timer = 0
score = 0

font = pygame.font.SysFont(None, 36)

# Function to create obstacles
def create_obstacle():
    x = random.randint(0, WIDTH - 30)
    y = -30
    obstacles.append(pygame.Rect(x, y, 30, 30))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and sled_x > 0:
        sled_x -= sled_speed
    if keys[pygame.K_RIGHT] and sled_x < WIDTH - 40:
        sled_x += sled_speed

    # Add obstacles over time
    obstacle_timer += 1
    if obstacle_timer > 30:
        create_obstacle()
        obstacle_timer = 0

    # Move and draw obstacles
    for obs in obstacles[:]:
        obs.y += obstacle_speed
        pygame.draw.rect(screen, BLACK, obs)
        if obs.colliderect(pygame.Rect(sled_x, sled_y, 40, 20)):
            running = False  # Game over if you hit an obstacle
        if obs.y > HEIGHT:
            obstacles.remove(obs)
            score += 1

    # Draw sled
    screen.blit(sled_img, (sled_x, sled_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
