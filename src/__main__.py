import sys
import pygame
from src.constants import HEIGHT, WIDTH


def main():
    """Start Here"""

    # Intialize pygame
    pygame.init()

    # Create window
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    pygame.display.set_icon(pygame.image.load("flappy.ico"))

    # Game loop
    while True:

        # event loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update display
        pygame.display.update()
