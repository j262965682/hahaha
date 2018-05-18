background_image = r'Koala.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen_size_my = (1024,768)
screen = pygame.display.set_mode(screen_size_my,0,32)
background = pygame.image.load(background_image).convert()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen

                if Fullscreen:
                    screen = pygame.display.set_mode(screen_size_my,HWSURFACE|DOUBLEBUF|FULLSCREEN,32)
                    pygame.display.flip()
                else:
                    screen = pygame.display.set_mode(screen_size_my,0,32)

        screen.blit(background,(0,0))
        pygame.display.update()