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
		self.movementSpeed = 1


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
		
		#States of the chracter
		self.nonState = IdleState()
		self.moveState = MoveState() 
		self.down = False
		self.characterAnimationHandler.changeAnimation(self.IdleAnimation)#set the current animation
		self.brain.Change(self.nonState)


		self.characterAnimationHandler.Update()#called to get the first image needed		
		self.characterImage=self.characterAnimationHandler.ImageReturn()

	def set_y(self,wert):
		self.y += wert

	def set_x(self,wert):
		self.x += wert

	def Render(self,destinationScreen):
		self.characterImage = self.characterAnimationHandler.ImageReturn()#get the image of the current animation
		destinationScreen.blit(self.characterImage , (self.x,self.y))#buffer it

	def Update(self):
		self.PlayerInputHandler.Update()
		self.PlayerInput = self.PlayerInputHandler.returnEvents()
		self.characterAnimationHandler.Update()#update the animation handler, later the state must be updated here too
		self.brain.Update(self)


class IdleState(BrainStateMachine.IState):

	def Update(self,player):
		self.player = player
		
		for event in self.player.PlayerInput:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					print("changeState to MoveState down")
					self.player.moveState.y_change = 1
					self.player.brain.Change(self.player.moveState)
				
				if event.key == pygame.K_UP: 
					print("changeState to MoveState up")
					self.player.moveState.y_change = -1
					self.player.brain.Change(self.player.moveState)				
				
				if event.key == pygame.K_RIGHT:
					print("changeState to MoveState")
					self.player.moveState.x_change = 1
					self.player.brain.Change(self.player.moveState)				
				
				if event.key == pygame.K_LEFT: 
					print("changeState to MoveState")
					self.player.moveState.x_change = -1
					self.player.brain.Change(self.player.moveState)
					
					
class MoveState(BrainStateMachine.IState):

	def __init__(self):
		print("gets called")
		self.x_change = 0
		self.y_change = 0
	
	def Update(self,player):
		self.player = player
		print(self.player.PlayerInput)

		for event in self.player.PlayerInput:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					if self.y_change != 1:
						self.y_change += 1
				if event.key == pygame.K_RIGHT:
					if self.x_change != 1:
						self.x_change += 1
				if event.key == pygame.K_LEFT:
					if self.x_change != -1:	
						self.x_change += -1
				if event.key == pygame.K_UP:
					if self.y_change != -1:
						self.y_change += -1

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					if self.y_change != -1:
						self.y_change += -1
				if event.key == pygame.K_RIGHT:
					if self.x_change != -1:
						self.x_change += -1
				if event.key == pygame.K_LEFT:
					if self.x_change != 1:
						self.x_change += 1
				if event.key == pygame.K_UP:
					if self.y_change != 1:
						self.y_change += 1
		
		if ((self.y_change == 0) and (self.x_change == 0)):
			print("Change to nonState")
			self.player.brain.Change(self.player.nonState)
		else:
			self.player.set_x(self.x_change)
			self.player.set_y(self.y_change)



