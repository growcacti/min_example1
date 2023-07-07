import pygame as pg




class Constants:
   
    WHITE = ((255,255,255))
    WIDTH = 1300
    HEIGHT = 800
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen_rect = screen.get_rect()
    SIZE = (WIDTH, HEIGHT)
    W = WIDTH
    H = HEIGHT
    W2 = 2*W
    H2 = 2*H
    HW = W / 2
    QW = W / 4
    HQW = HW + QW
    HH = H /2
    QH = H / 4
    HQH = HH + QH
    clock = pg.time.Clock()
    ticks = 30
    fps = ticks
    dt = fps / 1000
    


