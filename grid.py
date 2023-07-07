import pygame as pg



def grid(sel):
    bg1 = pg.Surface((1400, 900))
    bg4 = pg.Surface((1400, 900))
    sizex = 1400
    sizey = 900
    sel = sel
    rect = bg4.get_rect()
    rect2 = bg1.get_rect()
    if sel == 1:
        color=(100,0,0,0)
    elif sel== 2:
        color=(85,107,47,0)
        
    elif sel == 3:
        color = (99,99,99,0)
    elif sel == 4:   
        color = (10,20,30,0)
    elif sel == 5:   
        bg1.blit(bg4, rect)
    else:
        color = (3,3,3,0)

    for i in range(sizex):
        pg.draw.line(bg4, (color), (i * 20, 0), (i * 20, sizey), 1)

    for j in range(sizey):
        pg.draw.line(bg4, (color), (0, j * 20), (sizex, j * 20), 1)
        bg1.blit(bg4, rect)


