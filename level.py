"""
Level:
- Contains the class for the level, which uses the tilemap level to place the blocks in an easier way than hardcoding them. 
"""

import pygame
from pygame.locals import *
from sprites import *
coins = 0

class Level():
    def __init__(self):
        self.mode = 0
        self.level = [] #Storage for characters read from file
        self.tilemap = open("data/level","r")
        self.world = [] # Stores all sprites in the game. Forgot what I was going to use this for. Don't think it's necessary.
        self.enemies = pygame.sprite.Group()
        self.collidable = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.game_over = False
        self.game_won = False
        self.qblock = pygame.sprite.Group() #Stores question mark blocks
        self.font = pygame.font.Font("data/font.ttf",24)
        self.coins = 0
        # self.marios = pygame.sprite.Group()
    def addCoin(self):
        self.coins += 1
    def create(self,x,y):
        for tile in self.tilemap:
            self.level.append(tile)
        for row in self.level:
            for col in row:
                if col == "B":
                    brick = Brick(x,y)
                    self.world.append(brick)
                    self.collidable.add(brick)
                if col == "P":
                    platform = Platform(x,y)
                    self.world.append(platform)
                    self.collidable.add(platform)
                if col == "I":
                    pipe = Pipe(x,y)
                    self.world.append(pipe)
                    self.collidable.add(pipe)
                if col == "G":
                    goomba = Goomba(x,y)
                    self.world.append(goomba)
                    self.enemies.add(goomba)
                if col == "M":
                    mario = Mario(x,y)
                    self.mario = mario
                    # self.marios.add(mario)
                    print(mario.getX(), mario.getY())
                if col == "Q":
                    qblock = CoinQBlock(x,y)
                    self.qblock.add(qblock)
                    self.collidable.add(qblock)
                if col == "F":
                    flag = Flagpole(x,y)
                    self.collidable.add(flag)
                if col == "W":
                    flower = Flower(x,y)
                    self.powerups.add(flower)
                if col == "C":
                    iceflower = Iceflower(x,y)
                    self.powerups.add(iceflower)

                if col == "Z":
                    bowser = Bowser(x,y)
                    self.world.append(bowser)
                    self.enemies.add(bowser)
                if col == "K":
                    koopa = Koopa(x,y)
                    self.world.append(koopa)
                    self.enemies.add(koopa)
                if col == "J":
                    flyingkoopa = Flyingkoopa(x,y)
                    self.world.append(flyingkoopa)
                    self.enemies.add(flyingkoopa)
                if col == "X":
                    iceblock = Iceblock(x,y)
                    self.world.append(iceblock)
                    self.collidable.add(iceblock)

                x += 16
            y += 16
            x = 0
    def update(self,surface):
        if self.mode == 0:
            surface.fill((255,255,255))
            image = pygame.image.load('data/startscreen.jpg').convert_alpha()
            surface.blit(image, (0,0))
        else:
            if self.game_over:
                surface.fill((0,0,0))
                if self.game_won == True:
                    text = self.font.render("LEVEL CLEAR",1,(255,255,255))
                elif self.game_won == False:
                    text = self.font.render("GAME OVER",1,(255,255,255))
                surface.blit(text, (200,200))
            # elif self.game_over and self.game_won==False:
            #     surface.fill((0,0,0))
            #     text = self.font.render("GAME OVER",1,(255,255,255))
            #     surface.blit(text, (200,240))
            
            else:
                # self.mario.scroll()
                # surface.blit(self.mario.image,self.mario.rect)
                # for mario in self.marios:
                #     mario.scroll()
                #     surface.blit(self.mario.image,self.mario.rect)
                coinstxt = self.font.render("COINS x " + str(self.mario.coins),1,(255,255,255))
                surface.blit(coinstxt, (10,10)) 
                for powerup in self.powerups:
                    powerup.scroll()
                    powerup.update()
                    surface.blit(powerup.image,powerup.rect.topleft)     
                for enemy in self.enemies:
                    enemy.update()
                    surface.blit(enemy.image,enemy.rect.topleft)
                    if enemy.dead and enemy.squish_frame == 5: #Squish_frame is so that the goomba's squished image lasts for a bit longer duration, then it removes the Goomba
                        self.enemies.remove(enemy)
                        if self.mario.ice: # adds in ice block after removing enemy hit by ice ball
                            iceblock = Iceblock(enemy.x-enemy.scrollX,enemy.y)
                            self.world.append(iceblock)
                            self.collidable.add(iceblock)
                    enemy.scroll()
                for s in self.collidable:
                    s.scroll()
                    surface.blit(s.image,s.rect.topleft)
                surface.blit(self.mario.image,self.mario.rect)   
                for q in self.qblock:
                    surface.blit(q.image,q.rect)
                for projectile in self.projectiles:

                    projectile.collide(self.enemies,self.projectiles)
                    projectile.update()
                    if projectile.dead:
                        self.projectiles.remove(projectile)
                    surface.blit(projectile.image,projectile.rect)


