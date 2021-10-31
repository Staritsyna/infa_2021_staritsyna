import math
from random import choice, randint
import pygame
from pygame.draw import *
pygame.init()
FPS = 30

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (230, 230, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY=(192, 192,192)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
g=2
score=0
font = pygame.font.Font(None, 25)
class Ball:
    def __init__(self, screen: pygame.Surface, x=10, y=HEIGHT-10):
        """ Конструктор класса Ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = gun.xo
        self.y = gun.yo
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить снаряд по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if (abs(self.vy) <=g) and self.y+self.r>=HEIGHT:
            balls.remove(self)
        '''if self.vx >0 and  self.x+self.r>=WIDTH:
            self.vx=-self.vx
        if self.vx <0 and  self.x-self.r<=0:
            self.vx=-self.vx'''
        if self.vy <0 and  self.y+self.r>=HEIGHT:
            self.vy=-self.vy
        '''if self.vy >0 and  self.y-self.r<=0:
            self.vy=-self.vy'''
        self.x += self.vx
        self.vy-=g
        self.y -= self.vy-g/2
        

    def draw(self):
        'Фнкция рисует мяч'
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x-obj.x)**2+(self.y-obj.y)**2)<=(self.r+obj.r)**2:
            return True
        else:
            return False
class Bul1(Ball):
   pass
class Bul2(Ball):
   def __init__(self, screen: pygame.Surface):
        """ Конструктор класса Ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = gun.xo
        self.y = gun.yo
        self.r = 20
        self.vx = 0
        self.vy = 0
        self.color = BLACK
        self.live = 30
   def move(self):
        """Переместить снаряд по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if (abs(self.vy) <=g) and self.y+self.r>=HEIGHT:
            balls.remove(self)
        if self.vx >0 and  self.x+self.r>=WIDTH:
            self.vx=-self.vx
        if self.vx <0 and  self.x-self.r<=0:
            self.vx=-self.vx
        if self.vy <0 and  self.y+self.r>=HEIGHT:
            self.vy=-self.vy
        if self.vy >0 and  self.y-self.r<=0:
            self.vy=-self.vy
        self.x += self.vx
        self.vy-=g
        self.y -= self.vy-g/2
        self.live-=1
        if self.live==0:
            balls.remove(self)
            

class Gun:
    def __init__(self, screen):
        """ Конструктор класса Gun

        Args:
        f2_power - максимальная сила
        bn - угол вылета мяча от горизонта, угол наклона пушки
        color - цвет пушки
        attempt- количество попыток
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.bn = 1
        self.k=1
        self.color = GREY
        self.attempt=0
        self.num=1
        self.x=10
        self.vx=1
        self.y=10
        self.vy=1
        self.xo=10
        self.yo=10
    def move(self,event):
        if event.key==pygame.K_LEFT:
                self.vx=-10
                self.x += self.vx
        if event.key==pygame.K_RIGHT:
                self.vx=10
                self.x += self.vx
        if event.key==pygame.K_UP:
                self.vy=10
                self.y += self.vy
        if event.key==pygame.K_DOWN:
                self.vy=-10
                self.y += self.vy

    def fire2_start(self, event):
        self.f2_on = 1
        

    def fire2_end1(self, event):
        """Выстрел мячом 1.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        
        new_ball = Bul1(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.bn)
        new_ball.vy = self.f2_power * math.sin(self.bn)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.k=1
        self.attempt+=1
    def fire2_end2(self, event):
        """Выстрел мячом 2.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Bul2(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.bn)
        new_ball.vy = self.f2_power * math.sin(self.bn)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.k=1
        self.attempt+=1
        
        
    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event and event.pos[0]!=self.x:
            
            if (event.pos[0]-self.x)>0  :
                self.bn = math.atan((HEIGHT-event.pos[1]-self.y) / (event.pos[0]-self.x))
            if (event.pos[0]-self.x)<0:
                self.bn = 180+math.atan((HEIGHT-event.pos[1]-self.y) / (event.pos[0]-self.x))
        if self.f2_on:
            self.color = YELLOW
        else:
            self.color = GREY

    def draw(self):
        L=50+self.k
        H=5
        a=20
        b=10
        self.xo=self.x+L*math.cos(self.bn)
        self.yo=HEIGHT-L*math.sin(self.bn)-self.y
        polygon(screen,self.color,[(self.x,HEIGHT-b-self.y ),
                            (self.xo,self.yo),
                            (self.xo-H*math.sin(self.bn),
                             self.yo-H*math.cos(self.bn)),
                            (self.x-H*math.sin(self.bn), HEIGHT-b-self.y-H*math.cos(self.bn))],0)
        polygon(screen,self.color,[(self.x-a,HEIGHT-self.y),
                            (self.x+a,HEIGHT-self.y),
                            (self.x+a,HEIGHT-b-self.y),
                            (self.x-a,HEIGHT-b-self.y)],0)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 10
                self.k+=2
                
            self.color = YELLOW
        else:
            self.color = GREY
           

  
class Target:
    
    def __init__(self):
        """ Конструктор класса Target

        Args:
        points - начальные очки
        live - начальное число жизней
        """
        self.screen = screen
        self.points = 0
        self.live = 1
        self.new_target()
        self.w=20
        
 


    def new_target(self):
       'Инициализация новой цели.'
       self.x = randint(600, 780)
       self.y = randint(300, 550)
       self.r = randint(5, 50)
       self.color = BLUE
       self.vx = randint(-10, 10)
       self.vy = randint(-10, 10)
       self.live = 1
       self.w=20
       targets.append(self)
    def move(self):
        """Переместить цель по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy
        и стен по краям окна (размер окна 800х600).
        """
        pass
        if self.vx >0 and  self.x+self.r>=WIDTH:
            self.vx=-self.vx
        if self.vx <0 and  self.x-self.r<=0:
            self.vx=-self.vx
        if self.vy >0 and  self.y+self.r>=HEIGHT:
            self.vy=-self.vy
        if self.vy <0 and  self.y-self.r<=0:
            self.vy=-self.vy
        self.x += self.vx
        self.y += self.vy

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global score, text0,text1
        self.points += points
        score += points
        text0 = font.render("Score: "+str(score),True,BLACK)
        text1 = font.render("Вы уничтожили цель с попытки "+str(gun.attempt),True,BLACK)
        gun.attempt=0
        b.vx=-b.vx
        b.vy=-b.vy
        self.w=0
      
        
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)
class Target1(Target):
    pass
