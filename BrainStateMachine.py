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

""" This is the State Machine for AI handling. States will be defined in the actual Characterclass """
class BrainStateMachine(object):

#we will create States wich stand for every screen we need
#main menu , the game, ending screens ect ...

    def __init__(self):
        self.CurrentState = EmptyState()

#will run the update method of the current state
    def update(self,player):
        self.CurrentState.update(player)

    #will change the current state
    def Change(self,stateName):
        self.CurrentState.OnExit()
        self.CurrentState = stateName
        self.CurrentState.OnEnter()

class IState(object):
    #this is the Parent of all our other states
    
    def update(self):
        return
        #will do the game logic
    def OnEnter(self):
        #will do something when we go into that state
        return
    def OnExit(self):
        #will do something when we go out of that state
        return

class EmptyState (IState):
    def update(self):
        #epmty state doenst uodate somethign
        return
    def OnEnter(self):
        #will do something when we go into that state
        return
    def OnExit(self):
        #will do something when we go out of that state
        return

