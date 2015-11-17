__author__ = 'dylan'

import pygame
import game

black = (0,0,0) # on definit une couleur
pygame.font.init()

class Score():
    """La classe qui affiche le score"""

    def __init__(self):
        """on initialise la classe"""
        self.score = 0
        self.font = pygame.font.SysFont(None, 25)
        """on definit un font pour l'affichage"""
        self.text = self.font.render("Score : "+str(self.score), True, black)
        """on affiche notre score"""

    def update(self):
        self.score += 15
        print(str(self.score) + " fonction update")




