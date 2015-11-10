import pygame
import Level1

FPS = 30

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,255,255)

class mapRender(object):
    """ the Maprenderer which we need to render our Levellayers """
    def __init__(self,tilesize,width,height):
        self.tilesize = tilesize;
        self.tilemapWidth = 20;
        self.displayableCollums = width / tilesize; #number how many tiles fit on screen
        self.displayableRows = height / tilesize; #number how many rows fit on screen
        self.currentLevel = ""#current level
        self.todisplayableCollums = 0 #needed to display one more row than the screen usually can fit
        self.todisplayableRows = 0

    def changeLevel(self,Level):#changes the current Level which shall be displayed
        self.currentLevel = Level;

    def renderLayer(self,camera,layer,destinationScreen):#renders a specific layer of the Level with the help of the maincamera
        self.tileMap = pygame.image.load(self.currentLevel.Layers[layer].tileMap);
        self.level = self.currentLevel.Layers[layer].lmap;
        self.level_x = self.currentLevel.Layers[layer].x;
        self.level_y = self.currentLevel.Layers[layer].y;
        self.image = "";
        
        self.x = 0;
        self.y = 0;
        
        self.camera_x = camera.x;
        self.camera_y = camera.y;

        #first tile of the array which will be shown
        self.displayedTile =  (self.camera_x // self.tilesize) + (self.camera_y // self.tilesize * self.tilemapWidth ); # first tile to be shown // upper left tile
        
        #set those variables if the level is big enough
        if (self.todisplayableRows == 0) and (self.todisplayableCollums == 0):
            if self.displayableCollums < self.currentLevel.Layers[layer].x:
                self.todisplayableCollums = self.displayableCollums+1
            else:
                self.todisplayableCollums = self.displayableCollums

            if self.displayableRows < self.currentLevel.Layers[layer].y:
                self.todisplayableRows = self.displayableRows+1
            else:
                self.todisplayableRows = self.displayableRows+1
  



        """ todisplayableRows and todisplayableCollums will be reassigend if we reach the last rows or collums of th level array """
        if self.todisplayableRows != self.displayableRows:
            if ((self.level_y) * self.level_x - (self.level_x-1)) <= (self.displayedTile + self.displayableRows*(self.displayableCollums)):
                self.todisplayableRows = self.displayableRows
        else:
            if ((self.level_y) * self.level_x - (self.level_x-1)) > (self.displayedTile + self.displayableRows*(self.displayableCollums)):
                self.todisplayableRows = self.displayableRows + 1
        if self.todisplayableCollums != self.displayableCollums:
            if ((self.level_x) <= (self.displayedTile + self.displayableCollums)):
                self.todisplayableCollums = self.displayableCollums
        else:
            if ((self.level_x) > (self.displayedTile + self.displayableCollums)):
                self.todisplayableCollums = self.displayableCollums + 1

        

        #render the entire level on the screen
        while self.y < self.todisplayableRows:
            while self.x < self.displayableCollums:
                #get the screen of the current tile


                self.tileMap.set_clip(pygame.Rect((self.level[self.displayedTile]%self.tilemapWidth)*self.tilesize,(self.level[self.displayedTile] // self.tilemapWidth)*self.tilesize,self.tilesize,self.tilesize))
                self.image = self.tileMap.subsurface(self.tileMap.get_clip())
                destinationScreen.blit(self.image , ((self.x*self.tilesize-(self.camera_x%40)), (self.y*self.tilesize-(self.camera_y%40))));
                self.x +=1;
                self.displayedTile +=1;
                
            self.displayedTile += - self.x; # reset to the right collum
            self.displayedTile += - self.y*self.tilemapWidth; # reset to the right collum
            self.x = 0;
            
            self.y +=1; # go to next row
            self.displayedTile += self.y*self.tilemapWidth #get the right index for the level
        # end of the rendering of the screenlevel