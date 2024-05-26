import pygame
import sys

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


class MovingSquare:
    """A class to represent a moving square."""

    def __init__(self, x, y, size, color, speed):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.dx = speed
        self.dy = 0

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


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False
    return True


# Main loop
def main():
    run = True
    clock = pygame.time.Clock()

    square = MovingSquare(x=WIDTH // 2, y=HEIGHT // 2, size=SQUARE_SIZE, color=BLACK, speed=SPEED)

    while run:
        run = handle_events()
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
