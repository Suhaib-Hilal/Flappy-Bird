import sys
import pygame
from pygame import mixer
from src.bird import Bird

from src.obstacles import Ground
from src.constants import FPS, HEIGHT, WIDTH


def main():
    """Start Here"""

    # Intialize pygame
    pygame.init()

    # Initialize mixer
    mixer.init()
    mixer.music.load("music/background.mp3")

    # Create window
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    pygame.display.set_icon(pygame.image.load("flappy.ico"))

    # Create ground
    ground = Ground(0, HEIGHT - 168, pygame.image.load("sprites/base.png"))

    # Create sky
    sky = pygame.image.load("sprites/background.png")

    # Create bird
    birds = {
        "sprites/redbird-0.png": [pygame.image.load("sprites/redbird-0.png"), pygame.image.load("sprites/redbird-1.png"), pygame.image.load("sprites/redbird-2.png")], 
        "sprites/bluebird-0.png": [pygame.image.load("sprites/bluebird-0.png"), pygame.image.load("sprites/bluebird-1.png"), pygame.image.load("sprites/bluebird-2.png")], 
        "sprites/yellowbird-0.png": [pygame.image.load("sprites/yellowbird-0.png"), pygame.image.load("sprites/yellowbird-1.png"), pygame.image.load("sprites/yellowbird-2.png")],
    }
    bird = Bird(200, 200, birds)

    # Create clock
    CLOCK = pygame.time.Clock()

    start = True
    game_on = False

    # Game loop
    while True:

        # Event loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start = False
                game_on = True
                bird.jump()


        # Draw surfaces
        WINDOW.blit(sky, (0, 0))
        bird.draw(WINDOW)
        ground.draw(WINDOW)

        # Show message
        if start:
            WINDOW.blit(pygame.image.load("sprites/message.png"), (320, 100))

        # Animate ground
        if game_on:
            if bird.check_collision(ground.ground_rect):
                game_on = False
            else:
                bird.animate()
                ground.animate()

        # Update display
        CLOCK.tick(FPS)
        pygame.display.update()
