import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import Asteroidfield
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    Asteroidfield.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = Asteroidfield()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill("black")
         
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
        
        for obj in updatable:
            obj.update(dt)
            
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # print(f"Tick: {clock.tick(FPS)} und dt: {dt}")
        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
