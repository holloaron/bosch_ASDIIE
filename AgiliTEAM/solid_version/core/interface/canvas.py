from abc import ABC, abstractmethod
from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import Coordinates


class Canvas(ABC):
    @abstractmethod
    def draw_dots(self, coordinates: List[Coordinates], obj_type: str = None):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_width(self):
        pass
