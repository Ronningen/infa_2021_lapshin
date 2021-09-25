import random
import pygame
from pygame.draw import *

FPS = 30
W, H = 570, 800
G = 320
pygame.init()

scr = pygame.display.set_mode((W, H))


def back():
    '''draws background'''
    scr.fill((81, 158, 97))
    rect(scr, (107, 94, 84), (0, H-G, W, G))


def tree(x, y, w):
    '''draws tree from y upper than botoom to the height'''
    rect(scr, (205, 172, 57), (x - w//2, 0, w, H - y))


def spike(x, y, angle=0, sizeRatio=1, surface=scr):
    '''draws spike'''
    w, h = 20, 70
    s = pygame.Surface((10*w, 10*h))
    s = s.convert_alpha()
    s.fill([0]*4)

    polygon(s, (25, 28, 28), ((0, 0), (5*w, 10*h), (10*w, 0)))
    polygon(s, [12]*3, ((0, 0), (5*w, 10*h), (10*w, 0)), 20)

    s = pygame.transform.smoothscale(
        s, (round(w*sizeRatio), round(h*sizeRatio)))
    s = pygame.transform.rotate(s, 180 + angle)
    r = s.get_rect()
    surface.blit(s, (x - r.width, y - r.height))


def mushroom(x, y, angle=0, sizeRatio=1, surface=scr):
    '''draws mushroom'''
    s = pygame.Surface((1000, 1000))
    s = s.convert_alpha()
    s.fill([0]*4)

    ellipse(s, [250]*3, (350, 150, 300, 800)) # leg
    ellipse(s, (234, 51, 35), (0, 0, 1000, 300)) # hat
    ellipse(s, [250]*3, (380, 50, 80, 60)) # spots
    ellipse(s, [250]*3, (620, 70, 90, 65))
    ellipse(s, [250]*3, (50, 150, 40, 40))
    ellipse(s, [250]*3, (900, 120, 45, 60))
    ellipse(s, [250]*3, (200, 160, 100, 70))
    ellipse(s, [250]*3, (600, 220, 80, 50))

    s = pygame.transform.smoothscale(
        s, (round(100*sizeRatio), round(100*sizeRatio)))
    s = pygame.transform.rotate(s, angle)
    r = s.get_rect()
    surface.blit(s, (x - r.width//2, y - r.height//2))


def hedgehog(x, y, sizeRatio=1):
    '''draws hedgehog'''
    s = pygame.Surface((400, 400))
    s = s.convert_alpha()
    s.fill([0]*4)

    def spikes(n):
        i = 0
        while i < n:
            xs = random.randint(115, 285)
            ys = random.randint(200, 300)
            if (xs-200)**2/85**2 + (ys-250)**2/50**2 < 1:
                angle = random.randint(-10, 55)
                size = (1 + random.random())/2.3
                spike(xs, ys, angle, size, s)
                i += 1

    ellipse(s, (59, 46, 45), (240, 265, 20, 45)) # far legs
    ellipse(s, (59, 46, 45), (170, 265, 20, 45))
    ellipse(s, (69, 56, 55), (115, 200, 170, 100)) # body
    ellipse(s, (69, 56, 55), (210, 275, 20, 45)) # near legs
    ellipse(s, (69, 56, 55), (140, 267, 20, 45))
    spikes(120)
    ellipse(s, (189, 117, 67), (95, 190, 42, 45)) # peach1
    ellipse(s, (165, 136, 140), (95, 190, 42, 45), 2)
    spikes(20)
    ellipse(s, (189, 117, 67), (110, 180, 42, 45)) # peach2
    ellipse(s, (165, 136, 140), (110, 180, 42, 45), 2)
    mushroom(170, 190, -20, 0.8, s) # mushroom
    circle(s, (234, 51, 35), (235, 210), 24) # apple
    spikes(30)
    circle(s, (69, 56, 55), (235, 250), 12) # ear
    circle(s, (220, 150, 150), (233, 248), 5)
    ellipse(s, (69, 56, 55), (230, 235, 70, 60)) # head
    ellipse(s, [160]*3, (250, 254, 15, 12)) # eye
    circle(s, [0]*3, (260, 260), 7)
    circle(s, [200]*3, (258, 258), 3)
    circle(s, [0]*3, (298, 270), 10) # nose

    s = pygame.transform.smoothscale(
        s, (round(400*sizeRatio), round(400*sizeRatio)))
    scr.blit(s, (x, y))


back()
tree(0, 284, 90)
hedgehog(90, 365, 0.6)
tree(140, 10, 132)
tree(425, 284, 55)
hedgehog(350, 300, 0.7)
tree(540, 214, 38)
hedgehog(150, 400)
hedgehog(-60, 630, 0.4)
mushroom(270, H-10)
mushroom(330, H, 0, 0.55)
mushroom(370, H-10, -10, 0.6)
mushroom(420, H+8, -4, 0.5)
mushroom(470, H-7, 10)
mushroom(520, H-5, 0, 0.55)
mushroom(W, H-20, -10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
