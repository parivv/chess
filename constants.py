from pieces import *
import pygame
pygame.init()

WIDTH = 900
HEIGHT = 900
SQUARE = 80
COLORS = {"white" : (255, 255, 255), "black" : (0, 0, 0)}
screen = pygame.display.set_mode([WIDTH + 100, HEIGHT])
font = pygame.font.Font(None, 40)
timer = pygame.time.Clock()

piece = ["king", "queen", "rook", "bishop", "knight", "pawn"]
piece_order = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]

#white pieces at bottom,  black at the top
white_coordinates = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0, 6), (1, 6), (2,6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
black_coordinates = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2,1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]