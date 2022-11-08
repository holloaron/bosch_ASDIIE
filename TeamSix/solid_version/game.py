from direction import Direction
from constans import Constants
from maze import Maze
import pygame
from drawingService import DrawingService
from time import sleep


class Game:
    def __init__(self):
        self.maze = None
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption('TeamSix Pacman')
        screen = pygame.display.set_mode((Constants['WINDOW_WIDTH'].value, Constants['WINDOW_HEIGHT'].value))
        screen.fill(Constants['COLOR_BLACK'].value)
        fps = pygame.time.Clock()
        self.start_game()
        self.drawing_service = DrawingService(screen)
            self.maze.draw(self.drawing_service)
            self.pacman.draw(self.drawing_service)
            pygame.display.update()
            fps.tick(Constants.PACMAN_SPEED.value)
    def start_game(self):
        self.maze = Maze()
        self.maze.init()
        self.pacman = self.maze.place_pacman(1, 1)
if __name__ == '__main__':
    game = Game()
