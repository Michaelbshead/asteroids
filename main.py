# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main ():
    pygame.init()

    # Create a clock object to set frame rate
    clock  = pygame.time.Clock()
    # Initialize delta time
    dt = 0
    #create two groups
    # Updating
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)



    #create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Instantiate payer at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Allows quitting the game
    
        updatable.update(dt)
        screen.fill("black") # Clear the screen
        
        
        player.update(dt)
        for obj in drawable: # Draw Multi[ple Objects]
            obj.draw(screen)

        pygame.display.flip() # Update Display

        #Control the framerate and calcualte delta time
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()

