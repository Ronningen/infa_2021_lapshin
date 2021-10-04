import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((2500, 1500))

#colors 
black = (0, 0, 0)
skyblue = (178, 239, 255)
green = (0, 232, 87)
red = (255, 55, 53)
orange = (255, 206, 25)
pink = (255, 181, 245)
skin = (255, 237, 218)
white = (255, 255, 255)
blue = (139, 153, 255)
brown = (155, 27, 0)

def draw_background(surface, g, width, height):
    '''
    Функция рисует фон.
    surface - объект pygame.Surface
    g - высота уровня земли
    width, height - ширина и высота изображения
    '''
    rect(surface, skyblue, (0, 0, width, height)) #sky
    rect(surface, green, (0, g, width, height)) #grass


def draw_ice_cream(surface, x, y):
    '''
    Функция рисует мороженное.
    surface - объект pygame.Surface
    x, y - координаты изображения относительно эталонного
    '''
    polygon(surface, orange, [(2350+x, 1010+y), (2290+x, 950+y), (2250+x, 1060+y)])
    circle(surface, brown, (2350+x, 985+y), 29)
    circle(surface, red, (2310+x, 955+y), 29)
    circle(surface, white, (2350+x, 940+y), 29)

def draw_balloon(surface, x, y):
    '''
    Функция рисует воздушный шарик.
    surface - объект pygame.Surface
    x, y - координаты изображения относительно эталонного
    '''
    line(surface, black, (260+x, 1082+y), (230+x, 930+y), 2)
    polygon(surface, red, [(230+x, 930+y), (260+x, 850+y), (175+x, 880+y)])
    circle(surface, red, (232+x, 840+y), 29)
    circle(surface, red, (190+x, 855+y), 29)


def draw_left_man(surface, x, y):
    '''
    Функция рисует левого мужчину.
    surface - объект pygame.Surface
    x, y - координаты изображения относительно эталонного
    '''
    line(surface, black, (500+x, 800+y), (250+x, 1050+y), 2) #arm left
    line(surface, black, (500+x, 800+y), (750+x, 1050+y), 2) #arm right
    lines(surface, black, False, [(470+x, 1150+y), (420+x, 1400+y), (360+x, 1420+y)], 2) #leg left
    lines(surface, black, False, [(530+x, 1150+y), (550+x, 1400+y), (610+x, 1420+y)], 2) #leg right
    ellipse(surface, blue, (410+x, 800+y, 180, 400)) #body left
    circle(surface, skin, (500+x, 750+y), 75) #башка 


def draw_right_man(surface, x, y):
    '''
    Функция рисует правого мужчину.
    surface - объект pygame.Surface
    x, y - координаты изображения относительно эталонного
    '''
    line(surface, black, (2000+x, 800+y), (2250+x, 1050+y), 2) #arm left
    line(surface, black, (2000+x, 800+y), (1750+x, 1050+y), 2) #arm right
    lines(surface, black, False, [(2030+x, 1150+y), (2080+x, 1400+y), (2140+x, 1420+y)], 2) #leg right
    lines(surface, black, False, [(1970+x, 1150+y), (1950+x, 1400+y), (1890+x, 1420+y)], 2) #leg left
    ellipse(surface, blue, (1910+x, 800+y, 180, 400)) #body left
    circle(surface, skin, (2000+x, 750+y), 75) #башка 


def draw_left_woman(surface, x, y):
    '''
    Функция рисует левую женщину.
    surface - объект pygame.Surface
    x, y - координаты изображения относительно эталонного
    '''
    line(surface, black, (750+x, 1050+x), (1000+x, 830+y), 2) #arm left
    lines(surface, black, False, [(1000+x, 830+y), (1150+x, 930+y), (1250+x, 800+y)], 2) #arm right
    lines(surface, black, False, [(950+x, 1200+y), (950+x, 1400+y), (890+x, 1410+y)], 2) #leg left
    lines(surface, black, False, [(1050+x, 1200+y), (1050+x, 1400+y), (1110+x, 1410+y)], 2) #leg right
    polygon(surface, pink, [(1000+x, 800+y), (800+x, 1200+y), (1200+x, 1200+y)]) #body right 
    circle(surface, skin, (1000+x, 750+y), 75) #башка 


def draw_right_woman(surface, x, y):
    '''
    Функция рисует правую женщину.
    surface - объект pygame.Surface
    x, y - координаты изображения относительно эталонного
    '''
    line(surface, black, (1750+x, 1050+y), (1500+x, 830+y), 2) #arm left
    lines(surface, black, False, [(1500+x, 830+y), (1350+x, 930+y), (1250+x, 800+y)], 2) #arm right
    lines(surface, black, False, [(1550+x, 1200+y), (1550+x, 1400+y), (1610+x, 1410+y)], 2) #leg right
    lines(surface, black, False, [(1450+x, 1200+y), (1450+x, 1400+y), (1390+x, 1410+y)], 2) #leg left
    polygon(surface, pink, [(1500+x, 800+y), (1700+x, 1200+y), (1300+x, 1200+y)]) #body right 
    circle(surface, skin, (1500+x, 750+y), 75) #башка 


def draw_ice_cream_balloon(surface, x, y):
    '''
    Функция рисует воздушный шарик в виде мороженого.
    surface - объект pygame.Surface
    x, y - координаты изображения относительно эталонного
    '''
    line(surface, black, (1240+x, 950+y), (1260+x, 300+y), 2)
    polygon(surface, orange, [(1200+x, 190+y), (1260+x, 320+y), (1310+x, 190+y)])
    circle(surface, brown, (1225+x, 175+y), 40)
    circle(surface, red, (1295+x, 175+y), 40)
    circle(surface, white, (1260+x, 140+y), 40)


def draw_family(surface, x, y):
    '''
    Функция рисует семью из четверых людей.
    surface - объект pygame.Surface
    x, y - координаты изображения относительно эталонного
    '''
    draw_left_man(surface, x, y)
    draw_left_woman(surface, x, y)
    draw_right_woman(surface, x, y)
    draw_right_man(surface, x, y)


def draw_stuff(surface, x, y):
    '''
    Функция рисует аксессуары типа воздушных шаров, мороженого.
    surface - объект pygame.Surface
    x, y - координаты изображения относительно эталонного
    '''
    draw_ice_cream(surface, x, y)
    draw_balloon(surface, x, y)
    draw_ice_cream_balloon(surface, x, y)


def draw_picture(surface):
    '''
    Функция рисует картинку.
    surface - объект pygame.Surface
    '''
    draw_background(surface, 750, 3000, 1000)
    draw_family(surface, 0, 0)
    draw_stuff(surface, 0, 0)

draw_picture(screen)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()