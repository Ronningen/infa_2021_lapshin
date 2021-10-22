import math
from random import choice, randint as rnd
from typing import NoReturn

import pygame

FPS = 30

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
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
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 1
        if self.x > 800:
            self.vx *= -0.5
            self.vy *= 0.5
            self.x = 800
        if self.y > 580:
            self.vy *= -0.5
            self.vx *= 0.5
            if abs(self.vy) < 4:
                self.vy *= 0.5
            if abs(self.vy) < 1.5:
                self.vy *= 0
                self.live -= 1
            self.y = 580
        

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (int(self.x), int(self.y)),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2


class Gun:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.x = 40
        self.y = 450
        self.an = 1
        self.color = GREY

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
        self.an = math.atan2(
            (event.pos[1]-self.y), (event.pos[0]-self.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if not (event.pos[0]-self.x):
                self.an = math.pi/2
            else:
                self.an = math.atan(
                    (event.pos[1]-self.y) / (event.pos[0]-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [
                (self.x - math.sin(self.an) * 3, 
                 self.y + math.cos(self.an) * 3),
                (self.x + math.sin(self.an) * 3, 
                 self.y - math.cos(self.an) * 3),
                (self.x + math.sin(self.an) * 3 + math.cos(self.an) * self.f2_power,
                 self.y - math.cos(self.an) * 3 + math.sin(self.an) * self.f2_power),
                (self.x - math.sin(self.an) * 3 + math.cos(self.an) * self.f2_power,
                 self.y + math.cos(self.an) * 3 + math.sin(self.an) * self.f2_power)
            ]
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen: pygame.Surface):
        """ Инициализация новой цели. """
        self.screen = screen
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.live = 1
        self.color = RED

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (int(self.x), int(self.y)),
            self.r
        )


pygame.init()
FONT = pygame.font.SysFont("monospace", 15)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
score = 0

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    label_score = FONT.render('Score: ' + str(score), 1, BLACK)
    bullet_label = FONT.render('Misshits: ' + str(bullet), 1, BLACK)
    screen.blit(label_score, (10, 10))
    screen.blit(bullet_label, (10, 30))
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    new_balls = []
    for b in balls:
        if b.live > 0:
            new_balls.append(b)
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            bullet = 0
            new_balls = []
            target = Target(screen)
            score += 1
            break
    gun.power_up()
    balls = new_balls 

pygame.quit()
