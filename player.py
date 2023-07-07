import pygame as pg
import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2
from constants import Constants
import get_info



con = Constants

HEIGHT = con.HEIGHT
WIDTH = con.WIDTH

screen = con.screen
WHITE =con.WHITE
CW = WIDTH / 2
CH = HEIGHT / 2
class Player:
    def __init__(
        self, x, y, angle=0.0, length=4, max_rotation=10, max_acceleration=5.0):
       
            
        self.ship = pg.Surface((50,50))
        
        self.x = x
        self.y = y
        self.position  = (self.x, self.y)
        self.image= pg.Surface((80,80))
        self.surf=  pg.Surface((80,80))
        self.rect = pg.Rect(self.image.get_rect())
        self.pos = self.position
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
         
        self.ship = pg.draw.polygon(self.image,pg.Color("dodgerblue"),((0, 0), (32, 16), (0, 32)))
        self.img = pg.draw.polygon(self.surf,pg.Color("dodgerblue"),((0, 0), (32, 16), (0, 32)))
        self.max_acceleration = 1500
        self.max_rotation = max_rotation
        self.max_velocity = 80
        self.thrust = 25
        self.sim_inertia = 0.5  # iner
        self.font = pg.font.Font(None, 20)
        self.acceleration = 0.0
        self.rotation = 0.0
        self.background = Vector2(self.position)
        self.camera = Vector2(0, 0)
        self.revcam = Vector2(0, 0)
        self.subcam = Vector2(0, 0)
        self.invcam = Vector2(0, 0)
        self.extcam = Vector2(0, 0)
        self.fcam = Vector2(0, 0)
        # Assigned the camera.era as an attribute.
        self.direction = Vector2(0, 0)
        self.warp = 0
        
        self.ship = pg.transform.rotozoom(self.surf, 0, 1)
       
    def update(self, dt, warp=0):
        
        con = Constants
        self.warp = warp
        if self.warp == 0:
            self.max_velocity = 600
            self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
            self.velocity += (self.acceleration * dt, 0)
                    
        elif self.warp == 1:
            self.max_velocity = 800
            self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
            self.velocity += (self.acceleration * 100 * dt, 0)
          
        elif self.warp == 2:
            self.max_velocity = 8000
            self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
            self.velocity += (self.acceleration, 0)
            self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
        else:
          
            self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
            self.velocity += (self.acceleration * dt, 0)
      

        if self.rotation:
            turning_radius = self.length / tan(radians(self.rotation))
            angular_velocity = self.velocity.x / turning_radius / 4
        else:
            angular_velocity = 0

        vel = self.velocity.rotate(-self.angle) * dt
        self.position += vel
        fvel = vel * 1.1
        bvel = vel / -300
        
        cvel = vel / -100
        rvel = vel / -1
        svel = vel / -40
        invvel = vel / -10
        extvel = vel / -400
        self.camera += cvel  # Update the camera.era position as well.
        self.revcam += rvel
        self.subcam += svel
        self.invcam += invvel
        self.extcam += extvel
        self.background += bvel
        self.fcam -= fvel
        # If you use the rect as the blit position, you should update it, too.
        self.rect.center = self.position
        self.angle += degrees(angular_velocity) * dt
       
     
     
        self.direction = pg.Vector2(1, 0).rotate(-self.angle)
        pg.display.set_caption("Space Fronteerer")
 
        text1 = self.font.render("position: " + str(self.position), True, WHITE)
       
        screen.blit(text1, (WIDTH - 200, HEIGHT - 750))
    
        origin = (650, 400)
        destination = self.rect.center
        svp = math.sqrt (vel[0] ** 2 + vel[1]**2) * 671000000
        sp = abs(svp) // 100000
        
        distance, angle, x_ref, y_ref, op_ang, project, project2 =  get_info.info(origin, destination)
        dist = distance // 1
        show_angle = self.angle % 360
       
                
        self.project = project[0] // 1, project[1] // 1
        self.project2 = project2[0] // 1, project2[1] // 1
        text2 = self.font.render("Distance from Start: " + str(dist), True, WHITE)
        screen.blit(text2, (WIDTH - 200, HEIGHT - 780))
        text3 = self.font.render("Angle " + str(show_angle), True, WHITE)
        screen.blit(text3, (WIDTH - 200, HEIGHT - 770))
        text5 = self.font.render("MPH " + str(sp), True, WHITE)
        screen.blit(text5, (WIDTH - 200, HEIGHT - 760))
    
        self.projected = int(self.project[0]), int(self.project[1])
       
        self.projected2 = int(self.project2[0]), int(self.project2[1])
        self.distance = distance
        text6 = self.font.render("projected1 " + str(self.projected), True, WHITE)
        screen.blit(text6, (WIDTH - 200, HEIGHT - 720))

        text7 = self.font.render("projected2 " + str(self.projected2), True, WHITE)
        screen.blit(text7, (WIDTH - 200, HEIGHT - 700))
        return self.distance, self.projected, self.projected2
    def offset(self):
        MARGINX = 550
        MARGINY = 350
        self.cam = self.camera 
     
        
        if (self.cam.x + CW) - self.position.x > MARGINX:
        
            self.cam.x = (self.position.x + MARGINX - CW) 

        elif self.position.x - (self.cam.x + CW) > MARGINX:
            self.cam.x = (self.position.x - MARGINX - CW) 
        if (self.cam.y + CH) - self.position.y > MARGINY:
            self.cam.y = int(self.position.y + MARGINY - CH) 
        elif self.position.y - (self.cam.y + CH) > MARGINY:
            self.cam.y = int(self.position.y - MARGINY - CH)

    def offset2(self):
        mx = 200
        my = 100
        self.cam = self.camera 
     
        
        if (self.cam.x + CW) - self.position.x > mx:
        
            self.cam.x = (self.position.x + mx - CW) 

        elif self.position.x - (self.cam.x + CW) > mx:
            self.cam.x = (self.position.x - mx - CW) 
        if (self.cam.y + CH) - self.position.y > my:
            self.cam.y = int(self.position.y + my - CH) 
        elif self.position.y - (self.cam.y + CH) > my:
            self.cam.y = int(self.position.y - my - CH)


    def surface_offset(self):
        self.extx, self.exty = self.extcam
        self.extnegx, self.extnegy = -self.extcam
        self.extposx = 2 * self.position.x
        self.extposy = 2 * self.position.y

