import sys
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
  pygame.init()

  # create clock object for fps 
  clock = pygame.time.Clock()
  dt = 0

  # set a new GUI window
  screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
  on = True

  # create groups for player
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group() 
  shots = pygame.sprite.Group()

  # set up containers for each class
  Player.containers = (updatable,drawable)
  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

  Asteroid.containers = (updatable, drawable, asteroids)

  AsteroidField.containers = updatable
  asteroidField = AsteroidField()

  Shot.containers = (updatable, drawable, shots)
  
  while on:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    # calls on player objects that are updatable / drawable 
    for sprite in updatable:
      sprite.update(dt)

    for asteroid in asteroids:
      if asteroid.collides_with(player):
        print("Game over!")
        sys.exit()

    screen.fill("black")

    for sprite in drawable:
      sprite.draw(screen)

    pygame.display.flip()

    # limit frames to 60 fps
    dt = clock.tick(60) / 1000


  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
  main()

