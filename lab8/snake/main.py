import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 100, 0)
GRAY = (100, 100, 100)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Game variables
move_interval = 0.1  # Seconds between snake movements
move_timer = 0

# Font for UI
font = pygame.font.SysFont(None, 36)


class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)  # Start moving right
        self.grow_pending = False
        self.is_alive = True
        self.last_direction = self.direction

    def get_head_position(self):
        return self.positions[0]

    def set_direction(self, direction):
        # Prevent 180-degree turns
        if (direction[0] * -1, direction[1] * -1) != self.last_direction:
            self.direction = direction

    def move(self):
        if not self.is_alive:
            return

        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction

        # Calculate new position
        new_x = (head_x + dir_x) % GRID_WIDTH
        new_y = (head_y + dir_y) % GRID_HEIGHT

        # Check self-collision
        if (new_x, new_y) in self.positions[1:]:
            self.is_alive = False
            return

        # Add new head position
        self.positions.insert(0, (new_x, new_y))

        # Remove tail if not growing
        if not self.grow_pending:
            self.positions.pop()
        else:
            self.grow_pending = False

        self.last_direction = self.direction

    def grow(self):
        self.grow_pending = True

    def draw(self, surface):
        for i, (x, y) in enumerate(self.positions):
            # Draw snake segments
            color = DARK_GREEN if i == 0 else GREEN  # Head is darker
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)  # Border


class Food:
    def __init__(self, snake_positions):
        self.position = self.get_random_position(snake_positions)

    def get_random_position(self, snake_positions):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_positions:
                return (x, y)

    def draw(self, surface):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, RED, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)  # Border


def draw_grid(surface):
    for y in range(0, HEIGHT, GRID_SIZE):
        for x in range(0, WIDTH, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, GRAY, rect, 1)


def game_over_screen(surface, score):
    surface.fill(BLACK)

    game_over_text = font.render("GAME OVER", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    restart_text = font.render("Press SPACE to restart or ESC to quit", True, WHITE)

    surface.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 60))
    surface.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    surface.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 60))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True  # Restart game
                elif event.key == pygame.K_ESCAPE:
                    return False  # Quit game


def run_game():
    snake = Snake()
    food = Food(snake.positions)
    score = 0

    clock = pygame.time.Clock()
    running = True

    # Movement variables
    global move_timer
    move_timer = 0

    while running:
        # Calculate delta time in seconds
        dt = clock.tick(0) / 1000.0  # Uncapped framerate

        # Update movement timer
        move_timer += dt

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_UP:
                    snake.set_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.set_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.set_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.set_direction((1, 0))

        # Move snake at fixed intervals regardless of framerate
        if move_timer >= move_interval:
            snake.move()
            move_timer = 0  # Reset timer

            # Check for collisions with food
            if snake.get_head_position() == food.position:
                snake.grow()
                food = Food(snake.positions)
                score += 1

                # Increase speed as score increases
                global mv_i
                mv_i = max(0.05, 0.1 - (score * 0.001))

        # Fill background
        screen.fill(BLACK)

        # Draw grid
        draw_grid(screen)

        # Draw food and snake
        food.draw(screen)
        snake.draw(screen)

        # Display score and FPS
        score_text = font.render(f"Score: {score}", True, WHITE)
        fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(fps_text, (WIDTH - fps_text.get_width() - 10, 10))

        # Update display
        pygame.display.flip()

        # Check if game over
        if not snake.is_alive:
            return game_over_screen(screen, score)

    return False


# Main game loop
def main():
    restart = True
    while restart:
        restart = run_game()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()