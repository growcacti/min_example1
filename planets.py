import pygame as pg
import os
import random
from constants import *


con = Constants

screen = con.screen

class Planets:
    def __init__(self):


        self.path ='/home/jh/Desktop/edits2/space_fronteerer_gm_34_12_17_22/gx/planets'
        self.folder = 'gx/planets/'
        self.accept =(".png", ".jpg", ".bmp")
        self.img_dict = {}
        self.keylist =[]
        self.x = 0
        self.y = 0
        self.z = 0
        self.posx = 10
        self.posy = 0
        self.posz = 0
        self.load_img()
    def load_img(self):
        self.folder = 'gx/planets/'
        for pic in os.listdir(self.folder):
            name, ext = os.path.splitext(pic)
            if ext.lower() in self.accept:
                self.img = pg.image.load(os.path.join(self.folder, pic))
                self.img = self.img.convert_alpha()
            self.img_dict[name] = self.img
     
        
     
    def getpos(self):
        self.x =[]
        self.y =[]
        self.z =[]
        for i in range(1, 100):
            self.posx = random.randint(500, 80000)
            self.x.append(self.posx)
            self.posy = random.randint(500, 80000)
            self.y.append(self.posy)
            self.posz = random.randint(500, 80000)
            self.z.append(self.posz)

      
            


