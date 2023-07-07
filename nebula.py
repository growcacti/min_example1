


import pygame as pg
import random
from constants import Constants

con  = Constants
W = con.W
H = con.H
screen = con.screen
class Nebula:
    neb1 = pg.image.load('gx/neb1.png').convert_alpha()
    neb2 = pg.image.load('gx/neb2.png').convert_alpha()
    neb3 = pg.image.load('gx/neb3.png').convert_alpha()
    def __init__(self, pcam):
        self.camx, self.camy = pcam
        self.surf = pg.Surface((2000,2000))
        self.neblist = [self.neb1, self.neb2, self.neb3]
        self.neb = random.choice(self.neblist)
        self.xlow = (self.camx + W) // 1
        self.xhigh = (self.camx + (2 * W)) // 1
        self.ylow = (self.camy + H) // 1
        self.yhigh = (self.camy + (2 * H)) // 1
     
        self.nebw = self.neb.get_width()
        self.nebh = self.neb.get_height()
        self.get_randpos()
        self.neblist = []

    def get_randpos(self):
        self.rx = random.randint(self.xlow, self.xhigh)
        self.ry = random.randint(self.ylow, self.yhigh)
        self.rx1 = random.randint(self.xlow, self.xhigh)
        self.ry1 = random.randint(self.ylow, self.yhigh)
        self.neblist.append(self.rx)
        self.neblist.append(self.ry)
        self.neblist.append(self.rx1)
        self.neblist.append(self.ry1)
        return self.rx, self.ry, self.rx1, self.ry1
        

    def draw(self, surface):
        
        self.nebrect = pg.Rect(self.rx1, self.ry1, self.rx, self.ry)
        for self.neb in self.neblist:
            screen.blit(self.neb, (200,200))
            surface.blit(self.neb, (200,200))
            self.surf.blit(self.neb, (200,200))
