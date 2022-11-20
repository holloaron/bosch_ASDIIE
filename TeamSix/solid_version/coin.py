from drawingService import DrawingService
from pacman import Pacman
from interactable import Interactable


class Coin(Interactable):
    POINT_VALUE = 1

    def __init__(self, field):
        super().__init__(field)

    def hit_by(self, p: Pacman):
        p.add_points(self.POINT_VALUE)
        self.field.remove(self)

    def collide_with(self, i: Interactable):
        return

    def draw(self, service: DrawingService):
        service.draw_coin(self.field.position_x, self.field.position_y)

    
