# constants
SCREEN_SIZE = (640, 480)

# count every man made star
SAT_COUNT = (0)

import math
from math import *

import pygame
from pygame.locals import *

from gameobjects.vector2 import Vector2

from sys import exit

class World(object):
  
  def __init__(self):
    self.entities = {}
    self.entities_id = 0
    self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
    # paint black even the heavens
    self.background.fill((0, 0, 0))

  def add_sat(self, entity):
    self.entities[self.entity_id] = entity
    entity.id = self.entity_id

  def remove_sat(self, entity):
    del self.entities[entity.id]

  def get(self, entity_id):
    if entity_id in self.entities:
      return self.entities[entity_id]
    else:
      return None

  def process(self, time_passed):
    time_passed_seconds = time_passed / 1000.0
    for entity in self.entities.values():
      entity.process(time_passed_seconds)

  def render(self, surface):
    surface.blit(self.background, (0, 0))
    for entity in self.entities.itervalues():
      entity.render(surface)

class GameEntity(object):
  def __init__(self, world, name, image):
    self.world = world
    self.name = name
    self.image = image
    self.location = Vector2(0, 0)
    self.destination = Vector2(0, 0)
    self.speed = 0.

class satellite(GameEntity):
  def __init__(self, world, image):
    GameEntity.__init__(self, world, "satellite", image)
    self.id = 0.
    self.name = name
    self.location = Vector2(0, 0)
    self.destination = Vector2(0, 0)
    self.size = 0.
    self.speed = 0.

  def render(self, surface):
    x, y = self.location
    w, h = self.image.get_size()

  def process(self, time_passed):
    x, y = self.location

    GameEntity.process(self, time_passed)

def run():
  pygame.init()

  screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

  world = World()

  screen_width, screen_height = SCREEN_SIZE

  clock = pygame.time.Clock()

  # world.add_sat(satellite)

  while True:

    for event in pygame.event.get():
        if event.type == QUIT:
          exit()
        if event.type == KEYDOWN:
          if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
              screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
            else:
              screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
          if event.key == K_q:
            exit()

    time_passed = clock.tick(30)

    world.process(time_passed)
    world.render(screen)

    # the center of the geocentric universe
    carmara = pygame.draw.circle(screen, (255, 255, 255), ((screen_width / 2), (screen_height / 2)), screen_height / 2 - 100, 1)

    # set the wheels in motion
    pygame.display.update()

    # show me that the arrow flies
    print time_passed

if __name__ == "__main__":
  run()