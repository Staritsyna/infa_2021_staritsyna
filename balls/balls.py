import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 10
WIDTH = 1200
HIGHT = 900 
screen = pygame.display.set_mode((WIDTH, HIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

font = pygame.font.Font(None, 25)
text = font.render("Score: 0",True,RED)
balls=[]
squares=[]
dict_rating={}

'''Считывем файл.Заполняем словарь со счетом, сортируем его'''
with open ('C:/Users/Анна/Documents/GitHub/infa_2021_staritsyna/rating.txt','r') as inf:
    for line_row in inf:
        if len(line_row)==0:
            continue
        line=line_row.strip().split()
        dict_rating.update({line[0]: line[1]})
        dict_rating.items()
        sorted_tuple = sorted(dict_rating.items(), key=lambda x: x[1])
        dict_rating=dict(sorted_tuple)
        print(dict_rating)

with open ('C:/Users/Анна/Documents/GitHub/infa_2021_staritsyna/rating.txt','w') as inf:
        inf.writelines([key+' '+dict_rating[key]+'\n' for key in dict_rating.keys()])  
          
def new_ball():
    '''Функция new_ball заносит в массив параметры нового шарика. 
     ''' 
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    dx=randint(-5,5)
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
    y = randint(110,500)
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
    if data[0]-data[4]<=0 and data[2]<0:
        if abs(data[2])<50:
            data[2]=-data[2]*randint(1, 3)
        else:
            data[2]=-data[2]*0.5
    if data[0]+data[4]>=WIDTH and data[2]>0:
        if abs(data[2])<50:
            data[2]=-data[2]*randint(1, 3)
        else:
            data[2]=-data[2]*0.5
    if data[1]-data[4]<=40 and data[3]<0:
        if abs(data[3])<50:
            data[3]=-data[3]*randint(1, 3)
        else:
            data[3]=-data[3]*0.5
    if data[1]+data[4]>=HIGHT*0.89 and data[3]>0:
        if abs(data[3])<50:
            data[3]=-data[3]*randint(1, 3)
        else:
            data[3]=-data[3]*0.5
    data[0]+=data[2]
    data[1]+=data[3]
    data[6]-=1
    if data[6]==0:
        death(data)
    return data

def updates(data):
    '''Функция update обновляет параметры квадрата. 
    data = [x, y, dx, dy, a ,color,t]''' 
    if data[0]<=0 and data[2]<0:
        if abs(data[2])<50:
            data[2]=-data[2]*2
        else:
            data[2]=-data[2]*0.5
    if data[0]+data[4]>=WIDTH and data[2]>0:
        if abs(data[2])<50:
            data[2]=-data[2]*2
        else:
            data[2]=-data[2]*0.5
    if data[1]<=100 and data[3]<0:
        if abs(data[3])<50:
            data[3]=-data[3]*2
        else:
            data[3]=-data[3]*0.5
    if data[1]+data[4]>=HIGHT*0.89 and data[3]>0:
        if abs(data[3])<50:
            data[3]=-data[3]*2
        else:
            data[3]=-data[3]*0.5
    data[0]+=randint(-2,2)*data[2]
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
    polygon(screen,data[5],[(data[0], data[1]),
                            (int(data[0])+int(data[4]),data[1]),
                            (int(data[0])+int(data[4]), 
                             int(data[1])+int(data[4])),
                            (data[0], int(data[1])+int(data[4]))],0)

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
username=str(input())
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
                    text = font.render("Score: "+str(score),True,RED)
                    i[6]=1
                    i=update(i)
            for i in squares:
                if abs(x1-i[0])<=i[4] and abs(y1-i[1])<=i[4]:
                    score+=randint(-10,10)
                    text = font.render("Score: "+str(score),True,RED)
                    i[6]=1
                    i=updates(i)
    for i in range(len(balls)):
        balls[i]=update(balls[i])
        draw(balls[i])
    for i in range(len(squares)):
        squares[i]=updates(squares[i])
        draws(squares[i])
    polygon(screen,WHITE,[(0,0),(0,140),(200,140),(200,0)],0)     #вывод счета  
    screen.blit(text, [40,100])    

    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
'''Заносим счет в файл'''
with open ('C:/Users/Анна/Documents/GitHub/infa_2021_staritsyna/rating.txt','a') as inf:
    inf.write(username+' '+str(score)+'\n')
    
    

