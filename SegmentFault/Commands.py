"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Commands.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Collection of command definitions and command parser

/*********************************************************************
/*********************************************************************
"""
from enum import Enum

class Commands(str, Enum):
    SetDirection_Up = 'w'
    SetDirection_Right = 'd'
    SetDirection_Down = 's'
    SetDirection_Left = 'a'
    Restart = "restart"
    Exit = "exit"
    Nothing = ""


def command_parser(user_input: str) -> str:
    """ Checks the input format
        Allows case-insensitivity
        Allows aliases for command

    @args:
        user_input [str] - string command provided from the user
    @return:
        parsed_command [str] - input command that the program able to handle
    """

    # case-insesitive parsing
    parsed_command = user_input.lower()
    if parsed_command in Commands.__members__.values():
        return parsed_command
    
    # directional aliases
    if parsed_command == '0':
        return Commands.SetDirection_Up
    if parsed_command == '1':
        return Commands.SetDirection_Right
    if parsed_command == '2':
        return Commands.SetDirection_Down
    if parsed_command == '3':
        return Commands.SetDirection_Left
    
    # restart aliases
    restart_aliases = ["new", "reset", 'r']
    if parsed_command in restart_aliases:
        return Commands.Restart

    # exit aliases
    exit_aliases = ["end", "quit", 'q']
    if parsed_command in exit_aliases:
        return Commands.Exit

    # input cannot be parsed and there is no alias
    return Commands.Nothing


def is_movement_command(command: Commands) -> bool:
    """ Determines if the given command is
    
    """
    if command == Commands.SetDirection_Up:
            return True
    
    if command == Commands.SetDirection_Right:
            return True

    if command == Commands.SetDirection_Down:
            return True

    if command == Commands.SetDirection_Left:
            return True
    
    return False