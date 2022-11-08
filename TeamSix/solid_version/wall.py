from drawingService import DrawingService
from field import Field
from pacman import Pacman
from thing import Thing


class Wall(Field):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.things = []

