from random import choice
import pygame

class Bird:
    def __init__(self, x: int, y: int, birds: dict):
        self.x = x
        self.y = y
        self.birds = birds
        self.chosen_bird = choice(list(birds.keys()))
        self.bird = pygame.image.load(self.chosen_bird)
        self.fying = False
        self.bird_rect = self.bird.get_rect()
        self.bird_animations = birds[self.chosen_bird]

    def draw(self, window: pygame.Surface):
        window.blit(self.bird, (self.x, self.y))

    def animate(self, window: pygame.Surface):
        for bird in self.bird_animations:
            self.bird = pygame.image.load(bird)
            self.draw(window)

    def jump(self, ground_rect: pygame.Rect):
        if not self.fying:
            self.y -= 100
            self.flying = True
            while not self.bird_rect.colliderect(ground_rect):
                self.y += 100
            self.flying = False

    def check_collision(self):
        pass
