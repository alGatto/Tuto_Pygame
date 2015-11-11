__author__ = 'alGatto'

import pygame

class Player(pygame.sprite.Sprite):
    """Classe du personnage principal"""
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('ressources/Ducky-static.png') #charge l'image du personnage
        self.rect = pygame.rect.Rect((320,240), self.image.get_size())

    def update(self, dt, game):
        last = self.rect.copy() #copie de la position

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: #si la touche flèche gauche est appuyée
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]: #si la touche flèche droite est appuyée
            self.rect.x += 300 * dt
        if key[pygame.K_UP]: #si la touche flèche haut est appuyée
            self.rect.y -= 300 * dt
        if key[pygame.K_DOWN]: #si la touche flèche bas est appuyée
            self.rect.y += 300 * dt

        # Bloquer la sortie d'écran du perso
        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
