__author__ = 'alGatto'

import pygame
import player
import tmx
import pytmx


class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        self.size = self.width, self.height = 1024, 683

        background =pygame.image.load('ressources/level1back.png') #charge l'image de fond

        self.tilemap = tmx.load('levelMap/map.tmx', screen.get_size())

        self.sprites = tmx.SpriteLayer()
        start_cell = self.tilemap.layers['triggers'].find('player')[0]
        self.player = player.Player((start_cell.px, start_cell.py), self.sprites)
        self.tilemap.layers.append(self.sprites)

        while 1:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si la croix en haut à gauche de la fenêtre est cliquée
                    running = False # la boucle de jeu s'arrête
                    pygame.quit()
                    quit()



            self.tilemap.update(dt / 1000., self)
            screen.blit(background, (0, 0)) # place le fond
            self.tilemap.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init() #initialise pygame
    screen = pygame.display.set_mode((1024,683)) #dessine une fenêtre de 1024 x 683 px
    pygame.display.set_caption('Duck Approves')
    Game().main(screen)