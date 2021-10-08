from typing import Collection
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
SPAWNING_RATE = 20
WIDTH, HEIGHT = WINDOW_SCALE = 700, 700
screen = pygame.display.set_mode(WINDOW_SCALE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

X = 'x'
Y = 'y'
Radius = 'radius'
Color = 'color'
Alive = 'alive'

balls = []
score = 0

# --

def new_random_ball(xArea, yArea):
    """
    Создает новый случайный шарик с координатоми где-то в области area

    param: xArea: кортеж вида (x1, x2), где x1 - минимальная разрешенная координата x шарика, x2 - максимальная.
    param: yArea: кортеж вида (y1, y2), где y1 - минимальная разрешенная координата y шарика, y2 - максимальная.
    """
    x = randint(xArea[0], xArea[1])
    y = randint(yArea[0], yArea[1])
    radius = randint(30, 60)
    color = COLORS[randint(0, len(COLORS)-1)]
    return {X: x, Y: y, Radius: radius, Color: color, Alive: True}


def draw_ball(screen, ball):
    """
    Рисует шарик

    param: screen: элемент pygame.surface
    param: ball: объект, созданной функцией new_random_ball
    """
    circle(screen, ball[Color], (ball[X], ball[Y]), ball[Radius])


def evulate_ball(ball):
    """
    Изменяет шарик согласно временю: перемещает, может изменять размер и т.д.

    param: ball: объект, созданной функцией new_random_ball
    """
    ball[Radius] -= 1
    if ball[Radius] <= 0:
        ball[Alive] = False


def handle_click(event):
    """
    Обрабатывает событие нажатия мышки

    param: event: элемент pygame.event
    """
    pass


def show_score(screen):
    """
    Выводит количество очков

    param: screen: элемент pygame.surface
    """
    pass

#--

pygame.display.update()
clock = pygame.time.Clock()
frame = 0
finished = False
while not finished:
    clock.tick(FPS)
    frame += 1
    if frame % SPAWNING_RATE == 0:
        balls.append(new_random_ball((60, WIDTH-60), (60, HEIGHT-60)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(event)

    screen.fill(BLACK)
    show_score(screen)
    alive_balls = []
    for ball in balls:
        evulate_ball(ball)
        draw_ball(screen, ball)
        if ball[Alive]:
            alive_balls.append(ball)
    balls = alive_balls

    pygame.display.update()
pygame.quit()
