from collections import deque
from typing import List
from bosch_ASDIIE.solid_version.core.canvas import Canvas
from bosch_ASDIIE.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.solid_version.core.map import Coordinates, MapSize
from bosch_ASDIIE.solid_version.core.snake import Snake
from bosch_ASDIIE.solid_version.gui.console_canvas import ConsoleCanvas


class SpyCanvas(Canvas):
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self._dots_on_canvas = []

    @property
    def dots_on_canvas(self):
        return self._dots_on_canvas

    def draw_dots(self, coordinates: List[Coordinates]):
        self._dots_on_canvas.extend(coordinates)
        self.canvas.draw_dots(coordinates)

    def clear(self):
        self._dots_on_canvas = []

    def render(self):
        pass


def testCanvas_whenSnakeMoving_thenNewHeadAppearsAndTailDisappears():
    canvas = ConsoleCanvas(10, 10)
    spy_canvas = SpyCanvas(canvas)
    snake = Snake(
        deque([Coordinates(0, 1), Coordinates(0, 2), Coordinates(0, 3)]),
        starting_direction=KeyEvent.RIGHT
    )
    snake.draw(spy_canvas)
    dots_before_moving = spy_canvas.dots_on_canvas
    spy_canvas.clear()
    snake.tick()
    snake.draw(spy_canvas)
    dots_after_moving = spy_canvas.dots_on_canvas
    assert Coordinates(0, 1) in dots_before_moving and \
           Coordinates(0, 1) not in dots_after_moving, \
        "The tail should not be on the canvas after moving."
    assert Coordinates(0, 4) not in dots_before_moving and \
           Coordinates(0, 4) in dots_after_moving, \
        "The head should be moved on canvas after snake moving."


def testCanvas_whenSnakeMoving_thenOppositeKeyEventDoesNotDoAnything():
    canvas = ConsoleCanvas(10, 10)
    spy_canvas = SpyCanvas(canvas)
    snake = Snake(
        deque([Coordinates(0, 1), Coordinates(0, 2), Coordinates(0, 3)]),
        starting_direction=KeyEvent.RIGHT
    )
    snake.draw(spy_canvas)
    dots_before_moving = spy_canvas.dots_on_canvas
    spy_canvas.clear()
    snake.take_action(KeyEvent.LEFT)
    snake.tick()
    snake.draw(spy_canvas)
    dots_after_moving = spy_canvas.dots_on_canvas
    assert Coordinates(0, 1) in dots_before_moving and \
           Coordinates(0, 1) not in dots_after_moving, \
        "The tail should not be on the canvas after moving."
    assert Coordinates(0, 4) not in dots_before_moving and \
           Coordinates(0, 4) in dots_after_moving, \
        "The head should be moved to forward the original direction " \
        "after snake got opposite KeyEvent."

def testCanvas_whenSnakeHitTheEndOfCanvas_thenAppearsOnOppositeSide():
    canvas = ConsoleCanvas(5, 5)
    spy_canvas = SpyCanvas(canvas)
    snake = Snake(
        deque([Coordinates(0, 3), Coordinates(0, 2), Coordinates(0,1)]),
        starting_direction=KeyEvent.LEFT,
        map_size=MapSize(5, 5)
    )
    snake.tick()
    snake.tick()
    snake.take_action(KeyEvent.UP)
    snake.tick()
    snake.take_action(KeyEvent.RIGHT)
    snake.tick()
    snake.take_action(KeyEvent.DOWN)
    snake.tick()
    snake.draw(spy_canvas)
    body_on_canvas = spy_canvas.dots_on_canvas
    assert Coordinates(0, 0) in body_on_canvas and \
           Coordinates(4, 0) in body_on_canvas and \
           Coordinates(4, 4) in body_on_canvas, \
        "The snake should be reappear on the opposite side of the screen " \
        "when it hits the end of the screen."