from abc import ABC, abstractmethod
from typing import List

from bosch_ASDIIE.solid_version.core.map import Coordinates


class Canvas(ABC):
    @abstractmethod
    def draw_dots(self, coordinates: List[Coordinates]):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def clear(self):
        pass