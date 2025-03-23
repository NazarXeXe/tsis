def main():
    import pygame
    import sys
    from pygame.colordict import THECOLORS

    # Initialize pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 800, 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (128, 0, 128)
    GRAY = (200, 200, 200)

    # Set up the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Enhanced Paint Program")

    # Set up the drawing canvas
    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(WHITE)

    # Initialize variables
    drawing = False
    start_pos = None
    current_pos = None
    last_pos = None
    color = BLACK
    brush_size = 5
    tool = "brush"  # Available tools: "brush", "rectangle", "circle", "eraser"

    # For color picker
    expanded_colors = False
    color_list = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE,
                  (255, 165, 0), (0, 255, 255), (255, 192, 203),
                  (139, 69, 19), (107, 142, 35), (70, 130, 180)]

    # UI elements
    # Tool buttons
    tool_buttons = [
        {"tool": "brush", "rect": pygame.Rect(10, 10, 30, 30), "icon": "B"},
        {"tool": "rectangle", "rect": pygame.Rect(50, 10, 30, 30), "icon": "R"},
        {"tool": "circle", "rect": pygame.Rect(90, 10, 30, 30), "icon": "C"},
        {"tool": "eraser", "rect": pygame.Rect(130, 10, 30, 30), "icon": "E"}
    ]

    # Color selection button (main)
    color_button = pygame.Rect(180, 10, 30, 30)
    # Color palette (appears when color button is clicked)
    color_palette = []
    for i, col in enumerate(color_list):
        row = i // 4
        col_pos = i % 4
        color_palette.append({
            "color": col,
            "rect": pygame.Rect(180 + col_pos * 30, 50 + row * 30, 25, 25)
        })

    # Brush size buttons
    brush_buttons = [
        {"size": 2, "rect": pygame.Rect(230, 10, 20, 20)},
        {"size": 5, "rect": pygame.Rect(260, 10, 20, 20)},
        {"size": 10, "rect": pygame.Rect(290, 10, 20, 20)},
        {"size": 20, "rect": pygame.Rect(320, 10, 20, 20)}
    ]

    clear_button = pygame.Rect(360, 10, 80, 30)
    save_button = pygame.Rect(450, 10, 80, 30)

    # Preview layer (for shapes)
    preview_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    # Function to draw shapes on the preview layer
    def update_preview():
        preview_layer.fill((0, 0, 0, 0))  # Clear with transparent
        if tool == "rectangle" and start_pos and current_pos:
            rect = pygame.Rect(
                min(start_pos[0], current_pos[0]),
                min(start_pos[1], current_pos[1]),
                abs(current_pos[0] - start_pos[0]),
                abs(current_pos[1] - start_pos[1])
            )
            pygame.draw.rect(preview_layer, color, rect, brush_size)
        elif tool == "circle" and start_pos and current_pos:
            radius = int(((current_pos[0] - start_pos[0]) ** 2 +
                          (current_pos[1] - start_pos[1]) ** 2) ** 0.5)
            pygame.draw.circle(preview_layer, color, start_pos, radius, brush_size)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Check if any tool button was clicked
                    for btn in tool_buttons:
                        if btn["rect"].collidepoint(event.pos):
                            tool = btn["tool"]
                            break

                    # Check if color button was clicked
                    if color_button.collidepoint(event.pos):
                        expanded_colors = not expanded_colors

                    # Check if any color in palette was clicked
                    if expanded_colors:
                        for col in color_palette:
                            if col["rect"].collidepoint(event.pos):
                                color = col["color"]
                                expanded_colors = False
                                break

                    # Check if any brush size button was clicked
                    for btn in brush_buttons:
                        if btn["rect"].collidepoint(event.pos):
                            brush_size = btn["size"]
                            break

                    # Check if clear button was clicked
                    if clear_button.collidepoint(event.pos):
                        canvas.fill(WHITE)

                    # Check if save button was clicked
                    elif save_button.collidepoint(event.pos):
                        pygame.image.save(canvas, "my_drawing.png")
                        print("Drawing saved as 'my_drawing.png'")

                    # Start drawing if not clicking on UI
                    elif event.pos[1] > 50 and not expanded_colors:
                        drawing = True
                        start_pos = event.pos
                        current_pos = event.pos
                        last_pos = event.pos

                        # For brush and eraser, start drawing immediately
                        if tool == "brush":
                            pygame.draw.circle(canvas, color, event.pos, brush_size // 2)
                        elif tool == "eraser":
                            pygame.draw.circle(canvas, WHITE, event.pos, brush_size)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:  # Left mouse button
                    drawing = False

                    # Finalize shapes
                    if tool == "rectangle":
                        rect = pygame.Rect(
                            min(start_pos[0], current_pos[0]),
                            min(start_pos[1], current_pos[1]),
                            abs(current_pos[0] - start_pos[0]),
                            abs(current_pos[1] - start_pos[1])
                        )
                        pygame.draw.rect(canvas, color, rect, brush_size)
                    elif tool == "circle":
                        radius = int(((current_pos[0] - start_pos[0]) ** 2 +
                                      (current_pos[1] - start_pos[1]) ** 2) ** 0.5)
                        pygame.draw.circle(canvas, color, start_pos, radius, brush_size)

                    # Clear the preview
                    preview_layer.fill((0, 0, 0, 0))
                    start_pos = None
                    current_pos = None
                    last_pos = None

            elif event.type == pygame.MOUSEMOTION:
                current_pos = event.pos

                if drawing and last_pos and event.pos[1] > 50:
                    if tool == "brush":
                        pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                    elif tool == "eraser":
                        pygame.draw.line(canvas, WHITE, last_pos, event.pos, brush_size * 2)

                    # Update for continuous drawing
                    if tool in ["brush", "eraser"]:
                        last_pos = event.pos

                    # Update preview for shape tools
                    if tool in ["rectangle", "circle"]:
                        update_preview()

        # Draw everything
        screen.fill(GRAY)

        # Draw the canvas
        screen.blit(canvas, (0, 0))

        # Draw the preview layer
        if drawing and tool in ["rectangle", "circle"]:
            screen.blit(preview_layer, (0, 0))

        # Draw UI area background
        pygame.draw.rect(screen, (180, 180, 180), pygame.Rect(0, 0, WIDTH, 50))
        pygame.draw.line(screen, BLACK, (0, 50), (WIDTH, 50), 2)

        # Draw tool buttons
        for btn in tool_buttons:
            # Highlight selected tool
            if tool == btn["tool"]:
                pygame.draw.rect(screen, (255, 255, 100), btn["rect"])
            else:
                pygame.draw.rect(screen, WHITE, btn["rect"])

            pygame.draw.rect(screen, BLACK, btn["rect"], 2)  # Border

            # Add tool icon text
            font = pygame.font.SysFont(None, 24)
            icon_text = font.render(btn["icon"], True, BLACK)
            screen.blit(icon_text, (btn["rect"].centerx - icon_text.get_width() // 2,
                                    btn["rect"].centery - icon_text.get_height() // 2))

        # Draw color button
        pygame.draw.rect(screen, color, color_button)
        pygame.draw.rect(screen, BLACK, color_button, 2)  # Border

        # Draw expanded color palette if active
        if expanded_colors:
            # Background for color palette
            palette_height = ((len(color_list) + 3) // 4) * 30 + 10
            pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(170, 45, 130, palette_height))
            pygame.draw.rect(screen, BLACK, pygame.Rect(170, 45, 130, palette_height), 2)

            # Draw color swatches
            for col in color_palette:
                pygame.draw.rect(screen, col["color"], col["rect"])
                pygame.draw.rect(screen, BLACK, col["rect"], 1)  # Border

        # Draw brush size buttons
        for btn in brush_buttons:
            pygame.draw.rect(screen, WHITE, btn["rect"])
            pygame.draw.circle(screen, BLACK, btn["rect"].center, btn["size"] // 2)

            # Highlight selected brush size
            if brush_size == btn["size"]:
                pygame.draw.rect(screen, (255, 255, 100), btn["rect"], 3)
            else:
                pygame.draw.rect(screen, BLACK, btn["rect"], 1)  # Border

        # Draw clear and save buttons
        pygame.draw.rect(screen, (220, 220, 220), clear_button)
        pygame.draw.rect(screen, BLACK, clear_button, 2)
        pygame.draw.rect(screen, (220, 220, 220), save_button)
        pygame.draw.rect(screen, BLACK, save_button, 2)

        # Draw button labels
        font = pygame.font.SysFont(None, 24)
        clear_text = font.render("Clear", True, BLACK)
        save_text = font.render("Save", True, BLACK)
        screen.blit(clear_text, (clear_button.x + 10, clear_button.y + 5))
        screen.blit(save_text, (save_button.x + 10, save_button.y + 5))

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()