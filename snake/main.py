# Create a simple 10x10 grid using pygame and display it on the screen.

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 800
WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constants
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // ROWS


# Function to draw the grid
def draw_grid():
    """
    Draws a grid on the game window.

    This function fills the game window with a white color and then draws a grid of black rectangles on it.
    Each rectangle represents a cell in the grid.

    It uses the fill and draw.rect functions from the pygame module to draw the grid.

    Parameters:
        None

    Returns:
        None
    """
    WIN.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(WIN, BLACK, rect, 1)
    pygame.display.update()


# Main loop
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        draw_grid()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
