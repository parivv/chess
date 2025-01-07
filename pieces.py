import pygame
pygame.init()

#load images
bq = pygame.image.load('pieces/bq.png')
#scale pieces to 80x80 for each 100x100 square
bq = pygame.transform.scale(bq, (80, 80))

bking = pygame.image.load('pieces/bking.png')
bking = pygame.transform.scale(bking, (80, 80))

bb = pygame.image.load('pieces/bb.png')
bb = (pygame.transform.scale(bb, (80, 80)))

bk = pygame.image.load('pieces/bk.png')
bk = pygame.transform.scale(bk, (80, 80))

br = pygame.image.load('pieces/br.png')
br = pygame.transform.scale(br, (80, 80))

bp = pygame.image.load('pieces/bp.png')
bp = pygame.transform.scale(bp, (80, 80))

wq = pygame.image.load('pieces/wq.png')
wq = pygame.transform.scale(wq, (80, 80))

wking = pygame.image.load('pieces/wking.png')
wking = pygame.transform.scale(wking, (80, 80))

wb = pygame.image.load('pieces/wb.png')
wb = (pygame.transform.scale(wb, (80, 80)))

wk = pygame.image.load('pieces/wk.png')
wk = pygame.transform.scale(wk, (80, 80))

wr = pygame.image.load('pieces/wr.png')
wr = pygame.transform.scale(wr, (80, 80))

wp = pygame.image.load('pieces/wp.png')
wp = pygame.transform.scale(wp, (80, 80))

black_pieces_images = {"queen":bq, "king": bking, "bishop": bb, "knight": bk, "rook": br, "pawn": bp}
white_pieces_images = {"queen":wq, "king": wking, "bishop": wb, "knight": wk, "rook": wr, "pawn": wp}