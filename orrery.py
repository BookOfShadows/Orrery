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

Fullscreen = False

background = pygame.Surface(SCREEN_SIZE)
background = background.convert()
background.fill((0, 0 ,0))

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

  screen.blit(background, (0, 0))

  pygame.display.update()