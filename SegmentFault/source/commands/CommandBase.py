"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : CommandBase.py
/ AUTHOR       : Bozsóki Márk
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Superclass for Commands

/*********************************************************************
/*********************************************************************
"""

class CommandBase():

    @staticmethod
    def execute() -> None:
        """ Defines the Commands core functionality
        @args:
            None
        @returns:
            None
        """
        pass


    @staticmethod
    def can_execute() -> bool:
        """ Determines if the Command is executable
        @args:
            None
        @returns:
            True, if the Command is executable
        """
        return True