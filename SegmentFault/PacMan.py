"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : PacMan.py
AUTHOR       : Juhász Pál Lóránd; Őri Gergely László; Seregi Bálint Leon; Bozsóki Márk
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
Driver class and main script for our program

********************************************************************
********************************************************************
"""

import os
import threading
import time
from source.TimerThread import TimeCounter
from source.Config import Config
from source.dynamic_elements.Direction import Direction
from source.dynamic_elements.moveables.Player import Player
from source.map.MapData import MapData
from source.map.MapDataReader import MapDataReader
from source.map.MapGenerator import MapGenerator
from source.ui.Terminal import Terminal
from source.ui.Inputs import Inputs
from source.ui.GrayScaleVisualizer import GrayScaleVisualizer

class PacMan:
    def __init__(self):
        self.game_over = False

        self.terminal = Terminal()
        self.config = Config()
        #self.GAMEMODE, self.TIMEOUTLIMIT, self.MAP, self.GAMESPEED = Config.Getsettings()
        self.GAMEMODE, self.TIMEOUTLIMIT, self.MAP, self.GAMESPEED = self.config.Getsettings()
        self.timer = TimeCounter(self.TIMEOUTLIMIT)

        # init empty mapdata
        self.mapdata = MapData()

        self.show_menu()


    def show_menu(self):
        menuinput = Inputs.Nothing

        while menuinput != "exit":

            self.terminal.show_menu("Main Menu", self.terminal.main_menuitems)
            menuinput = self.terminal.get_menu_input("Choose menu option!", self.terminal.main_menuitems)

            # START GAME
            if menuinput == "start game":
                self.start_game_session()
                menuinput = Inputs.Nothing

            # GAMEMODE SETTINGS
            if menuinput == "game mode":
                while menuinput != "back":
                    self.terminal.show_menu("Change Gamemode", self.terminal.gamemode_menuitems)
                    menuinput = self.terminal.get_menu_input("Choose gamemode option!", self.terminal.gamemode_menuitems)
                    
                    if menuinput == "standard":
                        self.GAMEMODE = "standard"

                    if menuinput == "sandbox":
                        self.GAMEMODE = "sandbox"

            # MAP SETTINGS
            if menuinput == "change map":
                while menuinput != "back":
                    self.terminal.show_menu("Maps", self.terminal.changemap_menuitems)
                    menuinput = self.terminal.get_menu_input("Choose map option!", self.terminal.changemap_menuitems)
                    
                    if menuinput == "Basic":
                        self.MAP = "Basic.mapdat"
                    
                    if menuinput == "Bosch ASDIIE":
                        self.MAP = "Bosch ASDIIE.mapdat"

                    if menuinput == "Clyde's Maze":
                        self.MAP = "Clyde's Maze.mapdat"

                    if menuinput == "Double Trouble":
                        self.MAP = "Double Trouble.mapdat"

                    if menuinput == "Horizontal":
                        self.MAP = "Horizontal.mapdat"

                    if menuinput == "Vertical":
                        self.MAP = "Vertical.mapdat"

                    self.GAMEMODE = "standard"

                    #TODO: MAPDATA change based on the files contained in the "maps" directory
        
        self.terminal.clear()


    def start_game_session(self):

        #TODO: init mapdata based on config

        # init mapdata
        if self.GAMEMODE == "standard":
            map_reader = MapDataReader()
            map_reader.load_mapdata(self.MAP)
            self.mapdata = map_reader.fill_mapdata()
        else:
            map_generator = MapGenerator()
            map_generator.generate_mapdata(map_width=25, map_height=25)
            self.mapdata = map_generator.fill_mapdata()
            

        #self.timer.reset()
        #self.timer.run()

        # start game
        player_input_thread = threading.Thread(target=self.get_user_input())
        game_state = threading.Thread(target=self.render_game_state())

        player_input_thread.start()
        game_state.start()

        # gameover
        player_input_thread.join()
        game_state.join()

        #self.timer.stop()


    def get_user_input(self):
        player_input = Inputs.Nothing

        #TODO: init Ghosts based on config

        # init Player (PacMan)
        player = Player(self.mapdata, self.mapdata.Player, Direction.Down)

        # prevent for instant gameover for sandbox mode
        if self.GAMEMODE == "sandbox":
            for safe_direction in Direction.__members__.values():
                if not player.is_wall_infront(self.mapdata, player.position, safe_direction):
                    player.direction = safe_direction

        #TODO: init enemies and collectables

        while not self.game_over or not self.timer.is_timeout:
            self.terminal.clear()
            self.terminal.show_title()

            player_input = self.terminal.get_gameplay_input("Set new direction!")

            if player_input == Inputs.Restart:
                #TODO: implement game restart logic
                self.restart_game_session()
                break

            if player_input == Inputs.Exit:
                self.game_over = True
                break

            # direction changing
            if player_input == Inputs.SetDirection_Up:
                player.next_direction = Direction.Up

            if player_input == Inputs.SetDirection_Right:
                player.next_direction = Direction.Right
            
            if player_input == Inputs.SetDirection_Down:
                player.next_direction = Direction.Down

            if player_input == Inputs.SetDirection_Left:
                player.next_direction = Direction.Left

            # refresh player position
            if self.GAMEMODE == "sandbox":
                # game over in sandbox mode if player hits the wall
                last_player_position = player.position
                if player.get_next_position() == last_player_position:
                    # if the player not moved, than reached a wall -> game over
                    break
            else:
                player.position = player.get_next_position()

            # game session timeout
            if self.timer.is_timeout():
                break

        game_time = 2#self.timer.seconds_passed()
        self.terminal.show_gameplayresult(game_time, player.score)


    def render_game_state(self):
        visualiser = GrayScaleVisualizer(size_ratio=10)

        while not self.game_over or not self.timer.is_timeout:
            visualiser.refresh_game_state(self.mapdata)
            visualiser.render_game_state(self.mapdata.size)

            time.sleep(self.GAMESPEED)


    def restart_game_session(self):
        #TODO: implement session restart
        pass

# program entry point
if __name__ == "__main__":
    Game = PacMan()