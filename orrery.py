import math
from math import *

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# variables
APP_NAME = "Orrery"
SCREEN_SIZE = (640, 480)
message = "ELLW CARMARA "

pygame.display.set_caption(APP_NAME)

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

Fullscreen = False

background = pygame.Surface(SCREEN_SIZE)
background = background.convert()
background.fill((0, 0 ,0))

font = pygame.font.SysFont("arial", 80)
text_surface = font.render(message, True, (0, 0, 255))

x = 0
y = ( SCREEN_SIZE[1] - text_surface.get_height() ) / 2

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

  x-= 2
  if x < -text_surface.get_width():
    x = 0

  screen.blit(background, (0, 0))
  screen.blit(text_surface, (x, y))
  screen.blit(text_surface, (x+text_surface.get_width(), y))
  pygame.display.update()