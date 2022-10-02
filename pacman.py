# pacman code for ASDIIE
# Authors: Sárdi Ferenc Zsolt
# Note: I've seen this visualizing method in the code of team Namco. It is useful for me because my computer can't handle the opening window for some reason.

import numpy as np
import os

EMPTY = 0
PACMAN = 1
FOOD = 2
UPPER_WALL = 3
LOWER_WALL = 3
LEFT_WALL = 4
RIGHT_WALL = 4

class PacMan:
    # In this function the initial variables are declared.
    def __init__(self, map_size, num_of_food, max_step):
        # Function parameters:
        # map_size: maximal coordinates of the map
        # num_of_food: number of the placed food on the map
        # max_step: after this condition fullfilled the program stops

        self.map_size = map_size
        self.step_counter = 0
        self.max_step = max_step
        self.food = []
        self.num_of_food = num_of_food
        self.pacman = [0, 0]
        self.score = 0

        self.upper_wall = np.arange(0, map_size+2)
        self.lower_wall = np.arange(0, map_size+2)
        self.left_wall = np.arange(1, map_size+1)
        self.right_wall = np.arange(1, map_size+1)

    # In this function I placed the components and create the first visualization of the map
    def reset(self):
        
        self.place_pacman()
        self.place_food()
        visualization = self.create_visualization()

        # return the visualization of the map
        return visualization

    # In this function I calculated the new position of the map and check if any food is eaten
    def step(self, pressed_key):
        
        # Function parameters:
        # pressed_key: input from the user to determine the step direction 
        self.step_counter += 1
        self.new_position_of_pacman(pressed_key)
        self.eating_food()
        visualization = self.create_visualization()

        # We stop the loop when the step counter passes the step limit
        stop_the_game = False
        if self.step_counter > self.max_step:
            stop_the_game = True

        # return the visualization of the map, the score, or the fact if the program stops
        return visualization, self.score, stop_the_game

    # In this function I printed the actual step into the terminal
    def render(self, visualization):

        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Convert array to a list
        visualization = visualization.tolist()

        # In the map matrix I replaced the numerical values by symbols
        for x in range(self.map_size+2):
            for y in range(self.map_size+2):
                if visualization[x][y] == EMPTY:
                    visualization[x][y] = ' '
                elif visualization[x][y] == UPPER_WALL:
                    visualization[x][y] = '='
                elif visualization[x][y] == LOWER_WALL:
                    visualization[x][y] = '='
                elif visualization[x][y] == LEFT_WALL:
                    visualization[x][y] = '|'
                elif visualization[x][y] == RIGHT_WALL:
                    visualization[x][y] = '|'
                elif visualization[x][y] == PACMAN:
                    visualization[x][y] = 'C'
                elif visualization[x][y] == FOOD:
                    visualization[x][y] = '*'

        # Printing the score board and the map
        for line in visualization:
            print(*line, sep='  ')

        print("\nSCORE:", self.score)

    # In this function I created the initial position of the pacman
    def place_pacman(self):
        
        self.pacman[0] = np.random.randint(1, self.map_size-1)
        self.pacman[1] = np.random.randint(1, self.map_size-1)
    
    # In this function I created the postions of the food
    def place_food(self):

        for _ in range(self.num_of_food):
            food_coords = tuple(np.random.randint(1, self.map_size-1, (2,)))

            while (food_coords in self.food) or (food_coords == tuple(self.pacman)):
                food_coords = tuple(np.random.randint(1, self.map_size-1, (2,)))

            self.food.append(food_coords)

    # In this function I checked if the pacman position identical with any of the food positions
    def eating_food(self):

                for food in self.food:
                    if food == tuple(self.pacman):
                
                        self.score += 1
                        self.food.remove(food)
    
    # In this function the new position of the pacman are calculated based on the pressed key
    def new_position_of_pacman(self, pressed_key: str):

        if pressed_key == 'w':
            self.pacman[0] = max(self.pacman[0] - 1, 0)

        elif pressed_key == 'a':
            self.pacman[1] = max(self.pacman[1] - 1, 0)

        elif pressed_key == 's':
            self.pacman[0] = min(self.pacman[0] + 1, self.map_size - 1)

        elif pressed_key == 'd':
            self.pacman[1] = min(self.pacman[1] + 1, self.map_size - 1)
        
        elif pressed_key == 'q':
            quit()

    # In this function I assigned labels to the different components of the map matrix
    def create_visualization(self):

        visualization = np.zeros((self.map_size+2, self.map_size+2), dtype=int)

        for upper_bound in self.upper_wall:
            visualization[0, upper_bound] = UPPER_WALL

        for lower_bound in self.lower_wall:
            visualization[map_size+1, lower_bound] = LOWER_WALL
        
        for left_bound in self.left_wall:
            visualization[left_bound, 0] = LEFT_WALL

        for right_bound in self.right_wall:
            visualization[right_bound, map_size+1] = RIGHT_WALL

        visualization[self.pacman[0]+1, self.pacman[1]+1] = PACMAN

        for food in self.food:
            visualization[food[0]+1, food[1]+1] = FOOD

        # return of the numerical arry for the visualization
        return visualization

if __name__ == "__main__":

    # Asking the user for the intial parameters
    map_size = int(input("What map size would you like to play with? "))
    num_of_food = int(input("How many food would you like on the map? "))

    # Running the enviroment
    env = PacMan(map_size,
                 num_of_food,
                 max_step=100)

    # Clear the enviroment             
    state = env.reset()
    env.render(state)

    done = False

    # Running the main loop
    while not done:
        user_input = input("Move by pressing 'w, a, s, d' or quit by pressing 'q': ")
        state, reward, done = env.step(user_input)
        env.render(state)
