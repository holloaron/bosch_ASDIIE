"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Config.py
/ AUTHOR       : Pal Lorand Juhasz
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/
Creates and handles arguments

optional arguments:
  -h, --help            show this help message and exit
  --gamemode GAMEMODE, -gm GAMEMODE
                        Determins game type, standard/sandbox
  --timeout TIMEOUT, -to TIMEOUT, --int TIMEOUT
                        Determins the time in seconds after the game ends. By default it is 180 s
  --mapdata MAPDATA, -md MAPDATA, --str MAPDATA
                        The path of the mapdata container file, but generated can be used
  --gamespeed GAMESPEED, -gs GAMESPEED
                        Value of the gamespeed

/*********************************************************************
/*********************************************************************
"""

import argparse


class Config():
    
    def __init__(self) -> None:
        self.Arguments = argparse.ArgumentParser(prog = "SegmentFault's Pacman")
        self.AddArguments()
        self.GivenArguments = self.Arguments.parse_args()

    """ Initializes the flag with the help of argparse module
    @args:
        self
    @return:
            None
    """
    def AddArguments(self) -> None:
        self.Arguments.add_argument("--gamemode", "-gm", action='store',
                                    help="Determins game type, standard/sandbox ", default="standard")
        self.Arguments.add_argument("--timeout", "-to", '--int',
                                    help="Determins the time in seconds after the game ends. By default it is 180 s",
                                    default="180")
        self.Arguments.add_argument("--mapdata", "-md", '--str',
                                    help="The path of the mapdata container file, but generated can be used",
                                    default="Basic.mapdat")
        self.Arguments.add_argument("--gamespeed", "-gs", help="Value of the gamespeed", default=1)


    """ Returns the value of the given gamemode flag
    @args:
        self

    @return:
            gamemode [str]
    """
    def GetGamemode(self) -> str:
        gamemode = self.GivenArguments.gamemode
        return gamemode

    """ Returns the value of the given timeout flag
    @args:
        self

    @return:
            Timeout[int]
    """
    def GetTimeout(self) -> int:
        Timeoutlimit = self.GivenArguments.timeout
        return int(Timeoutlimit)

    """ Returns the value of the given mapdata flag
        @args:
            self

        @return:
                Mapdatafile[str]
    """
    def GetMapdata(self) -> str:
        Mapdatafile = self.GivenArguments.mapdata
        return Mapdatafile

    """ Returns the value of the given GameSpeed flag
    @args:
        self

    @return:
            GameSpeed[int]
    """
    def GetGamespeed(self) -> int:
        GameSpeed = self.GivenArguments.gamespeed
        return int(GameSpeed)