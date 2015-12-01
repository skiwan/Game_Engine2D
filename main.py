#!/usr/bin/env python
""" Date 8.nov.15"""
import pygame, sys
#import Level1
import StateMachine
import ScreenState
#initates some stuff
pygame.init()
pygame.key.set_repeat(1,1)

FPS = 30

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,255,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("")
clock = pygame.time.Clock()
#saves the events


""" Initilazing the main game Loop with all States like Menu e.g. """
def main():
    StateM = StateMachine.StateMachine()
    MapScreen = ScreenState.ScreenState()
    gameExit = False
    StateM.Change(MapScreen)
    while not gameExit:
        StateM.update()
        StateM.render(gameDisplay)
        clock.tick(FPS)
#run the main loop
main ()