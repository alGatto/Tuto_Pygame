__author__ = 'alGatto'

import pygame
import bullet

class Player(pygame.sprite.Sprite):
    """Classe du personnage principal"""
    def __init__(self, location, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('ressources/Ducky-static.png') #charge l'image du personnage pour la direction droite
        self.right_image = self.image
        self.left_image = pygame.image.load('ressources/Ducky-left.png') #charge l'image du perso pour la direction gauche
        self.rect = pygame.rect.Rect(location, self.image.get_size())

        self.resting = False
        self.dy = 0 #delta y
        self.is_dead = False

        self.direction = 1

        #nombre de shoot possible avant que la balle ne se supprime
        self.gun_cooldown = 0

    def update(self, dt, game):
        last = self.rect.copy() #copie de la position

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: #si la touche flèche gauche est appuyée
            self.rect.x -= 300 * dt
            self.image = self.left_image #change l'image du perso
            self.direction = -1 #change lea valeur de la direction du perso
        if key[pygame.K_RIGHT]: #si la touche flèche droite est appuyée
            self.rect.x += 300 * dt
            self.image = self.right_image #change l'image du perso
            self.direction = 1
        if key[pygame.K_UP]:
            self.rect.y -= 800 * dt

        #Tirer des projectiles
        if key[pygame.K_LSHIFT] and not self.gun_cooldown:
            if self.direction > 0:
                #on crée une balle dans la direction du joueur
                bullet.Bullet(self.rect.midright, 1, game.sprites)
            else:
                bullet.Bullet(self.rect.midleft, -1, game.sprites)
            self.gun_cooldown = 1

        self.gun_cooldown = max(0, self.gun_cooldown - dt)

        #Gravité
        if self.resting and key[pygame.K_SPACE]:
            game.jump.play()
            self.dy = - 500
        self.dy = min(400, self.dy + 40)

        self.rect.y += self.dy * dt

        # Bloquer la sortie d'écran du perso
        new = self.rect
        self.resting = False
        for cell in game.tilemap.layers['triggers'].collide(new, 'blockers'):
            blockers = cell['blockers']
            if 'l' in blockers and last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if 'r' in blockers and last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if 't' in blockers and last.bottom <= cell.top and new.bottom > cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if 'b' in blockers and last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.dy = 0

        game.tilemap.set_focus(new.x, new.y) #suivre le perso
