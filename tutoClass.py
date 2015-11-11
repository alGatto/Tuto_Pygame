__author__ = 'alGatto'

import pygame

class Game(object):
    def main(selfself, screen):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si la croix en haut à gauche de la fenêtre est cliquée
                    running = False # la boucle de jeu s'arrête
                if event.type == pygame.KEYDOWN and event.key == pygame.ESCAPE: # si une touche plus la touche esc est préssée
                    running = False # la boucle de jeu s'arrête

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game().main(screen)