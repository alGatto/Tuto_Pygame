__author__ = 'alGatto'

import pygame
import score

class Bullet(pygame.sprite.Sprite):
    image = pygame.image.load('levelMap/bullet.png')
    def __init__(self, location, direction, *groups):
        super(Bullet, self).__init__(*groups)
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.direction = direction
        self.lifespan = 1

    def update(self, dt, game):
        self.lifespan -= dt
        if self.lifespan < 0:
            self.kill()
            return
        self.rect.x += self.direction * 400 * dt

        if pygame.sprite.spritecollide(self, game.enemies, True):
            game.explosion.play()
            score.Score().update()
            print(score.Score().score)
            self.kill()
