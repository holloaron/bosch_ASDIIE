"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : ActionParser.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Collection of action definitions and implementations from the player

/*********************************************************************
/*********************************************************************
"""

from enum import Enum

class Action(str, Enum):
    """ Collection of actions
    """
    Up = 'w'
    Right = 'd'
    Down = 's'
    Left = 'a'
    Restart = "restart"
    Exit = "exit"
    Nothing = ""


def action_parser(user_input: str) -> str:
    """ Checks the input format
        Allows case-insensitivity
        Allows aliases for actions

    @args:
        user_input [str] - string command provided from the user
    @return:
        action [str] - input command that the program able to handle
    """

    # case-insesitive parsing
    parsed_action = user_input.lower()
    if parsed_action in Action.__members__.values():
        return parsed_action
    
    # directional aliases
    if parsed_action == '0':
        return Action.Up
    if parsed_action == '1':
        return Action.Right
    if parsed_action == '2':
        return Action.Down
    if parsed_action == '3':
        return Action.Left
    
    # restart aliases
    restart_aliases = ["new", "reset", 'r']
    if parsed_action in restart_aliases:
        return Action.Restart

    # exit aliases
    exit_aliases = ["end", "quit", 'q']
    if parsed_action in exit_aliases:
        return Action.Exit

    # input cannot be parsed and there is no alias
    return Action.Nothing