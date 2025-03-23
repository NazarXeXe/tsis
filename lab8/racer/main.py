def main():
    import pygame
    import sys
    import random

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
    CAR_RED = (220, 20, 60)

    # Road properties
    road_width = 300
    road_x = (WIDTH - road_width) // 2
    road_left_edge = road_x
    road_right_edge = road_x + road_width

    # Stripe properties
    stripe_width = 10
    stripe_height = 80
    stripe_gap = 40
    scroll_speed = 300  # Pixels per second

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

    # Function to spawn a new coin
    def spawn_coin():
        # Random position on the road
        coin_x = random.randint(road_left_edge + coin_radius, road_right_edge - coin_radius)
        coin_y = -coin_radius  # Start just above the screen

        coins.append({
            'x': coin_x,
            'y': coin_y,
            'radius': coin_radius,
            'collected': False
        })

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

        # Update coins
        for coin in coins[:]:
            coin['y'] += scroll_speed * dt

            # Check for collision with car
            if not coin['collected']:
                # Simple collision detection using rectangles
                car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
                coin_rect = pygame.Rect(coin['x'] - coin_radius, coin['y'] - coin_radius,
                                        coin_radius * 2, coin_radius * 2)

                if car_rect.colliderect(coin_rect):
                    coin['collected'] = True
                    coin_count += 1

            # Remove coins that are off screen
            if coin['y'] > HEIGHT + coin_radius:
                coins.remove(coin)

        # Fill background
        screen.fill(SKY_BLUE)

        # Draw road at both positions
        screen.blit(road, (0, int(road_pos1)))
        screen.blit(road, (0, int(road_pos2)))

        # Draw coins
        for coin in coins:
            if not coin['collected']:
                pygame.draw.circle(screen, COIN_GOLD, (int(coin['x']), int(coin['y'])), coin_radius)

        # Draw car
        pygame.draw.rect(screen, CAR_RED, (int(car_x), int(car_y), car_width, car_height))

        # Display current FPS and coin count
        fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))

        coin_text = font.render(f"Coins: {coin_count}", True, (255, 255, 255))
        screen.blit(coin_text, (10, 50))

        # Update display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()