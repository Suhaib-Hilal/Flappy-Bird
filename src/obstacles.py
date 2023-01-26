import pygame

class Ground:
    def __init__(self, x: int, y: int, image: pygame.Surface):
        self.x = x
        self.y = y
        self.image = image
        self.ground_rect = image.get_rect()
        self.animation_speed = 2
    
    def draw(self, window: pygame.Surface):
        window.blit(self.image, (self.x, self.y))
    
    def animate(self):
        if self.x >= -30:
            self.x -= self.animation_speed
        else:
            self.x = 0
