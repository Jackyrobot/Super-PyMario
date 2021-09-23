"""
Main File
- Has most of the "Controller" elements in this file
- Contains main pygame loop
- Controls for mario
"""

import pygame, sys
from pygame.locals import *
from level import Level
from sprites import *
clock = pygame.time.Clock()
pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE)
bg = pygame.image.load("data/background-2.png")
bg_rect = bg.get_rect()
level = Level()
level.create(0 ,10)
pygame.mouse.set_visible(0)
up=left=right=False

started = False

while True:
    if level.mario.won:
        print("WON")
        level.game_won = True
        level.mario.dead = True
    if level.mario.dead: 
        level.mario.death()
        if level.mario.rect.y > screen.get_height():
            level.game_over = True
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    else:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                level.mode = 1 # starts game 
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
                level.mario.dx = level.mario.velocity
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
                level.mario.dx = -level.mario.velocity
            if event.type == KEYDOWN and event.key == K_UP:
                if level.mario.on_ground:
                    up = True
                    level.mario.jumping = True
                    level.mario.dy = level.mario.jump_speed 
                    level.mario.on_ground = False
                    level.mario.play_jump = True
            if event.type == KEYDOWN and event.key == K_SPACE:
                if level.mario.fire == True:
                    print("Fireball!")
                    level.mario.ice == False
                    print(int(level.mario.getX()),int(level.mario.getY()))
                    if level.mario.face == "right":
                        fireball = Fireball(level.mario.getX(),level.mario.getY(),10)
                        level.projectiles.add(fireball)
                    else:
                        fireball = Fireball(level.mario.getX(),level.mario.getY(),-10)
                        level.projectiles.add(fireball)
                elif level.mario.ice == True:
                    print("Iceball!")
                    level.mario.fire = False
                    if level.mario.face == "right":
                        iceball = Iceball(level.mario.getX(),level.mario.getY(),10)
                        level.projectiles.add(iceball)
                    else:
                        iceball = Iceball(level.mario.getX(),level.mario.getY(),-10)
                        level.projectiles.add(iceball)


            if event.type == KEYUP and event.key == K_RIGHT:
                level.mario.image = pygame.image.load("data/mario1.png")
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                level.mario.image = pygame.image.load("data/mario1-left.png")
                left = False
            if event.type == KEYUP and event.key == K_UP:
                # if level.mario.on_ground:
                #     level.mario.jump_speed = -8
                level.mario.jumping = False
                up = False
        if level.mode != 0:
            level.mario.update(screen,left,right,up,level.collidable,level.enemies,level.powerups)
            level.qblock.update(level.mario)
    for x in range(0,screen.get_width(),bg_rect.w):
        for y in range(0,screen.get_height(),bg_rect.h):
            screen.blit(bg,(x,y))
    level.update(screen)
    pygame.display.flip()
    clock.tick(30)
