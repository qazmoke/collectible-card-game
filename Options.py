import pygame, sys
from pygame.locals import *

pygame.init()

#Create a displace surface object
#Below line will let you toggle from maximize to the initial size
DISPLAYSURF = pygame.display.set_mode((400, 300), RESIZABLE)

mainLoop = True

while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
    pygame.display.update()

pygame.quit()