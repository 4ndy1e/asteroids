from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
  def __init__(self,x,y,radius):
    super().__init__(x,y,radius)

  def draw(self,screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      print("small radius")
      return
    else:
      # spawn two asteroids
      angle = random.uniform(20,50)
      vect1, vect2 = self.velocity.rotate(-angle), self.velocity.rotate(angle)
      newRadius = self.radius - ASTEROID_MIN_RADIUS 

      # create two new asteroids
      asteroid1, asteroid2 = Asteroid(self.position.x, self.position.y, newRadius), Asteroid(self.position.x, self.position.y, newRadius)
      asteroid1.velocity = vect1 * 1.2
      asteroid2.velocity = vect2 * 1.2








