from random import choice
import pygame

class Bird:
    def __init__(self, x: int, y: int, birds: dict):
        self.birds = birds
        self.chosen_bird = choice(list(birds.keys()))
        self.bird = pygame.image.load(self.chosen_bird)
        self.gravity = 0.3
        self.y_velocity = 1
        self.max_velocity = 4
        self.bird_rect = self.bird.get_rect()
        self.bird_rect.x = x
        self.bird_rect.y = y
        self.bird_animations = birds[self.chosen_bird]
        self.flap_state = 0
        self.flap_timer = 0
        self.rotation = 0
        self.jump_velocity = self.max_velocity * 20

    def draw(self, window: pygame.Surface):
        rotated_bird = pygame.transform.rotate(self.bird_animations[self.flap_state], self.rotation)
        rotated_rect = rotated_bird.get_rect()
        rotated_rect.center = self.bird_rect.center
        window.blit(rotated_bird, rotated_rect)

    def animate(self):
        self.flap_timer += 1
        for bird in self.bird_animations:
            if self.flap_timer > 10:
                self.flap_state = (self.flap_state + 1) % 3
                self.flap_timer = 0
            self.bird = bird
            
        self.apply_gravity()

    def jump(self):
        self.bird_rect.y -= self.jump_velocity
        # self.rotation = -self.jump_velocity * 5
        # self.bird = pygame.transform.rotate(self.bird, self.rotation)

    def apply_gravity(self):
        # self.rotation = self.jump_velocity * 5
        self.bird_rect.y += self.y_velocity
        if self.y_velocity <= self.max_velocity:
            self.y_velocity += self.gravity
        # self.bird = pygame.transform.rotate(self.bird, self.rotation)

    def check_collision(self, collision_rect: pygame.Rect) -> bool:
        return self.bird_rect.colliderect(collision_rect)
