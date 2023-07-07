import pygame as pg
import os
import random
from constants import Constants
from player import Player


con = Constants
screen = con.screen
W = con.W
H = con.H
W2 = con.W2
H2 = con.H2
QW = W / 4
HW = W/2
HH = H /2
QH = H / 4




screen = con.screen


WIDTH = con.WIDTH
HEIGHT = con.HEIGHT
WHITE = con.WHITE
    
pg.init()
 

RED = (255,0,0)

# Game Setup

 
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('testing Game coded!')

class Expanding_Galaxy:
    
	
                 
    def __init__(self, player):

        self.wht = pg.Color('white')
        self.gry = pg.Color('gray59')
        self.cyan = pg.Color("turquoise1")
        self.colorlist = [self.wht,self.gry,self.cyan]
        self.surf1 = pg.Surface((6,6)).convert_alpha()
        self.surf2 = pg.Surface((6,6)).convert_alpha()
        self.surf3 = pg.Surface((6,6)).convert_alpha()
        self.surf4 = pg.Surface((6,6)).convert_alpha()
        self.surf5 = pg.Surface((6,6)).convert_alpha()
        self.surf6 = pg.Surface((6,6)).convert_alpha()
        self.surf7 = pg.Surface((6,6)).convert_alpha()
        self.surf8 = pg.Surface((6,6)).convert_alpha()
        self.surf9 = pg.Surface((6,6)).convert_alpha()
        self.surf10 = pg.Surface((6,6)).convert_alpha()
        self.surf11 = pg.Surface((6,6)).convert_alpha()
        self.surf12 = pg.Surface((6,6)).convert_alpha()
        self.starlist = []
        for i in range(1, 12):
            self.starlist.append('surf%d' % i)
            print(self.starlist)

       
    
            for self.color in self.colorlist:
                self.color = random.choice(self.colorlist)
                self.radius = 1
                self.pos = (3, 3)
                pg.draw.circle(self.surf1, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf2, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf3, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf4, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf5, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf6, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf7, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf8, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf9, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf10, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf11, self.color, self.pos, self.radius)
                pg.draw.circle(self.surf12, self.color, self.pos, self.radius)




       
 

    
        self.player = player
        self.cam = self.player.camera
        self.camx, self.camy = self.cam
        self.img = []
        self.bgdata = []
        self.player = player
        self.x = 1000
        self.y = 1000
        self.w = W
        self.H = H
        


    def coordinates(self, camx, camy, objw, objh):
      
        self.camxx = 2*self.camx
        self.camyy = 2*self.camy
        self.camrect = pg.Rect(self.camx, self.camy, W, H)
        while 1:
           
            self.startx = int(self.camx) - (W) //1
            self.stopx = int(self.camx) + (W2)// 1
            self.starty = int(self.camy) - (H) //1
            self.stopy = int(self.camy) + (H2)// 1
            self.rx = random.randint(self.startx, self.stopx)
            self.ry = random.randint(self.starty, self.stopy)
            self.objrect = pg.Rect(self.rx, self.ry, objw, objh)
            if not self.objrect.colliderect(self.camrect):
               
                return self.rx, self.ry
    
    
    def add_bg(self, camx, camy):
        self.bg = {}
     
    
        self.bg['img'] = self.starlist
       
        self.bg['width'] = 6
        self.bg['height'] = 6

      
        self.bg['x'], self.bg['y'] = self.coordinates(camx, camy, self.bg['width'], self.bg['height'])
        self.bg['rect'] = pg.Rect( (self.bg['x'], self.bg['y'], self.bg['width'], self.bg['height']) )
        
        return self.bg
    def boundaries(self, camx, camy, bg):
        # Return False if camx and camy are more than
        # a half-window length beyond the edge of the window.
        self.bounds_left = self.camx - W
        self.bounds_top = self.camy - H
        self.boundsrect = pg.Rect(self.bounds_left, self.bounds_top, W2*2, H2*2)
        self.objrect = pg.Rect(self.bg['x'], self.bg['y'], self.bg['width'], self.bg['height'])
        return not self.boundsrect.colliderect(self.objrect)        



    def bgupdate(self, camx, camy):
       
         self.camx = camx
         self.camy  = camy
         if len(self.bgdata) < 3000000:
             self.bgdata.append(self.add_bg(self.camx, self.camy))
         for self.bg in self.bgdata:
            self.mrect = pg.Rect( (self.bg['x'] - self.camx, self.bg['y'] - self.camy, self.bg['width'], self.bg['height']) )
            
            screen.blit(self.surf1, self.mrect)
            screen.blit(self.surf2, self.mrect)
            screen.blit(self.surf3, self.mrect) 
            screen.blit(self.surf4, self.mrect)
            screen.blit(self.surf5, self.mrect)
            screen.blit(self.surf6, self.mrect) 
          
         for i in range(len(self.bgdata) - 1, -1, -1):
            if self.boundaries(self.camx, self.camy, self.bgdata[i]):
                del self.bgdata[i]
         return self.starlist, self.mrect 
     






    


   
class Galaxy:
   
   
    pass
                    
con = Constants()
class Stars:
    
    def __init__(self, player):
        pass
##        
##       
##        self.player = player
##        self.cam = self.player.camera
##        self.sizex = int(1300)
##        self.sizey = int(800)
##        self.size = (1300, 800)
##        self.invcam = self.player.invcam
##        self.subcam = self.player.subcam
##        self.revcam = self.player.revcam
##        self.extcam = self.player.extcam
##        self.camx, self.camy = self.cam
##        self.center_pos = (650, 400)
##        self.bg = pg.Surface((self.size))
##        self.rect = self.bg.get_rect()
##        self.bg.set_colorkey((0, 0, 0))
##        self.color = [0,0,0,0]
##       
##              
##
##       
##      
##        
##    def starmap(self):
##        
##     
##        wht = pg.Color('white')
##        gry = pg.Color('gray59')
##        gry2 = pg.Color('gray80')
##        gry3 = pg.Color('gray93')
##        snow = pg.Color('snow')
##        ivory = pg.Color('ivory')
##        cyan = pg.Color("turquoise1")
##        self.colorlist = [wht, gry, gry2, gry3, snow, ivory, cyan]
##       
##        for self.color in self.colorlist:
##            
##            for self.stars in range(10):
##                self.color = random.choice(self.colorlist)
##                self.starx = random.randint(10, self.sizex)
##                self.stary = random.randint(10, self.sizey)
##                self.star = self.starx, self.stary
##                self.radius = 1
##                for self.stars in range(5):
##                    self.color = random.choice(self.colorlist)
##                    self.starx = random.randint(10, self.sizex)
##                    self.stary = random.randint(10, self.sizey)
##                    self.star = self.starx, self.stary
##                    self.radius = 1
##                    pg.draw.circle(self.bg, self.color, self.star, self.radius)
##
##
##     
##
##
