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

pygame.init()
pygame.display.set_caption('TeamSix Pacman')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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

            screen.fill(COLOR_BLACK)
            self.draw_on_screen()
            pygame.display.update()
            fps.tick(PACMAN_SPEED)

    def draw_on_screen(self):
        pygame.draw.circle(screen, COLOR_YELLOW, (self.pacman_position[0] + 15, self.pacman_position[1] + 15),
                           15)

    def step(self):
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


if __name__ == '__main__':
    game = Pacman()
    game.play()