class Target2(Target):
    def new_target(self):
       'Инициализация новой цели.'
       self.x = randint(600, 780)
       self.y = randint(300, 550)
       self.r = randint(50, 60)
       self.color = RED
       self.vx = randint(-10, 10)
       self.vy = randint(-10, 10)
       self.live = 1
       
       targets.append(self)
    def move(self):
        """Переместить цель по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy
        и стен по краям окна (размер окна 800х600).
        """
        if self.vx >0 and  self.x+self.r>=WIDTH:
            self.vx=-self.vx
        if self.vx <0 and  self.x-self.r<=0:
            self.vx=-self.vx
        if self.vy >0 and  self.y+self.r>=HEIGHT:
            self.vy=-self.vy
        if self.vy <0 and  self.y-self.r<=0:
            self.vy=-self.vy
        self.x += self.vx
        self.y += self.vy
        if self.r>30:
            self.r-=0.1
    def hit(self, points=5):
        """Попадание шарика в цель."""
        global score,text0,text1
        self.points += points
        score+= points
        text0 = font.render("Score: "+str(score),True,BLACK)
        
        
        self.w=0
class Enemy(): 
    def __init__(self):
        """ Конструктор класса Enemy
        """
        self.screen = screen
        self.points = 2
        self.live = 1
        self.text1 = font.render(" ",True,BLACK)
        self.screen.blit(self.text1, [200,150]) 
        self.xo = 40
        self.yo = 40
        self.ro=30
        self.color = BLACK
        self.rd=0
        self.x = self.xo
        self.y = self.yo
        self.vy = 1
        self.vx = 1
        self.r = randint(20, 50)
        self.w=0
    def new_ball(self):
       'Инициализация нового снаряда.'
       self.x = self.xo
       self.y = self.yo
       self.r = randint(20, 50)
       self.vx = randint(0,10)
       self.vy = randint(1, 10)
       self.live = 1
       self.color = BLACK
       
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)
    def draw0(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.xo, self.yo),
            self.ro)
    def move(self):
        self.x += self.vx
        self.y += self.vy
    def hit0(self,obj,screen, points=5):
        """Попадание снаряда в танк."""
        global score, text0
        if abs(self.x-obj.x)<self.r and abs(HEIGHT-self.y-obj.y)<self.r:
            score+= -points
            text0 = font.render("Score: "+str(score),True,BLACK)
            self.text2 = font.render("Вы повреждены ",True,BLACK)
            self.new_ball()
            self.rd=0
            self.w=20
        else:
           self.w-=1 
            
            
    def fire(self):
        self.rd+=1
        if int(self.rd) >200:
            self.new_ball()
            self.rd=0
            
        
 

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
balls = []
targets = []
clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target1()
target2 = Target1()
target3 = Target2()
targets = [target1, target2,target3]
enemy0=Enemy()
enemy1=Enemy()
text0 = font.render("Score: 0",True,BLACK)
text1 = font.render("Вы уничтожили цель с попытки",True,BLACK)

finished = False

while not finished:
    screen.fill(WHITE)
    polygon(screen,WHITE,[(0,0),(200,0),(200,200),(0,200)],0)
    screen.blit(text0, [40,100])
    
    if gun.attempt==0:
        screen.blit(text1, [100,200])
    for t in targets:
        t.move()
    if enemy1.w>1:
        screen.blit(enemy1.text2, [300,300])
        
    gun.draw()
    enemy0.draw0()
    enemy1.fire()
    for t in targets:
        t.draw()
    for b in balls:
        b.draw()
    enemy1.draw()
    enemy1.move()
    
    enemy1.hit0(gun,screen)                     
    
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                finished = True
            gun.move(event)  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                gun.fire2_start(event)
                gun.num=1
            if event.button ==3:
                gun.fire2_start(event)
                gun.num=2
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if gun.num==1:
                gun.fire2_end1(event)
            if gun.num==2:
                gun.fire2_end2(event)
            
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            
    for b in balls:
        b.move()
        for t in targets:
            if b.hittest(t) and t.live==1:
                    t.hit()
                    if gun.attempt==0:
                        gun.attempt=1
                    text1 = font.render("Вы уничтожили цель с попытки "+str(gun.attempt),True,BLACK)
                    gun.attempt=0
                    t.new_target()
                    t.draw()
                    
    gun.power_up()
    

pygame.quit()
