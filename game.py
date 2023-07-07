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

class Game:
    def __init__(self):
        self.con = Constants()
        self.WHITE = self.con.WHITE
        self.W = self.con.W
        self.H = self.con.H
        self.screen = self.con.screen
        self.clock = self.con.clock
        self.ticks = self.con.ticks
        self.fps = self.con.fps
        self.dt = self.con.dt
        self.player = Player((650), (400))
      
        self.textsurface = None
        self.displaysurf = None
        self.displayrect = None
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.nme = None
        self.nme2 = None
        self.nme2nmedist = None
        self.surf = None
        self.projectiles = []
        self.bullets = []
        self.bullet = None
        self.projectile = None
        self.hit_count = 0
        self.c = None
        self.counter = 0
        self.time_delay = 1000
        self.timer_event = pg.USEREVENT + 1
        
        
        self.ang = self.player.angle

    def setup(self):
        pg.init()
        pg.time.set_timer(self.timer_event, self.time_delay)
        
        self.pos = self.player.position
        self.bg = Expanding_Galaxy(self.player)
        self.font = pg.font.Font(None, 18)
        self.textsurface = self.font.render('Screen Grid Options                          greybutton                     off                   green grid            Button5', False, (255, 255, 255))
        self.displaysurf = pg.Surface((1300, 800))
        self.displayrect = pg.Rect(self.displaysurf.get_rect())
        self.s1 = pg.Surface((110, 130))
        self.s2 = pg.Surface((30, 30))
        self.s3 = pg.Surface((30, 30))
        self.nme = Nme((7000), (5000))
        self.nme2 = Nme((3500), (3200))
        self.nme2nmedist = Vector2(50, 50)
        self.surf = pg.Surface((3, 3))
        self.c = Controls(self.player, self.dt)
        self.loop = True

    def handle_events(self):
        pressed = pg.key.get_pressed()
        pressed2 = pg.mouse.get_pressed(num_buttons=5)
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
            elif event.type == self.timer_event:
                self.counter += 1
                self.nmefires = []
                self.nmefire = Bullet(self.nmebullet, self.pdir)
                self.nmefires.append(self.nmefire)
                for self.nmefire in self.nmefires:
                    self.displaysurf.blit(self.nmefire.image, self.nmefire.rect)
                    self.nmefire.draw(self.screen)
            elif event.type == self.timer_event:
                self.counter += 1
            if event.type == pg.MOUSEWHEEL:
                if event.y == 1:
                    self.player.rotation -= 20 * self.dt
                    pg.transform.rotate(self.player.image, 270,1)
                elif event.y == -1:
                    self.player.rotation += 20 * self.dt
                    pg.transform.rotate(self.player.image, 90,-1)
            if pressed[pg.K_UP] or pg.mouse.get_pressed()[0]:
                if self.player.velocity.x < 0:
                    self.player.acceleration = self.player.thrust
                else:
                    self.player.acceleration += 890 * self.dt
            elif pressed[pg.K_DOWN] or pg.mouse.get_pressed()[1]:
                if self.player.velocity.x > 0:
                    self.player.acceleration = -self.player.thrust
                else:
                    self.player.acceleration -= 1 * self.dt
            elif pressed[pg.K_h]:
                if abs(self.player.velocity.x) > self.dt * 10 * self.player.thrust:
                    self.player.acceleration = -copysign(
                        self.player.thrust, self.player.velocity.x
                    )
                else:
                    self.player.acceleration = -self.player.velocity.x / self.dt
            else:
                if abs(self.player.velocity.x) > self.dt * self.player.sim_inertia:
                    self.player.acceleration = -copysign(
                        self.player.sim_inertia, self.player.velocity.x
                        )
                else:
                    if self.dt != 0:
                        self.player.acceleration = -self.player.velocity.x / self.dt
                        self.player.acceleration = max(
                            -self.player.max_acceleration,
                            min(self.player.acceleration, self.player.max_acceleration),
                        )
            if pressed[pg.K_RIGHT] or event.type == pg.MOUSEWHEEL:
                self.player.rotation -= 40 * self.dt
                pg.transform.rotozoom(self.player.image, -90, 1)
            elif pressed[pg.K_LEFT] or pg.mouse.get_pressed(num_buttons=5)[4]:
                self.player.rotation += 40 * self.dt
                pg.transform.rotozoom(self.player.image,90,1)
            else:
                self.player.rotation = 0
            self.player.rotation = max(
                -self.player.max_rotation,
                min(self.player.rotation, self.player.max_rotation),
            )
            if pressed[pg.K_SPACE] or pg.mouse.get_pressed()[2]:
                self.projectiles.append(Projectile(self.ppbullet, self.pdir))
            for projectile in self.projectiles[:]:
                projectile.update()
                if not self.screen.get_rect().collidepoint(projectile.pos):
                    self.projectiles.remove(projectile)
            for projectile in self.projectiles:
                projectile.draw(self.screen)
            for projectile in self.projectiles:
                if self.player.rect.collidepoint(projectile.pos):
                    print("laser_hit")
    def update(self):
        self.screen.fill((0, 0, 0, 0))
        self.pos = pg.Vector2(self.player.position)
        self.ang = self.player.angle
        text8 = self.font.render("NME position: " + str(self.nme.position), True, self.con.WHITE)
        self.screen.blit(text8, (self.con.WIDTH - 1100, self.con.HEIGHT - 680))
        self.c.draw()
        v1 = pg.math.Vector2(self.player.position)
        v2 = pg.math.Vector2(self.nme.position)
        v3 = pg.math.Vector2(self.nme2.position)
        off1 = pg.math.Vector2(-71, -70)
        fcam = pg.Vector2(self.player.fcam)
        pcam = pg.Vector2(self.player.camera)
        self.pppos = pg.Vector2(self.player.position) - pg.Vector2(self.player.rect.width / 2, self.player.rect.height / 2) - pcam

        self.ppbullet = pg.Vector2(self.player.position - pg.Vector2(self.player.rect.width / 64, self.player.rect.height / 64) - pcam)
        self.nme_pos = (self.nme.position - pcam)
        self.nmebullet = pg.Vector2(self.nme.rect.center - pcam - off1)
        self.camx, self.camy = pcam
        self.pdir = self.player.direction
        self.ndir = self.nme.direction
        start_time = pg.time.get_ticks()
        ffppos = pg.Vector2(self.player.position - pg.Vector2(self.player.rect.width / 128, self.player.rect.height / 128) - self.player.subcam)
       
        self.nmefire = Bullet(self.ppbullet, self.pdir)
        
        
        self.bg.bgupdate(self.camx, self.camy)
        self.player.update(self.dt)
        self.player.offset2()
        self.nme.update(self.dt)
        self.nme2.update(self.dt)
        self.screen.blit(self.s2, self.nme.position - self.player.camera)
        self.screen.blit(self.s3, self.nme2.position - self.player.camera)
        self.nme.move_towards_player(self.pos, self.ang)
        self.nme2.move_towards_player(self.pos, self.ang)
        player_hits = 0
        vv = v1.distance_to(v2)
        vvv = v1.distance_to(v3)
        if v1.distance_to(v2) <= 20:
            self.hit_count += 1
            print("nmehit:")
        text9 = self.font.render("NME dist: " + str(vv), True, self.con.WHITE)
        self.screen.blit(text9, (self.con.WIDTH - 1100, self.con.HEIGHT - 700))
        text10 = self.font.render("NME dist: " + str(vvv), True, self.con.WHITE)
        self.screen.blit(text10, (self.con.WIDTH - 1100, self.con.HEIGHT - 720))
        text11 = self.font.render("NME pos: " + str(v2), True, self.con.WHITE)
        self.screen.blit(text11, (self.con.WIDTH - 1100, self.con.HEIGHT - 740))
        text12 = self.font.render("hits" + str(self.hit_count), True, self.con.WHITE)
        self.screen.blit(text12, (self.con.WIDTH - 200, self.con.HEIGHT - 800))
        self.screen.blit(self.textsurface, (10, 50))
        self.screen.blit(self.nme.image, self.nme_pos)
        self.screen.blit(self.player.ship, self.pppos)
        pg.display.flip()

    def main(self):
        self.setup()
        while self.loop:
            self.handle_events()
            self.update()

        pg.quit()

def main():
    game = Game()
    game.main()

if __name__ == "__main__":
    main()
