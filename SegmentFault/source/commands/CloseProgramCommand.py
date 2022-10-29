"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : ExitProgramCommand.py
/ AUTHOR       : Bozsóki Márk
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Closes the program

/*********************************************************************
/*********************************************************************
"""

import os
import CommandBase

class CloseProgramCommand(CommandBase):

    @staticmethod
    def execute() -> None:
        """ Forces the program to shut down
        """
        os._exit(0)