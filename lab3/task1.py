import pygame
from pygame.draw import *

pygame.init()
FPS = 30


def task1():
    screen = pygame.display.set_mode((500, 500))
    screen.fill((255, 255, 255))
    circle(screen, (255, 255, 0), (250, 250), 200)
    circle(screen, (0, 0, 0), (250, 250), 200, 3)
    circle(screen, (255, 0, 0), (175, 200), 40)
    circle(screen, (0, 0, 0), (175, 200), 40, 3)
    circle(screen, (255, 0, 0), (330, 200), 30)
    circle(screen, (0, 0, 0), (330, 200), 30, 3)
    circle(screen, (0, 0, 0), (175, 200), 15)
    circle(screen, (0, 0, 0), (330, 200), 15)
    rect(screen, (0, 0, 0), (150, 350, 200, 25))
    line(screen, (0, 0, 0), (80, 100), (220, 175), 13)
    line(screen, (0, 0, 0), (280, 180), (440, 130), 10)

    pygame.display.update()
