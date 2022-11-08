from direction import Direction
from constans import Constants
from maze import Maze
import pygame
from drawingService import DrawingService
from time import sleep


class Game:
    def __init__(self):
        self.maze = None
        self.start_game()
    def start_game(self):
        self.maze = Maze()
        self.maze.init()
if __name__ == '__main__':
    game = Game()
