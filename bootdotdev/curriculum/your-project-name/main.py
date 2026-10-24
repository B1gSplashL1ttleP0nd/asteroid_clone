import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state
from logger import log_event
from shot import Shot






def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

      


if __name__ == "__main__":
    main()
