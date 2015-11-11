__author__ = 'alGatto'

import pygame
import player

class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        image_x = 320
        image_y = 240

        sprites = pygame.sprite.Group()
        self.player = player.Player(sprites)

        while 1:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si la croix en haut à gauche de la fenêtre est cliquée
                    running = False # la boucle de jeu s'arrête
                    pygame.quit()
                    quit()



            sprites.update(dt / 1000.)
            sprites.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game().main(screen)