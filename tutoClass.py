__author__ = 'alGatto'

import pygame

class Game(object):
    def main(selfself, screen):
        clock = pygame.time.Clock()

        image = pygame.image.load('ressources/Ducky-static.png') #charge l'image du personnage
        image_x = 320
        image_y = 240

        while 1:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si la croix en haut à gauche de la fenêtre est cliquée
                    running = False # la boucle de jeu s'arrête

                if event.type == pygame.KEYDOWN and event.key == pygame.ESCAPE: # si une touche plus la touche esc est préssée
                    running = False # la boucle de jeu s'arrête

            image_x += 10
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                image_x -= 10
            if key[pygame.K_RIGHT]:
                image_x +=10
            if key[pygame.K_UP]:
                image_y -= 10
            if key[pygame.K_DOWN]:
                image_y +=10

            screen.fill((200, 200, 200))
            screen.blit(image, (image_x, image_y))
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game().main(screen)