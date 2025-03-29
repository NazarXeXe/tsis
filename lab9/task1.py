import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road Runner - Collect Coins!")

# Colors
SKY_BLUE = (135, 206, 235)
ROAD_GRAY = (105, 105, 105)
STRIPE_WHITE = (255, 255, 255)
GRASS_GREEN = (34, 139, 34)
COIN_GOLD = (255, 215, 0)
COIN_SILVER = (192, 192, 192)
COIN_BRONZE = (205, 127, 50)
COIN_DIAMOND = (185, 242, 255)
CAR_RED = (220, 20, 60)
ENEMY_BLACK = (30, 30, 30)

# Road properties
road_width = 300
road_x = (WIDTH - road_width) // 2
road_left_edge = road_x
road_right_edge = road_x + road_width

# Stripe properties
stripe_width = 30
stripe_height = 80
stripe_gap = 40
base_scroll_speed = 300  # Base pixels per second
scroll_speed = base_scroll_speed  # Current scroll speed

# Car properties
car_width = 50
car_height = 80
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 50
car_speed = 300  # Pixels per second

# Coin properties
coin_radius = 15
coins = []  # List to store active coins
coin_spawn_timer = 0
coin_spawn_interval = 1.0  # Seconds between coin spawns
coin_count = 0
speed_increase_threshold = 10  # Increase speed every 10 coins
speed_increase_factor = 1.2

# Enemy properties
enemies = []  # List to store active enemies
enemy_spawn_timer = 0
enemy_spawn_interval = 3.0  # Seconds between enemy spawns
enemy_width = 50
enemy_height = 80

# Create road surface
road = pygame.Surface((WIDTH, HEIGHT * 2))
road.fill(GRASS_GREEN)
pygame.draw.rect(road, ROAD_GRAY, (road_x, 0, road_width, HEIGHT * 2))

