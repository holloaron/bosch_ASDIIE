from abc import ABC, abstractmethod

from bosch_ASDIIE.AgiliTEAM.solid_version.core.canvas import Canvas


class Visualizable(ABC):
    @abstractmethod
    def draw(self, canvas: Canvas):
        pass
