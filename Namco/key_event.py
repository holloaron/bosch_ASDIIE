from enum import Enum


class KeyEvent(Enum):
    """
    Key events possibly detected while using the application
    """
    UP = 'w'
    RIGHT = 'd'
    DOWN = 's'
    LEFT = 'a'