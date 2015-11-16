__author__ = 'alGatto'

import pygame
import tmx
import life
import player
import game

class Enemy(pygame.sprite.Sprite):
    image = pygame.image.load('levelMap/enemy-right.png')
    image_right = image
    image_left = pygame.image.load('levelMap/enemy-left.png')
    def __init__(self, location, *groups):
        super(Enemy, self).__init__(*groups)
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.direction = 1

    def update(self, dt, game):
        self.rect.x += self.direction * 100 * dt
        for cell in game.tilemap.layers['triggers'].collide(self.rect, 'reverse'):
            if self.direction > 0:
                self.image = self.image_left
                self.rect.right = cell.left
            else:
                self.image = self.image_right
                self.rect.left = cell.right
            self.direction *= -1
            break
        if self.rect.colliderect(game.player.rect):
            LIFE.nb_life -= 1
            new_life = LIFE.nb_life
            LIFE.update(new_life)
            print(LIFE.nb_life)
            #if LIFE.nb_life == 0:
                #game.player.is_dead = True


LIFE = life.Life()
