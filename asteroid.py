import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape): #inherits Circle Shape class
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)  # White outline

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Will always kill current asteroid
        self.kill()

        # If asteroid is too small just stop
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

    # 1. Pick a random angle between 20 and 50 degrees
        random_angle = random.uniform(20,50)
    # 2. Create two new velocity directions, rotated left and right
        velocity_speed1 = self.velocity.rotate(random_angle)
        velocity_speed2 = self.velocity.rotate(-random_angle)
    # 3. Shrink the radius for the new asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

    # 4. Create two new Asteroid objects
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius) 
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

    # 5. Make them move faster
        asteroid1.velocity = velocity_speed1 * 1.2
        asteroid2.velocity = velocity_speed2 * 1.2