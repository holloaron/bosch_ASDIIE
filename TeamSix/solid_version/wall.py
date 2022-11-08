from drawingService import DrawingService
from field import Field
from pacman import Pacman
from thing import Thing


class Wall(Field):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.things = []

    def accept(self, t: Thing):
        if type(t) is Pacman:
            t.die()
        self.things.append(t)
        t.field = self

    def remove(self, t: Thing):
        self.things.remove(t)

    def draw(self, service: DrawingService):
        service.draw_field(self.position_x, self.position_y, 'WALL')
