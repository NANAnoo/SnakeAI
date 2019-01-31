import pygame
#from Snake import*
from pygame.locals import *

class Show():
	"""docstring for Show"""
	def __init__(self,w,h,l):
		self.BLOCK_WIDTH = l
		self.GRID_WIDTH = w
		self.GRID_HEIGHT = h
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode([self.GRID_WIDTH*(self.BLOCK_WIDTH+2),self.GRID_HEIGHT*(self.BLOCK_WIDTH+2)])
		screentitle = pygame.display.set_caption("snake")

	def addPlayer(self,player):
		self.player = player


	def demo(self,brains,fps):
		index = 0
		size = len(brains)
		while True:
			self.screen.fill([0,0,0])
			if(self.player.dead):
				print(self.player.food_count)
				self.player.reburn()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit(0)
				if event.type == KEYDOWN:
					if event.key == pygame.K_UP:
						index -=1
						if index < 0:
							index = size -1
						self.player.load_from(brains[index])
						print(brains[index])
						self.player.reburn()
					if event.key == pygame.K_DOWN:
						index +=1
						if index >=size:
							index = 0
						self.player.load_from(brains[index])
						print(brains[index])
						self.player.reburn()
			if fps>0:
				ime_pass = self.clock.tick(fps)
			self.player.auto_play()
			self.player.MOVE()
			f = [self.player.food[0]* (self.BLOCK_WIDTH + 2)+1,self.player.food[1]* (self.BLOCK_WIDTH + 2)+1]
			h = [self.player.head[0]* (self.BLOCK_WIDTH + 2)+1,self.player.head[1]* (self.BLOCK_WIDTH + 2)+1]
			pygame.draw.rect(self.screen, [0,255,0], [f,[self.BLOCK_WIDTH,self.BLOCK_WIDTH]], 0)
			pygame.draw.rect(self.screen, [255,0,0], [h ,[self.BLOCK_WIDTH,self.BLOCK_WIDTH]], 0)

			for point in self.player.body:
				p = [point[0]* (self.BLOCK_WIDTH  + 2)+1,point[1]* (self.BLOCK_WIDTH  + 2)+1]
				pygame.draw.rect(self.screen, [255,255,255], [p,[self.BLOCK_WIDTH,self.BLOCK_WIDTH]], 0)
			pygame.display.update()

	def Run(self,auto):
		stop = False
		cont = False
		while not cont:
			self.screen.fill([0,0,0])
			if(self.player.dead and not stop):
				self.player.reburn()
			if auto:
				ime_pass = self.clock.tick(50)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit(0)
					if event.type == KEYDOWN:
						if event.key == pygame.K_DOWN:
			 				stop = True
			 				cont = True

				self.player.auto_play()
			else:
				ime_pass = self.clock.tick(15)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit(0)
					if event.type == KEYDOWN:
			 			if event.key == pygame.K_UP:
			 				self.player.move_up()
			 			if event.key == pygame.K_DOWN:
			 				self.player.move_down()
			 			if event.key == pygame.K_LEFT:
			 				self.player.move_left()
			 			if event.key == pygame.K_RIGHT:
			 				self.player.move_right()
			#print(self.player.See())
			self.player.MOVE()
			f = [self.player.food[0]* (self.BLOCK_WIDTH + 2)+1,self.player.food[1]* (self.BLOCK_WIDTH + 2)+1]
			h = [self.player.head[0]* (self.BLOCK_WIDTH + 2)+1,self.player.head[1]* (self.BLOCK_WIDTH + 2)+1]
			pygame.draw.rect(self.screen, [0,255,0], [f,[self.BLOCK_WIDTH,self.BLOCK_WIDTH]], 0)
			pygame.draw.rect(self.screen, [255,0,0], [h ,[self.BLOCK_WIDTH,self.BLOCK_WIDTH]], 0)

			for point in self.player.body:
				p = [point[0]* (self.BLOCK_WIDTH + 2)+1,point[1]* (self.BLOCK_WIDTH + 2)+1]
				pygame.draw.rect(self.screen, [255,255,255], [p,[self.BLOCK_WIDTH,self.BLOCK_WIDTH]], 0)
			pygame.display.update()
