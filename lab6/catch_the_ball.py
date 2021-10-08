import pygame
from random import randint, random
pygame.init()

FPS = 30
BAll_SPAWNING_RATE = 20
BALL_INITIAL_VELOCITY = 5
BALL_VANISHING_SPEED = 0.2
WIDTH, HEIGHT = WINDOW_SCALE = 700, 700
FONT = pygame.font.SysFont("monospace", 15)

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
Strange = 'strange'

screen = pygame.display.set_mode(WINDOW_SCALE)
score = 0
balls = []

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
    return {X: x, Y: y, Radius: radius, Color: color, Alive: True, Vx: vx, Vy: vy, Strange: False}


def new_strange_ball(xArea, yArea):
    """
    Создает новый странный шарик с координатоми где-то в области area

    param: xArea: кортеж вида (x1, x2), где x1 - минимальная разрешенная координата x шарика, x2 - максимальная.
    param: yArea: кортеж вида (y1, y2), где y1 - минимальная разрешенная координата y шарика, y2 - максимальная.
    """
    x = (xArea[0] + xArea[1])/2
    y = (yArea[0] + yArea[1])/2
    vx = 4*(random()-0.5)*BALL_INITIAL_VELOCITY
    vy = 4*(random()-0.5)*BALL_INITIAL_VELOCITY
    radius = 30
    color = COLORS[randint(0, len(COLORS)-1)]
    return {X: x, Y: y, Radius: radius, Color: color, Alive: True, Vx: vx, Vy: vy, Strange: True}


def draw_ball(screen, ball):
    """
    Рисует шарик

    param: screen: элемент pygame.surface
    param: ball: объект, созданной функцией new_random_ball
    """
    pygame.draw.circle(screen, ball[Color],
                       (round(ball[X]), round(ball[Y])), round(ball[Radius]), 8 * ball[Strange])


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

    if ball[Strange]:
        ball[Color] = COLORS[randint(0, len(COLORS)-1)]
        ball[Vx] += (random() - 0.5)*2
        ball[Vy] += (random() - 0.5)*2
    else:
        ball[Radius] -= BALL_VANISHING_SPEED
        if ball[Radius] <= 0:
            ball[Alive] = False


def handle_click():
    """
    Обрабатывает событие нажатия мышки
    """
    global score
    for ball in balls:
        x, y = pygame.mouse.get_pos()
        if (ball[X] - x)**2 + (ball[Y] - y)**2 < ball[Radius]**2:
            score += 1
            ball[Alive] = False


def show_score(screen, x, y):
    """
    Выводит количество очков

    param: screen: элемент pygame.surface
    param: x: координата x верхнего левого угла надписи
    param: y: координата y верхнего левого угла надписи
    """
    label = FONT.render("Your score is " + str(score), 1, (255, 255, 255))
    screen.blit(label, (x, y))

# --


pygame.display.update()
clock = pygame.time.Clock()
frame = 0
finished = False
while not finished:
    clock.tick(FPS)
    frame += 1
    if frame % BAll_SPAWNING_RATE == 0:
        if randint(1, 5) != 1:
            balls.append(new_random_ball((60, WIDTH-60), (60, HEIGHT-60)))
        else:
            balls.append(new_strange_ball((0, WIDTH), (0, HEIGHT)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click()

    screen.fill(BLACK)
    show_score(screen, 20, 20)
    alive_balls = []
    for ball in balls:
        evulate_ball(ball, (0, WIDTH), (0, HEIGHT))
        draw_ball(screen, ball)
        if ball[Alive]:
            alive_balls.append(ball)
    balls = alive_balls

    pygame.display.update()
pygame.quit()
