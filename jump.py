# -*- coding: utf-8 -*-
import os
import time
import pygame
from pygame.locals import *

def jump(distance):
    press_time = distance * 2.86
    press_time = int(press_time)
    cmd = 'adb shell input swipe 320 410 320 410 ' + str(press_time)
    print(cmd)
    os.system(cmd)

def get_pic():
    os.system('adb exec-out screencap -p > 1.png')
    img = pygame.image.load('1.png')
    img = pygame.transform.scale(img, (540, 960))
    return img

def compute_dis(pos):
    x=pos[0][0]-pos[1][0]
    y=pos[0][1]-pos[1][1]
    print(x,y)
    return ((x**2+y**2)**0.5)
    

pygame.init()
screen=pygame.display.set_mode((600,1000))
count = 0
pos=[0,0]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type==MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = event.pos
                pos[count]=[x,y]
                count+=1
                count = count%2
            else :
                dis=compute_dis(pos)
                jump(dis)
                #time.sleep(dis*1.4)
    img=get_pic()
    screen.blit(img,(0,0)) 
    pygame.display.update()