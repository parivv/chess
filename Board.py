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