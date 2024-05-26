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


class BoardWindow:
    """A class to represent the game window."""

    def __init__(self, width=800, height=800, title="Snake"):
        self.width = width
        self.height = height
        self.title = title
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

    def draw(self):
        pygame.display.update()


class Board:
    """A class to represent a game board."""

    def __init__(
        self,
        board_window: BoardWindow,
        color1=BLACK,
        color2=GREEN,
        rows=ROWS,
        cols=COLS,
    ):
        self.board_window = board_window
        self.color1 = color1
        self.color2 = color2
        self.rows = rows
        self.cols = cols

        self.cell_with = self.board_window.width // self.cols
        self.cell_height = self.board_window.height // self.rows
        self.cw = self.cell_with
        self.ch = self.cell_height

    def draw(self):
        self.draw_grid(self.board_window.surface, self.color1, self.color2)

    # Function to draw the grid
    def draw_grid(self, surface: pygame.Surface, color1=BLACK, color2=GREEN):
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

        self.board_window.surface.fill(WHITE)
        for row in range(0, self.rows, 1):
            for col in range(0, self.cols, 1):
                rect = pygame.Rect(col * self.cw, row * self.ch, self.cw, self.ch)
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.board_window.surface, color1, rect)
                else:
                    pygame.draw.rect(self.board_window.surface, color2, rect)

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

    board_window = BoardWindow(width=WIDTH, height=HEIGHT, title="Snake")

    board = Board(
        board_window=board_window,
        color1=YELLOW,
        color2=BLUE,
        rows=10,
        cols=10,
    )

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
