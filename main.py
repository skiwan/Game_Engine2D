#!/usr/bin/env python
""" Date 8.nov.15"""
import pygame, sys
#import Level1
import StateMachine
import ScreenState
#initates some stuff
pygame.init()

FPS = 30

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,255,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("")
clock = pygame.time.Clock()
#saves the events



def main():
    StateM = StateMachine.StateMachine()
    Screen = ScreenState.ScreenState()
    gameExit = False
    StateM.Change(Screen);
    while not gameExit:
        StateM.Update()
        StateM.Render(gameDisplay)
        clock.tick(FPS)

main ();