__author__ = 'alGatto'

import pygame
import player

class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        background =pygame.image.load('ressources/level1back.png')

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
            screen.blit(background, (0, 0))
            sprites.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1024,683))
    Game().main(screen)