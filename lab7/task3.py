import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
MOVE_DISTANCE = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movable Red Ball")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - MOVE_DISTANCE >= BALL_RADIUS:
                    ball_y -= MOVE_DISTANCE
            elif event.key == pygame.K_DOWN:
                if ball_y + MOVE_DISTANCE <= SCREEN_HEIGHT - BALL_RADIUS:
                    ball_y += MOVE_DISTANCE
            elif event.key == pygame.K_LEFT:
                if ball_x - MOVE_DISTANCE >= BALL_RADIUS:
                    ball_x -= MOVE_DISTANCE
            elif event.key == pygame.K_RIGHT:
                if ball_x + MOVE_DISTANCE <= SCREEN_WIDTH - BALL_RADIUS:
                    ball_x += MOVE_DISTANCE
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()