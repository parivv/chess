import pygame
from constants import *

class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen

    def draw_board(self):
        for i in range(64):
            col = i % 8
            row = i // 8
            if (row + col) % 2 == 0:
                color = (255,255,255)
            else:
                color = (175,208,130)
            pygame.draw.rect(self.screen, color, [col*100, row*100, 100, 100])

    def draw_pieces(self):
       for i, name in enumerate(piece_order):
           img_location = white_pieces_images[name]
           self.screen.blit(img_location, (white_coordinates[i][0] * 100 + 10, white_coordinates[i][1] * 100 + 10))

       for i, name in enumerate(piece_order):
           img_location = black_pieces_images[name]
           screen.blit(img_location, (black_coordinates[i][0] * 100 + 10, black_coordinates[i][1] * 100 + 10))