import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
    # screen.lock()    #很快你就会知道这两句lock和unlock的意思了

    rand_pos = pygame.mouse.get_pos()
    screen.set_at(rand_pos, rand_col)
    # screen.unlock()
    pygame.display.set_caption('pos {}'.format(rand_pos))

    pygame.display.update()