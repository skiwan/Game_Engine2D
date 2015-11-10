class camera(object):
    """ The camera which helps us to only render those parts of the Map that we need """
    def __init__(self):
        """ we can set a target here e.g. the player to focus on"""
        self.target = "";
        #use these coordinates to display stuff properly
        self.x = 0;
        self.y = 0;

    def setCamera(self,target):
        #change camera focus
        self.target = target;

    def update(self,width,height,level,tilesize):
        # this will center the target if possible
        if ((self.target.x > 0 + int(0.5*width)) and (self.target.x < ((level.x * tilesize) - (int(0.5*(width+tilesize)))-19))):
            self.x = (self.target.x) - int(0.5*width);
        if ((self.target.y > 0 + int(0.5*height)) and (self.target.y < ((level.y * tilesize) - (int(0.5*(height-tilesize)))-19))):
                self.y = ((self.target.y) - int(0.5*height))

        
