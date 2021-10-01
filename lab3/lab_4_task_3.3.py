import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 400))

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
'''#girl2
polygon(screen,PINK,[[500,110],[460,270],[540,270]])
circle(screen,LGRAY , (500,100),30)
line(screen, BLACK,[400,140],[450,160],2)
line(screen, BLACK,[495,140],[450,160],2)
line(screen, BLACK,[600,190],[510,140],2)
#legs
line(screen, BLACK,[480,270],[480,340],2)
line(screen, BLACK,[480,340],[465,340],2)
line(screen, BLACK,[520,270],[520,340],2)
line(screen, BLACK,[520,340],[535,340],2)'''
def women(x,y):#x-расстояние от центра 400,x,y -положение головы
    polygon(screen,PINK,[[x+400,y],[x+360,y+170],[x+440,y+170]])
    circle(screen,LGRAY , (400+x,y),30)
    #line(screen, BLACK,[400+x-100,y+40],[400+x-50,y+60],2)
    #line(screen, BLACK,[400+x-5,y+40],[400+x-50,y+60],2)
    #line(screen, BLACK,[400+x+100,y+90],[400+x+110,y+40],2)
    #legs
    line(screen, BLACK,[400+x-20,y+170],[400+x-20,y+240],2)
    line(screen, BLACK,[400+x-20,y+240],[400+x-35,y+240],2)
    line(screen, BLACK,[400+x+20,y+170],[420+x,y+240],2)
    line(screen, BLACK,[400+x+20,y+240],[430+x,y+240],2)
  
#f
screen.fill(GREEN)
rect(screen,BLUE,(0,0,800,160))
women(-100,100)
#body1
circle(screen,LGRAY , (120,100),30)
ellipse(screen,GRAY,(90,130,60,170))

line(screen, BLACK,[140,160],[200,190],2)
line(screen, BLACK,[95,160],[70,210],2)
line(screen, BLACK,[50,110],[70,210],1)
#legs
line(screen, BLACK,[95,270],[80,340],2)
line(screen, BLACK,[65,340],[80,340],2)

line(screen, BLACK,[143,270],[160,340],2)
line(screen, BLACK,[175,340],[160,340],2)

#ball
polygon(screen,RED,[[30,65],[50,110],[70,60]])
circle(screen,RED , (40,57),13)
circle(screen,RED , (60,57),13)
#girl1
polygon(screen,PINK,[[300,110],[260,270],[340,270]])
circle(screen,LGRAY , (300,100),30)
line(screen, BLACK,[200,190],[295,140],2)
#hand
line(screen, BLACK,[350,160],[305,140],2)
line(screen, BLACK,[350,160],[400,140],2)
#sh
line(screen, BLACK,[400,90],[400,140],1)
polygon(screen,YELLOW,[[425,50],[375,50],[400,90]])
circle(screen,BROWN , (385,40),15)
circle(screen,RED , (415,40),15)
circle(screen,WHITE , (400,30),15)
#legs
line(screen, BLACK,[280,270],[280,340],2)
line(screen, BLACK,[280,340],[265,340],2)

line(screen, BLACK,[320,270],[320,340],2)
line(screen, BLACK,[320,340],[335,340],2)

#girl2
polygon(screen,PINK,[[500,110],[460,270],[540,270]])
circle(screen,LGRAY , (500,100),30)
line(screen, BLACK,[400,140],[450,160],2)
line(screen, BLACK,[495,140],[450,160],2)
line(screen, BLACK,[600,190],[510,140],2)
#legs
line(screen, BLACK,[480,270],[480,340],2)
line(screen, BLACK,[480,340],[465,340],2)
line(screen, BLACK,[520,270],[520,340],2)
line(screen, BLACK,[520,340],[535,340],2)

#body2
circle(screen,LGRAY , (680,100),30)
ellipse(screen,GRAY,(650,130,60,170))

line(screen, BLACK,[660,160],[600,190],2)
line(screen, BLACK,[705,160],[730,210],2)
#legs
line(screen, BLACK,[705,270],[720,340],2)
line(screen, BLACK,[735,340],[720,340],2)

line(screen, BLACK,[657,270],[640,340],2)
line(screen, BLACK,[625,340],[640,340],2)

#icecream
polygon(screen,YELLOW,[[770,170],[730,210],[720,160]])
circle(screen,RED , (730,160),15)
circle(screen,BROWN , (765,165),15)
circle(screen,WHITE, (750,150),15)


pygame.display.update()
clock = pygame.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()