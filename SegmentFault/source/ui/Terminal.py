"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Terminal.py
/ AUTHOR       : 
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module responsible for terminal input and output

/*********************************************************************
/*********************************************************************
"""

import os
from posixpath import relpath

class Terminal():

    @staticmethod
    def show_menu(menuitems: dict) -> None:


        pass

    @staticmethod
    def show_gameplayresult() -> None:
        pass
    
    @staticmethod
    def show_title() -> None:
        current_dir = os.path.dirname(__file__)
        title_source_path = os.path.relpath("..\\data\\assets\\TerminalTitle.txt", current_dir)
        title = open(title_source_path, 'r')

        while True:
            line = title.readline()

            # EndOfFile
            if not line:
                break

            print(line)


    @staticmethod
    def clear():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    @staticmethod
    def get_input() -> str:
        pass