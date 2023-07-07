import pygame
from pygame.locals import *

#initstuff
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('PiMaze')
instances=[]
level='save.bin'

#loadsprites
menuspr=pygame.image.load('images/menu.png').convert()
b1spr=pygame.image.load('images/b1.png').convert()
b2spr=pygame.image.load('images/b2.png').convert()
b3spr=pygame.image.load('images/b3.png').convert()
currentbspr=b1spr
curspr=pygame.image.load('images/curs.png').convert()
curspr.set_colorkey((0,255,0))

#menu
menuspr.set_alpha(185)
menurect=menuspr.get_rect(x=-260,y=4)

class MenuItem(object):
    def __init__(self,pos,spr):
        self.x=pos[0]
        self.y=pos[1]
        self.sprite=spr
        self.pos=(self.x,self.y)
        self.rect=self.sprite.get_rect(x=self.x,y=self.y)

class Block(object):
    def __init__(self,x,y,spr):
        self.x=x
        self.y=y
        self.sprite=spr
        self.rect=self.sprite.get_rect(x=self.x,y=self.y)

def CreateLevel(levelname):
    f=open(levelname,'r')
    obj=f.read()
    f.close()
    obj=obj.split('.')
    for b in obj:
        instances.append(eval(b))

try:
    CreateLevel(level)
except:
    pass

f=open(level,'a+')

while True:
    #menu items
    b1menu=b1spr.get_rect(x=menurect.left+32,y=48)
    b2menu=b2spr.get_rect(x=menurect.left+64,y=48)
    b3menu=b3spr.get_rect(x=menurect.left+96,y=48)
    menuitems=[MenuItem(b1menu,b1spr),MenuItem(b2menu,b2spr),MenuItem(b3menu,b3spr)]

    screen.fill((20,30,85))
    mse=pygame.mouse.get_pos()
    key=pygame.key.get_pressed()
    placepos=((mse[0]/16)*16,(mse[1]/16)*16)
    if key[K_q]:
        if mse[0]<260:
            if menurect.right<255:
                menurect.right+=1
        else:
            if menurect.left>-260:
                menurect.left-=1
    else:
        if menurect.left>-260:
            menurect.left-=1
    for e in pygame.event.get():
        if e.type==QUIT:
            f.close()
            exit()

        if menurect.right<100:
            if key[K_LSHIFT]:
                if pygame.mouse.get_pressed()==(1,0,0):
                    to_remove = [i for i in instances if i.rect.collidepoint(placepos)]
                    if not to_remove:
                        instances.append(Block(placepos[0],placepos[1],currentbspr))
                        f.write('Block('+str(placepos[0])+','+str(placepos[1])+',b1spr).')
                    to_remove = []

            if not key[K_LSHIFT] or key[K_RSHIFT]:    
                if e.type==MOUSEBUTTONUP:
                    if e.button==1:
                        to_remove = [i for i in instances if i.rect.collidepoint(placepos)]
                        for i in to_remove:
                            instances.remove(i)
                        if not to_remove:
                            instances.append(Block(placepos[0],placepos[1],currentbspr))
                            f.write('Block('+str(placepos[0])+','+str(placepos[1])+',b1spr).')

            if key[K_RSHIFT]:
                if pygame.mouse.get_pressed()==(1,0,0):
                    to_remove = [i for i in instances if i.rect.collidepoint(placepos)]
                    for i in to_remove:
                                instances.remove(i)
                    to_remove=[]

    for i in instances:
        screen.blit(i.sprite,i.rect)
    if not key[K_q]:
        screen.blit(curspr,placepos)

    screen.blit(menuspr,menurect)

    for item in menuitems:
        screen.blit(item.sprite,item.pos)
        if item.rect.collidepoint(mse):
            if pygame.mouse.get_pressed()==(1,0,0):
                currentbspr=item.sprite
            pygame.draw.rect(screen, ((255,0,0)), item, 1)
    pygame.display.flip()
