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
        
        self.place_pacman()
        self.place_food()
        visualization = self.create_visualization()

        # return the visualization of the map
        return visualization

    def step(self, pressed_key: str) -> [np.ndarray, int, bool]:
        
        # Function parameters:
        # pressed_key: input from the user to determine the step direction 
        self.step_counter += 1
        self.move_pacman(pressed_key)
        self.eat_food()
        visualization = self.create_visualization()

        stop_the_game = False
        if self.step_counter > self.max_step:
            stop_the_game = True

        return visualization, self.score, stop_the_game

    def render(self, visualization: np.ndarray):

        os.system('cls' if os.name == 'nt' else 'clear')

        visualization = visualization.tolist()

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

    def place_pacman(self):
        
        self.pacman[0] = np.random.randint(1, self.map_size-1)
        self.pacman[1] = np.random.randint(1, self.map_size-1)
    
    def place_food(self):

        for _ in range(self.num_of_food):
            food_coords = tuple(np.random.randint(1, self.map_size-1, (2,)))

            while (food_coords in self.food) or (food_coords == tuple(self.pacman)):
                food_coords = tuple(np.random.randint(1, self.map_size-1, (2,)))

            self.food.append(food_coords)

    def eat_food(self):

                for food in self.food:
                    if food == tuple(self.pacman):
                
                        self.score += 1
                        self.food.remove(food)
    
    def move_pacman(self, pressed_key: str):

        if pressed_key == 'w':
            self.pacman[0] = max(self.pacman[0] - 1, 0)

        elif pressed_key == 'a':
            self.pacman[1] = max(self.pacman[1] - 1, 0)

        elif pressed_key == 's':
            self.pacman[0] = min(self.pacman[0] + 1, self.map_size - 1)

        elif pressed_key == 'd':
            self.pacman[1] = min(self.pacman[1] + 1, self.map_size - 1)

    def create_visualization(self) -> np.ndarray:

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

    map_size = int(input("What map size would you like to play with? (Suggested: 10...20) "))
    num_of_food = int(input("How many food would you like on the map? (Suggested: 1...100"))

    env = PacMan(map_size,
                 num_of_food,
                 max_step=100)
             
    state = env.reset()
    env.render(state)

    done = False

    while not done:
        user_input = input("Move by pressing 'w, a, s, d' or quit by pressing 'q': ")
        state, reward, done = env.step(user_input)
        env.render(state)
