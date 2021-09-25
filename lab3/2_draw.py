from pygame.draw import *
import pygame

FPS = 30
W, H = 600, 700
G = 400

pygame.init()

scr = pygame.display.set_mode((W, H))


def back():
    '''draws background'''
    rect(scr, [200]*3, (0, 0, W, H))


back()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
