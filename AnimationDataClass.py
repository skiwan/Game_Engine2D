FPS = 30

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,255,255)

class animation(object):
    """ DataClass to store pieces of information of an animation
    should be modified to have an onStart and OnEnd method for better animation use like skills ,best would be if it only returns true
    like a notifier to the state machine aka brain"""

    def __init__(self,animation,width,height,frames,speed):
        self.animation = animation;
        self.width = width;
        self.height = height;
        self.frames = frames; #ATTENTION!!! frames == actual number of images of the animation -1 (reason: counting starts at 0)
        self.framesPerSecond = speed;

