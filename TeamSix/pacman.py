import pygame
import random

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900

COLOR_YELLOW = pygame.Color(255, 255, 0)
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WHITE = pygame.Color(255, 255, 255)

POSITION_UP = 'UP'
POSITION_DOWN = 'DOWN'
POSITION_RIGHT = 'RIGHT'
POSITION_LEFT = 'LEFT'

PACMAN_SPEED = 4
NUMBER_OF_COINS = 100

pygame.init()
pygame.display.set_caption('TeamSix Pacman')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(COLOR_BLACK)
fps = pygame.time.Clock()


class Pacman:

    def __init__(self):
        self.pacman_position = [50, 50]

        self.direction = POSITION_RIGHT
        self.new_direction = self.direction
        #pygame.init()
        #pygame.display.set_caption('TeamSix Pacman')
        #self.game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        #self.fps = pygame.time.Clock()

    def play(self):
        while True:
            self.handle_key_events()
            self.change_direction()
            self.step()
            #screen.fill(COLOR_BLACK)
            self.draw_on_screen()
            pygame.display.update()
            fps.tick(PACMAN_SPEED)

    def draw_on_screen(self):
        pygame.draw.circle(screen, COLOR_YELLOW, (self.pacman_position[0], self.pacman_position[1]),
                           15)

    def step(self):
        pygame.draw.circle(screen, COLOR_BLACK, (self.pacman_position[0], self.pacman_position[1]),
                           15)
        if self.direction == POSITION_UP:
            self.pacman_position[1] -= 30
        if self.direction == POSITION_DOWN:
            self.pacman_position[1] += 30
        if self.direction == POSITION_LEFT:
            self.pacman_position[0] -= 30
        if self.direction == POSITION_RIGHT:
            self.pacman_position[0] += 30

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
        position_x = 80
        position_y = 50
        position_x_tmp = 50
        position_y_tmp = 50
        self.positions.append([position_x, position_y])

        while len(self.positions) < self.number_of_coins:
            if cycle_counter % 5 == 0:
                random_number = random.randint(0, 2)
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
                position_x = 80
                position_y = 50
                position_x_tmp = 50
                position_y_tmp = 50
                continue
            if [position_x, position_y] not in self.positions:
                self.positions.append([position_x, position_y])

            else:
                continue

    def draw(self):
        for coin_pos in self.positions:
            pygame.draw.circle(screen, COLOR_WHITE, coin_pos, 5)
            pygame.display.update()


class Game:
    def __init__(self, pacman, coins):
        self.pacman = pacman
        self.coins = coins

    def play(self):
        while True:
            self.pacman.handle_key_events()
            self.pacman.change_direction()
            self.pacman.step()

            if self.pacman.pacman_position in self.coins.positions:
                self.coins.positions.remove(self.pacman.pacman_position)

            screen.fill(COLOR_BLACK)
            self.pacman.draw_on_screen()
            self.coins.draw()
            pygame.display.update()
            fps.tick(PACMAN_SPEED)


if __name__ == '__main__':
    pacman = Pacman()
    coins = Coins(NUMBER_OF_COINS)
    coins.generate()
    game = Game(pacman, coins)
    game.play()
