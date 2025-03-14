import pygame
import sys
import math
import time
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

center_x, center_y = WIDTH // 2, HEIGHT // 2

try:
    minute_hand_orig = pygame.image.load("min.svg")
    second_hand_orig = pygame.image.load("sec.svg")
    minute_hand_offset_x = minute_hand_orig.get_width() // 4
    minute_hand_offset_y = minute_hand_orig.get_height()
    minute_hand_size = max(minute_hand_orig.get_width(), minute_hand_orig.get_height()) * 2
    minute_hand = pygame.Surface((minute_hand_size, minute_hand_size), pygame.SRCALPHA)
    minute_hand.blit(minute_hand_orig, (minute_hand_size // 2 - minute_hand_offset_x,
                                        minute_hand_size // 2 - minute_hand_offset_y))
    second_hand_offset_x = second_hand_orig.get_width() // 2
    second_hand_offset_y = second_hand_orig.get_height()
    second_hand_size = max(second_hand_orig.get_width(), second_hand_orig.get_height()) * 2
    second_hand = pygame.Surface((second_hand_size, second_hand_size), pygame.SRCALPHA)
    second_hand.blit(second_hand_orig, (second_hand_size // 2 - second_hand_offset_x,
                                        second_hand_size // 2 - second_hand_offset_y))

except pygame.error:
    minute_hand = None
    second_hand = None
    print("Images not found. Using fallback design.")

minute_hand_length = 120
second_hand_length = 140

clock = pygame.time.Clock()
running = True


def draw_clock_face():
    pygame.draw.circle(screen, WHITE, (center_x, center_y), 200)
    pygame.draw.circle(screen, BLACK, (center_x, center_y), 200, 2)
    # Draw hour marks
    for i in range(12):
        angle = i * 30
        start_x = center_x + 180 * math.sin(math.radians(angle))
        start_y = center_y - 180 * math.cos(math.radians(angle))
        end_x = center_x + 200 * math.sin(math.radians(angle))
        end_y = center_y - 200 * math.cos(math.radians(angle))
        pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 3)



def draw_hand(image, angle, length, thickness):
    if image:
        rotated_hand = pygame.transform.rotate(image, -angle)
        rect = rotated_hand.get_rect()
        rect.center = (center_x, center_y)
        screen.blit(rotated_hand, rect)
    else:
        end_x = center_x + length * math.sin(math.radians(angle))
        end_y = center_y - length * math.cos(math.radians(angle))
        pygame.draw.line(screen, BLACK if thickness > 3 else RED, (center_x, center_y), (end_x, end_y), thickness)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    minute_angle = (minutes * 6) + (seconds * 0.1)
    second_angle = seconds * 6
    draw_clock_face()

    draw_hand(minute_hand, minute_angle, minute_hand_length, 6)

    draw_hand(second_hand, second_angle, second_hand_length, 3)

    pygame.draw.circle(screen, BLACK, (center_x, center_y), 15)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()