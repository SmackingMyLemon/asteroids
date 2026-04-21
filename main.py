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
    score = 0
    player_lives = 3

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
    bg = pygame.image.load("hbyjPE.png").convert()
    bg = pygame.transform.scale(bg, (1280, 720))
    text = pygame.font.SysFont("Arial", 36)





    while True:
        log_state()
        score_surface = text.render(f"Score: {score}", True, "White")
        life_surface = text.render(f"Lives: {player_lives}", True, "White")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(bg, (0, 0))
        screen.blit(score_surface, (50, 50))
        screen.blit(life_surface, (1100, 50))
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        for roid in asteroids:
            if roid.collides_with(player):
                log_event("player_hit")
                if player_lives > 1:
                    player_lives -= 1
                    player.kill()                    
                    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
                else:
                    print("Game over!")
                    sys.exit()
        for roid in asteroids:
            for shot in shots:
                if roid.collides_with(shot):
                    log_event("asteroid_shot")
                    score += roid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
