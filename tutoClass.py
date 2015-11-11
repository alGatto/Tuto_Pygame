__author__ = 'alGatto'

import pygame

class Game(object):
    def main(selfself, screen):
        image = pygame.image.load('ressources/Ducky-static.png') #charge l'image du personnage
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si la croix en haut à gauche de la fenêtre est cliquée
                    running = False # la boucle de jeu s'arrête
                if event.type == pygame.KEYDOWN and event.key == pygame.ESCAPE: # si une touche plus la touche esc est préssée
                    running = False # la boucle de jeu s'arrête

            screen.fill((200, 200, 200))
            screen.blit(image, (320, 240))
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game().main(screen)