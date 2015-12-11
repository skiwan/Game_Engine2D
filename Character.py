import AnimationHandler
import pygame
import AnimationDataClass
import StateMachine

FPS = 30

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,255,255)

class Character(object):
    """ This is the Character Class which is the Parent of every
    Character based thing in our world. Here we store Stats that everyone needs and we will implement the brain here """

    def __init__(self):
        self.spriteSheet = pygame.image.load("charspritesheet.png") 
        self.x = 40#starting positions
        self.y = 40
        self.width = 40#size
        self.height = 40
        self.animation = 0
        self.characterAnimationHandler = AnimationHandler.AnimationHandler(self.animation,self.width,self.height,self.spriteSheet)#animation handler
        self.brain = StateMachine.StateMachine()
        
        #animations of this Character
        IdleAnimation = AnimationDataClass.animation(0,40,40,3,2)


        self.characterAnimationHandler.changeAnimation(IdleAnimation)#set the current animation



        self.characterAnimationHandler.Update()#called to get the first image needed        
        self.characterImage=self.characterAnimationHandler.ImageReturn()



    def Render(self,destinationScreen):
        self.characterImage = self.characterAnimationHandler.ImageReturn()#get the image of the current animation
        destinationScreen.blit(self.characterImage , (self.x,self.y))#buffer it

    def Update(self):
        self.characterAnimationHandler.Update()#update the animation handler, later the state must be updated here too
