import pygame as pg

import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2




LERP_FACTOR      = 0.01
minimum_distance = 200

maximum_distance = 10000
class Nme:
    def __init__(
        self, x, y, angle=0.0, length=4, max_rotation=10, max_acceleration=5.0
    ):
        self.x = x
        self.y = y
        self.image = pg.Surface((30,30))
        self.ship = pg.draw.polygon(self.image,
                                    pg.Color("red"),
                                    ((0, 0), (32, 16), (0, 32)))
        
       
        self.font = pg.font.Font(None, 18)
        self.orig_image = self.image.copy()
        self.rect = pg.Rect(self.image.get_rect())
        self.position = Vector2(self.x, self.y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = 2
        self.max_rotation = max_rotation
        self.max_velocity = 5
        self.thrust = 5
        self.sim_inertia = 50  # iner

        self.acceleration = 1
        self.rotation = 0.0
        
        self.direction = Vector2(0, 0)
        self.group = []
    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(
            -self.max_velocity, min(self.velocity.x, self.max_velocity)
        )

##        if self.rotation:
##            turning_radius = self.length / tan(radians(self.rotation))
##            angular_velocity = self.velocity.x / turning_radius / 128
##        else:


        angular_velocity = 0
##        
        vel = self.velocity * dt
        self.position += vel
       
        self.rect.center = self.position
        self.angle += degrees(angular_velocity) * dt * 10

        self.rect = self.image.get_rect(center=self.rect.center)
      
        self.direction = pg.Vector2(1, 0).rotate(-self.angle)
    def move_towards_player(self, pos, ang):
        
   


        distance = self.position.distance_to(pos)
        if distance > minimum_distance:
            direction_vector    = (pos - self.position) / distance
            min_step            = max(0, distance - maximum_distance)
            max_step            = distance - minimum_distance
            step_distance       = min_step + (max_step - min_step) * LERP_FACTOR
            self.position = self.position + direction_vector * step_distance

            
        if self.position == minimum_distance:
            self.angle = 0

      
            
        if self.position[0] >= pos[0] and self.position[1] <= pos[1]:
              
            self.angle = 215
            
        elif self.position[0] == pos[0] and self.position[1] < pos[1]:
            
            self.angle = 270

        elif self.position[0] == pos[0] and self.position[1] > pos[1]:
            
            self.angle = 90
          
        elif self.position[0] < pos[0] and self.position[1] == pos[1]:
            
            self.angle = 0

        elif self.position[0] < pos[0] and self.position[1] == pos[1]:
            
            self.angle = 180
                  
        elif self.position[0] <= pos[0] and self.position[1] <= pos[1]:
            
            self.angle = 330
           
          
        elif self.position[0] >= pos[0] and self.position[1] >= pos[1]:
            self.angle = 120
          
            
        elif self.position[0] <= pos[0] and self.position[1] >= pos[1]:
            
            self.angle = 45
           
        else:
            self.angle = ang

       

            
        return (self.position, self.angle) 



