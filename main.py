import pygame

from Board import Board
from constants import *

pygame.init()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #turn on timer to 60 seconds, draw board
    screen.fill((120, 66, 18))
    board = Board(WIDTH, HEIGHT, screen)
    board.draw_board()
    pygame.display.flip()

    timer.tick(60)


