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
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si la croix en haut à gauche de la fenêtre est cliquée
                    running = False # la boucle de jeu s'arrête
                    pygame.quit()
                    quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]: #si la touche flèche gauche est appuyée
                image_x -= 10
            if key[pygame.K_RIGHT]: #si la touche flèche droite est appuyée
                image_x +=10
            if key[pygame.K_UP]: #si la touche flèche haut est appuyée
                image_y -= 10
            if key[pygame.K_DOWN]: #si la touche flèche bas est appuyée
                image_y +=10

            sprites.update()
            sprites.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game().main(screen)