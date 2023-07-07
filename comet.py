import pygame as pg
from pygame.math import Vector2


class Comet:
    def __init__(self, image, x, y, angle=0.0):
        
        
        self.orig_image = image
        
        self.image = image
        self.rect = self.image
        self.position = Vector2(x, y)
        self.velocity = Vector2(1.0, 1.0)
        self.angle = angle
        self.max_acceleration = 0.01
        self.max_velocity = 0.01
        self.thrust = 0.01
        self.angle = 45

        self.acceleration = 0.0
        self.rotation = 0.0
       
        self.direction = Vector2(1, 0)
        
    def update(self, dt):
        vel = self.velocity.rotate(-self.angle) * dt
        self.velocity += (self.acceleration * dt, 0)
        if self.rotation:
            turning_radius = self.length / tan(radians(self.rotation))
            angular_velocity = self.velocity.x / turning_radius / 2
        else:
            angular_velocity = 0

        vel = self.velocity.rotate(-self.angle) * dt
        self.position += vel
        
        # If you use the rect as the blit position, you should update it, too.
        self.rect.center = self.position
       
       
       
        #self.direction = self.angle
        self.direction = pg.Vector2(1, 0).rotate(-self.angle)
       
        self.route()
    def route(self):
     
       
        self.boundaries()
    def boundaries(self):


        topleft = Vector2(0,0)
        bottomleft = Vector2(0, 15000)
        bottomright = Vector2(15000, 15000)
        topright = Vector2(15000, 0)
        if self.position[0] > 14000:
            self.angle = 180
        elif self.position[0] < 200:
            self.angle = 0
        elif self.position[1] < 200:
            self.angle = 270
        elif self.position[1] > 14000:
            self.angle = 90
        elif self.position[0] <= topleft[0] and self.position[0] <= topleft[1]:
            self.angle = 330 
        elif self.position[0] <= topright[0] and self.position[1] <= topright[1]:
            self.angle = 225
        elif self.position[0] <= bottomleft[0] and self.position[1] >= bottomleft[1]:
            self.angle = 45
            self.acceleration = self.thrust
        elif self.position[0] >= bottomright[0] and self.position[1] >= bottomleft[1]:
            self.angle = 135  
                  

    
            
