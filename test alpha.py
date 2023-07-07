import pygame as pg


pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255, 50)  # This color contains an extra integer. It's the alpha value.
PURPLE = (255, 0, 255)

screen = pg.display.set_mode((200, 325))
screen.fill(WHITE)  # Make the background white. Remember that the screen is a Surface!
clock = pg.time.Clock()

size = (50, 50)
red_image = pg.Surface(size)
green_image = pg.Surface(size)
blue_image = pg.Surface(size, pg.SRCALPHA)  # Contains a flag telling pg that the Surface is per-pixel alpha
purple_image = pg.Surface(size)

red_image.set_colorkey(BLACK)
green_image.set_alpha(50)
# For the 'blue_image' it's the alpha value of the color that's been drawn to each pixel that determines transparency.
purple_image.set_colorkey(BLACK)
purple_image.set_alpha(50)

pg.draw.rect(red_image, RED, red_image.get_rect(), 10)
pg.draw.rect(green_image, GREEN, green_image.get_rect(), 10)
pg.draw.rect(blue_image, BLUE, blue_image.get_rect(), 10)
pg.draw.rect(purple_image, PURPLE, purple_image.get_rect(), 10)

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                screen.blit(red_image, (75, 25))
            elif event.key == pg.K_2:
                screen.blit(green_image, (75, 100))
            elif event.key == pg.K_3:
                screen.blit(blue_image, (75, 175))
            elif event.key == pg.K_4:
                screen.blit(purple_image, (75, 250))

    pg.display.update()
