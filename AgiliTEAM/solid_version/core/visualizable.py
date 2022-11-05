from abc import ABC, abstractmethod

from bosch_ASDIIE.solid_version.core.canvas import Canvas


class Visualizable(ABC):
    @abstractmethod
    def draw(self, canvas: Canvas):
        pass