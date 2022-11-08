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

    def accept(self, t: Thing):
        for thing in self.things:
            t.collide_with(thing)
        self.things.append(t)
        t.field = self

    def remove(self, t: Thing):
        self.things.remove(t)

    def draw(self, service: DrawingService):
        service.draw_field(self.position_x, self.position_y, 'blank')
        for t in self.things:
            t.draw(service)
