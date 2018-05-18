import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1080,980),0,32)

pygame.display.set_caption('hello,world!')

background_image_filename = r'Koala.jpg'
mouse_image_filename = r'Desert.jpg'

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))

    x,y = pygame.mouse.get_pos() #获取鼠标位置

    x = x - mouse_cursor.get_width()/2
    y = y - mouse_cursor.get_width()/2
    #计算光标在左上角位置
    screen.blit(mouse_cursor,(x,y))

    pygame.display.update()
'''
初始化 - （图像、声音）
主循环 -
    事件处理（鼠标、键盘）
    逻辑层
    渲染层
释放资源
'''