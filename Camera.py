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
        if (target.x > 0 + int(0.5*width)) and (target.x < ((level.x * tilesize) - (int(0.5*width)))):
            self.x = target.x;
        if (target.y > 0 + int(0.5*height)) and (target.y < ((level.y * tilesize) - (int(0.5*height)))):
            self.y = target.y;