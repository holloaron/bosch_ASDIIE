from enum import Enum


class Constants(Enum):
    """
    Constants for action selection and tile symbols
    """
    UP = 'w'
    RIGHT = 'd'
    DOWN = 's'
    LEFT = 'a'
    AGENT_SLOT = '0'
    RESTRICTED_SLOT = '#'
    AWARD_SLOT = '-'
    TERMINATING_SLOT = 'X'
    EMPTY_SLOT = ' '
