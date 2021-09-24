import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 84)
YELLOW = (225, 225, 0)
LGRAY = (235,245,255)
GRAY = (125, 125, 125)
RED = (255,0,0)
BLUE=(64, 128, 255)
PINK=(230, 50, 230)
BROWN=(100,40,0)


screen.fill(GREEN)
rect(screen,BLUE,(0,0,400,200))



#body
circle(screen,LGRAY , (120,100),30)
ellipse(screen,GRAY,(90,130,60,170))

line(screen, BLACK,[140,160],[200,190],2)
line(screen, BLACK,[95,160],[70,210],2)
#legs
line(screen, BLACK,[95,270],[80,340],2)
line(screen, BLACK,[65,340],[80,340],2)

line(screen, BLACK,[143,270],[160,340],2)
line(screen, BLACK,[175,340],[160,340],2)

#icecream
polygon(screen,YELLOW,[[30,170],[70,210],[80,160]])
circle(screen,RED , (70,160),15)
circle(screen,BROWN , (35,165),15)
circle(screen,WHITE, (50,150),15)

#hand
line(screen, BLACK,[340,160],[305,140],2)
line(screen, BLACK,[340,160],[370,140],2)

#girl
polygon(screen,PINK,[[300,110],[260,270],[340,270]])
circle(screen,LGRAY , (300,100),30)
line(screen, BLACK,[200,190],[295,140],2)

line(screen, BLACK,[380,90],[370,140],1)
polygon(screen,RED,[[380,90],[350,50],[390,45]])
circle(screen,RED , (380,45),12)
circle(screen,RED , (360,50),12)
#legs
line(screen, BLACK,[280,270],[280,340],2)
line(screen, BLACK,[280,340],[265,340],2)

line(screen, BLACK,[320,270],[320,340],2)
line(screen, BLACK,[320,340],[335,340],2)






pygame.display.update()
clock = pygame.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()