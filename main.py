# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)


    Player.containers = (updatable, drawable)




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

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
            if player.collides_with(asteroid):
                print("Game Over!")
                pygame.quit()
                sys.exit()
            


        screen.fill("black") # Clear the screen
        
#        player.update(dt)
        for obj in drawable: # Draw Multiple Objects]
            obj.draw(screen)

        pygame.display.flip() # Update Display

        #Control the framerate and calcualte delta time
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()

