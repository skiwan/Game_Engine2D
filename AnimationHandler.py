#maybe import stuff here from pygame
import pygame
#import main

FPS = 30

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,255,255)

class AnimationHandler(object):

    """ The AnimationHandler is able to get an animation as input and then give back a specific
    image to play an animation until the animation is changed
    he animationclass should be updated so we can call an onstart and onend animation trigger"""

    def __init__(self,animation,width,height,spriteSheet):
        self.width = width
        self.height = height
        self.animation = animation #row in which the actual animation is
        self.spriteSheet = spriteSheet 
        self.frame = 0 #current Frame
        self.image = "" #Image which will be returned
        self.currentTime = 0 #needed for FPS
        self.frames = 3 #frames of the current Animation
        self.framesPerSecond = 2 #Speed of the Animation

    def Update(self):
        
        #get the Image on the Spritesheet
        self.spriteSheet.set_clip(pygame.Rect(self.frame*self.width,self.animation*self.height,self.width,self.height))
        self.image = self.spriteSheet.subsurface(self.spriteSheet.get_clip())


        # calculate picture when a frame shall be changed
        if self.currentTime % (FPS//self.framesPerSecond) == 0:
            if self.frame < self.frames: #ATTENTION!!! frames == actual number of images of the animation -1 (reason: counting starts at 0)
                self.frame += 1
                self.currentTime = 0
            else:
                self.frame = 0
                self.currentTime = 0
        self.currentTime += 1


       
    #changes the current animation
    def changeAnimation(self,animation):
        # change animation based stuff
        self.animation = animation.animation
        self.width = animation.width
        self.height = animation.height
        self.frames = animation.frames
        self.framesPerSecond = animation.framesPerSecond


    def ImageReturn(self):
        #return the fuck
        return self.image

