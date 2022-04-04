import pygame
from pygame.draw import *

pygame.init()
FPS = 30


def task2():
    screen = pygame.display.set_mode((800, 500))
    screen.fill((255, 211, 153))
    line(screen, (179, 134, 148), (0, 500), (800, 490), 300)
    line(screen, (255, 226, 188), (0, 180), (800, 180), 120)
    circle(screen, (252, 255, 87), (400, 120), 50)
    line(screen, (250, 155, 47), (0, 280), (800, 180), 5)
    polygon(screen, (250, 155, 47),
            [(165, 108), (196, 119), (205, 140), (307, 220), (350, 210), (375, 230), (410, 200), (430, 210), (450, 190),
             (470, 223), (165, 260)])

    A = []
    for i in range(0, 165, 1):
        A.append((i, (-1 / 200) * (i - 17) ** 2 + 217))
    A.append((165, 260))
    A.append((0, 280))
    polygon(screen, (252, 153, 45), A)

    B = []
    for i in range(470, 580, 1):
        B.append((i, (-1 / 4000) * (i - 510) ** 3 + 180))
    B.append((590, 205))
    B.append((440, 225))

    polygon(screen, (252, 153, 45), B)

    C = []
    for i in range(570, 620, 1):
        C.append((i, (1 / 7) * (i - 592) ** 2 + 70))
    C.append((620, 200))
    C.append((520, 215))
    polygon(screen, (252, 153, 45), C)

    polygon(screen, (252, 153, 45), [(610, 205), (595, 70), (670, 165), (700, 150), (740, 175), (770, 160), (800, 180)])

    # нижние горы
    D = []
    for i in range(0, 200, 1):
        D.append((i, (1 / 120) * (i - 80) ** 2 + 220))
    D.append((200, 350))  # верхняя
    D.append((0, 350))
    polygon(screen, (172, 67, 52), D)

    polygon(screen, (172, 67, 52),
            [(180, 350), (225, 300), (270, 320), (320, 250), (370, 265), (400, 300), (460, 285), (460, 350), ])

    E = []
    for i in range(430, 550, 1):
        E.append((i, (1 / 49) * (i - 500) ** 2 + 250))
    E.append((550, 320))
    E.append((550, 350))
    polygon(screen, (172, 67, 52), E)

    F = []
    for i in range(530, 610, 1):
        F.append((i, (-1 / 128) * (i - 610) ** 2 + 320))
    F.append((610, 350))
    F.append((530, 350))
    polygon(screen, (172, 67, 52), F)

    polygon(screen, (172, 67, 52),
            [(610, 350), (590, 318), (630, 260), (680, 280), (700, 255), (750, 260), (800, 200), (800, 350)])

    pygame.display.update()
