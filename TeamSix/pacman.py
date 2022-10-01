import pygame
import random

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

pygame.display.init()
pygame.display.set_caption('TeamSix Pacman')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(COLOR_BLACK)
fps = pygame.time.Clock()


class Pacman:

    def __init__(self):
        self.pacman_position = [60, 60]
        self.steps = 0

        self.direction = POSITION_RIGHT
        self.new_direction = self.direction

    def draw_on_screen(self):
        pygame.draw.circle(screen, COLOR_YELLOW, (self.pacman_position[0], self.pacman_position[1]),
                           15)

    # Method for stepping:
    # Screen coordinates: upper left corner's position is [0,0], coordinates increase to the right and downward.
    # Checking walls: walls are defined by pixel/coordinate values that pacman can't surpass.
    # TOP and LEFT wall: sum of pacman size and a step size -> pacman's coordinate can not be lower.
    # BOTTOM and RIGHT wall: subtracting a step size plus 1 from the window height/width -> pacman's coordinate can not be higher.
    # STEPS: moving to the right or downward -> adding a step to the coordinate values;
    # moving to the left or upward -> subtracting a step from the coordinate values
    def step(self):
        pygame.draw.circle(screen, COLOR_BLACK, (self.pacman_position[0], self.pacman_position[1]),
                           15)
        if self.direction == POSITION_UP and self.pacman_position[1] >= STEP_SIZE + PACMAN_SIZE:
            self.pacman_position[1] -= STEP_SIZE
        if self.direction == POSITION_DOWN and self.pacman_position[1] <= (WINDOW_HEIGHT - (STEP_SIZE + 1)):
            self.pacman_position[1] += STEP_SIZE
        if self.direction == POSITION_LEFT and self.pacman_position[0] >= STEP_SIZE + PACMAN_SIZE:
            self.pacman_position[0] -= STEP_SIZE
        if self.direction == POSITION_RIGHT and self.pacman_position[0] <= (WINDOW_WIDTH - (STEP_SIZE + 1)):
            self.pacman_position[0] += STEP_SIZE

    def change_direction(self):
        if self.new_direction == POSITION_UP:
            self.direction = POSITION_UP
        if self.new_direction == POSITION_DOWN:
            self.direction = POSITION_DOWN
        if self.new_direction == POSITION_LEFT:
            self.direction = POSITION_LEFT
        if self.new_direction == POSITION_RIGHT:
            self.direction = POSITION_RIGHT

    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.new_direction = POSITION_UP
                if event.key == pygame.K_DOWN:
                    self.new_direction = POSITION_DOWN
                if event.key == pygame.K_LEFT:
                    self.new_direction = POSITION_LEFT
                if event.key == pygame.K_RIGHT:
                    self.new_direction = POSITION_RIGHT


class Coins:
    def __init__(self, number_of_coins):
        self.positions = []
        self.number_of_coins = number_of_coins

    def generate(self):
        cycle_counter = 0
        position_x = 90
        position_y = 90
        position_x_tmp = 30
        position_y_tmp = 30
        self.positions.append([position_x, position_y])

        while len(self.positions) < self.number_of_coins:
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
                    position_y += 30
                else:
                    position_y -= 30
            elif delta_y != 0:
                if random_number == 0:
                    position_y += delta_y
                elif random_number == 1:
                    position_x += 30
                else:
                    position_x -= 30
            if position_x > WINDOW_WIDTH or position_x < 0 or position_y > WINDOW_HEIGHT or position_y < 0:
                position_x = 90
                position_y = 90
                position_x_tmp = 30
                position_y_tmp = 30
                continue
            if [position_x, position_y] not in self.positions and self._is_in_map(position_x, position_y):
                self.positions.append([position_x, position_y])

    def _is_in_map(self, position_x, position_y):
        return 0 < position_x < WINDOW_WIDTH and 0 < position_y < WINDOW_HEIGHT

    def draw(self):
        for coin_pos in self.positions:
            pygame.draw.circle(screen, COLOR_WHITE, coin_pos, 5)


class Game:
    def __init__(self):
        self.pacman = Pacman()
        self.coins = Coins(NUMBER_OF_COINS)
        self.coins.generate()
        self.score = 0
        self.steps = 0

    def play(self):
        while self.steps < MAX_STEPS:
            self.pacman.handle_key_events()
            self.pacman.change_direction()
            self.pacman.step()
            self.steps += 1

            if self.pacman.pacman_position in self.coins.positions:
                self.coins.positions.remove(self.pacman.pacman_position)
                self.score += 1

            screen.fill(COLOR_BLACK)
            self.pacman.draw_on_screen()
            self.coins.draw()
            pygame.display.update()
            fps.tick(PACMAN_SPEED)


if __name__ == '__main__':
    game = Game()
    game.play()
