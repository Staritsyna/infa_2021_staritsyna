import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 10
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
balls=[]
squares=[]
def new_ball():
    '''Функция new_ball заносит в массив параметры нового шарика. 
     ''' 
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    dx=randint(-10,10)
    dy=randint(-5,5)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    t=60
    
    balls.append([x,y,dx,dy,r,color,t])
def new_square():
    '''Функция new_square заносит в массив параметры нового квадрата. 
     ''' 
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    dx=randint(-5,5)
    dy=randint(-5,5)
    a = randint(20,40)
    color = COLORS[randint(0, 5)]
    t=60
    
    squares.append([x,y,dx,dy,a,color,t])
def death(data):
    '''Функция death удаляет шарик из массива и создает новый. ''' 
    balls.remove(data)
    new_ball()
def deaths(data):
    '''Функция death удаляет квадрат из массива и создает новый. ''' 
    squares.remove(data)
    new_square()

def update(data):
    '''Функция update обновляет параметры шарика. 
     data = [x, y, dx, dy, r ,color,t]''' 
    if data[0]-data[4]<=0 or data[0]+data[4]>=1200:
        data[2]=-data[2]*randint(-2,2)
        data[0]=data[4]+10
    if data[1]-data[4]<=10 or data[1]+data[4]>=800:
        data[3]=-data[3]*randint(-2,2)
        data[1]=data[4]+10
    data[0]+=data[2]
    data[1]+=data[3]
    data[6]-=1
    if data[6]==0:
        death(data)
    return data

def updates(data):
    '''Функция update обновляет параметры квадрата. 
    #data = [x, y, dx, dy, a ,color,t]''' 
    if data[0]<=10:
        data[2]=-data[2]*randint(2,5)
        data[0]=data[4]+10
    if data[0]+data[4]>=1000:
        data[2]=-data[2]*randint(2,5)
        data[0]=-data[4]+1000
    if data[1]<=0:
        data[3]=-data[3]*randint(2,5)
        data[1]=10
    if data[1]+data[4]>=700:
        data[3]=-data[3]*randint(2,5)
        data[1]=700
    data[0]+=data[2]
    data[1]+=data[3]
    data[6]-=1
    if data[6]==0:
        deaths(data)
    return data
def draw(data):
    '''Функция draw рисует шарик. ''' 
    circle(screen,data[5],(data[0], data[1]),data[4])
def draws(data):
    '''Функция draw рисует шарик. ''' 
    polygon(screen,data[5],[(data[0], data[1]),(int(data[0])+int(data[4]), data[1]),(int(data[0])+int(data[4]), int(data[1])+int(data[4])),(data[0], int(data[1])+int(data[4]))],0)


score=0
pygame.display.update()
clock = pygame.time.Clock()
finished = False
# На экране все время будет 4 шарика. 
new_ball()
new_ball()
new_ball()
new_ball()
new_square()
while not finished:

    clock.tick(FPS)
    time=pygame.time.get_ticks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
       
            x1,y1=pygame.mouse.get_pos()
            for i in balls:
                if (x1-i[0])**2+(y1-i[1])**2<=i[4]**2:
                    score+=1
                    print(score)
                    i[6]=1
                    i=update(i)
            for i in squares:
                if (x1-i[0])**2+(y1-i[1])**2<=i[4]**2:
                    score+=10
                    print(score)
                    i[6]=1
                    i=updates(i)
    for i in range(len(balls)):
        balls[i]=update(balls[i])
        draw(balls[i])
    for i in range(len(squares)):
        squares[i]=updates(squares[i])
        draws(squares[i])
            
        

    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()