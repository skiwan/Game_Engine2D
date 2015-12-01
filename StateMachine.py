import Character
import Camera
import MapRender
import Level1
import pygame

FPS = 30

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,255,255)

class StateMachine(object):

#we will create States wich stand for every screen we need
#main menu , the game, ending screens ect ...

    def __init__(self):
        self.CurrentState = EmptyState()

#will run the update method of the current state
    def update(self):
        self.CurrentState.update()

#will run the render method of the current state
    def render(self,destinationScreen):
        self.CurrentState.render(destinationScreen)

    #will change the current state
    def Change(self,stateName):
        self.CurrentState.onExit()
        self.CurrentState = stateName
        self.CurrentState.onEnter()

class IState(object):
    #this is the Parent of all our other states
    
    def update(self):
        return
        #will do the game logic
    def render(self,destinationScreen):
        #will do all the screen display
        return
    def onEnter(self):
        #will do something when we go into that state
        return
    def onExit(self):
        #will do something when we go out of that state
        return

class EmptyState (IState):
    def update(self):
        #epmty state doenst uodate somethign
        return
    def render(self):
        #empts state doenst render anything
        return
    def onEnter(self):
        #will do something when we go into that state
        return
    def onExit(self):
        #will do something when we go out of that state
        return

