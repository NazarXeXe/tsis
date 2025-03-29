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
GOLD = (255, 215, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
DARK_GREEN = (0, 100, 0)
GRAY = (100, 100, 100)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enhanced Snake Game")

# Game variables
move_interval = 0.1  # Seconds between snake movements
move_timer = 0

# Font for UI
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 20)


class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)  # Start moving right
        self.grow_pending = 0  # Number of segments to grow
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
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.positions.pop()

        self.last_direction = self.direction

    def grow(self, amount=1):
        self.grow_pending += amount

    def draw(self, surface):
        for i, (x, y) in enumerate(self.positions):
            # Draw snake segments
            color = DARK_GREEN if i == 0 else GREEN  # Head is darker
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)  # Border


class Food:
    def __init__(self, snake_positions):
        # Food types: (color, point value, growth amount, lifetime in seconds)
        self.food_types = [
            {"color": RED, "points": 1, "growth": 1, "lifetime": None, "weight": 70},  # Regular food
            {"color": GOLD, "points": 5, "growth": 2, "lifetime": 5, "weight": 15},  # Golden food (timed)
            {"color": BLUE, "points": 2, "growth": 3, "lifetime": 8, "weight": 10},  # Blue food (timed)
            {"color": PURPLE, "points": 10, "growth": 5, "lifetime": 3, "weight": 5}  # Purple food (timed, rare)
        ]

        # Choose food type based on weights
        weights = [food["weight"] for food in self.food_types]
        self.type = random.choices(self.food_types, weights=weights)[0]

        # Set position and creation time
        self.position = self.get_random_position(snake_positions)
        self.creation_time = time.time()
        self.active = True

    def get_random_position(self, snake_positions):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_positions:
                return (x, y)

    def update(self, current_time):
        # Check if food should disappear
        if self.type["lifetime"] and current_time - self.creation_time >= self.type["lifetime"]:
            self.active = False

    def get_remaining_time(self, current_time):
        if not self.type["lifetime"]:
            return None
        return max(0, self.type["lifetime"] - (current_time - self.creation_time))

    def draw(self, surface):
        if not self.active:
            return

        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.type["color"], rect)
        pygame.draw.rect(surface, BLACK, rect, 1)  # Border

        # Draw timer for timed food
        remaining = self.get_remaining_time(time.time())
        if remaining:
            # Draw timer text
            timer_text = small_font.render(f"{int(remaining)}", True, WHITE)
            text_x = self.position[0] * GRID_SIZE + (GRID_SIZE - timer_text.get_width()) // 2
            text_y = self.position[1] * GRID_SIZE + (GRID_SIZE - timer_text.get_height()) // 2
            surface.blit(timer_text, (text_x, text_y))

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


def draw_food_legend(surface):
    legend_y = 50
    title = small_font.render("Food Types:", True, WHITE)
    surface.blit(title, (10, legend_y))
    legend_y += 25

    food_types = [
        {"color": RED, "desc": "Regular: +1 pt"},
        {"color": GOLD, "desc": "Gold: +5 pts, 5s"},
        {"color": BLUE, "desc": "Blue: +2 pts, 8s"},
        {"color": PURPLE, "desc": "Purple: +10 pts, 3s"}
    ]

    for food in food_types:
        pygame.draw.rect(surface, food["color"], (10, legend_y, 15, 15))
        pygame.draw.rect(surface, BLACK, (10, legend_y, 15, 15), 1)
        text = small_font.render(food["desc"], True, WHITE)
        surface.blit(text, (30, legend_y))
        legend_y += 20


def run_game():
    snake = Snake()
    foods = [Food(snake.positions)]
    score = 0

    clock = pygame.time.Clock()
    running = True

    # Movement variables
    global move_timer
    move_timer = 0

    # Food spawn timer
    food_spawn_timer = 0
    food_spawn_interval = 5  # New food every 5 seconds

    while running:
        current_time = time.time()

        # Calculate delta time in seconds
        dt = clock.tick(0) / 1000.0  # Uncapped framerate

        # Update movement timer
        move_timer += dt

        # Update food spawn timer
        food_spawn_timer += dt

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
        global move_interval
        if move_timer >= move_interval:
            snake.move()
            move_timer = 0  # Reset timer

            # Check for collisions with food
            for food in foods[:]:
                if food.active and snake.get_head_position() == food.position:
                    snake.grow(food.type["growth"])
                    score += food.type["points"]
                    foods.remove(food)

                    # Increase speed as score increases
                    move_interval = max(0.05, 0.1 - (score * 0.001))

        # Update food timers and remove expired food
        for food in foods[:]:
            food.update(current_time)
            if not food.active:
                foods.remove(food)

        # Spawn new food occasionally
        if food_spawn_timer >= food_spawn_interval:
            food_spawn_timer = 0
            # Limit total number of foods on screen
            if len(foods) < 5:
                foods.append(Food(snake.positions))

        # Fill background
        screen.fill(BLACK)

        # Draw foods and snake
        for food in foods:
            food.draw(screen)
        snake.draw(screen)

        # Display score and FPS
        score_text = font.render(f"Score: {score}", True, WHITE)
        fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(fps_text, (WIDTH - fps_text.get_width() - 10, 10))

        # Draw food legend
        draw_food_legend(screen)

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