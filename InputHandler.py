import pygame

class Input_Handler(object):
    """ A class to get the input of the player and returns that shit"""
    def __init__(self):
        self.GameEvents = []

    def update(self):
        self.GameEvents = []
        for event in pygame.event.get():
            self.GameEvents.append(event)

    def returnEvents(self):
        return (self.GameEvents)