__author__ = 'alGatto'

import pygame
import player

class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        self.size = self.width, self.height = 1024, 683

        background =pygame.image.load('ressources/level1back.png') #charge l'image de fond

        sprites = pygame.sprite.Group()
        #sprites.add(background)
        self.player = player.Player(sprites)
        self.walls = pygame.sprite.Group()
        block = pygame.image.load('ressources/brick1.png')
        for x in range(0, self.width, 16):
            for y in range(0, self.height, 16):
                if x in (0, self.width-16) or y in (0, self.height-16):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x, y), block.get_size())
        sprites.add(self.walls)

        while 1:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si la croix en haut à gauche de la fenêtre est cliquée
                    running = False # la boucle de jeu s'arrête
                    pygame.quit()
                    quit()



            sprites.update(dt / 1000., self)
            screen.blit(background, (0, 0)) # place le fond
            sprites.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init() #initialise pygame
    screen = pygame.display.set_mode((1024,683)) #dessine une fenêtre de 1024 x 683 px
    pygame.display.set_caption('Duck Approves')
    Game().main(screen)