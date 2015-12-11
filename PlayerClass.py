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

		#level for collision detection with the 0layer and the current tile we are on
		self.currentLevel = ""
		self.tile = 0

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


		self.characterAnimationHandler.update()#called to get the first image needed		
		self.characterImage=self.characterAnimationHandler.ImageReturn()

	def set_y(self,wert):
		self.y += wert

	def set_x(self,wert):
		self.x += wert

	""" Will display the Character """
	def render(self,destinationScreen,camera):
		self.characterImage = self.characterAnimationHandler.ImageReturn()#get the image of the current animation
		destinationScreen.blit(self.characterImage , (self.x-camera.x,self.y-camera.y))#buffer it

	"""updates the entire player, needs to be called every frame"""
	def update(self,Level):
		self.PlayerInputHandler.update()
		self.PlayerInput = self.PlayerInputHandler.returnEvents() # gets the input
		self.characterAnimationHandler.update()#update the animation handler
		self.brain.update(self)#updates the state
		self.currentLevel = Level
		self.tile = (int(self.x / 40) + int(self.y / 40 *self.currentLevel.Layers[1].x))

""" State when the Player doenst move """
class IdleState(BrainStateMachine.IState):

	def update(self,player):
		self.player = player
		
		for event in self.player.PlayerInput:

			""" Changes the States given on the Input """
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					self.player.brain.Change(self.player.moveState)
					self.player.characterAnimationHandler.changeAnimation(self.player.MoveDownAnimation)
				
				if event.key == pygame.K_UP: 
					self.player.brain.Change(self.player.moveState)	
					self.player.characterAnimationHandler.changeAnimation(self.player.MoveUpAnimation)			
				
				if event.key == pygame.K_RIGHT:
					self.player.brain.Change(self.player.moveState)
					self.player.characterAnimationHandler.changeAnimation(self.player.MoveRightAnimation)				
				
				if event.key == pygame.K_LEFT: 
					self.player.brain.Change(self.player.moveState)
					self.player.characterAnimationHandler.changeAnimation(self.player.MoveLeftAnimation)
					
""" State when the Player moves """					
class MoveState(BrainStateMachine.IState):

	def __init__(self):
		self.x_change = 0
		self.y_change = 0
	
	
	def update(self,player):
		self.player = player
		print(self.player.PlayerInput)
		for event in self.player.PlayerInput:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					if (self.y_change == 0) or (self.y_change == -1*self.player.movementSpeed):
						self.y_change += 1 * self.player.movementSpeed

				if event.key == pygame.K_RIGHT:
					if (self.x_change == 0) or (self.x_change == -1* self.player.movementSpeed):
						self.x_change += 1 * self.player.movementSpeed

				if event.key == pygame.K_LEFT:
					if (self.x_change == 0) or (self.x_change == 1* self.player.movementSpeed):	
						self.x_change += -1 * self.player.movementSpeed

				
				if event.key == pygame.K_UP:
					if (self.y_change == 0) or (self.y_change == 1* self.player.movementSpeed):
						self.y_change += -1 * self.player.movementSpeed
					

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					if(self.y_change == 1* self.player.movementSpeed):
						self.y_change += -1 * self.player.movementSpeed
				
				if event.key == pygame.K_RIGHT:
					if(self.x_change == 1* self.player.movementSpeed):
						self.x_change += -1 * self.player.movementSpeed
				
				if event.key == pygame.K_LEFT:
					if(self.x_change == -1* self.player.movementSpeed):
						self.x_change += 1 * self.player.movementSpeed
				
				if event.key == pygame.K_UP:
					if(self.y_change == -1* self.player.movementSpeed):
						self.y_change += 1 * self.player.movementSpeed

		""" Test if player is within boundries"""
		if self.player.y  >= ((self.player.currentLevel.Layers[1].y * 40) - 40) and self.y_change > 0 :
			self.y_change = 0
		if self.player.x  >= ((self.player.currentLevel.Layers[1].x *40)-40) and self.x_change > 0:
				self.x_change = 0
		if  self.player.x  <= 0 and self.x_change < 0:
			self.x_change = 0
		if self.player.y  <= 0 and self.y_change < 0:
			self.y_change =0
		#check if collide with bottom or top
		if(self.CollideWithWall(0, self.y_change, self.player)):
			self.y_change = 0
		#check if collide with left or right
		if(self.CollideWithWall(self.x_change, 0, self.player)):
			self.x_change = 0


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

	def CollideWithWall(self,x_change,y_change,player):
		""" Used to check for colliding with the collission Layer"""
		
		if (x_change > 0):
			if(player.y % 40 == 0):
				if (player.currentLevel.Layers[1].lmap[player.tile+1] == 0):
					return True
			else:
				if(player.currentLevel.Layers[1].lmap[player.tile+1] == 0 ):
					return True
				if (player.currentLevel.Layers[1].lmap[player.tile+1+(player.currentLevel.Layers[1].y)] == 0):
					return True
		
		
		elif (x_change < 0):
			if(player.y % 40 == 0):
				if (player.x % 40 == 0):
					if (player.currentLevel.Layers[1].lmap[player.tile-1] == 0):
						return True

			else:
				if(player.x % 40 == 0):
					if(player.currentLevel.Layers[1].lmap[player.tile-1] == 0 ):
						return True
					if (player.currentLevel.Layers[1].lmap[player.tile-1+(player.currentLevel.Layers[1].y)] == 0):
						return True
		
		
		elif (y_change > 0):
			if(player.x % 40 == 0):
				if (player.currentLevel.Layers[1].lmap[player.tile+(player.currentLevel.Layers[1].x)] == 0):
					return True
			else:
				if(player.currentLevel.Layers[1].lmap[player.tile+(player.currentLevel.Layers[1].x)] == 0 ):
					return True	
				if (player.currentLevel.Layers[1].lmap[player.tile+(1+(player.currentLevel.Layers[1].x))] == 0):
					return True

		
		elif (y_change < 0):
			if(player.x % 40 == 0):
				if (player.y % 40 == 0):
					if (player.currentLevel.Layers[1].lmap[player.tile-(player.currentLevel.Layers[1].x)] == 0):
						return True
			else:
				if (player.y % 40 == 0):
					if(player.currentLevel.Layers[1].lmap[player.tile-(player.currentLevel.Layers[1].x)] == 0 ):
						return True	
					if (player.currentLevel.Layers[1].lmap[player.tile+1-(player.currentLevel.Layers[1].x)] == 0):
						return True


		#will only be triggered if x_change and y_change both are zero
		else:
			return True


