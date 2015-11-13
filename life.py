__author__ = 'alGatto'

import pygame

class Life():
    def __init__(self):
        self.image = pygame.image.load('ressources/life3.png')
        self.image_life3 = pygame.image.load('ressources/life3.png')
        self.image_life2 = pygame.image.load('ressources/life2.png')
        self.image_life1 = pygame.image.load('ressources/life3.png')
        self.nb_life = 3

    def update(self, nb_life):
        if nb_life == 3:
            self.image = self.image_life3
        if nb_life == 2:
            self.image = self.image_life2
        if nb_life == 1:
            self.image = self.image_life1


