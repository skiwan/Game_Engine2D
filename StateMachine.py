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
    def Update(self):
        self.CurrentState.Update()

#will run the render method of the current state
    def Render(self,destinationScreen):
        self.CurrentState.Render(destinationScreen)

    #will change the current state
    def Change(self,stateName):
        self.CurrentState.OnExit()
        self.CurrentState = stateName
        self.CurrentState.OnEnter()

class IState(object):
    #this is the Parent of all our other states
    
    def Update(self):
        return
        #will do the game logic
    def Render(self,destinationScreen):
        #will do all the screen display
        return
    def OnEnter(self):
        #will do something when we go into that state
        return
    def OnExit(self):
        #will do something when we go out of that state
        return

class EmptyState (IState):
    def Update(self):
        #epmty state doenst uodate somethign
        return
    def Render(self):
        #empts state doenst render anything
        return
    def OnEnter(self):
        #will do something when we go into that state
        return
    def OnExit(self):
        #will do something when we go out of that state
        return
