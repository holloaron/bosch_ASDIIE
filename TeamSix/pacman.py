import pygame

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900


class Pacman:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('TeamSix Pacman')
        self.game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


if __name__ == '__main__':
    game = Pacman()
