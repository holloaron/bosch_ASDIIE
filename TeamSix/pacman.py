import pygame  # provides functions for creating programs with a graphical user interface
import random
from enum import Enum


class Constants(Enum):
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600
    PACMAN_SIZE = WINDOW_HEIGHT / 20
    STEP_SIZE = PACMAN_SIZE
    MAX_STEPS = 100

    COLOR_YELLOW = pygame.Color(255, 255, 0)
    COLOR_BLACK = pygame.Color(0, 0, 0)
    COLOR_WHITE = pygame.Color(255, 255, 255)

    POSITION_UP = 'UP'
    POSITION_DOWN = 'DOWN'
    POSITION_RIGHT = 'RIGHT'
    POSITION_LEFT = 'LEFT'

    PACMAN_SPEED = 4
    NUMBER_OF_COINS = 100

    FIRST_COIN_POSITION = 90
    FIRST_COIN_POSITION_TMP = 30


pygame.display.init()
pygame.display.set_caption('TeamSix Pacman')
screen = pygame.display.set_mode((Constants['WINDOW_WIDTH'].value, Constants['WINDOW_HEIGHT'].value))
screen.fill(Constants['COLOR_BLACK'].value)
fps = pygame.time.Clock()


class Pacman:

    # initial starting position in pixel values, starting direction and number of steps
    def __init__(self):
        self.pacman_position = [60, 60]
        self.steps = 0

        self.direction = Constants['POSITION_RIGHT'].value
        self.new_direction = self.direction

    def draw_on_screen(self):
        pygame.draw.circle(screen, Constants['COLOR_YELLOW'].value, (self.pacman_position[0], self.pacman_position[1]),
                           15)

    def step(self):
        """
        Method for stepping and checking walls:
        Screen coordinates: upper left corner's position is [0,0], coordinates increase to the right and downward.
        Checking walls: walls are defined by pixel/coordinate values that pacman can't surpass.
        TOP and LEFT wall: sum of pacman's size and a step size -> pacman's coordinate can not be lower.
        BOTTOM and RIGHT wall: subtracting a step size plus 1 from the window height/width -> pacman's coordinate can not be higher.
        STEPS: moving to the right or downward -> adding a step to the coordinate values;
        moving to the left or upward -> subtracting a step from the coordinate values
        """
        pygame.draw.circle(screen, Constants.COLOR_BLACK.value, (self.pacman_position[0], self.pacman_position[1]),
                           15)
        if self.direction == Constants['POSITION_UP'].value and self.pacman_position[1] >= Constants['STEP_SIZE'].value + Constants['PACMAN_SIZE'].value:
            self.pacman_position[1] -= Constants['STEP_SIZE'].value
        if self.direction == Constants['POSITION_DOWN'].value and self.pacman_position[1] <= (Constants['WINDOW_HEIGHT'].value - (Constants['STEP_SIZE'].value + 1)):
            self.pacman_position[1] += Constants['STEP_SIZE'].value
        if self.direction == Constants['POSITION_LEFT'].value and self.pacman_position[0] >= Constants['STEP_SIZE'].value + Constants['PACMAN_SIZE'].value:
            self.pacman_position[0] -= Constants['STEP_SIZE'].value
        if self.direction == Constants['POSITION_RIGHT'].value and self.pacman_position[0] <= (Constants['WINDOW_HEIGHT'].value - (Constants['STEP_SIZE'].value + 1)):
            self.pacman_position[0] += Constants['STEP_SIZE'].value

    # method that updates the current direction - needed for automatic steps, when there isn't any direction key pressed
    def change_direction(self):
        if self.new_direction == Constants['POSITION_UP'].value:
            self.direction = Constants['POSITION_UP'].value
        if self.new_direction == Constants['POSITION_DOWN'].value:
            self.direction = Constants['POSITION_DOWN'].value
        if self.new_direction == Constants['POSITION_LEFT'].value:
            self.direction = Constants['POSITION_LEFT'].value
        if self.new_direction == Constants['POSITION_RIGHT'].value:
            self.direction = Constants['POSITION_RIGHT'].value

    # function handling key events to update the direction
    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.new_direction = Constants['POSITION_UP'].value
                if event.key == pygame.K_DOWN:
                    self.new_direction = Constants['POSITION_DOWN'].value
                if event.key == pygame.K_LEFT:
                    self.new_direction = Constants['POSITION_LEFT'].value
                if event.key == pygame.K_RIGHT:
                    self.new_direction = Constants['POSITION_RIGHT'].value


