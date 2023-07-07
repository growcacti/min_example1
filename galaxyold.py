import pygame as pg
import random
from constants import Constants
from player import Player


con = Constants
screen = con.screen
W = con.W
H = con.H



class Galaxy:
    
   
    def __init__(self, player):
        self.player = player
        self.screen = screen.copy()
        
        self.img = pg.image.load('gx/bg6.png').convert_alpha()
        self.img6 = pg.image.load('gx/bg2.png').convert_alpha()
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.rect = pg.Rect(self.img.get_rect())
        self.rect2 = pg.Rect(self.img.get_rect())
        self.bgnd = player.background
        self.playrect = player.rect
        self.cam = self.player.camera
        self.invcam = self.player.invcam
        self.subcam = self.player.subcam
        self.revcam = self.player.revcam
        self.extcam = self.player.extcam
        self.camx, self.camy = self.cam
        self.playerpos = pg.math.Vector2(player.position)
        self.start = pg.Vector2(1000, 1000)
        self.markx, self.marky = (20000, 20000)
        self.marker = pg.math.Vector2(self.markx, self.marky)
        self.img2 = self.img.subsurface(self.rect)
        self.img3 = self.img.subsurface(self.rect2)
        self.img4 = pg.transform.smoothscale(self.img, (self.w // 4, self.h // 4))
        self.img5 = pg.transform.smoothscale(self.img, (self.w // 8, self.h // 8))
      
    def draw(self, surface, dt):
        self.dt = dt
        self.distance = self.player.update(dt)
       
        screen.blit(self.img, -self.cam)
        self.adf = abs(self.distance + 1)
        screen.blit(self.img6, self.extcam)     
        screen.blit(self.img, self.extcam)
        screen.blit(self.img4, self.revcam)
        screen.blit(self.img5, self.subcam)
        screen.blit(self.img3, self.extcam)
        if self.distance > 5000 or self.distance <-5000:
            screen.blit(self.img, self.revcam)
            
        if self.distance > 10000 or self.distance <-10000:
            screen.blit(self.img4, self.revcam)
            screen.blit(self.img5, self.subcam)
            screen.blit(self.img2, self.subcam)
        if self.distance > 20000 or self.distance <-20000:
            screen.blit(self.img4, self.invcam)
            screen.blit(self.img5, self.revcam)
            screen.blit(self.img2, self.subcam)
       
        if self.distance > 30000 or self.distance <-30000:
            screen.blit(self.img4, self.revcam)
            screen.blit(self.img5, self.subcam)
            screen.blit(self.img3, self.extcam)
        if self.distance > 40000 or self.distance <-40000:
            screen.blit(self.img5, self.revcam)
            screen.blit(self.img4, self.subcam)
            screen.blit(self.img2, self.subcam)
        if self.distance > 50000 or self.distance <-50000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img3, self.extcam)
            screen.blit(self.img2, self.subcam)
        if self.distance > 80000 or self.distance <-80000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img3, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance > 180000 or self.distance <-150000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img3, self.extcam)
        if self.distance > 250000 or self.distance <-250000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img3, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance > 350000 or self.distance <-350000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img4, self.extcam)
            screen.blit(self.img5, self.subcam)

        if self.distance > 450000 or self.distance <-450000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img4, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance > 550000 or self.distance <-550000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img3, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance > 650000 or self.distance < -650000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img4, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance > 750000 or self.distance <-750000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img4, self.extcam)
            screen.blit(self.img5, self.subcam)

        if self.distance > 850000 or self.distance <-850000:
            screen.blit(self.img3, self.extcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img4, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance > 950000 or self.distance <-950000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img3, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance > 1000000 or self.distance <-1e-6:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img4, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance > 2000000 or self.distance <-1e-7:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img3, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance > 3e6 or self.distance <-1e-8:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img4, self.extcam)
            screen.blit(self.img5, self.subcam)
##        if self.distance > 750000 or self.distance < -750000:
##            screen.blit(self.img3, self.extcam)
##            screen.blit(self.img2, self.subcam)
##            screen.blit(self.img4, self.extcam)
##            screen.blit(self.img5, self.subcam)
##
        if self.distance < 0:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.extcam)
            screen.blit(self.img4, self.extcam)
            screen.blit(self.img5, self.subcam)
        if self.distance < -10000:
            screen.blit(self.img3, self.revcam)
            screen.blit(self.img2, self.subcam)
            screen.blit(self.img4, self.extcam)
            screen.blit(self.img5, self.extcam)    
