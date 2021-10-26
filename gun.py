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
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

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

    def fire2_start(self, event):
        self.f2_on = 1
        

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.bn)
        new_ball.vy = - self.f2_power * math.sin(self.bn)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.k=1
        self.attempt+=1
        

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            self.bn = math.atan((HEIGHT-event.pos[1]) / (event.pos[0])+1)
        if self.f2_on:
            self.color = YELLOW
        else:
            self.color = GREY

    def draw(self):
        L=100+self.k
        H=5
        polygon(screen,self.color,[(10,HEIGHT-10 ),
                            (10+L*math.cos(self.bn),HEIGHT-10-L*math.sin(self.bn)),
                            (10+L*math.cos(self.bn)-H*math.sin(self.bn),
                             HEIGHT-10-L*math.sin(self.bn)-H*math.cos(self.bn)),
                            (10-H*math.sin(self.bn), HEIGHT-10-H*math.cos(self.bn))],0)


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.k+=1
                
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
        self.text0 = font.render("Score: 0",True,BLACK)
        self.text1 = font.render(" ",True,BLACK)
        self.screen.blit(self.text1, [200,150]) 
 


    def new_target(self):
       'Инициализация новой цели.'
       self.x = randint(600, 780)
       self.y = randint(300, 550)
       self.r = randint(5, 50)
       self.color = RED
       self.vx = randint(-10, 10)
       self.vy = randint(-10, 10)
       self.live = 1
       gun.attempt=0
       targets.append(self)
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
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

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
        self.text0 = font.render("Score: "+str(self.points),True,BLACK)
        self.text1 = font.render("Вы уничтожили цель с попытки "+str(gun.attempt),True,BLACK)
        
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []
clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
targets = [target1, target2]
finished = False

while not finished:
    screen.fill(WHITE)
    for t in targets:
        polygon(screen,WHITE,[(0,0),(400,0),(400,200),(0,200)],0)
        screen.blit(t.text0, [40,100])
        t.screen.blit(t.text1, [200,150]) 
        t.move()
    gun.draw()
    for t in targets:
        t.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
            
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            

    for b in balls:
        b.move()
        for t in targets:
            
            if b.hittest(t) and t.live==1:
                t.live = 0
                t.hit()
                t.new_target()
                t.draw()
    gun.power_up()
    

pygame.quit()