class Coins:
    def __init__(self, number_of_coins: int):
        self.positions = []
        self.number_of_coins = number_of_coins

    # function for generating coins
    def generate(self):
        # initialize variables
        cycle_counter = 0
        position_x, position_y, position_x_tmp, position_y_tmp = self._set_start_position()
        self.positions.append([position_x, position_y])
        # build a line of points
        while len(self.positions) < self.number_of_coins:
            # going straight, every third cycle it might turn to left or right based on random_number
            if cycle_counter % 3 == 0:
                random_number = random.randint(0, 2)
            else:
                random_number = 0
            cycle_counter += 1
            delta_x = position_x - position_x_tmp
            delta_y = position_y - position_y_tmp
            position_x_tmp = position_x
            position_y_tmp = position_y
            if delta_x != 0:
                if random_number == 0:
                    position_x += delta_x
                elif random_number == 1:
                    position_y += Constants['STEP_SIZE'].value
                else:
                    position_y -= Constants['STEP_SIZE'].value
            elif delta_y != 0:
                if random_number == 0:
                    position_y += delta_y
                elif random_number == 1:
                    position_x += Constants['STEP_SIZE'].value
                else:
                    position_x -= Constants['STEP_SIZE'].value
            # checking if the new point is inside the map, if not reset
            if position_x > Constants['WINDOW_WIDTH'].value or position_x < 0 or position_y > Constants['WINDOW_HEIGHT'].value or position_y < 0:
                position_x, position_y, position_x_tmp, position_y_tmp = self._set_start_position()
                continue
            # add the new point to the list
            if [position_x, position_y] not in self.positions and self._is_in_map(position_x, position_y):
                self.positions.append([position_x, position_y])

    # return x and y positions if they are on the map
    def _is_in_map(self, position_x, position_y):
        return 0 < position_x < Constants['WINDOW_WIDTH'].value and 0 < position_y < Constants['WINDOW_HEIGHT'].value

    # drawing the generated coins
    def draw(self):
        for coin_pos in self.positions:
            pygame.draw.circle(screen, Constants['COLOR_WHITE'].value, coin_pos, 5)

    # sets the position of first placed coin
    def _set_start_position(self):
        position_x = Constants['FIRST_COIN_POSITION'].value
        position_y = Constants['FIRST_COIN_POSITION'].value
        position_x_tmp = Constants['FIRST_COIN_POSITION_TMP'].value
        position_y_tmp = Constants['FIRST_COIN_POSITION_TMP'].value
        return position_x, position_y, position_x_tmp, position_y_tmp


class Game:
    def __init__(self):
        self.pacman = Pacman()
        self.coins = Coins(Constants['NUMBER_OF_COINS'].value)
        self.coins.generate()
        self.score = 0
        self.steps = 0

    # playing the game until max steps: moving pacman, updating coins, score, step number
    def play(self):
        while self.steps < Constants['MAX_STEPS'].value:
            self.pacman.handle_key_events()
            self.pacman.change_direction()
            self.pacman.step()
            self.steps += 1

            if self.pacman.pacman_position in self.coins.positions:
                self.coins.positions.remove(self.pacman.pacman_position)
                self.score += 1

            screen.fill(Constants['COLOR_BLACK'].value)
            self.pacman.draw_on_screen()
            self.coins.draw()
            pygame.display.update()
            fps.tick(Constants['PACMAN_SPEED'].value)


if __name__ == '__main__':
    game = Game()
    game.play()
