import pygame as pg
import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2
from constants import Constants


con = Constants
screen = con.screen
class Bullet:
    def __init__(self, pos, direction):
        self.x, self.y = pos
        self.pos = self.x, self.y
        self.vel = 2

        self.dir = direction
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
            angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.image = pg.Surface((13, 8))
        self.image.fill((255, 150, 0, 50))
        
        pg.draw.circle(self.image, pg.Color("green"), (8, 4), 3)
        pg.draw.circle(self.image, pg.Color("cyan"), (4, 1), 2)
        pg.draw.circle(self.image, pg.Color("purple"), (4, 1), 3)

        self.rect = self.image.get_rect(center = self.pos)

        self.image = pg.transform.rotate(self.image, angle)
        self.speed = 20
        self.update()
    def update(self):
       
        self.vel += self.speed
        self.pos = (self.pos[0]+self.dir[0]*self.vel, 
                    self.pos[1]+self.dir[1]*self.vel)

    def draw(self, surf):
        self.rect = self.image.get_rect(center = self.pos)
        surf.blit(self.image, self.rect)
        screen.blit(self.image, self.rect)
        pg.display.update(self.rect)   
        return self.rect

    
       
class Projectile:
    def __init__(self, pos, direction):
        self.x, self.y = pos
        self.pos = self.x, self.y

        self.dir = direction
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
            angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.image = pg.Surface((12, 10))
        self.image.fill((255, 180, 0, 1))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center = self.pos)
        pg.draw.circle(self.image, pg.Color("purple"), (6, 4), 3)
        pg.draw.circle(self.image, pg.Color("blue"), (4, 2), 5)
        pg.draw.circle(self.image, pg.Color("cyan"), (2, 3), 5)
##        self.projectile = pg.Surface((10, 6)).convert_alpha()
##        self.rect = self.image.get_rect(center = self.pos)
##        self.projectile.fill((255, 0, 0))
        self.image = pg.transform.rotate(self.image, angle)
        self.speed = 5
        self.update()
    def update(self):
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        self.rect = self.image.get_rect(center = self.pos)
        surf.blit(self.image, self.rect)
        pg.display.update(self.rect)   
        return self.rect
        
    
        

