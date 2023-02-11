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

class Pipe:
    def __init__(self, x: int, y: int, image: pygame.Surface) -> None:
        self.image = image
        self.rotated_image = pygame.transform.rotate(self.image, 180)
        self.pipe_rect = image.get_rect()
        self.pipe_rect.x = x
        self.pipe_rect.y = y
        self.animation_speed = 2

    def draw(self, window: pygame.Surface):
        window.blit(self.image, (self.pipe_rect.x, self.pipe_rect.y))
        window.blit(self.rotated_image, (self.pipe_rect.x, window.get_height()))

    def animate(self, window: pygame.Surface):
        pass
        