# Draw stripes on road
stripe_y = 0
while stripe_y < HEIGHT * 2:
    pygame.draw.rect(road, STRIPE_WHITE, (WIDTH // 2 - stripe_width // 2, stripe_y, stripe_width, stripe_height))
    stripe_y += stripe_height + stripe_gap

# Initial positions as floats for precise movement
road_pos1 = 0.0
road_pos2 = -HEIGHT

# Font for UI
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

# Game states
PLAYING = 0
GAME_OVER = 1
game_state = PLAYING

# Score variables
score = 0
high_score = 0

# Define coin types
COIN_TYPES = [
    {"type": "bronze", "color": COIN_BRONZE, "value": 1, "weight": 70, "radius": 15},
    {"type": "silver", "color": COIN_SILVER, "value": 3, "weight": 20, "radius": 15},
    {"type": "gold", "color": COIN_GOLD, "value": 5, "weight": 8, "radius": 15},
    {"type": "diamond", "color": COIN_DIAMOND, "value": 10, "weight": 2, "radius": 15}
]


# Function to spawn a new coin
def spawn_coin():
    # Select coin type based on weight
    weights = [coin_type["weight"] for coin_type in COIN_TYPES]
    coin_type = random.choices(COIN_TYPES, weights=weights)[0]

    # Random position on the road
    coin_x = random.randint(road_left_edge + coin_type["radius"],
                            road_right_edge - coin_type["radius"])
    coin_y = -coin_type["radius"]  # Start just above the screen

    coins.append({
        'x': coin_x,
        'y': coin_y,
        'radius': coin_type["radius"],
        'type': coin_type["type"],
        'color': coin_type["color"],
        'value': coin_type["value"],
        'collected': False
    })


# Function to spawn a new enemy
def spawn_enemy():
    # Random position on the road
    enemy_x = random.randint(road_left_edge, road_right_edge - enemy_width)
    enemy_y = -enemy_height  # Start just above the screen

    enemies.append({
        'x': enemy_x,
        'y': enemy_y,
        'width': enemy_width,
        'height': enemy_height,
        'speed': scroll_speed  # Enemy moves at current scroll speed
    })


# Function to reset the game
def reset_game():
    global car_x, coins, enemies, coin_count, score, scroll_speed, game_state
    car_x = WIDTH // 2 - car_width // 2
    coins = []
    enemies = []
    coin_count = 0
    scroll_speed = base_scroll_speed
    score = 0
    game_state = PLAYING


# Function to draw coin legend
def draw_coin_legend():
    legend_y = 120
    title = small_font.render("Coin Types:", True, (0, 0, 0))
    screen.blit(title, (10, legend_y))
    legend_y += 25

    for coin_type in COIN_TYPES:
        pygame.draw.circle(screen, coin_type["color"], (20, legend_y), 10)
        text = small_font.render(f"{coin_type['type'].capitalize()}: +{coin_type['value']}", True, (0, 0, 0))
        screen.blit(text, (35, legend_y - 10))
        legend_y += 30


# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Calculate delta time in seconds
    dt = clock.tick(0) / 1000.0  # Uncapped framerate

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE and game_state == GAME_OVER:
                reset_game()

    if game_state == PLAYING:
        # Get pressed keys for continuous movement
        keys = pygame.key.get_pressed()

        # Update car position based on input
        if keys[pygame.K_LEFT] and car_x > road_left_edge:
            car_x -= car_speed * dt
        if keys[pygame.K_RIGHT] and car_x < road_right_edge - car_width:
            car_x += car_speed * dt

        # Ensure car stays on the road
        car_x = max(road_left_edge, min(car_x, road_right_edge - car_width))

        # Move road positions using delta time
        road_pos1 += scroll_speed * dt
        road_pos2 += scroll_speed * dt

        # Reset positions when off screen
        if road_pos1 >= HEIGHT:
            road_pos1 = -HEIGHT + (road_pos1 - HEIGHT)
        if road_pos2 >= HEIGHT:
            road_pos2 = -HEIGHT + (road_pos2 - HEIGHT)

        # Update coin spawn timer
        coin_spawn_timer += dt
        if coin_spawn_timer >= coin_spawn_interval:
            spawn_coin()
            coin_spawn_timer = 0

        # Update enemy spawn timer
        enemy_spawn_timer += dt
        if enemy_spawn_timer >= enemy_spawn_interval:
            spawn_enemy()
            enemy_spawn_timer = 0

        # Update coins
        for coin in coins[:]:
            coin['y'] += scroll_speed * dt

            # Check for collision with car
            if not coin['collected']:
                # Simple collision detection using distance formula
                car_center_x = car_x + car_width / 2
                car_center_y = car_y + car_height / 2

                distance = ((car_center_x - coin['x']) ** 2 + (car_center_y - coin['y']) ** 2) ** 0.5

                if distance < car_width / 2 + coin['radius']:
                    coin['collected'] = True
                    coin_count += 1
                    score += coin['value']

                    # Check if we need to increase speed
                    if coin_count % speed_increase_threshold == 0:
                        scroll_speed *= speed_increase_factor
                        # Also update all existing enemies to the new speed
                        for enemy in enemies:
                            enemy['speed'] = scroll_speed

            # Remove coins that are off screen
            if coin['y'] > HEIGHT + coin['radius']:
                coins.remove(coin)

        # Update enemies
        for enemy in enemies[:]:
            enemy['y'] += enemy['speed'] * dt

            # Check for collision with car
            car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy['width'], enemy['height'])

            if car_rect.colliderect(enemy_rect):
                game_state = GAME_OVER
                high_score = max(high_score, score)

            # Remove enemies that are off screen
            if enemy['y'] > HEIGHT:
                enemies.remove(enemy)

    # Fill background
    screen.fill(SKY_BLUE)

    # Draw road at both positions
    screen.blit(road, (0, int(road_pos1)))
    screen.blit(road, (0, int(road_pos2)))

    # Draw coins
    for coin in coins:
        if not coin['collected']:
            pygame.draw.circle(screen, coin['color'], (int(coin['x']), int(coin['y'])), coin['radius'])

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_BLACK, (int(enemy['x']), int(enemy['y']), enemy['width'], enemy['height']))

    # Draw car
    pygame.draw.rect(screen, CAR_RED, (int(car_x), int(car_y), car_width, car_height))

    # Display current FPS, score, and coin count
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    coin_text = font.render(f"Coins: {coin_count}", True, (0, 0, 0))
    speed_text = font.render(f"Speed: {int(scroll_speed)}", True, (0, 0, 0))

    screen.blit(fps_text, (10, 10))
    screen.blit(score_text, (10, 50))
    screen.blit(coin_text, (10, 90))
    screen.blit(speed_text, (WIDTH - 150, 10))

    # Draw coin legend
    draw_coin_legend()

    # Game over screen
    if game_state == GAME_OVER:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        screen.blit(overlay, (0, 0))

        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        final_score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        restart_text = font.render("Press SPACE to restart", True, (255, 255, 255))

        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 80))
        screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 - 30))
        screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2 + 10))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 60))

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()