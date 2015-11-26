import Character
import Camera
import MapRender
import Level1
import pygame
import StateMachine
import PlayerClass

FPS = 30

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,255,255)


class ScreenState(StateMachine.IState):
    """We want to get a player and handle his animations"""

    def __init__(self):
        self.player = PlayerClass.Player()
        self.mainCamera = Camera.camera()
        self.mainCamera.setCamera(self.player)
        self.MapRenderer = MapRender.mapRender(40,800,600)
        self.MapRenderer.changeLevel(Level1)
 
        #initate player with default values also gives us the main camera and maprender

    def Update(self):
        self.mainCamera.update(800,600,self.MapRenderer.currentLevel.Layers[1],40)
        self.player.Update(self.MapRenderer.currentLevel)
        #calculates on which tile the player is right now
        #print(str(int(self.player.x / 40) + int(self.player.y / 40 * self.MapRenderer.level_x)))
        
        #call update function
        return

    def Render(self,destinationScreen):
        destinationScreen.fill(BLACK)
        self.MapRenderer.renderLayer(self.mainCamera,1,destinationScreen)
        self.player.Render(destinationScreen,self.mainCamera)
        pygame.display.update()
        #render display black and then render the first layer, after that show player
        return