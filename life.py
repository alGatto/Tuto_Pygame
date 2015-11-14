__author__ = 'alGatto'

import pygame
import game

class Life(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('ressources/life3.png')
        self.image_life3 = self.image
        self.image_life2 = pygame.image.load('ressources/life2.png')
        self.image_life1 = pygame.image.load('ressources/life1.png')
        self.rect = self.image.get_rect()
        self.nb_life = 3 # le hero démarre avec 3 vies


        self.section = pygame.Surface((96, 32))
        self.rect = self.section.get_rect()

    def update(self, nb_life):
        if nb_life == 3:
            print('trois')
            self.image = self.image_life3
        elif nb_life == 2:
            print('deux')
            self.section.blit(self.image_life2, (0, 0))
            self.image = self.image_life2
        elif nb_life == 1:

            self.image = self.image_life1

    def display(self, screen, image):
        screen.blit(image, (900, 0))


