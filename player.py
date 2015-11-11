__author__ = 'alGatto'

import pygame

class Player(pygame.sprite.Sprite):
    """Classe du personnage principal"""
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('ressources/Ducky-static.png') #charge l'image du personnage
        self.rect = pygame.rect.Rect((320,240), self.image.get_size())

    def update(self, dt):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: #si la touche flèche gauche est appuyée
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]: #si la touche flèche droite est appuyée
            self.rect.x += 300 * dt
        if key[pygame.K_UP]: #si la touche flèche haut est appuyée
            self.rect.y -= 300 * dt
        if key[pygame.K_DOWN]: #si la touche flèche bas est appuyée
            self.rect.y += 300 * dt
