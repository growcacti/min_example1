import pygame as pg
import sys
import os
from player import Player
from constants import Constants



con = Constants
screen = con.screen



class Controls:
    def __init__(self, player,dt):
        self.button = pg.Rect(10, 10, 30, 30)
        self.button2 = pg.Rect(30, 75, 30, 30)
        self.button3 = pg.Rect(50, 125, 30, 30)
        self.button4 = pg.Rect(80, 175, 30, 30)
        self.surf= pg.Surface((2000, 1000))
        self.player = player
        self.dt = dt
       




    def buttons(self, dt):
        self.dt = dt
        self.mouse_pos = pg.mouse.get_pos()
        self.mouse_rel = pg.mouse.get_rel()
       

        if self.button.collidepoint(self.mouse_pos):
            print("button 1")
            self.warp = 0
            self.player.update(self.dt, self.warp)
          
         

        if self.button2.collidepoint(self.mouse_pos):
            print("button2")
            self.warp = 1
            self.player.update(self.dt, self.warp)
          

        if self.button3.collidepoint(self.mouse_pos):
            print("button3")
            self.warp = 2
            self.player.update(self.dt, self.warp)

        if self.button4.collidepoint(self.mouse_pos):
            self.warp = 3
            self.player.update(self.dt, self.warp)

    def create_buttons(self):

        pg.draw.rect(screen, pg.Color(200, 0, 0,200), self.button)
        pg.draw.rect(screen, pg.Color(200,165,0,200), self.button2)
        pg.draw.rect(screen, pg.Color(200,0,200,200), self.button3)
        pg.draw.rect(screen, pg.Color(200, 255, 60,200), self.button4)
    def draw(self):
        screen.blit(self.surf, self.button)
    
