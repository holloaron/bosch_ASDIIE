from field import Field
from thing import Thing
from drawingService import DrawingService


class Coin_holder(Field):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.things = []
        self.neighbors = {
            'DOWN': None,
            'UP': None,
            'RIGHT': None,
            'LEFT': None,
        }
