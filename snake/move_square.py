import pygame
import sys
import logging

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Square")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constants
SQUARE_SIZE = 20
# SPEED = 5
SPEED = 5


# configure logging to print to console and print the line number from where the log was called
logging.basicConfig(
    # format="%(asctime)s - %(message)s",
    format="%(asctime)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)
# logging.basicConfig(level=logging.INFO)


class MovingSquare:
    """A class to represent a moving square."""

    def __init__(
        self,
        x,
        y,
        size,
        color,
        speed,
    ):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.dx = speed
        self.dy = 0
        self.direction = "right"

    def update_position(self):
        self.x += self.dx
        self.y += self.dy

        # Boundary checking
        if self.x < 0 or self.x + self.size > WIDTH:
            self.dx = -self.dx
        if self.y < 0 or self.y + self.size > HEIGHT:
            self.dy = -self.dy

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))


def handle_events(square):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False
            elif event.key == pygame.K_LEFT:
                if (not square.dx > 0) and (not square.dy == 0):
                    square.dx = -square.speed
                    square.dy = 0
                    square.direction = "left"
                    logging.info(f"Direction: {square.direction}")
            elif event.key == pygame.K_RIGHT:
                if not square.direction == "left":
                    square.dx = square.speed
                    square.dy = 0
                    square.direction = "right"
                    logging.info(f"Direction: {square.direction}")
            elif event.key == pygame.K_UP:
                if not square.direction == "down":
                    square.dy = -square.speed
                    square.dx = 0
                    square.direction = "up"
                    logging.info(f"Direction: {square.direction}")
            elif event.key == pygame.K_DOWN:
                if not square.direction == "up":
                    square.dy = square.speed
                    square.dx = 0
                    square.direction = "down"
                    logging.info(f"Direction: {square.direction}")
    return True


# Main loop
def main():
    run = True
    clock = pygame.time.Clock()

    square = MovingSquare(x=WIDTH // 2, y=HEIGHT // 2, size=SQUARE_SIZE, color=BLACK, speed=SPEED)

    while run:
        run = handle_events(square)
        if not run:
            break

        # Update the square's position
        square.update_position()

        # Clear the screen and draw the whiteboard and the square
        WIN.fill(WHITE)
        square.draw(WIN)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
