import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version : {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)





    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        for roid in asteroids:
            if roid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for roid in asteroids:
            for shot in shots:
                if roid.collides_with(shot):
                    log_event("asteroid_shot")
                    roid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
