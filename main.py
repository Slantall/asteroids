import pygame
import sys
from constants import * 
from circleshape import * 
from player import * 
from asteroid import * 
from asteroidfield import * 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for item in updatable:
            item.update(dt)

        for item in asteroids:
            if player.collisions(item):
                print("Game over!")
                sys.exit()
        
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        



if __name__ == "__main__":
    main()
