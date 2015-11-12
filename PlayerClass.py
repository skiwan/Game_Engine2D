import pygame
import Character
import BrainStateMachine
import AnimationHandler
import pygame
import AnimationDataClass
import InputHandler


class Player(Character.Character):
	""" This Will create a Player"""
	def __init__(self):
		#stats of the character
		self.movementSpeed = 5

		#variables that are not stats
		self.spriteSheet = pygame.image.load("charspritesheet.png") 
		self.x = 40#starting positions
		self.y = 40
		self.width = 40#size
		self.height = 40
		self.animation = 0
		self.characterAnimationHandler = AnimationHandler.AnimationHandler(self.animation,self.width,self.height,self.spriteSheet)#animation handler
		self.brain = BrainStateMachine.BrainStateMachine()#the brain of our Player
		self.PlayerInputHandler = InputHandler.Input_Handler()
		self.PlayerInput = self.PlayerInputHandler.returnEvents()

		#animations of this Character
		self.IdleAnimation = AnimationDataClass.animation(0,40,40,3,2)
		self.MoveLeftAnimation = AnimationDataClass.animation(1,40,40,4,3)
		self.MoveRightAnimation = AnimationDataClass.animation(2,40,40,4,3)
		self.MoveUpAnimation = AnimationDataClass.animation(3,40,40,4,3)
		self.MoveDownAnimation = AnimationDataClass.animation(4,40,40,4,3)
		#States of the chracter
		self.nonState = IdleState()
		self.moveState = MoveState()

		#set brain and animation 
		self.characterAnimationHandler.changeAnimation(self.IdleAnimation)#set the current animation
		self.brain.Change(self.nonState)


		self.characterAnimationHandler.Update()#called to get the first image needed		
		self.characterImage=self.characterAnimationHandler.ImageReturn()

	def set_y(self,wert):
		self.y += wert

	def set_x(self,wert):
		self.x += wert

	def Render(self,destinationScreen,camera):
		self.characterImage = self.characterAnimationHandler.ImageReturn()#get the image of the current animation
		destinationScreen.blit(self.characterImage , (self.x-camera.x,self.y-camera.y))#buffer it

	def Update(self):
		self.PlayerInputHandler.Update()
		self.PlayerInput = self.PlayerInputHandler.returnEvents() # gets the input
		self.characterAnimationHandler.Update()#update the animation handler
		self.brain.Update(self)#updates the state


class IdleState(BrainStateMachine.IState):

	def Update(self,player):
		self.player = player
		
		for event in self.player.PlayerInput:

			""" Later changes this so it only changes the state """
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					self.player.moveState.y_change = 1 * self.player.movementSpeed
					self.player.brain.Change(self.player.moveState)
					self.player.characterAnimationHandler.changeAnimation(self.player.MoveDownAnimation)
				
				if event.key == pygame.K_UP: 
					self.player.moveState.y_change = -1 * self.player.movementSpeed
					self.player.brain.Change(self.player.moveState)	
					self.player.characterAnimationHandler.changeAnimation(self.player.MoveUpAnimation)			
				
				if event.key == pygame.K_RIGHT:
					self.player.moveState.x_change = 1 * self.player.movementSpeed
					self.player.brain.Change(self.player.moveState)
					self.player.characterAnimationHandler.changeAnimation(self.player.MoveRightAnimation)				
				
				if event.key == pygame.K_LEFT: 
					self.player.moveState.x_change = -1 * self.player.movementSpeed
					self.player.brain.Change(self.player.moveState)
					self.player.characterAnimationHandler.changeAnimation(self.player.MoveLeftAnimation)
					
					
class MoveState(BrainStateMachine.IState):

	def __init__(self):
		self.x_change = 0
		self.y_change = 0
	
	def Update(self,player):
		self.player = player

		for event in self.player.PlayerInput:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					if self.y_change != 1:
						self.y_change += 1 * self.player.movementSpeed
				
				if event.key == pygame.K_RIGHT:
					if self.x_change != 1:
						self.x_change += 1 * self.player.movementSpeed
				
				if event.key == pygame.K_LEFT:
					if self.x_change != -1:	
						self.x_change += -1 * self.player.movementSpeed
				
				if event.key == pygame.K_UP:
					if self.y_change != -1:
						self.y_change += -1 * self.player.movementSpeed

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					if self.y_change != -1:
						self.y_change += -1 * self.player.movementSpeed
				
				if event.key == pygame.K_RIGHT:
					if self.x_change != -1:
						self.x_change += -1 * self.player.movementSpeed
				
				if event.key == pygame.K_LEFT:
					if self.x_change != 1:
						self.x_change += 1 * self.player.movementSpeed
				
				if event.key == pygame.K_UP:
					if self.y_change != 1:
						self.y_change += 1 * self.player.movementSpeed


		""" change the animation based on the velocity, left and right after up and down"""
		if self.y_change == 1 * self.player.movementSpeed:
			self.player.characterAnimationHandler.changeAnimation(self.player.MoveUpAnimation)		
		elif self.y_change != 0:
			self.player.characterAnimationHandler.changeAnimation(self.player.MoveDownAnimation)

		if self.x_change == 1 * self.player.movementSpeed:
			self.player.characterAnimationHandler.changeAnimation(self.player.MoveRightAnimation)
		elif self.x_change != 0:
			self.player.characterAnimationHandler.changeAnimation(self.player.MoveLeftAnimation)

		
		if ((self.y_change == 0) and (self.x_change == 0)):
			self.player.brain.Change(self.player.nonState)
			self.player.characterAnimationHandler.changeAnimation(self.player.IdleAnimation)#set the current animation
		else:
			self.player.set_x(self.x_change)
			self.player.set_y(self.y_change)

			#awesome



