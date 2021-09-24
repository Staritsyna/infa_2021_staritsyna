import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
GRAY = (125, 125, 125)
RED = (255,0,0)
screen.fill(GRAY)
circle(screen,YELLOW , (200,200),100)
circle(screen,BLACK , (200,200),100,2)
circle(screen,RED , (165,200),25)
circle(screen,BLACK, (165,200),25,2)
circle(screen,RED , (235,200),20)
circle(screen,BLACK , (235,200),20,2)
circle(screen,BLACK , (165,200),10)
circle(screen,BLACK, (235,200),10)
line(screen, BLACK,[165,250],[235,250],15)

line(screen, BLACK,[120,130],[200,190],11)
line(screen, BLACK,[210,190],[285,140],8)
pygame.display.update()
clock = pygame.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()