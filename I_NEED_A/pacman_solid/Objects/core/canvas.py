from abc import ABC, abstractmethod
from typing import List

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

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_width(self):
        pass