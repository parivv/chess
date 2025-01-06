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