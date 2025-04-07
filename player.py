import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape): #inherits from CircleShape
    def __init__(self, x:int, y: int):
        super().__init__(x,y, PLAYER_RADIUS) # Call parent class constructor
        self.rotation = 0 # Initlaize rotaiton to 0 (upwards)
        self.shooting_cooldown_timer = 0 # Set variable
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  # White outline

    def rotate(self, dt):
        #Rotates the player counterclockwise
        self.rotation += PLAYER_TURN_SPEED * dt #increment rotation based on time
    
    def update(self, dt):
        self.shooting_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  #Rotates the player counterclockwise
        if keys[pygame.K_d]:
            self.rotate(dt) #Rotates the player clockwise
        if keys[pygame.K_w]:  # Move forward
            self.move(dt)
        if keys[pygame.K_s]:  # Move forward
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shooting_cooldown_timer > 0:
            return # Cant shoot yet

        # Create the bullet
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
         
        #Reset the timer after shooting
        self.shooting_cooldown_timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
