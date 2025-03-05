import pygame

from circleshape import CircleShape

class Asteroid(CircleShape): #inherits Circle Shape class
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)  # White outline

    def update(self, dt):
        self.position += self.velocity * dt