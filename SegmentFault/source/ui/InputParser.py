"""
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : InputParser.py
/ AUTHOR       : 
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ 

/*********************************************************************
/*********************************************************************
"""

import Inputs

class InputParser():

    @staticmethod
    def parse(input: str) -> str:
        """ Parses the input from the console
        
        @args:
            input [str] - user input from the console
        @returns:
            parsed_input [str] - parsed input
        """
        input = input.lower()

        # case-insesitive input parsing
        if input in Inputs.__members__.values():
            return input

        # directional aliases
        if input == '1':
            return Inputs.SetDirection_Left
        if input == '2':
            return Inputs.SetDirection_Down
        if input == '3':
            return Inputs.SetDirection_Right
        if input == '5':
            return Inputs.SetDirection_Up
        
        # restart aliases
        restart_aliases = ["new", "reset"]
        if input in restart_aliases:
            return Inputs.Restart

        # exit aliases
        exit_aliases = ["end", "quit"]
        if input in exit_aliases:
            return Inputs.Exit

        # input cannot be parsed and there is no alias
        return Inputs.Nothing

    @staticmethod
    def parse(input: str, whitelist: list[str]) -> str:
        """ Parses the input from the console
        
        @args:
            input [str] - user input from the console
            whitelist [list(str)] - 
        @returns:
            parsed_input [str]
        """
        if input in whitelist:
            return input
        
        return Inputs.Nothing