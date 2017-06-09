# -*- coding: utf-8 -*-
import pygame,sys
from pygame.locals import *
blue=0,0,200
black=0,0,0
color=((0,0,0),(255,255,255))
pygame.init()
pygame.mixer.init()

audio=pygame.mixer.Sound('Timetravel.ogg')
channel=pygame.mixer.find_channel(True)
channel.play(audio)

screen=pygame.display.set_mode((1024,768))
myfont=pygame.font.Font(None,60)
image=myfont.render('victory',True,blue)


for event in pygame.event.get():
    if event.type in (QUIT,KEYDOWN):
        sys.exit()
screen.fill((202, 130, 22))
width=2
for i in range(1,18):
    pygame.draw.line(screen,black,(150+35*i,50),(150+35*i,680),width)
for i in range(1,18):
    pygame.draw.line(screen,black,(150,50+35*i),(780,50+35*i),width)
pygame.draw.line(screen, black, (150 , 50), (150 , 680), 4)
pygame.draw.line(screen, black, (780 , 50), (780 , 680), 4)
pygame.draw.line(screen, black, (150 , 50), (780 , 50), 4)
pygame.draw.line(screen, black, (150 , 680),(780 , 680), 4)
for x in (3,9,15):
    for y in (3,9,15):
        pygame.draw.circle(screen,black,(151+35*x,51+35*y),7,0)

i=0
lianxu=0
chess=[0 ,0,0,0,0,0,0,0,0,0,0,0]
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            x,y=event.pos
            px=x+17-((x-133)%35)
            py=y+17-((y-33)%35)
            pygame.draw.circle(screen, color[(i%2)], (px, py), 15, 0)
            i = i + 1
    pygame.display.update()