con = Constants()
class Stars:
    def __init__(self, player):
        
       
        self.player = player
        self.cam = self.player.camera
        self.sizex = int(1400)
        self.sizey = int(900)
        self.size = (1400, 900)
        self.invcam = self.player.invcam
        self.subcam = self.player.subcam
        self.revcam = self.player.revcam
        self.extcam = self.player.extcam
        self.camx, self.camy = self.cam
        self.center_pos = (700, 450)
        self.bg = pg.Surface((self.size))
        self.rect = self.bg.get_rect()
        self.bg.set_colorkey((0, 0, 0))
        self.color = [0,0,0,0]
        self.i =[i for i in range(1400)]
        self.j = [j for j in range(900)]
        self.bg2 = pg.image.load("gx/bg.png").convert_alpha()
        

        self.bg.blit(self.bg2, self.rect)

      
        
      
    def starmap(self):
        
     
        wht = pg.Color('white')
        gry = pg.Color('gray59')
        gry2 = pg.Color('gray80')
        gry3 = pg.Color('gray93')
        snow = pg.Color('snow')
        ivory = pg.Color('ivory')
       
        colorlist = [wht, gry, gry2, gry3, snow, ivory]
       
        for self.color in colorlist:
            self.color = random.choice(colorlist)
 

        # Drawing Stars
        for self.stars in range(400):
            self.starx = random.randint(10, self.sizex)
            self.stary = random.randint(10, self.sizey)
            self.star = self.starx, self.stary
            self.radius = random.randint(1, 2)
            pg.draw.circle(self.bg, self.color, self.star, self.radius)
         # Optional grid screen with 4 colors               
    def grid(self, sel):
        self.sel = sel
        dim = 20
        if self.sel == 1:
           
            self.color=(100,0,10,1)
        elif self.sel== 2:
         
            self.color=(45,94,27,0)
            
        elif self.sel == 3:
        
            self.color = (60,60,60,0)
        elif self.sel == 4:
         
            self.color = (0, 80, 0,0)
        elif self.sel == 5:
            self.bg.fill(0)
            dim = 0
            self.color = (0,0,0,0)
            self.starmap()
            self.bg.blit(self.bg, self.rect)
        elif self.sel == 6:
            self.color=(100,0,10,1)
            dim = 5
            
        elif self.sel== 7:
            self.color=(45,94,27,0)
            dim = 5
           
            
        elif self.sel == 8:
            self.color = (60,60,60,0)
            dim = 5
          
        elif self.sel == 9:
            dim = 10
            
        elif self.sel == 10:
            dim = 10
           
        elif self.sel == 11:
            dim = 50
            
        elif self.sel == 102:
            dim = 100
                

        for i in self.i:
            pg.draw.line(self.bg, (self.color), (i * dim, 0), (i * dim, self.sizey), 1)
            
        for j in self.j:
            pg.draw.line(self.bg, (self.color), (0, j * dim), (self.sizex, j * dim), 1)
            
            


##    def planets(self):
##        p2 = pg.image.load("gx/P2.png").convert_alpha()
##        p3 = pg.image.load("gx/P3.png").convert_alpha()
##        p5 = pg.image.load("gx/P5.png").convert_alpha()
##        p6 = pg.image.load("gx/P6.png").convert_alpha()
##        p7 = pg.image.load("gx/P7.png").convert_alpha()
##        p10 = pg.image.load("gx/P10.png").convert_alpha()
##        p11 = pg.image.load("gx/P11.png").convert_alpha()
##        p12 = pg.image.load("gx/P12.png").convert_alpha()
##        p15 = pg.image.load("gx/P15.png").convert_alpha()
##        p16 = pg.image.load("gx/P16.png").convert_alpha()
##        p17 = pg.image.load("gx/P17.png").convert_alpha()
##       ########################################
##       
##        p3_rect = p3.get_rect(center = (1500, 4600))
##        p5_rect = p5.get_rect(center = (3300, 10000))
##        p6_rect = p6.get_rect(center =  (4700, 8800))
##        p7_rect = p7.get_rect(center = (3600, 300))
##        p10_rect = p10.get_rect(center = (5200, 7100))
##        p11_rect = p11.get_rect(center = (5600, 12000))
##        p12_rect = p12.get_rect(center =  (5800, 14400))
##        p15_rect = p15.get_rect(center = (6600, 11000))
##        p16_rect = p16.get_rect(center = (6800, 3500))
##        p17_rect = p17.get_rect(center = (7000, 13000))
##      ##################################################
##
##       
##       
##        self.bg.blit(p3, p3_rect)
##        self.bg.blit(p5, p5_rect)
##        self.bg.blit(p6, p6_rect)
##        self.bg.blit(p7, p7_rect)
##        self.bg.blit(p10, p10_rect)
##        self.bg.blit(p11, p11_rect)
##        self.bg.blit(p12, p12_rect)
##        self.bg.blit(p15, p15_rect)
##        self.bg.blit(p16, p16_rect)
##        self.bg.blit(p17, p17_rect)
##        
##       

           
