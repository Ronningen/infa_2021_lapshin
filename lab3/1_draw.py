from pygame.draw import *
import pygame

BLACK = [0]*3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 30
W, H = 600, 700
HW, HH = W//2, H//2

pygame.init()

scr = pygame.display.set_mode((W, H))


def back():
    '''draws background'''
    rect(scr, [200]*3, (0, 0, W, H))


back()

'''body'''
circle(scr, YELLOW, (HW, HH), 150)

'''eyes'''
circle(scr, RED, (HW - 70, HH - 50), 40)
circle(scr, RED, (HW + 70, HH - 50), 40)
circle(scr, BLACK, (HW - 60, HH - 45), 20)
circle(scr, BLACK, (HW + 60, HH - 45), 20)

'''brows'''
line(scr, BLACK, (HW - 100, HH - 100), (HW - 20, HH - 70), 20)
line(scr, BLACK, (HW + 100, HH - 100), (HW + 20, HH - 70), 20)

'''mouse'''
line(scr, BLACK, (HW - 60, HH + 80), (HW + 60, HH + 80), 20)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
