"""
Sprites:
- Contains all sprites for the game
- Collidables: Brick, Platform, Flagpole, Iceblock, Pipe, Q-Block
- Enemies: Goomba, Koopa, Flying Koopa, Bowser
- Mario
"""

import pygame
from pygame.locals import *
import level
import random

class Brick(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.image = pygame.image.load("data/brick1.png").convert_alpha()
		self.x = x
		self.y = y
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.name = "brick"
		self.scrollX = 1
	def scroll(self):
		self.x -= self.scrollX
		self.rect.topleft = [self.x,self.y]

class Flagpole(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.image = pygame.image.load("data/flagpole.png").convert_alpha()
		self.x = x
		self.y = y
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.name = "flagpole"
		self.scrollX = 1
	def scroll(self):
		self.x -= self.scrollX
		self.rect.topleft = [self.x,self.y]
	def collide(self):
		pass

class Platform(Brick):
	def __init__(self,x,y):
		super().__init__(x, y)
		self.image = pygame.image.load("data/platform-top.png").convert_alpha()
		pygame.sprite.Sprite.__init__(self)
		self.name = "platform"

class Iceblock(Brick):
	def __init__(self,x,y):
		super().__init__(x, y)
		self.image = pygame.image.load("data/iceblock.png").convert_alpha()
		pygame.sprite.Sprite.__init__(self)
		self.name = "iceblock"

class Pipe(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.image = pygame.image.load("data/pipe_green.png").convert_alpha()
		self.x = x
		self.y = y
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.name = "pipe"
		self.scrollX = 1
	def scroll(self):
		self.x -= self.scrollX
		self.rect.topleft = [self.x,self.y]

class Bowser(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.max_x = x + 10
		self.min_x = x - 10
		self.max_y = y 
		self.min_y = y - 70
		self.x = x
		self.y = y
		self.left = False
		self.up = False # Direction the goomba is moving
		self.image = pygame.image.load("data/bowser.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = [x,y]
		self.rect.w -= 2
		self.rect.h -= 2
		pygame.sprite.Sprite.__init__(self)
		self.frame = 0
		self.squish_frame = 0
		self.dead = False
		self.scrollX = 1
	def scroll(self):
		self.min_x -= self.scrollX
		self.max_x -= self.scrollX
	def update(self):
		self.x -= self.scrollX
		if self.dead:
			self.image = pygame.image.load("data/empty.png").convert_alpha()
		else:
			self.frame += 1
			if self.frame > 9:
				self.frame = 0
			if self.up:
				self.rect.y -= 4
				if self.rect.y < self.min_y:
					self.rect.y = self.min_y
					self.up = False
			else:
				self.rect.y += 4
				if self.rect.y > self.max_y:
					self.rect.y = self.max_y
					self.up = True
			self.frame += 1
			if self.frame > 9:
				self.frame = 0
			if self.left:
				self.rect.x -= 4
				if self.rect.x < self.min_x:
					self.rect.x = self.min_x
					self.left = False
			else:
				self.rect.x += 4
				if self.rect.x > self.max_x:
					self.rect.x = self.max_x
					self.left = True

class Goomba(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.max_x = x + 60# min max vals for gommba
		self.min_x = x - 60
		self.x = x
		self.y = y
		self.left = False # Direction the goomba is moving
		self.image = pygame.image.load("data/goomba1.png").convert_alpha()
		self.animate = ['data/goomba1.png','data/goomba2.png']
		self.rect = self.image.get_rect()
		self.rect.topleft = [x,y]
		self.rect.w -= 2
		self.rect.h -= 2
		pygame.sprite.Sprite.__init__(self)
		self.frame = 0
		self.squish_frame = 0
		self.dead = False
		self.scrollX = 1
	def scroll(self):
		self.min_x -= self.scrollX
		self.max_x -= self.scrollX
	def update(self):
		self.x -= self.scrollX
		if self.dead:
			self.image = pygame.image.load('data/goomba3.png').convert_alpha()
			self.rect.y = self.rect.y - 8 
			self.squish_frame += 1
		else:
			self.frame += 1
			if self.frame > 9:
				self.frame = 0
			if self.left:
				self.rect.x -= 5
				self.x -= 4 # updates freeze location
				if self.rect.x < self.min_x:
					self.rect.x = self.min_x
					self.left = False
			else:
				self.rect.x += 3
				self.x += 4 # updates freeze location
				if self.rect.x > self.max_x:
					self.rect.x = self.max_x
					self.left = True
			self.image = pygame.image.load(self.animate[self.frame//5]).convert_alpha()

class Koopa(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super()
		self.max_x = x + 70
		self.min_x = x - 70
		self.x = x
		self.y = y
		self.image = pygame.image.load("data/koopa.png").convert_alpha()
		self.left = False # Direction the goomba is moving
		# self.image = pygame.image.load("data/goomba1.png").convert_alpha()
		# self.animate = []
		self.rect = self.image.get_rect()
		self.rect.topleft = [x,y]
		self.rect.w -= 2
		self.rect.h -= 2
		pygame.sprite.Sprite.__init__(self)
		self.frame = 0
		self.squish_frame = 0
		self.dead = False
		self.scrollX = 1
	def scroll(self):
		self.min_x -= self.scrollX
		self.max_x -= self.scrollX
		# self.animate = ['data/koopa.png','data/koopa1.png']
	def update(self):
		self.x -= self.scrollX
		if self.dead:
			self.image = pygame.image.load('data/shell.png').convert_alpha()
			# self.rect.y = self.rect.y - 8 
			self.squish_frame += 1
			self.rect.x += 5
		else:
			self.frame += 1
			if self.frame > 9:
				self.frame = 0
			if self.left:
				self.image = pygame.image.load('data/koopa.png')
				self.rect.x -= 2
				self.x -= 1 # updates freeze location
				if self.rect.x < self.min_x:
					self.rect.x = self.min_x
					self.left = False
			else:
				self.image = pygame.image.load('data/koopa1.png')
				self.rect.x += 0
				self.x += 1 #updates freeze location
				if self.rect.x > self.max_x:
					self.rect.x = self.max_x
					self.left = True
			# self.image = pygame.image.load(self.animate[self.frame//5]).convert_alpha()
class Flyingkoopa(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.max_x = x
		self.min_x = x
		self.max_y = y 
		self.min_y = y - 110
		self.x = x
		self.y = y
		self.left = False
		self.up = False # Direction the goomba is moving
		self.image = pygame.image.load("data/flyingkoopa.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = [x,y]
		self.rect.w -= 2
		self.rect.h -= 2
		pygame.sprite.Sprite.__init__(self)
		self.frame = 0
		self.squish_frame = 0
		self.dead = False
		self.scrollX = 1
	def scroll(self):
		self.min_x -= self.scrollX
		self.max_x -= self.scrollX
	def update(self):
		self.x -= self.scrollX
		if self.dead:
			self.image = pygame.image.load("data/empty.png").convert_alpha()
		else:
			self.frame += 1
			if self.frame > 9:
				self.frame = 0
			if self.up:
				self.rect.y -= 2
				self.y -= 2
				if self.rect.y < self.min_y:
					self.rect.y = self.min_y
					self.up = False
			else:
				self.rect.y += 2
				self.y += 2
				if self.rect.y > self.max_y:
					self.rect.y = self.max_y
					self.up = True
			self.frame += 1
			if self.frame > 9:
				self.frame = 0
			if self.left:
				self.rect.x -= 4
				self.x -= 4
				if self.rect.x < self.min_x:
					self.rect.x = self.min_x
					self.left = False
			else:
				self.rect.x += 4
				self.x += 4
				if self.rect.x > self.max_x:
					self.rect.x = self.max_x
					self.left = True



class CoinQBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.dy = 0
		self.image = pygame.image.load("data/platform-q.png").convert_alpha()
		self.animate = ["data/platform-q.png","data/platform-q1.png",
						"data/platform-q2.png","data/platform-q3.png"]
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.frame = 0
		self.hit = False
		self.name = "qblock"
		self.up = False 
		self.scrollX = 1
	def scroll(self):
		self.x -= self.scrollX
		self.rect.topleft = [self.x,self.y]
	def update(self,mario):
		if not self.hit:
			self.frame += 1
			if self.frame >= 16:
				self.frame = 0
			self.image = pygame.image.load(self.animate[self.frame//4]).convert_alpha()
		else:
			self.collide()
	def collide(self):
			if self.dy < -1:
				self.up = False
			self.rect.y += self.dy
			if self.rect.y >= self.y:
				self.rect.y = self.y
			self.image = pygame.image.load("data/platform-air.png").convert_alpha()

class Flower(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.image = pygame.image.load("data/flower.png").convert_alpha()
		self.x = x
		self.y = y
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.name = "flower"
		self.scrollX = 1
		self.collected = False
		self.collided = False
	def scroll(self):
		self.x -= self.scrollX
		self.rect.topleft = [self.x,self.y]
	def update(self):
		if self.collected:
			self.image = pygame.image.load('data/empty.png')

class Fireball(pygame.sprite.Sprite):
	def __init__(self,x,y,direction):
		self.image = pygame.image.load("data/fireball.png").convert_alpha()
		self.x = x
		self.y = y
		self.direction = direction
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.name = "fireball"
		self.dead = False
		self.scrollX = 1
	def update(self):
		self.x -= self.scrollX
		self.x += self.direction
		self.rect.topleft = [self.x,self.y]

	def collide(self,enemies,projectiles):
		for e in enemies:
			for p in projectiles:
				if not e.dead: # enemies aren't deleted until a few frames later
					if self.rect.colliderect(e):
					
						e.dead = True
						p.dead = True
					# 	self.dy = -6
					if p.x > 640:
						p.dead = True

class Iceflower(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.image = pygame.image.load("data/iceflower.png").convert_alpha()
		self.x = x
		self.y = y
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.name = "iceflower"
		self.scrollX = 1
		self.collected = False
		self.collided = False
	def scroll(self):
		self.x -= self.scrollX
		self.rect.topleft = [self.x,self.y]
	def update(self):
		if self.collected:
			self.image = pygame.image.load('data/empty.png')

class Iceball(pygame.sprite.Sprite):
	def __init__(self,x,y,direction):
		self.image = pygame.image.load("data/iceball.png").convert_alpha()
		self.x = x
		self.y = y
		self.direction = direction
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.name = "iceball"
		self.dead = False
		self.scrollX = 1
	def update(self):
		self.x -= self.scrollX
		self.x += self.direction
		self.rect.topleft = [self.x,self.y]

	def collide(self,enemies,projectiles):
		for e in enemies:
			for p in projectiles:
				if not e.dead: # enemies aren't deleted until a few frames later
					if self.rect.colliderect(e):
					
						e.dead = True
						p.dead = True
						# iceblock = Iceblock(e.x,e.y)
						# level.collidable.add(iceblock)
						
					if p.x > 640:
						p.dead = True
class Mario(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.dx = 0 # Distance moving X-axis
		self.dy = 0 # Distance moving Y-Axis
		self.x = x
		self.y = y
		self.image = pygame.image.load("data/mario1.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.rect.w -= 2 # Hitbox needs to be smaller or collison acts weird
		self.rect.h -= 2
		self.left_images = ["data/mario1-left.png","data/mario2-left.png",
							"data/mario3-left.png","data/mario4-left.png"]
		self.right_images = ["data/mario1.png","data/mario2.png",
							 "data/mario3.png", "data/mario4.png"]
		self.frame = 0
		self.on_ground = True
		self.jumping = False
		self.velocity = .8
		self.jump_speed = -8
		self.gravity = .5
		self.face = "right"
		self.dead = False
		self.won = False
		self.coins = 0
		self.jump_sound = pygame.mixer.Sound('data/sound/jump.ogg')
		self.collide_sound = pygame.mixer.Sound('data/sound/jump2.ogg')
		self.stomp_sound = pygame.mixer.Sound('data/sound/stomp.ogg')
		self.play_jump = False
		self.collided = False
		self.scrollX = 1

		# powerups
		self.fire = False
		self.ice = False

	def getX(self):
		return self.x
	def getY(self):
		return self.y
	# def scroll(self):
	#     self.dx -= self.scrollX
	#     self.rect.topleft = [self.x,self.y]
	def update(self,screen,left,right,up,sprites,enemies,powerups):
		# print(int(self.dx), int(self.dy))
		self.x -= self.scrollX
		# self.x += self.dx
		self.rect.topleft = [self.x,self.y]
		self.y += self.dy
		if self.rect.top >= screen.get_height()+30: #If you fall of bottom edge, Mario dies
			self.dead = True
			self.dy = -8
			return
		if right:
			print("right")
			self.rect.topleft = [self.x,self.y]
			self.dx += self.velocity
			if self.dx > 4:
				self.dx = 4
			self.face = "right"
			self.frame += 1
			self.rect.x += self.dx
			self.x += self.dx
			# self.y += self.dy
			# self.y += self.dy # scroll
			if self.frame == 16:
				self.frame = 0
			if not self.on_ground:
				self.image = pygame.image.load("data/mario5.png").convert_alpha()
			else:
				self.image = pygame.image.load(self.right_images[self.frame//4]).convert_alpha()
			self.collide(sprites,enemies,powerups)
		if left:
			self.rect.topleft = [self.x,self.y]
			print("Left")
			self.dx -= self.velocity
			if self.dx < -6:
				self.dx = -6
			self.face = "left"
			self.frame += 1
			self.rect.x += self.dx
			self.x += self.dx
			# self.y += self.dy # scroll
			if self.frame == 16:
				self.frame = 0
			if not self.on_ground:
				self.image = pygame.image.load("data/mario5-left.png").convert_alpha()
			else:
				self.image = pygame.image.load(self.left_images[self.frame//4]).convert_alpha()
			self.collide(sprites,enemies,powerups)
		if up:
			self.rect.topleft = [self.x,self.y]
			print("Up")
			if self.play_jump:
				self.jump_sound.stop()
				self.jump_sound.play()
				self.play_jump = False
			if self.face == "left" and not self.on_ground:
				self.image = pygame.image.load("data/mario5-left.png").convert_alpha()
			elif self.face == "right" and not self.on_ground:
				self.image = pygame.image.load("data/mario5.png").convert_alpha()
			self.rect.y += self.dy
			# self.y += self.dy
			self.dy += self.gravity
			# self.y += self.dy # scroll
			# self.x += self.dx
			# self.y += self.dy # scroll
			if self.dy >= 16:
				self.dy = 0
				self.jumping = False
				
			self.collide(sprites,enemies,powerups)


		if not (left or right):
			self.rect.topleft = [self.x,self.y]
			# print("not left or right")
			self.dx = 0
			# self.y += self.dy # scroll
			self.frame = 0
		if not self.jumping: # Always falling unless Mario jumps or collides with something under him
			self.rect.topleft = [self.x,self.y]
			# print("not self.jumping")
			self.dy += self.gravity
			# self.y += self.dy # scroll
			self.rect.y += self.dy
			self.collide(sprites,enemies,powerups)
		if self.rect.left < 0: #Prevents going off screen to the left
			self.rect.left = 0
		if self.rect.right > screen.get_width(): #Prevent going off screen to the right
			self.rect.right = screen.get_width()

	def death(self): # Death animation calculations
		self.rect.y += self.dy
		self.dy += self.gravity/1.5

	def collide(self,sprites,enemies,powerups):

		# Environment collision
		for s in sprites:
			if self.rect.colliderect(s):
				# print(s.name)
				if s.name == "flagpole":
					# level.mario.dead = True
					print("Reached flag pole!")
					level.game_won = True
					print(level.game_won)
					self.won = True
				if s.name == "flower":
					print("Collected Flower!!")
				if s.rect.collidepoint(self.rect.bottomright) and not s.rect.collidepoint(self.rect.bottomleft) and self.dx > 0 and not self.on_ground:
					self.rect.right = s.rect.left
					self.dx = -self.dx
				elif s.rect.collidepoint(self.rect.bottomleft) and not s.rect.collidepoint(self.rect.bottomright) and self.dx < 0 and not self.on_ground:
					self.rect.left = s.rect.right
					self.dx = -self.dx
				elif s.rect.collidepoint(self.rect.topright) and not s.rect.collidepoint(self.rect.topleft) and self.dx > 0:
					self.rect.right = s.rect.left
					self.dx = -self.dx
				elif s.rect.collidepoint(self.rect.topleft) and not s.rect.collidepoint(self.rect.topright)  and self.dx < 0:
					self.rect.left = s.rect.right
					self.dx = -self.dx
				elif self.dy < 0:
					self.play_jump = False
					self.jump_sound.stop()
					self.collide_sound.play()
					self.rect.top = s.rect.bottom
					self.dy = 0
					self.rect.topleft = [self.x,self.y]
					if s.name == "qblock":
						s.hit = True
						s.frame = 0
						self.coins += 1
						self.rect.topleft = [self.x,self.y]

				elif self.dy > 0:
					self.on_ground = True
					self.rect.bottom = s.rect.top
					self.dy = 0
					# self.y += self.dy # scroll
					if self.face == "left":
						self.image = pygame.image.load("data/mario1-left.png").convert_alpha()
					elif self.face == "right":
						self.image = pygame.image.load("data/mario1.png").convert_alpha()

				self.collided = True

		# Enemy collision
		for e in enemies:
			if not e.dead: # enemies aren't deleted until a few frames later
				if self.rect.colliderect(e):
					if e.rect.collidepoint(self.rect.bottomright) and e.rect.collidepoint(self.rect.midbottom):
						self.jump_sound.stop()
						self.stomp_sound.play()
						e.dead = True
						self.dy = -2
					elif e.rect.collidepoint(self.rect.bottomleft) and e.rect.collidepoint(self.rect.midbottom):
						self.jump_sound.stop()
						self.stomp_sound.play()
						e.dead = True
						self.dy = -2
					else:
						self.dead = True
						self.dy = -6

		# Powerups collision
		for p in powerups:
			if not p.collected:
				if self.rect.colliderect(p):
					print("Collected Flower!")
					p.collected = True
					if p.name == "flower": # powerups mario
						self.fire = True
						self.ice = False
					elif p.name == "iceflower":
						self.ice = True
						self.fire = False

