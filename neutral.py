import pygame as pg

import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2




LERP_FACTOR      = 0.005
minimum_distance = 80

maximum_distance = 10000
class Neutrals:
    def __init__(
        self, image, x, y, angle=0.0, length=4, max_rotation=10, max_acceleration=5.0
    ):
        self.x = x
        self.y = y
        self.orig_image = image
        self.font = pg.font.Font(None, 18)
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = 5
        self.max_rotation = max_rotation
        self.max_velocity = 12
        self.thrust = 5
        self.sim_inertia = 0.1  # iner

        self.acceleration = 5
        self.rotation = 0.0
        self.mask = pg.mask.from_surface(self.image)
        self.direction = Vector2(0, 0)
        self.group = []
    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(
            -self.max_velocity, min(self.velocity.x, self.max_velocity)
        )

        if self.rotation:
            turning_radius = self.length / tan(radians(self.rotation))
            angular_velocity = self.velocity.x / turning_radius / 2
        else:
            angular_velocity = 0

        vel = self.velocity.rotate(-self.angle) * dt
        self.position += vel
       
        self.rect.center = self.position
        self.angle += degrees(angular_velocity) * dt

        self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.direction = self.angle
        self.move_around()
    def move_around(self):
        
   

        goal1 = Vector2(13000, 13000)    
        goal2 = Vector2(100, 1000)
        goal3 = Vector2(7500, 7500)
        if self.position[0] >= goal2[0] and self.position[1] <= goal[1]:
              
            self.angle = 215
            
            
          
                  
        elif self.position[0] <= goal2[0] and self.position[1] <= goal2[1]:
            
            self.angle = 330
           
          
        elif self.position[0] >= goal3[0] and self.position[1] >= goal3[1]:
            self.angle = 120
          
            
        elif self.position[0] <= goal1[0] and self.position[1] >= goal1[1]:
            
            self.angle = 45
           
         elif self.position[0] <= goal2[0] and self.position[1] <= goal2[1]:
            
            self.angle = 330
           
          
        elif self.position[0] >= goal3[0] and self.position[1] >= goal3[1]:
            self.angle = 120
          
            
        elif self.position[0] <= goal1[0] and self.position[1] >= goal1[1]:
            
            self.angle = 45
        elif self.position[0] <= goal2[0] and self.position[1] <= goal2[1]:
            
            self.angle = 330
           
          
        elif self.position[0] >= goal1[0] and self.position[1] >= goal1[1]:
            self.angle = 120
          
            
        elif self.position[0] <= goal3[0] and self.position[1] >= goal1[1]:
            
            self.angle = 45
           

       

            
        return (self.position, self.angle) 



