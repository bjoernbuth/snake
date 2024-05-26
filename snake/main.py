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
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Constants
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // ROWS


class Board:
    """A class to represent a game board."""

    def __init__(self, color1=BLACK, color2=GREEN):
        self.color1 = color1
        self.color2 = color2

    def draw(self):
        draw_grid(self.color1, self.color2)


# Function to draw the grid
def draw_grid(color1=BLACK, color2=GREEN):
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
    for row in range(0, ROWS, 1):
        for col in range(0, COLS, 1):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if (row + col) % 2 == 0:
                pygame.draw.rect(WIN, color1, rect)
            else:
                pygame.draw.rect(WIN, color2, rect)
            # pygame.draw.rect(WIN, YELLOW, rect, 1)
            # pygame.draw.rect(WIN, GREEN, rect.move(CELL_SIZE, 0), 0)
            # pygame.draw.rect(WIN, RED, rect.move(20, 20), 0)

    # Print some text on the screen
    font = pygame.font.Font(None, 36)  # name, size
    # draw_text("Snake", font, BLACK, WIN, WIDTH // 2, 30)

    pygame.display.update()


def draw_text(text, font, color, surface, x, y):
    """
    Draws text on the game window.

    This function takes the text, font, color, surface, x, and y coordinates as input and draws the text on the game window.

    It uses the render function from the pygame.font module to render the text.

    Parameters:
        text (str): The text to be displayed.
        font (pygame.font.Font): The font to be used for the text.
        color (tuple): The color of the text in RGB format.
        surface (pygame.Surface): The surface on which the text is to be drawn.
        x (int): The x-coordinate of the text.
        y (int): The y-coordinate of the text.

    Returns:
        None
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)


# Main loop
def main():
    run = True

    board = Board(color1=YELLOW, color2=BLUE)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        # draw_grid()
        board.draw()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
