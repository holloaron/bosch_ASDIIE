from __future__ import annotations
import abc

from steppable import Steppable
from drawingService import DrawingService
from drawable import Drawable


class Thing(Drawable, Steppable):

    def __init__(self, field):
        self.field = field

    @abc.abstractmethod
    def collide_with(self, t: Thing):
        pass

    @abc.abstractmethod
    def hit_by(self, p: Thing):
        pass

    @abc.abstractmethod
    def draw(self, service: DrawingService):
        pass
    def step(self):
        return
