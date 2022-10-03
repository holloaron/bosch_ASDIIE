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

    def __init__(self, map_size: int, num_of_food:int, max_step:int):
        """
        Initial parameters are created for the game
        :param map_size: dimension of the map [map_size x map_size] (int)
        :param num_of_food: number of food on the map (int)
        :param max_time_step: Length of the game in pacman steps (int)
        """
        
        #Initial parameters for the game
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

    def reset(self) -> np.ndarray:
        """
        Creating an initial enviroment
        :return: Initial state of the map (np.ndarray)
        """
        
        #Placing the basic components on the map
        self.place_pacman()
        self.place_food()
        visualization = self.create_visualization()

        return visualization

    def step(self, pressed_key: str) -> [np.ndarray, int, bool]:
        """
        Creates the map in the next step
        :param pressed_key: input for stepping pacman (w, a ,s or d) (str)
        :return: visualization of the map (np.ndarray), score (int), game stopping decision (bool)
        """
        
        #Moving to the next step
        self.step_counter += 1
        self.move_pacman(pressed_key)
        self.eat_food()
        visualization = self.create_visualization()

        #Checking if we reached the maxium num of steps
        stop_the_game = False
        if self.step_counter > self.max_step:
            stop_the_game = True

        return visualization, self.score, stop_the_game

    def render(self, visualization: np.ndarray):
        """
        Displays the map created in the last step
        :param visualization: The created map (np.ndarray)
        """
        #Clearing the console/terminal    
        os.system('cls' if os.name == 'nt' else 'clear')

        visualization = visualization.tolist()

        #Substituting the labeld map array elements by symbols
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
        
        #Printing the map and the score
        for line in visualization:
            print(*line, sep='  ')

        print("\nSCORE:", self.score)

    def place_pacman(self):
        """
        Generates the pacman coordinates
        """
        
        #Random coordinates for pacman
        self.pacman[0] = np.random.randint(1, self.map_size-1)
        self.pacman[1] = np.random.randint(1, self.map_size-1)
    
    def place_food(self):
        """
        Generates the pacman coordinates
        """
        
        #Random coordinates for the food
        for _ in range(self.num_of_food):
            food_coords = tuple(np.random.randint(1, self.map_size-1, (2,)))

            while (food_coords in self.food) or (food_coords == tuple(self.pacman)):
                food_coords = tuple(np.random.randint(1, self.map_size-1, (2,)))

            self.food.append(food_coords)

    def eat_food(self):
        """
        Check if the new position of the pacman equal with any of the food coordinates
        """
        
                for food in self.food:
                    if food == tuple(self.pacman):
                
                        self.score += 1
                        self.food.remove(food)
    
    def move_pacman(self, pressed_key: str):
        """
        Calculating the new position of the pacman based on the preessed key
        :param pressed_key: input for stepping pacman (w, a ,s or d) (str)
        """
        
        if pressed_key == 'w':
            self.pacman[0] = max(self.pacman[0] - 1, 0)

        elif pressed_key == 'a':
            self.pacman[1] = max(self.pacman[1] - 1, 0)

        elif pressed_key == 's':
            self.pacman[0] = min(self.pacman[0] + 1, self.map_size - 1)

        elif pressed_key == 'd':
            self.pacman[1] = min(self.pacman[1] + 1, self.map_size - 1)

    def create_visualization(self) -> np.ndarray:
        """
        Displaying the map
        :return: the array of the map (np.ndarray)
        """
        
        #Labeling the map array elements by the entity which they represent
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

        return visualization

if __name__ == "__main__":
    
    #Asking the user for the enviroment inputs
    map_size = int(input("What map size would you like to play with? (Suggested: 10...20) "))
    num_of_food = int(input("How many food would you like on the map? (Suggested: 1...100"))
    
    #Running the enviroment
    env = PacMan(map_size,
                 num_of_food,
                 max_step=100)
             
    state = env.reset()
    env.render(state)

    done = False
    
    #Running the game loop
    while not done:
        user_input = input("Move by pressing 'w, a, s, d' or quit by pressing 'q': ")
        state, reward, done = env.step(user_input)
        env.render(state)
