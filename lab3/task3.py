import pygame
from pygame.draw import *
from task2 import task2

screen = pygame.display.set_mode((800, 500))
pygame.init()
FPS = 30


def bird(a, b, c):
    Q = []
    W = []
    for i in range(a, a + 15 * c, 1):
        Q.append((i, (0.08 / c) * (i - a - 10 * c) ** 2 + b - 15 * c))
        W.append((2 * a - i, (0.08 / c) * (i - a - 10 * c) ** 2 + b - 15 * c))
    polygon(screen, (48, 16, 38), Q)
    polygon(screen, (48, 16, 38), W)
    Q = []
    W = []


def task3_():
    polygon(screen, (48, 16, 38), [(0, 500), (0, 250), (100, 270), (220, 395), (300, 500)])

    G = []
    for i in range(200, 450, 1):
        G.append((i, (-1 / 250) * (i - 370) ** 2 + 490))
    G.append((450, 500))
    G.append((270, 500))
    polygon(screen, (48, 16, 38), G)

    polygon(screen, (48, 16, 38), [(445, 500), (445, 467), (530, 420), (580, 435), (575, 500)])

    H = []
    for i in range(560, 800, 1):
        H.append((i, (-1 / 300) * (i - 600) ** 2 + 435))
    H.append((800, 500))
    H.append((550, 500))
    polygon(screen, (48, 16, 38), H)

    I = []
    for i in range(650, 800, 1):
        I.append((i, (1 / 100) * (i - 865) ** 2 + 250))
    I.append((800, 500))
    I.append((600, 500))
    polygon(screen, (48, 16, 38), I)


def task3():
    task2()
    task3_()
    bird(320, 210, 1)
    bird(350, 200, 2)
    bird(420, 220, 2)
    bird(420, 250, 2)
    bird(550, 300, 2)
    bird(530, 350, 3)
    bird(600, 325, 2)
    bird(600, 400, 2)

    pygame.display.update()
