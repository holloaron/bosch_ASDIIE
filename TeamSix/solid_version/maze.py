import random
import numpy as np
from steppable import Steppable
from pacman import Pacman
from drawable import Drawable
from constans import Constants
from wall import Wall
from coin_holder import Coin_holder
from coin import Coin


class Maze(Drawable, Steppable):
    def __init__(self) -> None:
        self.fields = list(range(10))
        for f in range(0, len(self.fields)):
            self.fields[f] = list(range(10))
    def init(self):
        # generate outer walls
        for x in range(0, Constants.MAZE_SIZE_X.value):
            self.fields[x][0] = Wall(x, 0)
            self.fields[x][Constants.MAZE_SIZE_Y.value - 1] = Wall(x, Constants.MAZE_SIZE_Y.value - 1)
        for y in range(0, Constants.MAZE_SIZE_Y.value):
            self.fields[0][y] = Wall(0, y)
            self.fields[Constants.MAZE_SIZE_X.value - 1][y] = Wall(Constants.MAZE_SIZE_X.value - 1, y)

        # other tiles are empty or walls
        for x in range(1, Constants.MAZE_SIZE_X.value - 1):
            for y in range(1, Constants.MAZE_SIZE_Y.value - 1):
                # 10% chance of placing a wall, others are empty or have a coin with 30% chance
                chance_wall = random.randint(0, 9)
                if chance_wall == 0:
                    self.fields[x][y] = Wall(x, y)
                else:
                    coin_field = Coin_holder(x, y)
                    if random.randint(1, 9) == 1:
                        coin_field.things.append(Coin(coin_field))
                    self.fields[x][y] = coin_field

        self.set_neighbors()

    def set_neighbors(self):
        for x in range(0, Constants.MAZE_SIZE_X.value):
            for y in range(0, Constants.MAZE_SIZE_Y.value):
                if x > 0:
                    self.fields[x][y].neighbors['LEFT'] = self.fields[x - 1][y]
                if y > 0:
                    self.fields[x][y].neighbors['UP'] = self.fields[x][y - 1]
                if x < Constants.MAZE_SIZE_X.value - 1:
                    self.fields[x][y].neighbors['RIGHT'] = self.fields[x + 1][y]
                if y < Constants.MAZE_SIZE_Y.value - 1:
                    self.fields[x][y].neighbors['DOWN'] = self.fields[x][y + 1]
