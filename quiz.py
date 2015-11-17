# -*- coding: utf-8 -*-

__author__ = 'alGatto'

import pygame, game

BLACK = (0, 0, 0)
class Quiz():
    """La class des quiz"""
    def __init__(self):
        self.question = ""
        self.rep1 = ""
        self.rep2 = ""
        self.rep3 = ""
    def quiz(self):
        print("Question 1")
        print("What percentage of the land is used for farming?")
        print()
        print("a. 25%")
        print("b. 50%")
        print("c. 75%")
        answer = input("Make your choice: ")
        if answer == "c":
            print("Correct!")

    def quiz_screen(self):
        display = pygame.display.set_mode((1024,683))
        display.fill(BLACK)
        myfont = pygame.font.SysFont("impact", 25)
        quizfile = open("quiz.txt", 'r')
        labels = quizfile.read()
        label = myfont.render((labels), 1, (0, 0, 0))
        display.blit(label, (0, 0))

        self.back = pygame.image.load('ressources/level1back.png')
        self.back_r = self.back.get_bounding_rect()
        self.back_r.x,self.back_r.y = (100,600)
        display.blit(self.back,(100, 600))
        #display.blit(self.player,(self.mouse_pos))
        #if self.player_r.colliderect(self.back_r)and pygame.mouse.get_pressed()[0]:
            #self.state = 1

