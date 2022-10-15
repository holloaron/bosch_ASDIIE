import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# The game refresh rate
FPS = 60
FramePerSec = pygame.time.Clock()

#Necessary colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#Screen, character and game settings
SCREEN_SIZE = 1000


#Game window creation and title
DISPLAYSURF = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("PACMAN")


if __name__ == "__main__":

    while True:
        DISPLAYSURF.fill(BLACK)

        pygame.display.update()
        FramePerSec.tick(FPS)