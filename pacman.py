import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# The game refresh rate
FPS = 60
FramePerSec = pygame.time.Clock()

# Necessary colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Screen, character and game settings
SCREEN_SIZE = 1000
DOT_SIZE = (20, 20)

#Game window creation and title
DISPLAYSURF = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("PACMAN")

class DOT(pygame.sprite.Sprite):
    def __init__(self):

        #Dot load from file and transform to the required size

        super().__init__()
        self.image = pygame.image.load('dot.png')
        self.image = pygame.transform.scale(self.image, DOT_SIZE)
        self.rect = self.image.get_rect()

if __name__ == "__main__":

    while True:
        DISPLAYSURF.fill(BLACK)

        pygame.display.update()
        FramePerSec.tick(FPS)