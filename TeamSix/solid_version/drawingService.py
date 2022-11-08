import pygame
from constans import Constants


class DrawingService:

    def __init__(self, screen):
        self.screen = screen

    def draw_field(self, tile_position_x, tile_position_y, field_type):
        if field_type == 'WALL':
            color = Constants.COLOR_BLUE.value
        else:
            color = Constants.COLOR_BLACK.value
        pygame.draw.rect(self.screen, color, pygame.Rect(tile_position_x * Constants.TILE_SIZE.value,
                                                         tile_position_y * Constants.TILE_SIZE.value,
                                                         Constants.TILE_SIZE.value, Constants.TILE_SIZE.value))
