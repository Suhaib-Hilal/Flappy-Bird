import pygame

class Ground:
    def __init__(self, x: int, y: int, image: pygame.Surface):
        self.image = image
        self.ground_rect = image.get_rect()
        self.ground_rect.x = x
        self.ground_rect.y = y
        self.animation_speed = 2
    
    def draw(self, window: pygame.Surface):
        window.blit(self.image, (self.ground_rect.x, self.ground_rect.y))
    
    def animate(self):
        if self.ground_rect.x >= -30:
            self.ground_rect.x -= self.animation_speed
        else:
            self.ground_rect.x = 0
