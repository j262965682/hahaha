import pygame
from pygame.locals import *
from sys import exit

my_name = 'will McGuang'
background_image =  r'Koala.jpg'
screen_size_my = (1024,768)

pygame.init()
screen = pygame.display.set_mode(screen_size_my,0,32)

my_font = pygame.font.SysFont('arial',64)
text_surface = my_font.render(my_name,True,(0,0,255))

x = 1024
y = 480/2

back_ground = pygame.image.load(background_image).convert()

while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            exit()

        screen.blit(back_ground,(0,0))

    x -= 0.005
    if x <= 0 :
         x = 1024
        #    x = 640 - text_surface.get_width()

    screen.blit(text_surface,(x,y))

    pygame.display.update()
