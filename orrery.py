import math
from math import *

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# variables
APP_NAME = "Orrery"
SCREEN_SIZE = (640, 480)

pygame.display.set_caption(APP_NAME)

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
screen_width, screen_height = SCREEN_SIZE

Fullscreen = False

background = pygame.Surface(SCREEN_SIZE)
background = background.convert()
background.fill((0, 0 ,0))

class satellite:
  def __init__(self, name):
    sat_name = name
    sat_size = 0.
    sat_speed = 0.
    sat_location = Vector2(0, 0)
    sat_destination = Vector2(0, 0)
    sat_image = pygame.draw.ellipse(screen, (255, 255, 255), (carmara.width / 2, carmara.width / 2, 10, 10))
    sat_id = 0.

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

  # paint black even the heavens
  screen.blit(background, (0, 0))

  # news of great import!
  # circular heavenly bodies are defined by (plane, (colour - in rgb), (position), radius, width)
  # elliptical bodies are defined by (plane, (colour - in rgb), (pos x, pos y, width, height))

  # the center of the geocentric universe
  carmara = pygame.draw.circle(screen, (255, 255, 255), ((screen_width / 2), (screen_height / 2)), screen_height / 2 - 100, 1)

  sat1 = pygame.draw.ellipse(screen, (255, 255, 255), (carmara.width / 2, carmara.width / 2, 10, 10))

  pygame.display.update()