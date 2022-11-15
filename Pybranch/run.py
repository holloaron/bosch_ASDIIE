import pygame
import sys
from pygame.locals import *

from Pybranch.core.game import Game


pygame.init()

# The game refresh rate
FPS = 60
FramePerSec = pygame.time.Clock()


if __name__ == "__main__":
    Game_Run = Game()

    Game_Run.game_scene.starting_map()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        Game_Run.run()
        Game_Run.game_over()

        pygame.display.update()
        FramePerSec.tick(FPS)
