import pygame
from random import randint, random
pygame.init()

FPS = 30
BAll_SPAWNING_RATE = 20
BALL_INITIAL_VELOCITY = 5
BALL_VANISHING_SPEED = 0.2
WIDTH, HEIGHT = WINDOW_SCALE = 700, 700
screen = pygame.display.set_mode(WINDOW_SCALE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN, RED]

X = 'x'
Y = 'y'
Vx = 'vx'
Vy = 'vy'
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
    vx = 2*(random()-0.5)*BALL_INITIAL_VELOCITY
    vy = 2*(random()-0.5)*BALL_INITIAL_VELOCITY
    radius = randint(30, 60)
    color = COLORS[randint(0, len(COLORS)-1)]
    return {X: x, Y: y, Radius: radius, Color: color, Alive: True, Vx: vx, Vy: vy}


def draw_ball(screen, ball):
    """
    Рисует шарик

    param: screen: элемент pygame.surface
    param: ball: объект, созданной функцией new_random_ball
    """
    pygame.draw.circle(screen, ball[Color],
                       (round(ball[X]), round(ball[Y])), round(ball[Radius]))


def evulate_ball(ball, xBound, yBound):
    """
    Изменяет шарик согласно временю: перемещает, изменяет размер и т.д.

    param: ball: объект, созданной функцией new_random_ball
    param: xBound: кортеж вида (x1, x2), где x1 - левая граница координат, x2 - правая граница координат.
    param: xBound: кортеж вида (x1, x2), где x1 - левая граница координат, x2 - правая граница координат.
    """
    ball[X] += ball[Vx]
    if ball[X] < xBound[0] + ball[Radius]:
        ball[X] = xBound[0] + ball[Radius]
        ball[Vx] *= -1
    elif ball[X] > xBound[1] - ball[Radius]:
        ball[X] = xBound[1] - ball[Radius]
        ball[Vx] *= -1

    ball[Y] += ball[Vy]
    if ball[Y] < yBound[0] + ball[Radius]:
        ball[Y] = yBound[0] + ball[Radius]
        ball[Vy] *= -1
    elif ball[Y] > yBound[1] - ball[Radius]:
        ball[Y] = yBound[1] - ball[Radius]
        ball[Vy] *= -1

    ball[Radius] -= BALL_VANISHING_SPEED
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

# --


pygame.display.update()
clock = pygame.time.Clock()
frame = 0
finished = False
while not finished:
    clock.tick(FPS)
    frame += 1
    if frame % BAll_SPAWNING_RATE == 0:
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
        evulate_ball(ball, (0, WIDTH), (0, HEIGHT))
        draw_ball(screen, ball)
        if ball[Alive]:
            alive_balls.append(ball)
    balls = alive_balls

    pygame.display.update()
pygame.quit()
