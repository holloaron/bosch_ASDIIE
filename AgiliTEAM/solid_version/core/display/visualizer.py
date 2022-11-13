from typing import List
from core.interface.canvas import Canvas
from core.interface.visualizable import Visualizable


class Visualizer:
    def __init__(self,
                 visualizable_objects: List[Visualizable],
                 canvas: Canvas):
        """

        :param visualizable_objects:
        :param canvas:
        """
        self.visualizable_objects = visualizable_objects
        self.canvas = canvas

    def render(self) -> None:
        """

        :return: None
        """
        self.canvas.clear()
        for obj in self.visualizable_objects:
            obj.draw(self.canvas)
        self.canvas.render()
