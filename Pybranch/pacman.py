import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# The game refresh rate
FPS = 60
FramePerSec = pygame.time.Clock()

# Necessary colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Screen, character and game settings
SCREEN_SIZE = 1000
PACMAN_SIZE = (50, 50)
PACMAN_STARTING_POS_X = 160
PACMAN_STARTING_POS_Y = 520
PACMAN_SPEED = 5
DOT_SIZE = (20, 20)
DOT_NO_SPAWN_FRAME = 40
MAX_SCORE = 60
MAX_TIME = 45000
SCORE = 0
SCORE_POS = 10
TIME_POS = 950

# Font parameters
FONT_SIZE = 60
FONT_SMALL_SIZE = 20
font = pygame.font.SysFont("Verdana", FONT_SIZE)
font_small = pygame.font.SysFont("Verdana", FONT_SMALL_SIZE)
game_over = font.render("Game Over", True, YELLOW)
GAME_OVER_POS_X = 320
GAME_OVER_POS_Y = 500

# Game window creation and title
DISPLAYSURF = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("PACMAN")


class Dot(pygame.sprite.Sprite):
    def __init__(self, frame_min, frame_max):
        self.frame_min = frame_min
        self.frame_max = frame_max

        # Dot load from file and transform to the required size

        super().__init__()
        self.image = pygame.image.load('dot.png')
        self.image = pygame.transform.scale(self.image, DOT_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(frame_min, frame_max)
        self.rect.y = random.randint(frame_min, frame_max)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        # Character load from file, transform to the required size and display in the given position

        super().__init__()
        self.image = pygame.image.load("Pacman.png")
        self.image = pygame.transform.scale(self.image, PACMAN_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def move(self):

        # This function moves the character accordingly to the arrow key you press and check if we go through the wall

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -PACMAN_SPEED)
            if self.rect.top < 0:
                self.rect.move_ip(0, SCREEN_SIZE)
        elif pressed_keys[K_DOWN]:
            self.rect.move_ip(0, PACMAN_SPEED)
            if self.rect.bottom > SCREEN_SIZE:
                self.rect.move_ip(0, -SCREEN_SIZE)
        elif pressed_keys[K_LEFT]:
            self.rect.move_ip(-PACMAN_SPEED, 0)
            if self.rect.left < 0:
                self.rect.move_ip(SCREEN_SIZE, 0)
        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(PACMAN_SPEED, 0)
            if self.rect.right > SCREEN_SIZE:
                self.rect.move_ip(-SCREEN_SIZE, 0)


if __name__ == "__main__":
    Pac_man = Player(PACMAN_STARTING_POS_X, PACMAN_STARTING_POS_Y)
    dots = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # Create given number of dots on the screen
    for i in range(MAX_SCORE):
        Score_Dot = Dot(DOT_NO_SPAWN_FRAME, (SCREEN_SIZE - DOT_NO_SPAWN_FRAME))

        dots.add(Score_Dot)
        all_sprites.add(Score_Dot)

    all_sprites.add(Pac_man)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        game_time = pygame.time.get_ticks()

        DISPLAYSURF.fill(BLACK)
        current_score = font_small.render(str(SCORE), True, WHITE)
        current_time = font_small.render(str(round((game_time / 1000), 2)), True, WHITE)
        DISPLAYSURF.blit(current_score, (SCORE_POS, SCORE_POS))
        DISPLAYSURF.blit(current_time, (TIME_POS, SCORE_POS))

        Pac_man.move()

        dot_hit_list = pygame.sprite.spritecollide(Pac_man, dots, True)

        for Score_Dot in dot_hit_list:
            SCORE += 1
        all_sprites.draw(DISPLAYSURF)

        if SCORE == MAX_SCORE or game_time > MAX_TIME:
            time.sleep(0.5)

            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(game_over, (GAME_OVER_POS_X, GAME_OVER_POS_Y))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        FramePerSec.tick(FPS)

