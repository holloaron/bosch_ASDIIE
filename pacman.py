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
SCORE = 0
SCORE_POS = 10

#Font parameters
FONT_SIZE = 60
FONT_SMALL_SIZE = 20
font = pygame.font.SysFont("Verdana", FONT_SIZE)
font_small = pygame.font.SysFont("Verdana", FONT_SMALL_SIZE)
game_over = font.render("Game Over", True, YELLOW)
game_over_pos_x = 320
game_over_pos_y = 500

#Game window creation and title
DISPLAYSURF = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("PACMAN")

class DOT(pygame.sprite.Sprite):
    def __init__(self):

        #Dot load from file and transform to the required size

        super().__init__()
        self.image = pygame.image.load('dot.png')
        self.image = pygame.transform.scale(self.image, DOT_SIZE)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):

        # Character load from file, transform to the required size and display in the given position

        super().__init__()
        self.image = pygame.image.load("Pacman.png")
        self.image = pygame.transform.scale(self.image, PACMAN_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (PACMAN_STARTING_POS_X, PACMAN_STARTING_POS_Y)

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
    Pac_man = Player()
    dots = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # Create given number of dots on the screen
    for i in range(MAX_SCORE):
        Score_Dot = DOT()
        Score_Dot.rect.x = random.randint(DOT_NO_SPAWN_FRAME, SCREEN_SIZE - DOT_NO_SPAWN_FRAME)
        Score_Dot.rect.y = random.randint(DOT_NO_SPAWN_FRAME, SCREEN_SIZE - DOT_NO_SPAWN_FRAME)
        dots.add(Score_Dot)
        all_sprites.add(Score_Dot)

    all_sprites.add(Pac_man)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.fill(BLACK)
        current_score = font_small.render(str(SCORE), True, WHITE)
        DISPLAYSURF.blit(current_score, (SCORE_POS, SCORE_POS))

        Pac_man.move()

        dot_hit_list = pygame.sprite.spritecollide(Pac_man, dots, True)

        for Score_Dot in dot_hit_list:
            SCORE += 1
        all_sprites.draw(DISPLAYSURF)

        if SCORE == MAX_SCORE:
            time.sleep(0.5)

            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(game_over, (game_over_pos_x, game_over_pos_y))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)