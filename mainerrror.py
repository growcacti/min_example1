import pygame as pg
import random
import sys
import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2
from galaxy import *
import get_info

from player import Player
from nme import Nme
from bullets import *

from constants import Constants

from controls import Controls
pg.init()

path = '/home/jh/Desktop/edits2/space_fronteerer_gm_34_12_17_22/gx/planets/'
con = Constants
WHITE = con.WHITE
W = con.W
H - con.H
screen = con.screen
        
def main():

        pg.init()
        clock = con.clock
        ticks = con.ticks
        fps = con.fps
        dt = con.dt
       
      
       
        
       
        font = pg.font.Font(None, 18)
       
        textsurface = font.render('Screen Grid Options                          greybutton                     off                   green grid            Button5', False, (255, 255, 255))
        displaysurf = pg.Surface((1300,800))
        displayrect = pg.Rect(displaysurf.get_rect())
        
        
        s1 = pg.Surface((110,130))
        s2 = pg.Surface((30,30))
        s3 = pg.Surface((30,30))
        
        player = Player((650),(400))
        bg = Expanding_Galaxy(player)
        g = Galaxy(player, dt)
        st = Stars(player)
        control = Controls(player, dt, g,st)
        st.starmap()
        s4 = pg.Surface((75,75))
        nme = Nme((7000), (5000))
        nme2 = Nme((3500), (3200))
        nme2nmedist = Vector2(50, 50)
       
        surf = pg.Surface((3, 3))
        
  
        projectiles = []
        bullets = [] 
              
        bullet = Bullet(nme.position, nme.direction)
        projectile = Projectile(player.position, player.direction)
        hit_count = 0
        
      
                
        counter = 0
      
        
        time_delay = 1000
        timer_event = pg.USEREVENT+1
        pg.time.set_timer(timer_event, time_delay)
            
        loop =1
        while loop:
          
            screen.fill((0,0,0,0))
            
            g.draw(screen, dt)
            screen.blit(st.bg, st.rect)
                             
        
            pos = pg.Vector2(player.position)
            ang = player.angle
           
            text8 = font.render("NME position: " + str(nme.position), True, con.WHITE)
       
            screen.blit(text8, (con.WIDTH - 1100, con.HEIGHT - 680))

           
          
            g.update(dt)
            
            v1 = pg.math.Vector2(player.position)
            v2 = pg.math.Vector2(nme.position)
            v3 = pg.math.Vector2(nme2.position)
            off1 = pg.math.Vector2(-71, -70)
            fcam = pg.Vector2(player.fcam)
            pcam = pg.Vector2(player.camera)
            pppos = pg.Vector2(player.position - (player.rect.width /2, player.rect.height / 2)- pcam)
            ppbullet = pg.Vector2(player.position - (player.rect.width / 64, player.rect.height / 64)- pcam)
            nmebullet = pg.Vector2(nme.rect.center - pcam - off1)
            camx, camy = pcam
            pdir = player.direction
            ndir = nme.direction
           
            start_time = pg.time.get_ticks()
            ffppos = pg.Vector2(player.position - (player.rect.width /128, player.rect.height / 128) - player.subcam)
            tppos = pg.Vector2(player.position - (player.rect.width /256, player.rect.height / 256) - pcam)
            control.buttons(dt)
            nmefire = Bullet(ppbullet, ndir)
            # Event queue
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                        return

                elif event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    return    

                elif event.type == timer_event:
                    counter += 1
                    nmefires = []
                    nmefire = Bullet(nmebullet, ndir)
                    nmefires.append(nmefire)
                    for nmefire in nmefires:
                        displaysurf.blit(nmefire.image, nmefire.rect)
                        
                        nmefire.draw(screen) 
                    
                elif event.type == timer_event:
         
                    counter += 1
          


                if event.type == pg.MOUSEWHEEL:
                    if event.y == 1:
                        player.rotation -= 20 * dt
                    elif event.y == -1:
                        player.rotation += 20 * dt
            
                if event.type == pg.MOUSEMOTION:
                     control.buttons(dt)
   
         



                      # User input & Controls
            pressed = pg.key.get_pressed()
            pressed2 = pg.mouse.get_pressed(num_buttons=5)
            if pressed[pg.K_UP] or pg.mouse.get_pressed()[0]:
                if player.velocity.x < 0:
                    
                    player.acceleration = player.thrust
                    
                else:
                    player.acceleration  += 890 * dt
         
                    
            elif pressed[pg.K_DOWN] or pg.mouse.get_pressed()[1]:
                if player.velocity.x > 0:
                     
                    player.acceleration = -player.thrust
                else:
                    player.acceleration -= 1 * dt

            
               
            elif pressed[pg.K_h]:
                if abs(player.velocity.x) > dt * 10 * player.thrust:
                    player.acceleration = -copysign(
                        player.thrust, player.velocity.x
                    )
                else:
                    player.acceleration = -player.velocity.x / dt
            else:
                if abs(player.velocity.x) > dt * player.sim_inertia:
                    player.acceleration = -copysign(
                        player.sim_inertia, player.velocity.x
                    )
                else:
                    if dt != 0:
                        player.acceleration = -player.velocity.x / dt
            player.acceleration = max(
                -player.max_acceleration,
                min(player.acceleration, player.max_acceleration),
            )


            if pressed[pg.K_RIGHT] or event.type == pg.MOUSEWHEEL:
                player.rotation -= 10 * dt
                
            elif pressed[pg.K_LEFT] or pg.mouse.get_pressed(num_buttons=5)[4]:
                player.rotation += 10 * dt
               
            else:
                player.rotation = 0
            player.rotation = max(
                -player.max_rotation,
                min(player.rotation, player.max_rotation),
            )

        

  
            if pressed[pg.K_SPACE] or pg.mouse.get_pressed()[2]:
                 projectiles.append(Projectile(ppbullet, pdir))
                 for projectile in projectiles:
                     projectile.draw(screen) 

            for projectile in projectiles[:]:
                projectile.update()
                if not screen.get_rect().collidepoint(projectile.pos):
                    projectiles.remove(projectile)
                           
            for projectile in projectiles:
                projectile.draw(screen) 

            
                          
            for projectile in projectiles:
                
                if ship.collidepoint(projectile.pos):
                    print("laser_hit")
                     
            
                   
    

            control.create_buttons()       
            bg.bgupdate(camx, camy)
            player.update(dt)
            player.offset2()
            nme.update(dt)
            nme2.update(dt)
            screen.blit(s1, (640, 400))
            screen.blit(s2, (3000,3000))
            screen.blit(s3, (6000,6000))
            #Variables created to shorten equation for final blit below personal preference to reduce one time long equations.
            # I think the equation might be used again with slight difference
            
            # With the camera being the same velocity set in the Player Class, now is the time to blit the math to the screen to
            # break free of the screen boundary, follow the player position always
           
                     



            # the nme and other creations need the camera subtracted from for them to move independently
            # this took a long time to understand even after reading about it
            screen.blit(s2, nme.position - player.camera)
            screen.blit(s3, nme2.position - player.camera)
            nme.move_towards_player(pos, ang)
            nme2.move_towards_player(pos, ang) 
           
           
            

                          
            player_hits = 0
            vv = v1.distance_to(v2)
            vvv = v1.distance_to(v3)
               
            if v1.distance_to(v2) <= 20:
                 hit_count += 1
                 print("nmehit:")     
                                                 
          
          
                 
            text9 = font.render("NME dist: " + str(vv), True, con.WHITE)
       
            screen.blit(text9, (con.WIDTH - 1100, con.HEIGHT - 700))
            text10 = font.render("NME dist: " + str(vvv), True, con.WHITE)
       
            screen.blit(text10, (con.WIDTH - 1100, con.HEIGHT - 720))
            text11 = font.render("NME pos: " + str(v2), True, con.WHITE)
       
            screen.blit(text11, (con.WIDTH - 1100, con.HEIGHT - 740))
            

            text12 = font.render("hits" + str(hit_count), True, con.WHITE)
                    
            screen.blit(text12, (con.WIDTH - 200, con.HEIGHT - 800))
            
            screen.blit(textsurface,(10, 50))
            

            screen.blit(s1, pppos, player.rect)
       
            
            screen.blit(player.ship, pppos)       

           
            pg.display.flip()

      
            
          
       

       


        pg.quit()


if __name__ == "__main__":
    main()
    

